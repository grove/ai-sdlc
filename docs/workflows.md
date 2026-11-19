# Put the ideas together in a workflow

A single idea can bring local benefit. The workflows below show how several ideas can be connected to a full learning loop. They are suggestions for setup, and the results must be measured in the relevant project. Use a stable experiment identifier from problem card to learning record.

<a id="section-1"></a>

## Faster and safer changes to APIs

The team spends a lot of time on contract clarifications and finds compatibility errors late. Try one type of bounded API change with explicit contract and separate checkpoints.

|  **Rise**  |  **Idea**  |  **Practical use**  |
| --- | --- | --- |
| Problem |  [P20](ideas/P20.md)  | Find which interfaces create repeated clarification and errors. |
| Hypothesis |  [H23](ideas/H23.md)  | Try whether a better contract context reduces overall work. |
| Context |  [K06](ideas/K06.md)  | Gather current interfaces, versions and consumer requirements. |
| Agent execution |  [A17](ideas/A17.md)  | Create a limited proposal for the client or adapter. |
| Verification |  [V06](ideas/V06.md)  | Check compatibility with actual producers and consumers. |
| Production |  [R13](ideas/R13.md)  | Coordinate publishing and consumer transition. |
| Observation |  [O09](ideas/O09.md)  | Measure time for accepted use and necessary clarifications. |
| Learning |  [L09](ideas/L09.md)  | Update the recipe with validated requirements and error types. |

Primary goal: overall time to correct integration. Guardrail metrics: breach of contract, error correction, manual handling and actual use by the recipient.

<a id="section-2"></a>

## Better flow in a team with a growing review queue

AI has made it easy to produce change proposals, while code review stops deliveries. Try minor changes and a structured review guide on comparable cases.

|  **Rise**  |  **Idea**  |  **Practical use**  |
| --- | --- | --- |
| Problem |  [P11](ideas/P11.md)  | Describe review waiting and why changes are sent back. |
| Hypothesis |  [H24](ideas/H24.md)  | Test a different distribution of the verification work. |
| Context |  [K15](ideas/K15.md)  | Refine changes and make the approval criteria clear. |
| Agent execution |  [A01](ideas/A01.md)  | Make a small change proposal within the mandate. |
| Verification |  [V27](ideas/V27.md)  | Give the code owner a precise guide to decision and risk. |
| Production |  [R08](ideas/R08.md)  | Deliver the actual verified artifact. |
| Observation |  [O11](ideas/O11.md)  | Measure review, rework and eliminate errors together. |
| Learning |  [L24](ideas/L24.md)  | Make stable control tasks easier to automate. |

Primary goal: total time for review and rework per accepted change. Control measures: serious errors, age of the queue and total lead time.

<a id="section-3"></a>

## Controlled modernization of an older system

A project will upgrade technology without losing little documented behavior. Choose a limited module with an understandable interface and the possibility of parallel comparison.

|  **Rise**  |  **Idea**  |  **Practical use**  |
| --- | --- | --- |
| Problem |  [P17](ideas/P17.md)  | Find the area of high actual cost of change. |
| Hypothesis |  [H26](ideas/H26.md)  | Design a reversible sample with clear boundaries. |
| Context |  [K03](ideas/K03.md)  | Document actual behavior and known exceptions. |
| Agent execution |  [A12](ideas/A12.md)  | Create a migration proposal with limited scope. |
| Verification |  [V07](ideas/V07.md)  | Compare old and new results with suitable oracle. |
| Production |  [R12](ideas/R12.md)  | Plan controlled switching and reconciliation. |
| Observation |  [O29](ideas/O29.md)  | Also follow later maintenance and errors. |
| Learning |  [L08](ideas/L08.md)  | Weigh short-term gain against long-term labor cost. |

Primary objective: total cost of correct migration and subsequent changes. Guardrail metrics: behavioral anomalies, data integrity and real recoverability.

<a id="section-4"></a>

## More reliable data and reports

Data becomes available quickly, but report recipients must check and correct numbers manually. Try one pipeline and one key business concept, with concrete reconciliations.

|  **Rise**  |  **Idea**  |  **Practical use**  |
| --- | --- | --- |
| Problem |  [P21](ideas/P21.md)  | Link the data quality problem to an actual consequence. |
| Hypothesis |  [H09](ideas/H09.md)  | Choose the correct report outcome and control of manual efforts. |
| Context |  [K04](ideas/K04.md)  | Clarify terms, rules and data origin. |
| Agent execution |  [A19](ideas/A19.md)  | Create transformation and explicit data controls. |
| Verification |  [V18](ideas/V18.md)  | Try whether the calculation expresses the correct business concept. |
| Production |  [R24](ideas/R24.md)  | Publish approved version with owner and data agreement. |
| Observation |  [O22](ideas/O22.md)  | Monitor data quality and downstream deviations. |
| Learning |  [L10](ideas/L10.md)  | Update context with validated rules and examples. |

Primary objective: time to correct and used data delivery. Guardrail metrics: manual corrections, errors in decisions, data access and operating cost.

<a id="section-5"></a>

## Less repetitive troubleshooting in operation

The team handles the same incidents repeatedly. Try AI-supported incident understanding and documentation, with production intervention under existing emergency rules.

|  **Rise**  |  **Idea**  |  **Practical use**  |
| --- | --- | --- |
| Problem |  [P18](ideas/P18.md)  | Find a confirmed recurring operating pattern. |
| Hypothesis |  [H20](ideas/H20.md)  | Include error consequences and control costs in the experiment. |
| Context |  [K07](ideas/K07.md)  | Collect service maps and relevant operational context. |
| Agent execution |  [A09](ideas/A09.md)  | Create a fix for a reproducible bug. |
| Verification |  [V14](ideas/V14.md)  | Try errors in dependencies and expected recovery. |
| Production |  [R17](ideas/R17.md)  | Update and practice the operating procedure. |
| Observation |  [O17](ideas/O17.md)  | Measure the time to correct fault delineation and actual recovery. |
| Learning |  [L12](ideas/L12.md)  | Turn incident findings into preventive tests and controls. |

Primary measures: recurrence rate and total handling time. Control targets: incorrect interventions, data loss, overlooked alarms and maintenance work.

<a id="section-6"></a>

## A better AI-based search product

The product itself contains AI and must provide relevant answers with the correct source basis. Keep product quality separate from whether the developers use AI in their work.

|  **Rise**  |  **Idea**  |  **Practical use**  |
| --- | --- | --- |
| Problem |  [P01](ideas/P01.md)  | Collect validated user questions that are not resolved well. |
| Hypothesis |  [H30](ideas/H30.md)  | Define product trials with the correct task outcome. |
| Context |  [K19](ideas/K19.md)  | Limit sources and access for the actual user. |
| Agent execution |  [A22](ideas/A22.md)  | Implement a small product change with clear boundaries. |
| Verification |  [V20](ideas/V20.md)  | Test the source basis, correctness and expected deviation. |
| Production |  [R24](ideas/R24.md)  | Publish approved model and data versions. |
| Observation |  [O23](ideas/O23.md)  | Track validated task success and differences between use cases. |
| Learning |  [L18](ideas/L18.md)  | Improve retrieval and test the change on your own evaluations. |

Primary goal: correctly solved user task. Control measures: misinformation, access, unwanted rejection, response time and cost per useful response.

<a id="section-7"></a>

## Better basis for decision-making without code delivery

A preliminary project or architectural team must clarify a choice of route. Production means that a named recipient accepts and uses the decision basis.

|  **Rise**  |  **Idea**  |  **Practical use**  |
| --- | --- | --- |
| Problem |  [P28](ideas/P28.md)  | Describe what uncertainty is blocking the decision. |
| Hypothesis |  [H29](ideas/H29.md)  | Agree on how the analysis will improve decision-making. |
| Context |  [K05](ideas/K05.md)  | Gather current decisions and justifications. |
| Agent execution |  [A32](ideas/A32.md)  | Create models and comparable options. |
| Verification |  [V30](ideas/V30.md)  | Try the document as an actual assignment for the recipient. |
| Production |  [R23](ideas/R23.md)  | Deliver the correct version for the intended use. |
| Observation |  [O06](ideas/O06.md)  | Follow decision time and recorded rematches. |
| Learning |  [L01](ideas/L01.md)  | Clarify what was learned and what questions remain. |

Primary goal: time to professionally clarified decision. Guardrail metrics: source quality, significant errors, subsequent rematches and actual application.

<a id="section-8"></a>

## Safe introduction of a configured business process

A project changes ERP or another package solution. The solution must work with local roles, data and integrations, even when the supplier's standard tests are green.

|  **Rise**  |  **Idea**  |  **Practical use**  |
| --- | --- | --- |
| Problem |  [P05](ideas/P05.md)  | Map manual duplication and process errors. |
| Hypothesis |  [H17](ideas/H17.md)  | Calculate potential and additional control cost. |
| Context |  [K09](ideas/K09.md)  | Link the rules to concrete acceptance criteria. |
| Agent execution |  [A08](ideas/A08.md)  | Make suggestions for configuration or rule changes. |
| Verification |  [V24](ideas/V24.md)  | Test actual end-to-end processes with relevant roles. |
| Production |  [R16](ideas/R16.md)  | Only transfer approved configuration with traceability. |
| Observation |  [O07](ideas/O07.md)  | Follow work effort also in receiving processes. |
| Learning |  [L26](ideas/L26.md)  | Standardize only where local conditions are comparable. |

Primary objective: total effort per correct process outcome. Guardrail metrics: manual bypasses, authorization, integration errors and upgradeability.

[To the start of the catalog](index.md) · [All the ideas](idea-index.md)
