# Templates for Practical AI Experiments

These templates connect an AI opportunity to a verifiable outcome and a learning decision. Copy and adapt them to your project.

<a id="section-1"></a>

## Idea Brief

**Idea and project:** Catalog ID, local name, team, accountable owner, and date.

**Problem and affected users:** Observed issue, affected population, existing cost, and consequences.

**Current process:** How the task is done, volume, effort, lead time, current quality, and relevant variations.

**Proposed AI contribution:** What AI will analyze, draft, or execute and the specific output it should produce.

**Approved inputs:** Authoritative sources, versions, data classification, rights to use the data, authorized access, and required tools.

**Review and accountability:** Who assesses the output, required checks, and prohibited agent actions.

**Prerequisites and uncertainties:** What must exist before testing and which assumptions remain unverified.

**Next decision:** Owner and date for deciding whether to test, refine, adopt, or reject the idea.

<a id="section-2"></a>

## Experiment Brief

**Hypothesis:** If we change [process], we expect [outcome] because [causal mechanism].

**Population and comparison:** Eligible tasks, selection criteria, baseline or comparison group, and concurrent changes that could bias results.

**Primary metric:** Operational definition, units, numerator and denominator where applicable, data source, baseline, and minimum meaningful improvement.

**Guardrail metrics:** Quality, security, cost, human review burden, and explicit stop conditions appropriate to the risk.

**Effort and cost budget:** Setup, context engineering, execution, licenses, review, debugging, support, and operations. Distinguish one-time from recurring costs.

**Verification:** Acceptance criteria, reliable test oracle, actual checks performed, and who is authorized to approve the result.

**Observation and decision:** Measurement window, required data quality, decision date, accountable owner, and follow-up date.

**Learning update:** Which template, automated test, agent instruction, tool configuration, or workflow will change if the hypothesis is supported.

<a id="section-3"></a>

## Reusable Agent Task Instruction

Adapt this instruction to a bounded assignment. Written instructions do not replace technical access controls.

**Task:** Help with [idea ID and specific task]. Produce [verifiable output] for [recipient].

**Inputs:** Use only [approved sources and versions]. Cite source material for important claims.

**Authorization:** You may [allowed actions, tools, and file locations]. Changes outside this scope require approval from [role].

**Uncertainty:** Identify missing inputs and ask specific questions. Distinguish facts from assumptions and recommendations.

**Output:** Return [artifact], rationale, relevant alternatives, required checks, and anything not verified.

**Stop conditions:** Stop and request guidance when [risk trigger], authorization is missing, or the [time or cost] limit is reached.

**Acceptance:** [Role] assesses the output against [criteria]. Report only tests and reviews that actually ran.

<a id="section-4"></a>

## Experiment Learning Record

**Observed results:** Metrics, sample, observation window, data quality, and any missing evidence.

**Measured impact:** Primary outcome, guardrails, total effort and costs, uncertainty, and plausible alternative explanations.

**Decision:** Adopt, revise, extend measurement, scale, or stop. Include an accountable owner and justification.

**Updated practice:** Exact document, test, instruction, or workflow updated, including version and effective date.

**Follow-up:** How the team will check ongoing adoption, sustained impact, and emerging adverse effects.

[Catalog home](index.md) · [All 256 ideas](idea-index.md)
