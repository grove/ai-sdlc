# Verification

Produce sufficient and verifiable evidence that a delivery meets requirements, withstands relevant errors and can be approved for intended use. AI helps find gaps, perform limited tests and explain results; approval is based on actual evidence and responsible professionals.

**The question in this step:** Do we have sufficient proof of correct and safe delivery?

**Typical delivery:** Traceable tests and professional assessments with documented residual uncertainty.

## Place in the learning loop

An idea to generate or select tests is a suggestion for control. Approval must be based on actual test results, a suitable test oracle and responsible assessment. Quality in AI verification must be evaluated itself, including with known errors and relevant counterexamples.

Previous step is [Agent execution](agent-execution.md). The next step is [Production](production.md). The loop is repeated when the experience provides the supporting evidence for a new improvement.

## Find an idea

The four theme areas provide different ways to explore this stage. Choose ideas that meet the project's problem, and adapt the working method and measurements to the risk and available basis. Each idea has its own example, control point and suggested impact targets.

- [Requirements and functional correctness](#v-category-1)
- [Safety and robustness](#v-category-2)
- [Specialized deliveries](#v-category-3)
- [Verification process and evidence](#v-category-4)

<a id="v-category-1"></a>

## Requirements and functional correctness

Link requirements to factual evidence and a clear picture of correct behavior. Investigate thresholds, condition, compatibility, migration and regressions with relevant test oracles.

- [V01 Track claims to actual test evidence](../ideas/V01.md)
- [V02 Clarify what is a correct result](../ideas/V02.md)
- [V03 Check properties that should apply to many cases](../ideas/V03.md)
- [V04 Find missing limit values and negative trends](../ideas/V04.md)
- [V05 Investigate concurrency and state-dependent errors](../ideas/V05.md)
- [V06 Check compatibility between producers and consumers](../ideas/V06.md)
- [V07 Compare old and new solution when migrating](../ideas/V07.md)
- [V08 Detect unintended changes in user history](../ideas/V08.md)

<a id="v-category-2"></a>

## Safety and robustness

Test safety limits and robustness under representative conditions. Control access, agent actions, dependencies, infrastructure, performance, availability and agreed data processing.

- [V09 Control authorization across roles and objects](../ideas/V09.md)
- [V10 Try to break the agent's instructions and tool limits](../ideas/V10.md)
- [V11 Consider dependencies and the origin of the delivery](../ideas/V11.md)
- [V12 Check configuration and infrastructure against requirements](../ideas/V12.md)
- [V13 Examine performance under representative loads](../ideas/V13.md)
- [V14 Verify error handling in dependencies](../ideas/V14.md)
- [V15 Consider accessibility in real tasks](../ideas/V15.md)
- [V16 Check that data is processed as agreed](../ideas/V16.md)

<a id="v-category-3"></a>

## Specialized deliveries

Adapt the verification to what is actually delivered. Data, reports, models, generative responses, agents, embedded systems, clients and packaged solutions need different proofs.

- [V17 Verify data quality throughout the pipeline](../ideas/V17.md)
- [V18 Verify that reports express correct business terms](../ideas/V18.md)
- [V19 Check whether a model has been tested on the right basis](../ideas/V19.md)
- [V20 Test source basis and waiver in generative responses](../ideas/V20.md)
- [V21 Control the agent's actions throughout the task](../ideas/V21.md)
- [V22 Prepare verification of embedded systems](../ideas/V22.md)
- [V23 Plan tests across client variants](../ideas/V23.md)
- [V24 Verify configured business processes](../ideas/V24.md)

<a id="v-category-4"></a>

## Verification process and evidence

Makes the control work itself more targeted and verifiable. Examine the tests' ability to find errors, the representativeness of the environment and the supporting evidence for professional approval.

- [V25 Sort test failures by probable cause](../ideas/V25.md)
- [V26 Investigate whether the tests actually detect errors](../ideas/V26.md)
- [V27 Give code review a targeted decision-making basis](../ideas/V27.md)
- [V28 Prioritize test order by change risk](../ideas/V28.md)
- [V29 Gather verifiable evidence of approval](../ideas/V29.md)
- [V30 Try documentation as an actual work assignment](../ideas/V30.md)
- [V31 Prepare realistic tests for user acceptance](../ideas/V31.md)
- [V32 Assess whether the test environment represents the target environment](../ideas/V32.md)

## Use the step in the project

Agree what is a correct result and what independent evidence the approval requires. Measure the inspection effort together with errors that are detected, errors that are overlooked and unnecessary rejections.

- [Find ideas based on the needs of the project](../guides/find-by-need.md).
- [Choose and measure a bounded experiment](../guides/impact-measurement.md).
- [Use the templates for selection and testing](../templates.md).
- [Read about working methods and common assumptions](../guides/how-to-use.md).

[See all 256 ideas in the register](../idea-index.md).

| Previous step in the learning loop | The next step in the learning loop |
| --- | --- |
|  [Agent execution](agent-execution.md)  |  [Production](production.md)  |
