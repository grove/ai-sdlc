# Choose and measure a bounded experiment

<a id="section-1"></a>

## Clarify why this particular idea should be tried

First describe the problem with an example from your own project. Then choose an idea that affects this problem and clarify what will be easier, faster or more correct. If a simple rule, a script or clearer responsibility solves the problem better, there is a relevant alternative to compare with.

|  **Assessment**  |  **Questions the project must answer**  |
| --- | --- |
| Value | Who gets a better outcome, and how big is the problem today? |
| Volume and variety | Does the task repeat itself often enough, and are the cases comparable? |
| Context | Are there authoritative requirements, data and examples that the team is allowed to use? |
| Verification | How can another person or a controlled tool determine whether the result is correct? |
| Risk | What is the consequence of an incorrect answer or an unexpected action, and can the damage be limited? |
| Effort | What is the cost of setup, integration, training, control and maintenance? |
| Measurement | Do we have a baseline, data quality and a credible basis for comparison? |
| Ownership | Who approves the result, follows the measurement and changes practice after the experiment? |

Consider the criteria with specific reasons. Avoid an overall score that hides the fact that a critical requirement has not been met. A trial should have one clear primary effect, a few quality or risk limits, and a date for decision.

<a id="section-2"></a>

## Measure both the local task and the outcome of the delivery

The measurement proposal in each idea is a starting point. Define numerator, denominator, unit, time window, start and end, data source and owner before the experiment. Separate active working time from calendar and waiting time. Also count rejected attempts, control work, interruptions and error correction.

For ideas that aid analysis or decision-making, such as [P01](../ideas/P01.md), [P31](../ideas/P31.md) and [H01](../ideas/H01.md), shorter analysis time is a local goal. Also follow whether the decision later resulted in relevant work, fewer rematches or better user outcomes. A hasty, erroneous decision-making basis is no improvement.

SPACE describes developer productivity as multidimensional. Therefore, the team should look at task outcomes together with quality, collaboration, flow and work experience. Use team and task level with clear purpose; The number of prompts, code suggestions or lines of code is diagnostic and does not alone provide proof of value. [2](../sources.md#source-2)

|  **Dimension**  |  **Examples of performance measures**  |  **A balancing act**  |
| --- | --- | --- |
| Time | Active effort and time from clear task to accepted use. | Rework and errors after acceptance. |
| Capacity | Accepted comparable deliveries per period. | Task mix, quality and age of unfinished work. |
| Cost | Total cost per accepted task or useful transaction. | Maintenance, control and subsequent operating costs. |
| Quality | Correct problem solving and errors with known severity. | Errors that the control overlooks and unnecessary rejections. |
| User value | Completed user task, correct decision or reduced casework. | Availability, need for support and negative consequences. |
| People | Perceived friction, understanding and necessary control work. | Safety, learning and representativeness of the answers. |

<a id="section-3"></a>

## Use delivery targets where appropriate

For a service or application with a production rollout, DORA describes five measures: change lead time, rollout frequency, time to recovery after a failed rollout, change failure rate and proportion of rollouts that are unplanned work after production incidents. Use them in the context of the service and together with product outcomes. For documents and formal decisions, the team uses corresponding local acceptance and quality measures, without referring to them as DORA. [1](../sources.md#source-1)

<a id="section-4"></a>

## Make the comparison credible

Register hypothesis and analysis plan before the results arrive. When practical, use random assignment of comparable tasks or a controlled phased induction. Comparing before and after can provide useful learning, but staffing, task mix, season, training and other measures can explain the change. Show the number of observations, variation, data gaps and uncertainty. Define later follow-up when errors or value show up slowly.

AI can provide analysis and code, but outcomes and intervals must be calculated from actual data in verifiable tools. A linguistically plausible explanation is not proof of effect. Use analytical skills when the experiment requires a statistical method, and continue measurement when the data base is not sufficient.

<a id="section-5"></a>

## Calculate net resource use

Net freed up working time is saved effort minus new effort for context, agent follow-up, control, error correction and operation. Total cost also includes licenses, model use, infrastructure, integration, training and maintenance. State period and distribution assumptions. The same bet shall only be counted once.

Illustration: If comparable tasks use 40 fewer hours, but the experiment requires 9 hours of additional checking, 5 hours of context maintenance and 4 hours of error correction, the net freed up capacity is 22 hours. Model and license costs are added in NOK. The figures illustrate the calculation method and are not an expected profit. Saving cash actually requires reduced spending; Freed-up hours can also provide value through other prioritized work.

<a id="section-6"></a>

## Make an explicit decision

|  **What you observe**  |  **Recommended next action**  |
| --- | --- |
| Positive effect with sufficient basis and fulfilled limits | Expand to the next defined task group and follow the duration. |
| Promising effect but uncertain basis | Continue measurement or improve experimental design before scaling. |
| Small or negative net effect | Adjust the limit, try an easier option, or quit. |
| Breach of critical quality, access or security | Stop affected use, handle deviations and reconsider design. |
| Missing data or unclear outcome | Improve the measurement baseline and leave the gain as undecided. |

[To the start of the catalog](../index.md) · [All the ideas](../idea-index.md)
