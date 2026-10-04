# Zeest FYP report plan — Phase 1

Status: Setup is complete. The user approved the three-person folder structure and path-only assembly changes on 4 October 2026. Read README.md and your own START_HERE.md for current locations. Original setup evidence is archived outside the repository. Chapter writing has not started.

### Phase 2 working decisions (student-authorized assumptions)

| Question | Assumption used for setup |
|---|---|
| Q1 | [Likely] FYP-1, following the supplied rules. |
| Q2 | [Likely] R&D; retain both development and research coverage. |
| Q3 | [Guessing] Member A = Kashaf Ali; B = Fatima Malik; C = Eesha Irfan, following proposal order. Put these names in owner comments. |
| Q4 | [Certain] Retain every original chapter and section in Phase 2, including deferred FYP-2 sections. |
| Q5 | [Certain] Detailed model, language, knowledge-base and framework-role choices remain TBD; no implementation choice is needed for splitting files. |
| Q6 | [Certain] Do not assume approved dataset access or available clinical reviewers. These remain unresolved dependencies. |
| Q7 | [Certain] Leave hardware, numerical targets, case counts, dates and observed results unspecified. The prototype remains unbuilt. |
| Q8 | [Likely] Preserve the proposal's physician-reviewed diagnosis/treatment-plan scope without adding dosing, follow-up or investigation modules. |
| Q9 | [Certain] Preserve original metadata placeholders during setup and freeze main.tex afterward. Filling metadata would require a later explicit exception to that freeze. |
| Q10 | [Certain] Preserve all demonstration headings and appendix content for the comparison; later content writing is not authorized by this setup instruction. |
| Q11 | [Likely] Prefer the research summary format for later R&D evaluation coverage; conservatively do not rely on tool/dataset descriptions alone to meet the 15-work requirement. Both original example tables remain unchanged now. |
| Q12 | [Certain] Use a workspace-local compiler and PDF renderer if no existing toolchain is available. Preserve source/class/package choices and use the same engine for both builds. |

These are working decisions, not newly established project facts. No assumption supplies fabricated results, resources, access rights or references.

Report stage: **FYP-1 (working assumption)**. `Rules.txt` says “Latex Report (Overleaf) FYP 1”; the students authorized making assumptions for setup. This is not an independently confirmed departmental classification.

Project classification: **Research and Development (R&D), working assumption**. The proposal combines a software prototype with comparative research questions and an ablation framework. Use full research and development coverage conservatively; retain every original chapter during setup.

## 1. Sources and authority

The report structure comes from [main.tex](Report%20template/main.tex), formatting from [FastFyp.cls](Report%20template/FastFyp.cls), and local writing constraints from [Rules.txt](Rules.txt). Project facts come only from [F26-098.docx](F26-098.docx). Its supplied five-page PDF was cross-checked against the extracted DOCX text.

The proposal identifies the project as **Zeest: An Agentic Medical Copilot**, advisor **Miss Umm-e-Ammarah**, and students **Kashaf Ali (23L-0691)**, **Fatima Malik (23L-0826)**, and **Eesha Irfan (23L-0836)**. These identities do not establish which student is Member A, B, or C.

The six sample reports were read through their extracted text: ImageSense (90 pages), JobLens (75), ParkEase (88), RahZil (65), Recruit Ease (122), and SynapSure (73), totaling 513 pages. Review covered front matter, chapter inventories, prose, captions, tables, and references; truncated passages were reread. Embedded screenshot and diagram pixels have not received a complete visual audit, so this plan makes no claim about their visual fidelity. Their project facts, numerical results, extra headings, and apparent formatting exceptions are not transferable to Zeest. In particular, several samples add a Sequence Diagrams section or individual use-case headings that this template does not authorize.

`context.txt` was inspected as prior discussion, not a project source. For example, its patient portal, knowledge graph, model training, deployment options, and broader proposed outputs cannot expand the signed proposal's scope. The sample BibTeX entries in `fypbib.bib` are template examples, not Zeest references.

### Rules to enforce when writing is separately authorized

- Preserve fixed chapter/section names, sequence, hierarchy, and front matter; change only genuine content placeholders.
- Never edit `FastFyp.cls` or add packages. The class already supports `\textcolor{red}{...}`, figures, tables, algorithms, and three numbered heading levels.
- Keep title page, blank page, Anti-Plagiarism Declaration, Author's Declaration, Abstract, Executive Summary, Table of Contents, List of Figures, and List of Tables in their present sequence.
- Keep body headings numbered. The template's unnumbered front-matter headings are explicit exceptions to the general rules-file instruction.
- Use 150–250 words for ordinary prose paragraphs. The template's Abstract requirement takes precedence: one paragraph, 50–125 words, three to five sentences. Executive Summary: one to two pages, plain prose for a business audience.
- Do not use bold prose as a substitute for headings; avoid decorative emphasis. Class-generated heading/caption styles remain unchanged.
- Keep bullets within one rendered line. Use prose where longer explanation is necessary.
- Use a single descriptive caption for each figure/table, without subcaptions. The template calls the accessibility description a “sub-caption”; interpret this as descriptive text in the ordinary caption, consistent with `Rules.txt`.
- Introduce and reference every figure; use `\label`, `\ref`, and `\cite` rather than hard-coded numbering. Let floats move normally.
- Give chapters introductory and concluding prose without adding a new Conclusion heading where none exists. End Introduction with a paragraph outlining the report.
- Review at least 15 distinct relevant projects/papers, with verified citations, before presenting the proposed approach in detail. Chapter 2 necessarily precedes Chapter 3 under the template; do not reorder chapters to interpret the rules literally.
- Keep `ieeetr`. Cite external claims and methods accurately; do not attach example citations to invented descriptions.

## 2. Chapter applicability and exact structure

Numbers below describe the **unchanged ten-chapter template**, not a promise of final numbering if the department later authorizes exclusion of conditional chapters. For Phase 2, retain all ten chapters and the demo appendix exactly to preserve the original PDF. No conditional deletion is part of setup.

“Deferred” means the template assigns substantive material to FYP-II. Retain the heading in the mechanical split; later writing may use a clearly marked planned placeholder if the department requires the heading to remain in FYP-1.

| No. | Exact chapter title | Template project-type rule | FYP-1 treatment | FYP-2 treatment | Owner |
|---|---|---|---|---|---|
| 1 | Introduction | Mandatory | Required | Required | A |
| 2 | Project Vision | Mandatory; 2.7–2.9 optional for Research, compulsory for Development | Required; conditional subsections retained pending classification | Required | A |
| 3 | Literature Review / Related Work | Mandatory | Required; at least 15 distinct relevant works | Required, updated evidence | B |
| 4 | Software Requirement Specifications | Optional for Research; compulsory for Development | Include for this proposed software system; official R&D interpretation pending | Include, reflect verified system | A |
| 5 | Proposed Approach and Methodology | Optional for Development; compulsory for Research | Include for the proposal's ablation/research questions | Include, document actual procedure | B |
| 6 | High-Level and Low-Level Design | Explicitly compulsory for R&D and Development; pure Research not explicitly resolved | Required for likely R&D | Required | C |
| 7 | Implementation and Test Cases | No overall project-type exemption stated; FYP-1 may describe prototype | Prototype is unbuilt: planned description; test-case section deferred | Required implementation description and test evidence; use planned labels until built/executed | C |
| 8 | User Manual | FYP-II; optional for Research, compulsory for Development | Deferred; planned placeholder only if retained for submission | Required for Development; R&D interpretation pending | A |
| 9 | Experimental Results and Discussion | FYP-II; optional for Development, compulsory for Research | Deferred; planned evaluation only if retained | Include for proposal's research questions; no results before execution | B |
| 10 | Conclusions | Mandatory; FYP-1 must list FYP-2 work plan | Required; conclude planning status and give FYP-2 plan | Required; conclusions supported by evidence | A |

### Fixed sections and subordinate headings

Keep the following names and order. Spaces at the start of two original titles and the original long Database Design heading remain untouched during setup.

**Chapter 1:** 1.1 Purpose of this Document; 1.2 Intended Audience; 1.3 Definitions, Acronyms, and Abbreviations; 1.4 Conclusion.

**Chapter 2:** 2.1 Problem Domain Overview; 2.2 Problem Statement; 2.3 Problem Elaboration; 2.4 Goals and Objectives; 2.5 Project Scope; 2.6 Sustainable Development Goal (SDG); 2.7 Constraints; 2.8 Business Opportunity; 2.9 Stakeholders Description/ User Characteristics; 2.9.1 Stakeholders Summary; 2.9.2 Key High-Level Goals and Problems of Stakeholders.

**Chapter 3:** 3.1 Definitions, Acronyms, and Abbreviations; 3.2 Detailed Literature Review; 3.3 Literature Review Summary Table; 3.4 Conclusion. Under 3.2, the “Related Research Work 1 / Related Development Project ...” and two “Example LR ...” subsections are explicit demonstration placeholders. Later replace those examples with numbered reviews of actual verified proposal-listed works; retain the required parent sections. No sample customer-service content belongs in Zeest.

**Chapter 4:** 4.1 List of Features; 4.2 Functional Requirements; 4.3 Quality Attributes; 4.4 Non-Functional Requirements; 4.5 Assumptions; 4.6 Use Cases; 4.7 Hardware and Software Requirements; 4.7.1 Hardware Requirements; 4.7.2 Software Requirements; 4.8 Graphical User Interface; 4.9 Database Design (if required; this means if you are using noSQL, you will not provide ER but the other design element and data dictonary should still be there. Explain and elaborate your DB design); 4.9.1 ER Diagram; 4.9.2 Data Dictionary; 4.10 Risk Analysis (source title begins with a space).

PostgreSQL is in the proposal, so the ER diagram and data dictionary apply. The use-case tables must follow the provided fields and remain together under Use Cases; do not add one heading per use case. GUI pictures must identify their doctor user and mapped use cases. Hardware quantities, latency, user capacity, and storage sizes are not specified and remain unset.

**Chapter 5:** No section headings supplied. Explain the proposed procedural approach in chapter prose, figures, tables, and existing algorithm notation. Do not invent a new section hierarchy.

**Chapter 6:** 6.1 System Overview; 6.2 Design Considerations; 6.2.1 Assumptions and Dependencies; 6.2.2 General Constraints; 6.2.3 Goals and Guidelines; 6.2.4 Development Methods (source title begins with a space); 6.3 System Architecture; 6.3.1 Subsystem Architecture; 6.4 Architectural Strategies; two strategy-name placeholders beneath 6.4; 6.5 Domain Model/Class Diagram; 6.6 Policies and Tactics; two policy/tactic-name placeholders beneath 6.6.

System architecture must be diagrammatic. Strategy/tactic placeholder names may later describe proposal-supported decisions, such as hybrid memory and orchestration integration, or physician approval and evidence provenance. No separate Sequence Diagrams section exists in this template: place relevant sequences inside System Architecture/Subsystem Architecture or Policies and Tactics.

**Chapter 7:** 7.1 Implementation; 7.1.1 Implementation of First Component/Algorithm (component-name placeholder); 7.2 Test case Design and description; 7.3 Test Metrics; 7.3.1 Sample Test case Metric.No.2 (demo placeholder). Do not rename the chapter merely because the template permits an FYP-1 prototype description; preserve the user's requested chapter title. Explain all components within the existing structure without adding fixed headings.

**Chapter 8:** User Manual has no supplied section headings. Later use prose and concise numbered steps within the chapter; new subheadings require a template-permitted, approved choice.

**Chapter 9:** Experimental Results and Discussion has no supplied section headings. Later put the evaluation protocol, results tables, and discussion within the chapter without importing sample-report section names.

**Chapter 10:** `aa`, `dfs`, and `dsd` are demo section/subsection/subsubsection titles, not substantive requirements. Preserve them for the setup comparison only. Later replace the placeholder hierarchy with meaningful titles at the same levels, proposed as “Summary of Work”, “Limitations and Remaining Work”, and “FYP-2 Work Plan” for FYP-1; final wording needs approval. Do not claim any objectives were achieved by an unbuilt prototype.

**Bibliography:** remains after Conclusions, with `\bibliographystyle{ieeetr}`.

**Appendix A:** “First Appendix if Required”, followed by References, Equations, Figures, Tables, Pseudo Code, Code of Programming Languages, and Recommendations for `\LaTeX`. These are demonstration material; appendices are explicitly optional. Preserve all of them during Phase 2. Do not retain the FAST-logo example, `E=mc^2`, demo algorithm, C program, or LaTeX tutorial as Zeest content in a later writing phase. No project appendix is currently justified by the proposal; any replacement/removal must be an explicit later decision, outside the fidelity-preserving setup.

## 3. Three-member ownership and workload

Owners are exclusive editors. Other members provide review comments or handoff notes, never edits to another owner's chapter or figure source. Do not infer student roles from the order of names in the proposal.

Page estimates are **planning estimates**, not report requirements or measured outcomes. They exclude title/declarations/contents/bibliography and include diagram/table space. Deferred chapters have short placeholders in the FYP-1 estimate. The FYP-2 column estimates the same unbuilt system's eventual reporting space, not its completion.

| Owner | Related responsibility | Chapters and proposed files | FYP-1 pages | FYP-2 pages | Diagram load |
|---|---|---|---:|---:|---|
| A | Project scope, physician requirements, patient-data specification, interface/manual | `01_introduction.tex` (3); `02_project_vision.tex` (5); `04_software_requirement_specifications.tex` (12); `08_user_manual.tex` (1 deferred / 4 later); `10_conclusions.tex` (3); Executive Summary (2) | 26 | 29 | 3 PlantUML diagrams, 3 proposed screen views, existing SDG image |
| B | Literature, scientific methods, evidence/multimodal evaluation | `03_literature_review.tex` (16); `05_proposed_approach_and_methodology.tex` (7); `09_experimental_results_and_discussion.tex` (1 deferred / 5 later); Abstract (less than 1 page of text) | about 24–25 | about 28–29 | 3 PlantUML diagrams; 1 results chart deferred |
| C | Integrated architecture, agent/data flow, prototype implementation and test evidence | `06_high_level_and_low_level_design.tex` (14); `07_implementation_and_test_cases.tex` (10 planned / 14 later) | 24 | 28 | 6 PlantUML diagrams |

This balances total writing effort rather than chapter counts: B's literature verification is substantial; C's architecture and detailed test specification offset fewer chapters; A handles more short chapters and specification tables. Re-estimate when the stage and classification are confirmed, without splitting any chapter between editors.

Member A owns the demo appendix file for the setup extraction and serves as assembly coordinator. Each member owns only their own `kashaf/references.bib`, `fatima/references.bib`, or `esha/references.bib`. A owns `kashaf/executive_summary.tex`; B owns `fatima/abstract.tex`. The temporary Phase 2 setup operator performs the one authorized mechanical edit of `main.tex`; thereafter nobody edits it. Resolve final metadata in a separately authorized step before declaring that freeze, or keep the original placeholders: setup itself must preserve them.

### Handoff contracts

| Dependent material | May assume | Must not assume |
|---|---|---|
| Ch. 3 (B), from Ch. 2 (A) | Exact objective list and in/out-of-scope boundary from proposal | A respiratory-only scope, new user roles, or prototype results |
| Ch. 4 (A), from Ch. 2 and Ch. 5 (B) | Physician is the primary user; named agents, hybrid memory, evidence, approval workflow; proposed evaluation definitions | Final speech/model/knowledge-base choices, sample count, response-time targets, or data access approval |
| Ch. 5 (B), from Ch. 3 | Source-supported methods and limitations once verified | Broad “no existing system” claim or guaranteed superiority |
| Ch. 6 (C), from Ch. 4 and Ch. 5 | Stable requirement IDs, proposed data concepts, approval boundary, proposed experiment variants | Database schema/API route/interface details already implemented |
| Ch. 7 (C), from Ch. 4 and Ch. 6 | Requirement/use-case IDs and proposed component contracts; B's approved metric definitions | Any component has been built, a test has passed, or a model is clinically validated by this team |
| Ch. 8 (A), from Ch. 4 and Ch. 7 | Intended physician workflow; later verified UI behavior if evidence exists | Screenshots, working controls, or installation commands exist now |
| Ch. 9 (B), from Ch. 5 and Ch. 7 | Approved protocol and later actual versioned outputs/test records | Synthetic cases prove clinical utility, or unexecuted comparisons have a direction/magnitude |
| Ch. 10 and summaries, from all owners | Documented planning status and, later, measured evidence | Completion, clinical safety, deployment readiness, or superiority without evidence |

## 4. Diagram and table inventory

This is a production list for a **later authorized writing phase**, not an instruction to create graphics in Phase 2. IDs are working asset IDs, not LaTeX figure numbers.

Keep `.puml` files under `each owner's diagrams/ folder: ` and rendered `.png` files under the existing `Report template/Figures/`. Match basenames, for example `diagrams/D07_system_architecture.puml` and `Figures/D07_system_architecture.png`. Render outside LaTeX and insert through existing `\includegraphics`; no package, shell-escape, or class change. Use chapter-specific labels. Source and image have the same chapter owner.

All diagrams describe a **proposed** system until verified. Mark proposed diagram descriptions accordingly. Use “proposed”, visible actors/components, arrow meaning, and important branches in the ordinary caption. Avoid unexplained acronyms or a caption that only repeats “Architecture Diagram”.

### Figures

| ID / basename | Owner | Location | What the image and descriptive caption must show | Format / timing |
|---|---|---|---|---|
| F00_existing_sdg | A | 2.6 | Existing `Picture1` overview of SDGs; explain its visible grid and the confirmed relevant goal without claiming achieved impact | Retain supplied image; PlantUML is unsuitable for official artwork. Verify visually before final caption |
| D01_doctor_use_cases | A | 4.6 | Physician interaction with consultation input, relevant history, proposal/evidence review, approval/modification/rejection, and audit viewing; named external services shown as dependencies, not new users | PlantUML use-case diagram |
| D02_doctor_navigation | A | 4.8 | Proposed physician navigation among patient history, consultation, evidence/proposal review, and approval/audit views, linked to use-case IDs | PlantUML activity diagram |
| D03_hybrid_memory_er | A | 4.9.1 | Proposed patient/encounter/clinical-data/proposal/review/audit concepts, relationships, temporal links, and links to semantic records; no knowledge graph | PlantUML ER diagram; exact fields/cardinalities are design choices to confirm |
| W01_history_view | A | 4.8 | Planned patient longitudinal history and related encounter data; no realistic patient details or completed results | Clear placeholder now; later static wireframe, then genuine prototype capture |
| W02_consultation_view | A | 4.8 | Planned transcription/structured notes and multimodal inputs, mapped to consultation use cases | Placeholder now; later wireframe/capture |
| W03_review_audit_view | A | 4.8 | Planned proposal, evidence citations, critic review, approve/modify/reject actions, and audit history | Placeholder now; later wireframe/capture; views may separate if actual GUI requires it |
| D04_method_pipeline | B | Ch. 5 | Proposed audio/clinical-data intake, structured notes, memory retrieval, specialized analyses, evidence retrieval, clinical reasoning, critic review, and physician decision | PlantUML activity diagram; explain data versus control arrows |
| D05_ablation_protocol | B | Ch. 5 | Shared case inputs and reference evaluation for single LLM, memory-augmented, and full-system variants; separately identify critic/multimodal contrasts proposed in the Introduction | PlantUML component/activity diagram; does not imply results |
| D06_evidence_retrieval | B | Ch. 5 | Patient-specific context separated from external guideline retrieval, then cited evidence supplied to reasoning/review | PlantUML activity diagram; avoid assuming an unnamed embedding model/reranker |
| D07_system_architecture | C | 6.3 | Proposed Next.js physician interface, FastAPI, agent orchestration, Gemini, PyTorch imaging integration, PostgreSQL/pgvector, and external evidence/model dependencies | PlantUML component diagram; LangGraph/ADK division unresolved |
| D08_agent_subsystems | C | 6.3.1 | Patient Memory, Clinical Case, Imaging, Laboratory, Medication Safety, Evidence and RAG, Clinical Reasoning, and Safety and Critic agents; inputs/outputs and integration points | PlantUML component diagram; scheduling remains proposed |
| D09_domain_classes | C | 6.5 | Proposed domain objects/services for encounters, multimodal findings, evidence, proposals, physician decisions, and audit entries | PlantUML class diagram; reuse A's data meanings; not duplicate ER schema |
| D10_consultation_sequence | C | 6.3.1 | Proposed call/message sequence from consultation transcription and multimodal input to history/evidence retrieval, reasoning, critic review, and physician presentation | PlantUML sequence diagram; no fabricated latencies |
| D11_approval_states | C | 6.6 | Proposed pending, approved, modified-and-approved, and rejected states; distinguish audit retention from approved clinical-record entry | PlantUML state diagram; exact state labels are design choices |
| D12_memory_update_sequence | C | 6.3.1 | Proposed physician action, audit entry, approved decision persistence, and subsequent patient-memory retrieval; rejected/unapproved proposals excluded as final clinical decisions | PlantUML sequence diagram; approval/write atomicity details remain unconfirmed |
| R01_ablation_comparison | B | Ch. 9, FYP-II | Comparison of actually measured shared-case outcomes, with metric/units, sample size, and uncertainty if applicable | Placeholder until results exist. Use Python/Matplotlib after data exists; PlantUML is a poor fit for scientific plots |

PlantUML is appropriate for UML, ER, activity, and dependency diagrams. It is a poor fit for polished interface screens, genuine screenshots, official SDG imagery, and quantitative plots. Suggest a simple HTML/SVG wireframe or Figma only if approved; neither adds functionality. Store exported screens/plots under `Figures/` too. Never pass a wireframe off as a working-prototype screenshot. No generated medical scans or invented screen results.

The three UI views are a minimum proposed grouping, not proof of the eventual screen count. When screen boundaries are known, capture every distinct required screen and update this inventory; no unlisted functionality may appear.

Example descriptive caption to use later: “Proposed physician-review workflow: a diagnosis proposal passes through critic review before the physician approves, modifies and approves, or rejects it. Only approved decisions enter the clinical record; each physician action is retained in the audit log.”

### Tables

Use LaTeX tables with the existing template commands, not rasterized PlantUML tables: text stays selectable and columns remain readable. Continue a long table as separately captioned parts using existing environments if necessary; do not add a package. Numeric entries below are never prefilled.

| ID | Owner | Location | Required content |
|---|---|---|---|
| T01_terms | A | 1.3 | Only acronyms actually used in Zeest; no example SCRUM/ORM/CRUD entries unless needed and supported |
| T02_objective_traceability | A | 2.4 | Proposal objective → report location → planned test, using Section 6 of this plan |
| T03_scope_constraints | A | 2.5/2.7 | Exact proposal inclusions, exclusions, and unresolved dependencies |
| T04_stakeholders | A | 2.9.1–2.9.2 | Physician's role/goals; distinguish patient as data subject from application user; other stakeholder claims need confirmation |
| T05_literature_summary | B | 3.3 | At least 15 verified distinct works; Development format: Application / Features / Relevance / Limitations; Research format: Author / Method / Results / Limitations. R&D selection to confirm |
| T06_requirements | A | 4.2 | Stable FR IDs mapped to proposal objectives and doctor actions; no inherited inventory/login example features |
| T07_quality_constraints | A | 4.3–4.4 | Proposal-grounded reviewability, traceability, groundedness, data handling, and real-time transcription needs; numeric thresholds TBD |
| T08_use_cases | A | 4.6 | One template-format table per core use case: review longitudinal context; transcribe consultation; supply imaging/labs/notes; generate/review proposal with evidence/critic output; approve; modify and approve; reject; view audit history |
| T09_resources | A | 4.7 | Proposal-listed software stack and unresolved hardware/resource needs; no invented GPU/RAM/cloud requirements |
| T10_data_dictionary | A | 4.9.2 | Proposed entities/fields, types, nullability, keys, relationships, meaning, and temporal/provenance links, consistent with D03; fields await design confirmation |
| T11_risks | A | 4.10 | Proposal-derived risks and proposed mitigations: access/model/domain constraints, unsupported evidence, transcription errors, memory mismatch, integration, and approval handling; no invented probability scores |
| T12_dataset_model_register | B | Ch. 5 | Proposal-listed MIMIC-IV/MIMIC-CXR, Synthea, PubMed, CheXpert/NIH candidates; distinguish selected datasets, model candidates, registered access, actual access, preprocessing, and permitted domain |
| T13_experiment_protocol | B | Ch. 5 | Three named ablation variants and proposed critic/multimodal contrasts, common inputs/references, controlled variables, proposed measures, unresolved sample counts and thresholds |
| T14_component_contracts | C | 6.3.1 | Each agent's proposed input/output, memory/evidence usage, status/error reporting, and next recipient; implementation details TBD |
| T15_design_decisions | C | 6.4/6.6 | Proposal-supported stack choices versus unresolved design decisions; no claim that alternatives were evaluated by the students without evidence |
| T16_prototype_status | C | 7.1 | Every named prototype capability, intended behavior, and status “PLANNED — not built”; later update only from supplied implementation evidence |
| T17_test_cases | C | 7.2, FYP-II | Template's test ID/version/engineer/reviewer/date/use-case/objective/environment/assumptions/prerequisite/steps/comments/status fields, one table per planned case; expected and observed behavior separated |
| T18_test_metrics | C | 7.3 | Counts planned/executed/passed/failed, traceability, and relevant metric definitions; values remain not measured, with denominator handling specified |
| T19_research_results | B | Ch. 9, FYP-II | Actual variant outcomes for shared cases, supporting records, approved measures, sample counts, limitations; planned blank slots now |
| T20_critic_multimodal_results | B | Ch. 9, FYP-II | Critic-enabled/disabled and multimodal/text-only comparison on matched cases, if protocol approved; all entries pending execution |
| T21_scope_completion | A | Ch. 10 | Objective-by-objective evidence/status; “planned/unbuilt” for prototype capabilities, not “achieved” |
| T22_fyp2_work_plan | A | Ch. 10, FYP-1 | Ordered remaining implementation, integration, evaluation, documentation tasks and dependencies; dates/actual student names pending |

No unnecessary research-result graphics, literature architecture replicas, branding figures, or extra appendix tables are required now. A later figure/table addition must have a clear proposal objective or explicit template requirement and an owner.

## 5. Unbuilt prototype: planned implementation, tests, and results

The user's current statement that the prototype is unbuilt controls implementation status. The proposal reports preparatory literature/architecture/dataset/stack work, but this is not executable prototype evidence. Describe it as “the proposal reports ...” until supporting artifacts are available.

Use the literal LaTeX pattern `\textcolor{red}{PLANNED: ...}` for every prospective implementation, test, result, screenshot, and unsupported performance assertion. Existing `color` support is sufficient. Planned markers apply even if FYP-2 is selected and the prototype remains unbuilt.

| Prototype part | Proposal basis | Later Chapter 7 wording pattern |
|---|---|---|
| Hybrid patient memory | Objective 1 | `\textcolor{red}{PLANNED: Implement relational patient history and semantic retrieval using PostgreSQL and pgvector; document temporal and patient links. No prototype evidence is available.}` |
| Voice notes | Objective 2 | `\textcolor{red}{PLANNED: Convert consultation audio into structured clinical notes in real time. The transcription model, languages, latency target, and measured quality remain unspecified.}` |
| Specialized analyses | Objective 3 | `\textcolor{red}{PLANNED: Integrate Patient Memory, Clinical Case, Imaging, Laboratory, and Medication Safety agents with documented input and output contracts.}` |
| Validated imaging integration | Objective 4 | `\textcolor{red}{PLANNED: Integrate an existing pre-trained classification model for a supported dataset/domain; record its provenance and limitations. No diagnostic model will be trained from scratch.}` |
| Evidence retrieval | Objective 5 | `\textcolor{red}{PLANNED: Retrieve relevant clinical guidelines with citations and retain source links with the evidence supplied to clinical reasoning.}` |
| Proposed diagnosis/plan | Objective 6 and scope | `\textcolor{red}{PLANNED: Produce a reviewable proposed diagnosis and treatment plan from the available longitudinal and multimodal context, subject to physician approval before recording.}` |
| Critic review | Objective 7 | `\textcolor{red}{PLANNED: Review the proposal for unsupported outputs before physician presentation. Evaluation has not been executed.}` |
| Physician controls/audit | Objective 8 | `\textcolor{red}{PLANNED: Provide approve, modify, and reject controls and a full audit log. Verify that unapproved proposals cannot become approved clinical decisions.}` |
| Comparative evaluation | Objective 9 and Introduction | `\textcolor{red}{PLANNED: Compare a single LLM, a memory-augmented variant, and full Zeest on matched cases; evaluate the critic and multimodal questions through an approved protocol. No comparative results exist.}` |

Use explicit empty placeholders, for example:

```latex
\textcolor{red}{PLANNED: Screenshot of the consultation view will be inserted after the prototype exists.}
\textcolor{red}{PLANNED: Expected behavior: rejecting a proposal leaves the approved clinical record unchanged and records the action in the audit history.}
\textcolor{red}{PLANNED: Observed output: NOT EXECUTED. Test date and pass/fail status are unavailable.}
\textcolor{red}{PLANNED: Comparative outcome: NOT MEASURED. Case count, rubric, and reference labels remain to be confirmed.}
```

The proposed **ideal** prototype should connect all nine objectives in an end-to-end physician workflow using de-identified or synthetic data. Do not silently downgrade mandatory voice transcription or omit a named agent. A staged prototype may demonstrate a subset, but document the missing parts and request a scope decision rather than calling the full proposal complete.

For tests, cover component behavior, multimodal integration, relevant history retrieval, source traceability, critic handling, and all physician decision branches. Cases and expected behavior are plans; all execution outcomes are “not executed”. For results, distinguish software correctness from research comparisons and from clinical effectiveness. No invented accuracy, case counts, confidence values, timestamps, screenshots, pass totals, or claimed clinical validation.

The proposal's wording that an ablation “will confirm” superiority is a hypothesis, not a guaranteed result. Report whether the evidence supports it after testing, including negative or inconclusive findings.

## 6. Proposal objective → report location → planned verification

These are proposed ways to test existing objectives, not new features or numerical acceptance commitments. Test procedures remain `\textcolor{red}{PLANNED: ...}` when copied into the report.

| Proposal objective, in proposal order | Report locations | Planned verification / evidence |
|---|---|---|
| 1. Hybrid longitudinal relational + semantic memory | 2.4; 4.2/4.9; Ch. 5; 6.3; 7.1–7.3; Ch. 9 | Known de-identified/synthetic multi-encounter cases; check correct patient/event/temporal retrieval and persistence; compare with current-case-only variant |
| 2. Real-time consultation transcription into structured notes | 4.2/4.8; Ch. 5; 6.3.1; 7.1–7.3 | Compare supplied audio and approved reference notes; check clinical fields and observed processing delay; language/model/reference process and targets TBD |
| 3. Patient Memory, Clinical Case, Imaging, Laboratory, Medication Safety agents | 4.1–4.2; Ch. 5; 6.3.1; 7.1–7.3 | Proposed contract/integration cases verify each named agent receives relevant input and returns inspectable output; include known lab/medication-history cases without inventing medical reference answers |
| 4. Imaging Agent integrating pre-trained validated classification model | 3.2; 4.7; Ch. 5; 6.3.1; 7.1–7.3; Ch. 9 | Verify source/model version, preprocessing, supported labels and datasets; compare actual outputs against reference labels in the supported domain |
| 5. Evidence and RAG Agent with cited clinical guidelines | 3.2; 4.2; Ch. 5; 6.3.1; 7.1–7.3; Ch. 9 | Check retrieved evidence relevance and whether cited passages support generated claims; source corpus and reference rubric TBD |
| 6. Clinical Reasoning Agent producing reviewable proposed diagnosis | 4.2/4.6; Ch. 5; 6.3.1; 7.1–7.3; Ch. 9 | Matched-case review against justified reference cases/rubric; show evidence and proposal status; scope also includes physician-reviewed treatment plans |
| 7. Safety and Critic Agent before presentation | Ch. 5; 6.3.1/6.6; 7.1–7.3; Ch. 9 | Seed unsupported/contradictory proposals with known reference judgments; observe flags/revisions; matched critic-enabled/disabled contrast if approved |
| 8. Doctor interface: approve, modify, reject, full audit log | 4.6/4.8/4.9; 6.6; 7.1–7.3; Ch. 8 | Test each action; inspect clinical record and audit entry; verify pending/rejected proposals are not committed as final clinical decisions and modified decisions require approval |
| 9. Single LLM vs memory-augmented vs full-system ablation | 3.2/3.3; Ch. 5; 7.2–7.3; Ch. 9; Ch. 10 | Same case set, controlled model/input settings where feasible, explicit variant configuration and scoring rubric; record all outputs and discuss confounding/limitations |

The Introduction separately asks about multimodal versus text-only input. Include this contrast in the proposed evaluation protocol without treating it as a new objective. Specify exactly what each comparison changes; the three main variants alone cannot isolate every agent's individual contribution.

No particular metric, clinician reviewer availability, sample size, or acceptance threshold is confirmed by the proposal. Proposed measures require student/advisor agreement before becoming commitments.

## 7. Literature and reference plan

Use proposal-listed works as the initial candidate pool; do not invent references to reach the minimum. A possible **18-item pool**, all already named in the proposal: Isabel DDx [9], UpToDate [10], OpenMRS [11], Med-PaLM 2 [3], GPT-4 medical challenge work [4], ClinicalBERT [5], BioGPT [6], CheXNet [7], CheXpert [8], BioViL-T [12], ReAct [13], original RAG [17], MedRAG [18], MedCPT [19], MIMIC-IV [20], MIMIC-CXR [21], Huang et al. [22], and Synthea [23]. Bracket numbers here identify proposal entries only; the final report's citation numbers will be generated automatically.

For each retained item, B verifies the actual source and writes its summary, strengths/limitations, and relationship to a specific Zeest objective. Dataset/framework descriptions may supplement related work; confirm whether the department counts them toward the 15-work minimum. If fewer than 15 eligible verified works remain, flag the shortfall and propose sources for approval rather than inventing them.

LangGraph [15], Google ADK [16], and other proposal references may support methods/stack descriptions. Bibliographic details, including Huang et al. [22] and AutoGPT [14], require checking against original sources before use. Listing an entry in the proposal does not verify its metadata or claims.

Do not import the template's six sample references as Zeest literature. During Phase 2, preserve their existing cited keys and entries to reproduce the baseline. Later replace example content/citations only during an approved writing phase.

Avoid carrying over the proposal's broad categorical comparisons or “No existing system ...” wording as established literature findings. Attribute them to the proposal and assess against verified sources. No medical advice or clinical claims are being validated by this planning document.

For bibliography ownership after setup, reserve key prefixes `zeestA:`, `zeestB:`, and `zeestC:`. If two members need one source, the first assigned canonical entry owner retains it; the other cites that key without duplicating the entry. B owns the initial literature pool, A owns approved stakeholder/domain sources, C owns verified implementation-method sources. Prefixes are a collaboration convention, not additional project technology.

## 8. Likely defense questions per chapter

| Chapter | Questions to prepare for |
|---|---|
| Introduction | What problem does Zeest address? Why does longitudinal context matter? What is the difference between a proposed diagnosis and a physician-approved decision? What has actually been completed? |
| Project Vision | Which objectives are mandatory? Which domains can be supported with available datasets and validated models? What is explicitly out of scope? Why is the claimed SDG relationship an intended contribution rather than proven impact? |
| Literature Review / Related Work | Which verified works support the claimed gap? How is Zeest different from existing CDSS, medical LLM, imaging, and RAG approaches? Which limitations are source-supported? Are at least 15 distinct relevant works actually analyzed? |
| Software Requirement Specifications | Who is the user? What happens on approval, modification, and rejection? Which data enters memory and when? How are requirements traceable to the proposal? Which requirements/thresholds remain undecided? |
| Proposed Approach and Methodology | Why combine relational and semantic memory? What makes the agent decomposition useful? What are the baseline and ablation controls? How will critic and multimodal contributions be isolated? Where do reference judgments come from? |
| High-Level and Low-Level Design | How do the agents exchange data? Why these proposed stack components? What is the LangGraph/ADK division? How are patient identity, time, evidence provenance, and approval boundaries represented? What happens when a dependency fails? |
| Implementation and Test Cases | Which modules are implemented versus planned? How is pre-trained inference integrated without training a diagnostic model? What does each test verify? Where are execution evidence and actual outputs? How is an unapproved clinical-record write prevented? |
| User Manual | Can a physician complete the intended workflow? How are evidence and critic concerns shown? What exactly changes on each review action? Are images genuine prototype screenshots or planned wireframes? |
| Experimental Results and Discussion | Are comparisons based on identical cases and controlled settings? What is the reference standard? Does synthetic-data evaluation generalize? Do results support the memory, agent, critic, and multimodal hypotheses? What are the uncertainties and confounders? |
| Conclusions | Which objectives are supported by actual evidence? What remains unbuilt or untested? What are the principal limitations? What is the FYP-2 plan, and which dependencies could prevent completion? |

If a diagram/source appendix is later justified: why was it placed outside the chapters, and is its content required to reproduce the described procedure?

## 9. Order of work and dependencies

1. Resolve stage, project type, and conditional-heading interpretation. Students approve or revise this plan. Inspect any supplied visual asset before reusing it or finalizing its descriptive caption; sample screenshots are not Zeest evidence.
2. **Phase 2 only after plan approval:** compile the untouched template and retain its PDF, exact sources, class/assets hashes, build recipe, logs, and warnings. If compilation fails, preserve the failed log and report the exact blocker; do not repair the class or add packages.
3. Split chapter blocks and summary bodies into exclusive owner files. The approved current locations are the root `kashaf/`, `fatima/` and `esha/` folders, including the unchanged demo appendix in `kashaf/`. Add exclusive owner comments. Replace content blocks in `main.tex` with `\input` lines in exactly the same positions. Keep whitespace-sensitive boundaries and all existing commands/page breaks intact.
4. Create the three member bibliography files. For fidelity, copy each original example entry into exactly one of them (suggest A owns the unchanged example set for setup, B/C initially contain comments only). Keep the original `fypbib.bib` as an untouched baseline source. Change only the bibliography database list to `\bibliography{../kashaf/references,../fatima/references,../esha/references}` and retain `ieeetr`.
5. Recompile with the same engine, dependency versions, figure paths, date, and auxiliary-file handling. Compare page count, extracted text, headings/order/numbering, bibliography, contents/figure/table lists, page breaks, and page images. Matching file bytes are not required because PDF metadata can differ; visible/textual/layout fidelity is required. Report every discrepancy and pre-existing warning. Only then freeze `main.tex`. No chapter writing or diagram replacement during setup.
6. **Later writing phase, separately authorized:** A finalizes proposal traceability, terminology, scope and requirements; B verifies literature. Share handoff notes before methods/design become fixed.
7. B defines proposed procedure and evaluation protocol using verified sources and confirmed resources; A supplies data/use-case meanings; C develops consistent architecture/design. Owners create their own `.puml` sources/images and caption/reference them inside existing headings.
8. C describes planned implementation and tests from the approved contracts; A drafts planned physician workflow/manual if applicable; B drafts planned result slots if applicable. All unbuilt/unexecuted material stays red and explicitly planned.
9. When an actual prototype exists, collect versioned evidence before changing planned status. C records implementation/test behavior; A captures verified screens/manual steps; B records measured comparisons. This is outside both currently requested phases.
10. A writes Conclusions and Executive Summary last; B writes Abstract last. Cross-review vocabulary, objective coverage, citations, captions, stage wording, paragraph lengths, and final compilation without editing another owner's file.

Critical path: scope/type/stage → literature/requirements → method/data contracts → architecture → planned implementation/test specification → actual build/evidence → experiments → conclusions/summaries. Requirements and literature may proceed concurrently; full shared-file editing may not.

### Current approved file map and safeguards

```text
Report template/        # shared frozen main.tex, untouched class, original bib, Figures/
kashaf/                 # Chapters 1, 2, 4, 8, 10, demo appendix, Executive Summary
fatima/                 # Chapters 3, 5, 9, Abstract
esha/                   # Chapters 6, 7
```

Each person folder also contains `references.bib`, `START_HERE.md`, `HANDOFF.md`, scoped `AGENTS.md` and `diagrams/`. Read the individual guide for exact filenames. Rendered assets remain in the required shared Figures folder with owner prefixes. Setup tools and original baseline evidence were moved to the external archive recorded in README.md. The approved restructuring updated only assembly paths; main.tex is frozen again.

Put `% Owner: Member A` (or B/C) at the top of each extracted file; add actual student names only after mapping is confirmed. Keep `\appendix` and bibliography positioning as in the original assembly. Extract the original `\chapter` commands with their content so each chapter file remains a complete exclusive editing unit. For summaries, leave the original headings/page breaks in `main.tex` and extract their body text only, preserving front matter exactly.

The expected local build recipe, if tools are available, is LaTeX → BibTeX → LaTeX → LaTeX until references and contents settle. Read-only discovery found Java but no `pdflatex`, `latexmk`, `bibtex`, `plantuml`, or `soffice` on `PATH`. This does not prove they are absent everywhere. Phase 2 must locate a usable TeX toolchain or use an approved alternative such as Overleaf before claiming either PDF exists or matches. PlantUML is needed only in the later diagram-writing phase.

Known baseline issues to observe, not silently repair during setup: the SDG figure refers to `fig:my_label` while its label is `fig:1`; a citation uses `ref:guyon:2007` while the example bibliography spells that entry `ref:Guyon:2007`; long demonstration headings/tables and already empty sections may produce warnings. Preserve the original behavior for comparison, then report it. Do not change metadata placeholders, example heading names, sample text, existing figures, or the date command in the setup pass. Compare both builds on the same date because the template uses `\today`.

## 10. Suggestions — undecided, not project facts

- Classify Zeest as R&D and retain both specification/design and methodology/evaluation coverage, subject to the department's rules.
- Use SDG 3 as the candidate alignment for the template's mandatory SDG section; the proposal does not name an SDG. Confirm and source the official goal description before adding it.
- Agree on operational metric definitions (for example history retrieval correctness, source support, transcription quality/delay, and proposal-review quality) and a scoring rubric. These are proposed evaluation choices, not promised scores.
- Agree on who supplies reference case judgments and whether qualified reviewers are available; do not assume physician participation.
- Limit the first evaluated domain to one with both suitable available data and a validated pre-trained model. A chest-radiograph domain is a candidate supported by the proposal's dataset/model discussion, not a confirmed exclusive domain.
- Confirm how both LangGraph and Google ADK are used; do not invent an integration role merely because both appear in the proposal's confirmed stack.
- Once setup has passed, separately authorize replacing genuine placeholder headings/demo appendix content and filling metadata. This cannot be mixed into a baseline-equivalent split, and the requirement to freeze `main.tex` means metadata timing needs an explicit decision.

No proposed new product features. Knowledge graphs, patient chat/portal, native mobile apps, autonomous treatment/prescribing, emergency/ICU systems, real deployment, and training diagnostic models from scratch remain excluded unless the proposal is formally revised.

## 11. Open questions and assumptions

### Open questions

- **[Certain] Q1:** The request's FYP-stage placeholder is unset and `Rules.txt` explicitly says FYP-1. Confirm FYP-1 or FYP-2.
- **[Likely] Q2:** R&D best matches the proposal. Confirm the official classification and how the Research/Development exemptions apply to it, especially Chapters 4, 5, 8, 9 and sections 2.7–2.9.
- **[Certain] Q3:** No A/B/C-to-student mapping is provided. Confirm which of Kashaf Ali, Fatima Malik, and Eesha Irfan owns each role.
- **[Certain] Q4:** Confirm whether FYP-1 submission must retain deferred Chapters 8/9 and 7.2 with planned placeholders; setup retains everything regardless.
- **[Certain] Q5:** No domain/model choice, transcription model/languages, medication knowledge-base name, embedding model, or LangGraph/ADK division is specified sufficiently for detailed design. Which choices are already approved?
- **[Certain] Q6:** PhysioNet registration is reported, but approved dataset access is not established. Which data/models are actually available for evaluation, and which reference-case review process can be supported?
- **[Certain] Q7:** Hardware resources, numerical targets, experiment case counts, scoring rubric, acceptance criteria, schedule, and prototype evidence are unavailable. Confirm these before making report commitments.
- **[Certain] Q8:** The proposal says diagnoses in its objectives and diagnosis/treatment plans in its scope. Confirm the intended detail of treatment-plan output; do not infer dosage, investigation, or follow-up modules from `context.txt`.
- **[Certain] Q9:** The freeze of `main.tex` conflicts with filling title/student/advisor placeholders after an exactly unchanged setup. Should metadata remain placeholder text until a separately approved pre-freeze update, or be handled in an explicitly authorized later assembly step?
- **[Certain] Q10:** Confirm permission for later meaningful substitutions of demo headings (`aa/dfs/dsd`, LR examples, strategy/tactic/component/metric placeholders) and optional demo appendix removal. No such edits occur in Phase 2.
- **[Likely] Q11:** Research-style literature summary columns suit the evaluation component. Confirm which template table format the R&D report should use and whether dataset/framework items count toward the 15-work minimum.
- **[Certain] Q12:** Local TeX/PlantUML tools were not found on `PATH`. Resolve a build route before any PDF fidelity claim. Existing images must be visually inspected before reuse or final captions; sample screenshot contents cannot establish Zeest behavior.

### Assumptions

- **[Certain]** The proposal is the sole source of project identity, objectives, scope, named stack, datasets, and agents.
- **[Certain]** The prototype is unbuilt; no execution results or screenshots may be invented.
- **[Certain]** The proposal includes real-time voice transcription and the full named agent pipeline; they are not optional extensions in this plan.
- **[Certain]** Every proposed clinical decision needs explicit physician approval before entering the patient record; audit retention must be distinguished from final clinical-record entry.
- **[Certain]** Existing diagnostic models are integration dependencies; Zeest does not train diagnostic models from scratch or claim clinical deployment/regulatory approval.
- **[Certain]** The original class and package set remain unchanged. Phase 2 is purely mechanical and preserves demonstration content for its PDF comparison.
- **[Likely]** FYP-1 is the intended stage because the supplied rules name it. No stage-dependent section is removed on that assumption.
- **[Likely]** R&D is the appropriate classification; the department must resolve conditional applicability.
- **[Likely]** The proposed screen groupings and diagrams adequately cover the workflow; their details remain design choices until confirmed.
- **[Guessing]** The estimated page distribution will yield a balanced workload; revise estimates after confirmed stage, data access, and advisor feedback.
- **[Guessing]** A chest-radiograph domain may be the first feasible evaluation domain; no disease coverage or imaging label set is yet fixed.

**Approval gate:** Phase 2 was approved with permission to make the working assumptions recorded above. Stop after setup and its verification report; chapter writing requires a later instruction.
