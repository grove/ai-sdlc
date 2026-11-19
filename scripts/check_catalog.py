#!/usr/bin/env python3
"""Check catalog structure and portable Markdown links using only the stdlib.

Run from any directory: python scripts/check_catalog.py
The optional --root argument is useful when checking a temporary checkout.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass, field
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit


STAGES = {
    "P": "problem", "H": "hypothesis", "K": "context",
    "A": "agent-execution", "V": "verification", "R": "production",
    "O": "observation", "L": "learning",
}
EXPECTED_IDS = {f"{prefix}{number:02}" for prefix in STAGES for number in range(1, 33)}
SECTIONS = (
    "Opportunity", "Inputs and Evidence", "Prerequisites", "Example and Deliverable",
    "Safeguards and Review", "Measuring Impact", "Applying This Idea",
)
METADATA = ("Stage", "Category", "Operating Mode", "Especially Relevant To")
MODES = {"Advisory", "Drafting", "Bounded Execution"}
HEADING = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.*?)(?:[ \t]+#+[ \t]*)?$")
LINK_START = re.compile(r"(?<!\\)!?\[(?:\\.|[^\[\]\\]|\[[^\]\n]*\])*\]\(\s*")
REFERENCE = re.compile(r"^ {0,3}\[([^\]\n]+)\]:[ \t]*(?:<([^>\n]*)>|(\S+)).*$", re.M)
BRACKETS = re.compile(r"(?<!\\)!?\[([^\]\n]+)\](?:\[([^\]\n]*)\])?")


def mask_code(text: str, inline: bool = True) -> str:
    """Keep line positions while excluding examples in comments and code."""
    blank = lambda match: re.sub(r"[^\n]", " ", match.group())
    text = re.sub(r"<!--[\s\S]*?-->", blank, text)
    lines, fence = [], None
    for line in text.splitlines(keepends=True):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                fence = None
            lines.append(re.sub(r"[^\n]", " ", line))
        elif marker:
            fence = marker[1]
            lines.append(re.sub(r"[^\n]", " ", line))
        else:
            lines.append(line)
    text = "".join(lines)
    return re.sub(r"(`+)(.+?)\1(?!`)", blank, text, flags=re.S) if inline else text


def plain_heading(text: str) -> str:
    text = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"\\([\\`*{}\[\]()#+\-.!_>])", r"\1", text)
    text = re.sub(r"(?<!\w)(_{1,2}|~~)(.+?)\1(?!\w)", r"\2", text)
    return unescape(text).replace("*", "").replace("`", "").strip()


def slug(text: str, platform: str) -> str:
    text = plain_heading(text).lower().strip()
    if platform == "mkdocs":
        text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
        text = re.sub(r"[^\w\s-]", "", text)
        return re.sub(r"[-\s]+", "-", text)
    text = "".join(
        char for char in text
        if char in "-_" or unicodedata.category(char)[0] not in "PS"
    )
    return text.replace(" ", "-")


class HtmlLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.anchors: list[tuple[str, int]] = []
        self.links: list[tuple[str, int]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if value is None:
                continue
            if key == "id" or (tag == "a" and key == "name"):
                self.anchors.append((value, self.getpos()[0]))
            if key == "href" or (tag in {"img", "script", "source"} and key == "src"):
                self.links.append((value, self.getpos()[0]))


@dataclass
class Document:
    path: Path
    text: str
    headings: list[tuple[int, str, int]] = field(default_factory=list)
    links: list[tuple[str, int]] = field(default_factory=list)
    anchors: dict[str, set[str]] = field(default_factory=dict)
    parse_errors: list[tuple[str, int]] = field(default_factory=list)

    def __post_init__(self) -> None:
        clean = mask_code(self.text)
        html = HtmlLinks()
        html.feed(clean)
        explicit = [anchor for anchor, _ in html.anchors]
        for anchor, count in Counter(explicit).items():
            if count > 1:
                self.parse_errors.append((f"duplicate explicit anchor #{anchor}", 1))
        self.anchors = {platform: set(explicit) for platform in ("github", "mkdocs")}
        generated: dict[str, set[str]] = {platform: set() for platform in self.anchors}
        lines = mask_code(self.text, inline=False).splitlines()
        for index, line in enumerate(lines):
            match = HEADING.match(line)
            if match:
                level, title = len(match[1]), match[2]
            elif index and re.fullmatch(r" {0,3}(?:=+|-+)[ \t]*", line) and lines[index - 1].strip():
                level, title = (1 if "=" in line else 2), lines[index - 1].strip()
            else:
                continue
            self.headings.append((level, plain_heading(title), index + 1))
            attribute = re.search(r"\s*\{#([^\s}]+)(?:\s+[^}]*)?\}\s*$", title)
            for platform in self.anchors:
                if attribute and platform == "mkdocs":
                    anchor = attribute[1]
                    self.anchors[platform].add(anchor)
                    continue
                anchor = slug(title, platform)
                candidate, suffix = anchor, 0
                while candidate in generated[platform] or (platform == "mkdocs" and not candidate):
                    suffix += 1
                    candidate = anchor + ("-" if platform == "github" else "_") + str(suffix)
                if platform == "mkdocs" and candidate in explicit:
                    self.parse_errors.append((f"generated heading anchor #{candidate} duplicates an explicit HTML id", index + 1))
                generated[platform].add(candidate)
                self.anchors[platform].add(candidate)

        references = {}
        for match in REFERENCE.finditer(clean):
            references[" ".join(match[1].lower().split())] = match[2] if match[2] is not None else match[3]
        clean = REFERENCE.sub(lambda match: re.sub(r"[^\n]", " ", match.group()), clean)
        self.links = html.links
        occupied = []
        for match in LINK_START.finditer(clean):
            position, depth = match.end(), 0
            start = position
            if position < len(clean) and clean[position] == "<":
                end = clean.find(">", position + 1)
                target = clean[position + 1:end] if end != -1 else ""
                position = end + 1 if end != -1 else position
            else:
                while position < len(clean):
                    char = clean[position]
                    if char == "\\":
                        position += 2
                        continue
                    if char == "(":
                        depth += 1
                    elif char == ")":
                        if depth == 0:
                            break
                        depth -= 1
                    elif char.isspace() and depth == 0:
                        break
                    position += 1
                target = clean[start:position]
            self.links.append((target, clean.count("\n", 0, match.start()) + 1))
            occupied.append((match.start(), position))
        for match in BRACKETS.finditer(clean):
            if any(start <= match.start() < end for start, end in occupied):
                continue
            label = " ".join((match[2] or match[1]).lower().split())
            line = clean.count("\n", 0, match.start()) + 1
            if label in references:
                self.links.append((references[label], line))
            elif match[2] is not None:
                self.parse_errors.append((f"undefined link reference [{label}]", line))


def check(root: Path) -> int:
    errors: list[str] = []

    def error(path: Path, message: str, line: int = 1) -> None:
        errors.append(f"{path.relative_to(root)}:{line}: {message}")

    paths = sorted((root / "docs").rglob("*.md"))
    if not (root / "docs" / "index.md").is_file():
        error(root / "docs" / "index.md", "required documentation landing page is missing")
    readme = root / "README.md"
    if not readme.is_file():
        error(readme, "required README.md is missing")
    else:
        paths.append(readme)
    documents = {}
    for path in paths:
        try:
            documents[path] = Document(path, path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as exc:
            error(path, f"cannot read UTF-8 Markdown: {exc}")
    for doc in documents.values():
        for message, line in doc.parse_errors:
            error(doc.path, message, line)

    idea_dir = root / "docs" / "ideas"
    idea_docs = {path.stem: doc for path, doc in documents.items() if path.parent == idea_dir}
    for missing in sorted(EXPECTED_IDS - idea_docs.keys()):
        error(idea_dir / f"{missing}.md", "required idea is missing")
    for extra in sorted(idea_docs.keys() - EXPECTED_IDS):
        error(idea_docs[extra].path, "unexpected idea file or invalid ID")
    seen_ids = Counter()
    for idea_id, doc in idea_docs.items():
        h1 = [(title, line) for level, title, line in doc.headings if level == 1]
        if len(h1) != 1 or not re.fullmatch(re.escape(idea_id) + r"\s+\S.*", h1[0][0]):
            error(doc.path, f"expected one H1 beginning with {idea_id} and a title")
        for title, _ in h1:
            if match := re.match(r"([PHKAVROL]\d{2})\b", title):
                seen_ids[match[1]] += 1
        for label in METADATA:
            values = re.findall(r"^[ \t]*[-*][ \t]+\*\*" + re.escape(label) + r":\*\*[ \t]*(\S[^\n]*)$", doc.text, re.M)
            if len(values) != 1:
                error(doc.path, f"expected one nonempty metadata field: {label}")
            elif label == "Operating Mode" and values[0].strip() not in MODES:
                error(doc.path, f"unrecognized working mode: {values[0]}")
        h2 = [(title, line) for level, title, line in doc.headings if level == 2]
        for section in SECTIONS:
            matches = [line for title, line in h2 if title == section]
            if len(matches) != 1:
                error(doc.path, f"expected one H2 section: {section}")
                continue
            line = matches[0]
            end = next((number - 1 for level, _, number in doc.headings if number > line and level <= 2), len(doc.text.splitlines()))
            body = "\n".join(doc.text.splitlines()[line:end])
            if not re.sub(r"<[^>]*>|\s", "", body):
                error(doc.path, f"empty required section: {section}", line)
        for platform in doc.anchors:
            if idea_id.lower() not in doc.anchors[platform]:
                error(doc.path, f"missing portable idea anchor #{idea_id.lower()}")
                break
    for idea_id, count in seen_ids.items():
        if count != 1:
            error(idea_dir, f"idea ID {idea_id} occurs in {count} H1 headings")

    resolved: dict[Path, list[Path]] = {}
    link_count = 0
    for doc in documents.values():
        resolved[doc.path] = []
        for raw_target, line in doc.links:
            link_count += 1
            target = re.sub(r"\\([\\`*{}\[\]()#+\-.!_>])", r"\1", unescape(raw_target))
            try:
                url = urlsplit(target)
            except ValueError as exc:
                error(doc.path, f"invalid link {raw_target!r}: {exc}", line)
                continue
            if url.scheme or url.netloc:
                continue
            local_path = unquote(url.path)
            if local_path.startswith("/") or "\\" in local_path:
                error(doc.path, f"use a portable relative source link: {raw_target}", line)
                continue
            destination = (doc.path.parent / local_path).resolve() if local_path else doc.path
            if not destination.is_relative_to(root):
                error(doc.path, f"link escapes the repository: {raw_target}", line)
                continue
            if not destination.exists():
                error(doc.path, f"missing link target: {raw_target}", line)
                continue
            resolved[doc.path].append(destination)
            if not url.fragment:
                continue
            if destination.is_dir():
                destination = next((destination / name for name in ("index.md", "README.md") if (destination / name).is_file()), destination)
            if destination.suffix.lower() == ".md":
                linked = documents.get(destination)
                if linked is None:
                    linked = Document(destination, destination.read_text(encoding="utf-8"))
                fragment = unquote(url.fragment)
                missing_on = [platform for platform, anchors in linked.anchors.items() if fragment not in anchors]
                if missing_on:
                    error(doc.path, f"anchor #{fragment} missing on {' and '.join(missing_on)} in {destination.relative_to(root)}; use an explicit HTML id for shared anchors", line)

    def check_index(path: Path, expected: set[str]) -> None:
        if path not in documents:
            error(path, "required catalog index is missing")
            return
        actual = Counter(target.stem for target in resolved[path] if target.parent == idea_dir)
        for idea_id in sorted(expected):
            if actual[idea_id] != 1:
                error(path, f"expected one link to {idea_id}, found {actual[idea_id]}")
        for idea_id in sorted(actual.keys() - expected):
            error(path, f"unexpected idea link: {idea_id}")

    for prefix, stage in STAGES.items():
        check_index(root / "docs" / "stages" / f"{stage}.md", {f"{prefix}{number:02}" for number in range(1, 33)})
    for path in documents:
        if path.parent == root / "docs" / "stages" and path.stem not in STAGES.values():
            error(path, "unexpected stage file; the catalog has eight stages")
    check_index(root / "docs" / "idea-index.md", EXPECTED_IDS)
    if errors:
        print(f"Catalog validation failed with {len(errors)} error(s):", file=sys.stderr)
        for message in errors:
            print(f"  {message}", file=sys.stderr)
        return 1
    print(f"Catalog OK: {len(EXPECTED_IDS)} unique ideas, {len(STAGES)} stages, {len(documents)} Markdown files, {link_count} links checked.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1], help="repository root (default: parent of scripts)")
    args = parser.parse_args()
    return check(args.root.resolve())


if __name__ == "__main__":
    sys.exit(main())
