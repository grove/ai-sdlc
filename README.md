# AI in the SDLC: 256 Practical Opportunities

**A searchable catalog of AI use cases across the software development life cycle (SDLC), grounded in measurable improvements to team effectiveness.**

[Browse the catalog](docs/index.md) · [Find opportunities by need](docs/guides/find-by-need.md) · [Explore all 256 ideas](docs/idea-index.md) · [Published site](https://grove.github.io/ai-sdlc/)

**The learning loop:** Problem → Hypothesis → Context → Agent Execution → Verification → Production → Observation → Learning.

The catalog is intended for developers, product teams, architects, quality and security specialists, platform engineers, and leaders. Every idea describes required inputs, prerequisites, a concrete example, safeguards, measurement suggestions, and relevant project types. AI adoption alone is not a benefit: the goal is demonstrably faster, lower-cost, higher-quality delivery with better outcomes.

## Explore the eight stages

| Stage | Ideas | Guiding question |
| --- | --- | --- |
| [Problem](docs/stages/problem.md) | P01–P32 | What problem is worth solving? |
| [Hypothesis](docs/stages/hypothesis.md) | H01–H32 | What measurable improvement do we expect? |
| [Context](docs/stages/context.md) | K01–K32 | Do people and agents have reliable, relevant context? |
| [Agent Execution](docs/stages/agent-execution.md) | A01–A32 | What work can AI safely perform within its authorized scope? |
| [Verification](docs/stages/verification.md) | V01–V32 | What evidence shows the result is correct and safe? |
| [Production](docs/stages/production.md) | R01–R32 | How can the change be released and adopted safely? |
| [Observation](docs/stages/observation.md) | O01–O32 | What changed after delivery, and how confident are we? |
| [Learning](docs/stages/learning.md) | L01–L32 | What should we improve in the next iteration? |

The letter R identifies Production to distinguish it from Problem (P). Idea IDs stay stable for reference in project backlogs, experiments, and lessons learned.

The catalog also includes [eight end-to-end workflows](docs/workflows.md), [16 project profiles](docs/project-profiles.md), an [impact measurement guide](docs/guides/impact-measurement.md), [templates](docs/templates.md), a [glossary](docs/glossary.md), and [source references](docs/sources.md).

## Use the catalog

1. Identify a meaningful problem supported by evidence.
2. Find relevant opportunities through the [needs guide](docs/guides/find-by-need.md) or [idea index](docs/idea-index.md).
3. Design a bounded experiment with a baseline, a primary metric, quality guardrails, and an accountable owner.
4. Follow the full learning loop, not merely the speed of initial AI output.
5. Record the actual impact, including human review, rework, model and infrastructure costs, and business or user outcomes.

Every idea is a candidate for local evaluation, not a promised benefit. Recovered capacity is not automatically a reduction in cash spending.

## Edit and contribute

The Markdown files under the docs directory are the maintained source of the published site. Each of the 256 ideas is a separate file in the docs/ideas directory.

- Preserve stable idea IDs and each idea's description, inputs, prerequisites, example, safeguards, measurements, operating mode, and project types.
- When changing an idea title or category, update the relevant stage overview and [idea index](docs/idea-index.md).
- Use relative Markdown links so that navigation works both on GitHub and on the generated site.
- Use explicit HTML IDs for anchors that must work consistently across both interfaces.
- Document outcomes with measurement methods, limitations, and decision criteria.

See [catalog maintenance](docs/maintenance.md) for how to add new evidence and ideas.

## Build and preview locally

Use Python 3.12, then run the following commands:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-docs.txt
python scripts/check_catalog.py
python -m mkdocs build --strict
python -m mkdocs serve
```

On Windows, activate the environment using `.venv\\Scripts\\Activate.ps1` in PowerShell. MkDocs prints a local preview URL when the server starts. Do not commit generated site files or the local virtual environment.

The catalog check verifies stable IDs, required fields, stage indexes, the idea index, and internal links. The strict MkDocs build validates navigation and linked anchors.

## Publish on GitHub Pages

The [documentation workflow](.github/workflows/docs.yml) validates pull requests. It deploys only after a change reaches main or on a manual run from main.

**One-time setup:** In repository **Settings → Pages → Build and deployment**, set **Source** to **GitHub Actions**. Once merged and deployed, the site is available at [https://grove.github.io/ai-sdlc/](https://grove.github.io/ai-sdlc/). GitHub Pages environment approvals, if configured, still apply.

The workflow uses GitHub's built-in token, restricts write permissions to deployment, and pins its build dependencies and actions.

See [GitHub's custom Pages workflow guidance](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) and the [MkDocs deployment guide](https://www.mkdocs.org/user-guide/deploying-your-docs/).

## License

[Apache License 2.0](LICENSE).
