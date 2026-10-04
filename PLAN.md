# Zeest report plan: R&D Deliverable II

Scope approved by the user on 4 October 2026: Chapters 1 through 6, compulsory Abstract, Executive Summary and References, plus an included Appendix. This supersedes the earlier full-template applicability and workload plan. Chapters 7 through 10 are archived outside the repository; do not write or assemble them for this deliverable. No project prose has been written.

## Sources and rules

F26-098.docx alone supplies project facts. The user-supplied Deliverable II instruction controls current chapter inclusion; template/class/rules control the retained headings and formatting. Sample reports guide presentation only. Read README.md, Rules.txt and your START_HERE.md. Never edit FastFyp.cls or add packages. main.tex is frozen after this scope change. Keep ordinary paragraphs 150 to 250 words; Abstract is one paragraph of 50 to 125 words and three to five sentences. Executive Summary is one to two pages of plain prose.

## Chapter list and ownership

| Chapter | Owner | Exclusive file |
|---|---|---|
| 1. Introduction | Kashaf | kashaf/01_introduction.tex |
| 2. Project Vision | Kashaf | kashaf/02_project_vision.tex |
| 3. Literature Review and Related Applications | Fatima | fatima/03_literature_review.tex |
| 4. Software Requirement Specifications | Kashaf | kashaf/04_software_requirement_specifications.tex |
| 5. Proposed Approach and Methodology | Fatima | fatima/05_proposed_approach_and_methodology.tex |
| 6. High-level and Low-level Design | Esha | esha/06_high_level_and_low_level_design.tex |

These labels follow the supplied deliverable list. Existing template chapter commands retain their exact original spelling, capitalization and spacing. No heading renaming occurs during setup. Kashaf additionally owns Executive Summary and Appendix; Fatima owns Abstract; each owns their references.bib. Appendix is included but its project-specific title/content still needs approval. Template appendix demonstrations are not final Zeest content.

## Workload and dependencies

Planning estimates, not requirements: Kashaf roughly 20 to 24 pages plus an approved appendix, with three PlantUML diagrams, proposed interface views and the existing SDG image; Fatima roughly 20 to 25 pages with three PlantUML diagrams and substantial source verification; Esha roughly 14 to 18 pages with six design diagrams. Rebalance only by agreement, preserving one owner per chapter.

Kashaf establishes objectives, scope, requirements/use-case IDs and proposed data meanings. Fatima can verify literature concurrently and then defines the proposed method/evaluation protocol. Esha can sketch proposed components immediately, but final design depends on both handoffs. No owner assumes models, data access, reviewers or implementation exist because another chapter mentions them. Write Abstract and Executive Summary last, summarizing this planning/design deliverable rather than completed experiments. Each owner updates only their HANDOFF.md.

## Exact retained sections

**Chapter 1:** 1.1 Purpose of this Document; 1.2 Intended Audience; 1.3 Definitions, Acronyms, and Abbreviations; 1.4 Conclusion.

**Chapter 2:** 2.1 Problem Domain Overview; 2.2 Problem Statement; 2.3 Problem Elaboration; 2.4 Goals and Objectives; 2.5 Project Scope; 2.6 Sustainable Development Goal (SDG); 2.7 Constraints; 2.8 Business Opportunity; 2.9 Stakeholders Description/ User Characteristics; 2.9.1 Stakeholders Summary; 2.9.2 Key High-Level Goals and Problems of Stakeholders.

**Chapter 3:** 3.1 Definitions, Acronyms, and Abbreviations; 3.2 Detailed Literature Review; 3.3 Literature Review Summary Table; 3.4 Conclusion. Under 3.2, the “Related Research Work 1 / Related Development Project ...” and two “Example LR ...” subsections are explicit demonstration placeholders. Later replace those examples with numbered reviews of actual verified proposal-listed works; retain the required parent sections. No sample customer-service content belongs in Zeest.

**Chapter 4:** 4.1 List of Features; 4.2 Functional Requirements; 4.3 Quality Attributes; 4.4 Non-Functional Requirements; 4.5 Assumptions; 4.6 Use Cases; 4.7 Hardware and Software Requirements; 4.7.1 Hardware Requirements; 4.7.2 Software Requirements; 4.8 Graphical User Interface; 4.9 Database Design (if required; this means if you are using noSQL, you will not provide ER but the other design element and data dictonary should still be there. Explain and elaborate your DB design); 4.9.1 ER Diagram; 4.9.2 Data Dictionary; 4.10 Risk Analysis (source title begins with a space).

PostgreSQL is in the proposal, so the ER diagram and data dictionary apply. The use-case tables must follow the provided fields and remain together under Use Cases; do not add one heading per use case. GUI pictures must identify their doctor user and mapped use cases. Hardware quantities, latency, user capacity, and storage sizes are not specified and remain unset.

**Chapter 5:** No section headings supplied. Explain the proposed procedural approach in chapter prose, figures, tables, and existing algorithm notation. Do not invent a new section hierarchy.

**Chapter 6:** 6.1 System Overview; 6.2 Design Considerations; 6.2.1 Assumptions and Dependencies; 6.2.2 General Constraints; 6.2.3 Goals and Guidelines; 6.2.4 Development Methods (source title begins with a space); 6.3 System Architecture; 6.3.1 Subsystem Architecture; 6.4 Architectural Strategies; two strategy-name placeholders beneath 6.4; 6.5 Domain Model/Class Diagram; 6.6 Policies and Tactics; two policy/tactic-name placeholders beneath 6.6.

System architecture must be diagrammatic. Strategy/tactic placeholder names may later describe proposal-supported decisions, such as hybrid memory and orchestration integration, or physician approval and evidence provenance. No separate Sequence Diagrams section exists in this template: place relevant sequences inside System Architecture/Subsystem Architecture or Policies and Tactics.


## 4. Diagram and table inventory

This is a production list for a **later authorized writing phase**, not an instruction to create graphics in Phase 2. IDs are working asset IDs, not LaTeX figure numbers.

Keep `.puml` files under each owner's `diagrams/` folder and rendered `.png` files under the existing `Report template/Figures/`. Match basenames, for example `esha/diagrams/esha_D07_system_architecture.puml` and `Report template/Figures/esha_D07_system_architecture.png`. Render outside LaTeX and insert through existing `\includegraphics`; no package, shell-escape, or class change. Use chapter-specific labels. Source and image have the same chapter owner.

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

No unnecessary research-result graphics, literature architecture replicas, branding figures, or extra appendix tables are required now. A later figure/table addition must have a clear proposal objective or explicit template requirement and an owner.


## Prototype status and objective traceability

The prototype is unbuilt. All prospective implementation, testing and results use `\textcolor{red}{PLANNED: ...}` wherever mentioned. Do not create results, screenshots, measured figures or fabricated reference answers. Chapter 5 contains proposed evaluation, not execution evidence. No numerical targets, hardware, sample counts, clinical reviewers or access permissions are established.

| Proposal objective | Current report location | Planned verification, not executed |
|---|---|---|
| Hybrid relational/semantic memory | 2.4, 4.2/4.9, Chapters 5/6 | Check patient/encounter continuity and retrieval on approved reference cases |
| Consultation transcription | 2.4, 4.2/4.8, Chapters 5/6 | Compare transcription/structured fields with approved reference notes |
| Named specialist agents | 4.1/4.2, Chapters 5/6 | Check proposed input/output contracts for each named agent |
| Validated pre-trained imaging integration | 4.7, Chapters 3/5/6 | Verify model provenance, supported labels and reference-case outputs |
| Evidence/RAG with citations | 4.2, Chapters 3/5/6 | Check evidence relevance and citation support using an agreed rubric |
| Reviewable proposed diagnosis | 4.2/4.6, Chapters 5/6 | Compare proposals with justified reference judgments; approval boundary remains explicit |
| Safety and Critic review | Chapters 5/6 | Check handling of unsupported/contradictory proposals against approved reference judgments |
| Physician approve/modify/reject and audit | 4.6/4.8/4.9, Chapter 6 | Verify state transitions, audit retention and exclusion of unapproved final clinical decisions |
| Single LLM/memory/full-system ablation | Chapters 3/5 | Plan controlled shared-case comparisons; critic and multimodal contrasts require explicit controls |

These are proposed checks only. Exact evaluation resources, rubrics and thresholds need agreement before becoming commitments.

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

If a diagram/source appendix is later justified: why was it placed outside the chapters, and is its content required to reproduce the described procedure?


## Order of work

1. Confirm the retained chapter outlines before drafting; Kashaf reviews two at a time and approves every saving step.
2. Kashaf drafts scope and requirements; Fatima verifies actual literature sources in parallel.
3. Share stable requirement IDs, data meanings, citation keys and method/evaluation contracts.
4. Esha finalizes proposed architecture/design; owners create their assigned diagrams and tables under existing headings.
5. Agree Appendix contents; retain its assembly position after References. Do not submit tutorial/example content.
6. Write Abstract and Executive Summary from the six agreed chapters.
7. Review consistency and compile the combined report. Preserve front matter and metadata placeholders until a separate explicit metadata approval.

## Open questions and assumptions

- [Certain] Current deliverable is six-chapter R&D with mandatory Abstract, Executive Summary and References; the user also chose Appendix.
- [Certain] Kashaf/A, Fatima/B and Esha/C ownership is approved.
- [Certain] The prototype is unbuilt; no measured results or execution evidence may be invented.
- [Certain] Appendix inclusion is approved, but its actual content/title remains to be agreed.
- [Likely] SDG 3 is suitable; the proposal names no SDG, so confirm and verify before drafting.
- [Certain] Domain/model choice, transcription languages, embedding model, medication knowledge base and LangGraph/ADK role division remain unresolved.
- [Certain] Dataset registration does not establish approved access; reviewers, hardware, metrics, sample counts and thresholds are unresolved.
- [Guessing] Page estimates balance effort; revisit after outlines and diagram detail are agreed.

## Suggestions requiring a separate decision

Confirm SDG alignment, operational metric definitions and appropriate reference-case review resources. Choose only appendix material that supports retained chapters and the proposal. Do not add product features beyond the proposal. No chapter content is authorized by this coordinator setup task.
