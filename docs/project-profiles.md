# Adapt the ideas to the project

The methodology can be Scrum, Kanban, waterfall, a program or ongoing maintenance. Adjust timing and formalization, but keep the connection between problem, expected effect, actual delivery and learning. The project tags in the catalog are a search aid and do not indicate exhaustive limitations.

|  **Project profile**  |  **Important local adaptation**  |  **Examples**  |
| --- | --- | --- |
| New digital products | Start with needs and a small prototype. Measure actual user task and learning before full build. |  [P02](ideas/P02.md)  [H06](ideas/H06.md)  [A02](ideas/A02.md)  [V31](ideas/V31.md)  [O01](ideas/O01.md)  |
| Existing products and services | Consider users, contracts and historical behavior. Measure the entire flow and subsequent errors. |  [K02](ideas/K02.md)  [A01](ideas/A01.md)  [V08](ideas/V08.md)  [R09](ideas/R09.md)  [O09](ideas/O09.md)  |
| Older systems and mainframes | Clarify actual rules, data types, batch windows and hidden dependencies. Use differential comparison. |  [P17](ideas/P17.md)  [K03](ideas/K03.md)  [A12](ideas/A12.md)  [V07](ideas/V07.md)  [R12](ideas/R12.md)  |
| Integrations and APIs | Make ownership, contracts and consumer transition explicit. Try timeouts, duplicates, and partial errors. |  [K06](ideas/K06.md)  [A17](ideas/A17.md)  [A18](ideas/A18.md)  [V06](ideas/V06.md)  [R13](ideas/R13.md)  |
| Data analysis and reporting | Maintain definitions, data origin and quality throughout the chain. Test against actual business rules. |  [K04](ideas/K04.md)  [A19](ideas/A19.md)  [V17](ideas/V17.md)  [V18](ideas/V18.md)  [O22](ideas/O22.md)  |
| AI and machine learning in the product | Separate development assistance from the product's model. Evaluate data, predictions or responses and human takeover. |  [H30](ideas/H30.md)  [A21](ideas/A21.md)  [A22](ideas/A22.md)  [V19](ideas/V19.md)  [V20](ideas/V20.md)  |
| Platform infrastructure and DevOps | Try changes in isolation, with policy and plan. Include self-service, operation and recovery. |  [K22](ideas/K22.md)  [A25](ideas/A25.md)  [A26](ideas/A26.md)  [V12](ideas/V12.md)  [R32](ideas/R32.md)  |
| Mobile client and offline use | Try device variation, local storage, sync and upgrade. Distribution may be delayed or offline. |  [A06](ideas/A06.md)  [V23](ideas/V23.md)  [R14](ideas/R14.md)  [O04](ideas/O04.md)  [O30](ideas/O30.md)  |
| Embedded OT and IoT | Use relevant hardware or validated simulator, secure stop modes and traceable authentication. Field update can be expensive. |  [P24](ideas/P24.md)  [H31](ideas/H31.md)  [A07](ideas/A07.md)  [V22](ideas/V22.md)  [R15](ideas/R15.md)  |
| ERP off-the-shelf and low code | Test local roles, configuration and integrations. Check provider restrictions and future upgrade. |  [A08](ideas/A08.md)  [V24](ideas/V24.md)  [R16](ideas/R16.md)  [O07](ideas/O07.md)  [L08](ideas/L08.md)  |
| Regulated or safety-critical work | Maintain requirements traceability, independent evidence and required sign-off. Expand control based on the consequences of errors. |  [K12](ideas/K12.md)  [K13](ideas/K13.md)  [V01](ideas/V01.md)  [V29](ideas/V29.md)  [R07](ideas/R07.md)  |
| Research and scientific calculations | Use dimensional analysis, known results, numerical stability, reproducibility and independent professional judgment. |  [H05](ideas/H05.md)  [A20](ideas/A20.md)  [A32](ideas/A32.md)  [V02](ideas/V02.md)  [V03](ideas/V03.md)  |
| Game simulation and visual systems | Try rules, condition, performance, content and variation in units. Combine automated checks with actual usage tests. |  [A02](ideas/A02.md)  [A03](ideas/A03.md)  [V05](ideas/V05.md)  [V08](ideas/V08.md)  [V13](ideas/V13.md)  |
| Architecture, discovery, and decision documents | Define a named recipient and decision. Measure correctness, usefulness in later work and reduced need for clarification. |  [H29](ideas/H29.md)  [A29](ideas/A29.md)  [A32](ideas/A32.md)  [V30](ideas/V30.md)  [R23](ideas/R23.md)  |
| Operations and incident response | Link support and incidents to confirmed errors and prevention. Separate analysis from authorized production intervention. |  [P18](ideas/P18.md)  [P30](ideas/P30.md)  [O17](ideas/O17.md)  [R26](ideas/R26.md)  [L12](ideas/L12.md)  |
| Migration, transition, and retirement | Map dependencies, history and data retention. Try transition, reconciliation and recovery before removing old solution. |  [A13](ideas/A13.md)  [A16](ideas/A16.md)  [V07](ideas/V07.md)  [R27](ideas/R27.md)  [R31](ideas/R31.md)  |

<a id="section-1"></a>

## Working conditions that change the layout

|  **Condition**  |  **Customize this way**  |
| --- | --- |
| Sensitive data or offline environment | Only use approved treatment center and data. Prepare local source packages, package archive and tools without assuming web access. |
| Little history or few deliveries | Start with task tests and qualitative findings. Show the uncertainty and plan longer observation instead of asserting a certain effect. |
| Large deliveries with few production windows | Try parts of the loop in simulator or representative environment. Include integration and observation after the actual introduction. |
| Many teams and external suppliers | Clarify data rights, contracts, boundaries and who owns measurements. Do not transfer profit or risk to the recipient without following it. |
| Accessibility and multiple languages | Use actually relevant users and aids, and professionally checked translations. An automatic check does not cover all user needs. [7](sources.md#source-7)  |
| Long life or infrequent use | Schedule checking of archives, recovery, expired dependencies and rare workflows even after the project is finished. |

<a id="section-2"></a>

## Expand an idea with a concrete variant

Combine work task, artefact, user group and risk condition. [A29](ideas/A29.md) for example, could be maintaining an installation guide for an offline customer environment. [V03](ideas/V03.md) can become a check of conservation laws in a simulator. [A24](ideas/A24.md) can become synthetic geographic datasets or event streams. Keep the same requirements for foundation, control and effect measurement as in the original idea.

[To the start of the catalog](index.md) · [All the ideas](idea-index.md)
