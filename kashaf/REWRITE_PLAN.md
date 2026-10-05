# Kashaf's complete rewrite plan

Date: 5 October 2026. Owner: Kashaf / Member A.

Status: Chapters 1, 2 and 4 rewritten under the user's explicit implementation approval on 5 October 2026. GUI HTML and rendered screen images are unchanged and await separate review. Paragraphs use similar lengths with natural variation.

## 1. What was reviewed

The six supplied sample PDFs were extracted as searchable full text. Their contents were checked to distinguish research-oriented reports from development reports. The close reading focused on the complete Introduction and Project Vision chapters of the four research-oriented samples and the complete SRS chapters of the three that include one. This was a reading of the writing, tables, actor actions, system responses and captions, not a screenshot-only review. This is not a claim that every literature review or results chapter was read in full.

| Sample | Sections closely read | What it contributes to this rewrite |
|---|---|---|
| SynapSure: Mapping Brain Health | Introduction, PDF pp. 14-16; Vision, pp. 17-21; SRS, pp. 37-50 | Closest medical example. Separate account access, scan upload, result viewing and report generation; conventional quality attributes; basic and alternative use-case flows. |
| Recruit Ease | Introduction, PDF pp. 15-16; Vision, pp. 17-22; SRS, pp. 44-70 | Most detailed application workflow: login/logout, list views, individual profiles, add/edit/delete actions and processing steps. FRs identify users; 17 separate use-case descriptions connect actions to visible responses. |
| ParkEase | Introduction, PDF pp. 13-15; Vision, pp. 16-19; SRS, pp. 33-47 | Connects the domain problem to concrete modules; specifies setup, start, monitoring and record viewing separately. Shows operational assumptions, performance constraints and screen coverage. |
| JobLens | Introduction, PDF pp. 12-14; Vision, pp. 15-17; chapter inventory | Useful research framing: problem, application workflow and research question. Its Chapter 4 is methodology, not SRS, so it cannot supply an FR/NFR model. |
| ImageSense | Front matter and chapter inventory | Labels itself development-based and lacks the separate research-methodology chapter. It is not treated as the primary R&D writing model. |
| RahZil | Front matter and chapter inventory | Development structure; useful as a secondary sample rather than the primary research model. |

Also reviewed: README.md, PLAN.md, Rules.txt, ownership instructions, F26-098.docx, the original template's Introduction/SRS instructions, current Chapters 1/2/4, Executive Summary, Appendix, current GUI sources and other members' handoff status.

The original template specifically requires an overview of the problem and background, project purpose and research questions, externally observable functional behaviour, and a final Introduction paragraph outlining every included chapter. These requirements remain binding.

## 2. Findings from the actual writing

The samples generally move from a practical problem to what the application lets its users do. They do not spend most of each paragraph explaining what the chapter is allowed to claim. Individual processing steps and user tasks receive their own requirements and use-case descriptions.

Their prose lengths are not uniformly compliant with our Rules.txt. Approximate word counts after repairing line-break hyphenation for selected complete opening paragraphs are:

| Sample | Selected paragraph lengths | Consequence |
|---|---|---|
| JobLens | 170 and 138 words | Two substantive opening paragraphs introduce the problem and solution. |
| Recruit Ease | 93, 111 and 78 words | Several connected paragraphs develop the argument; shorter length does not override our rules. |
| ParkEase | 77 and 93 words for the first two paragraphs | Explains context and alternatives before introducing the application. |
| SynapSure | 56 and 99 words for two later opening paragraphs | Uses several paragraphs and an illustration; paragraph count matters more than copying its page count. |

These are selected measurements, not whole-report paragraph averages. Pagination differs because the samples use different tables, figures and formatting. We will use connected paragraphs of 150-250 words and add substantive explanation rather than filler to reach an arbitrary number of pages.

The samples also contain weaknesses we must not reproduce: unsupported promises about medical accuracy, absolute availability claims, vague requirements, guessed performance targets, inconsistent users, and occasional template instructions left in the GUI section. Some add headings that our retained template does not contain. Their value is concrete writing and workflow detail, not permission to copy all their decisions.

## 3. Diagnosis of the current draft

| Current issue | Planned correction |
|---|---|
| One short opening paragraph in Chapter 1 | Develop clinical context, documentation burden, disconnected AI capabilities and Zeest's integrated workflow across several substantive paragraphs. |
| First sentences define their headings | Begin with a concrete problem, user need, system action or design relationship. |
| Repeated references to the source document | Remove narrative phrases such as "the proposal states", "proposal-grounded" and "the proposal does not specify" from the report body and captions. Keep source traceability in planning notes. |
| Repeated "this report/chapter describes" statements | Keep document-purpose language only where the mandatory Purpose section and final roadmap need it. Other sections discuss Zeest directly. |
| Disclaimers consume large parts of paragraphs | State the prototype status clearly, retain required PLANNED notices for prospective implementation/evaluation, and place unresolved details where they belong. |
| Audience paragraph mixes readers and affected people | Identify academic/technical readers and physicians; discuss patients as people whose information is handled in Stakeholders. |
| Chapter 1 ending is detached from its opening | Connect the closing discussion to the clinical problem and physician control, then provide the required concise chapter roadmap. |
| FRs often describe architecture rather than complete interactions | Rewrite as atomic "The system shall..." statements with actor, trigger, observable outcome and verification intent. |
| One use case combines several different clinical inputs | Separate imaging, laboratory and medication-context tasks, with input-specific failures. |
| QA/NFR sections repeat approval and evidence features | Use conventional quality categories; put functions in FRs and concrete quality constraints in NFRs. |
| Evaluation appears as another application feature | Distinguish research/evaluation requirements from physician-facing operations without adding headings. |
| GUI starts with a preselected patient and has passive input rows | Specify the entry, patient selection, encounter selection and input controls needed to make the workflow understandable. |
| Long captions repeatedly say nothing is implemented | Describe the image and its purpose concisely; keep its planned status clear without repeating a full disclaimer in every caption. |
| Assumptions are mostly a list of unresolved choices | Separate actual operating assumptions from configuration decisions and external dependencies. |
| Database is detailed before workflows are settled | Derive the schema from the approved actions and required persisted information, then update the ER diagram and dictionary together. |

"Clinical proposal" is a system concept: the generated diagnosis/treatment draft awaiting physician approval. Removing references to the project proposal document must not erase that distinction. "Recommendation" or "draft diagnosis and treatment plan" can replace repetitive wording where clearer, while all states and labels remain consistent.

## 4. Scope of the rewrite

Rewrite Kashaf's Chapters 1, 2 and 4 completely, including tables and figure descriptions. Update Kashaf's bibliography where verified sources are needed, owned PlantUML/HTML sources, rendered owner-prefixed images, START_HERE.md and HANDOFF.md. Preserve useful existing figure layouts where possible, but revise their coverage after the workflow is approved.

Prepare the Executive Summary after the rewritten chapters agree with the other members' contributions. The Appendix currently contains tutorial examples and needs an agreed project-specific outline. Both are included in the completion plan, but neither will invent material from unfinished Chapters 3/5/6.

Keep the current owner folder structure. This plan lives in kashaf/; root PLAN.md and README.md remain coordinator-owned. Do not edit another member's files, main.tex, FastFyp.cls, front matter, or add packages. Preserve every retained chapter/section/subsection heading and its order. Do not copy the samples' extra subsection hierarchy.

## 5. Chapter 1: Introduction

Planning target for the opening: four connected paragraphs of roughly 150-200 words each, around 600-800 words in total. Adjust if the material becomes repetitive; this is a content estimate, not a fixed page requirement.

| Existing location | Replacement content |
|---|---|
| Opening beneath Introduction | Paragraph 1: patient information across encounters and input types; why continuity matters. Paragraph 2: consultation documentation and the need to bring current inputs together. Paragraph 3: the limitations motivating integration of language models, specialist analysis and evidence retrieval, supported by verified original sources. Paragraph 4: Zeest's workflow, retained physician responsibility and the research contribution. |
| Purpose of this Document | Describe the project goal and four research questions directly: memory contribution, agent workflow versus a single LLM, critic contribution, and multimodal versus text-only input. Explain the planned investigation without predicting results. Usually two substantive paragraphs. |
| Intended Audience | Academic evaluators/supervisor, technical researchers/developers, and physicians interested in the workflow. Explain what each needs to understand. Remove the patient-chatbot line entirely from this section. |
| Definitions, Acronyms, and Abbreviations | Keep a readable glossary of terms actually used, including longitudinal memory, encounter, RAG, clinical draft, physician approval and audit history. Remove unnecessary administrative terms if unused. |
| Conclusion | Briefly reconnect the problem and intended contribution. The last paragraph gives one concise sentence per included chapter, followed by the compulsory references and supporting appendix. No extra unrelated warning paragraph after the roadmap. |

Use direct statements about the project and appropriate original-source citations for external claims. Do not cite the internal source document after every paragraph. Do not make unsupported "no existing system" claims or promise improved patient outcomes.

## 6. Chapter 2: Project Vision

| Existing location | Replacement content |
|---|---|
| Chapter opening | A practical account of the physician's fragmented case information and the intended integrated workspace. No definition of "project vision". |
| Problem Domain Overview | Explain the system from the physician's perspective: selecting a patient and encounter, reviewing history, collecting current inputs, inspecting a generated draft and evidence, and deciding what to record. Mark newly approved supporting workflows as design requirements, not previously implemented facts. |
| Problem Statement | State the specific problem clearly: disconnected longitudinal/current information and documentation within a reviewable, physician-controlled decision-support workflow. |
| Problem Elaboration | Several connected paragraphs developing history retrieval, documentation, multimodal integration, evidence support and review control. Explain their consequences and relationship, not just enumerate agents. |
| Goals and Objectives | Retain all nine objectives. Express a clear goal and concise action-oriented objectives; keep stable O1-O9 identifiers for coordination. |
| Project Scope | Describe what users can do and what processing is included. State exclusions once clearly, without repeatedly explaining why the report cannot claim other features. |
| Sustainable Development Goal (SDG) | Explain the intended relationship with SDG 3 directly, cite the verified UN source and reference the existing figure. Do not assert measured health impact. |
| Constraints | Discuss data access, suitable models/domains, service dependencies, project resources and physician approval. Keep configuration unknowns concise. |
| Business Opportunity | Explain the practical value of a single physician workspace and reusable integration. Avoid invented market sizes, subscriptions, customers or revenue forecasts. |
| Stakeholders Description/ User Characteristics | Physicians are the direct users. Patients are the people whose clinical information informs the workflow. Academic/development stakeholders have separate project roles. No assumed institutional partnership or extra application roles. |
| Stakeholders Summary | A concise role/interest/responsibility table introduced by substantive text, without confusing stakeholders with login roles. |
| Key High-Level Goals and Problems of Stakeholders | Connect each stakeholder's needs to the system: case continuity, manageable documentation, inspectable evidence, accountable review and careful handling of information. End with a natural chapter synthesis without adding a Conclusion heading. |

A clearer stakeholder sentence, if needed, is: "Patients are affected by how their clinical information is handled and how recommendations are reviewed; physicians are the direct users of Zeest." The exclusion of a patient-facing chatbot belongs in Scope, not Audience.

## 7. Chapter 4: features and functional requirements

Rebuild the chapter around the complete clinical workflow rather than agent names alone. Keep a compact introductory paragraph about that workflow, not a paragraph defining the SRS heading.

### Proposed functional coverage

The following inventory specifies the complete intended system. Functional requirements and use cases describe required behaviour directly, without development-status qualifiers such as "available in the prototype", "not implemented" or "not executed". Different actions become separate requirements where their outcome or failure conditions differ. Scope decisions and implementation/evaluation status remain separate planning information.

| Group | Actions to specify | Basis / approval status |
|---|---|---|
| Physician access | Login; logout; reject invalid credentials; prevent an unauthenticated session from using protected actions | Supporting addition proposed for approval. No public signup, account administrator or password-reset module is assumed. |
| Patient navigation | View all patients; select a patient; view the selected patient's information | Supporting interface requirements proposed for approval. Any agreed access restrictions belong in separate security requirements and use-case preconditions. |
| Encounter navigation | View encounter history; open an encounter; associate a current consultation with the selected patient/encounter | Derived workflow detail to approve. Creation versus selection of a current encounter must be settled. |
| Consultation audio | Start capture; stop capture; obtain transcription; present structured notes for review | Core transcription goal plus proposed control details. No pause, diarisation or language claims are assumed. |
| Notes review | Display the notes; permit physician correction of transcription/structured notes before downstream use | Display follows the transcription goal; editing/persistence is a supporting design addition to approve. |
| Imaging input | Select/supply a supported image; reject unsupported/unusable input; run the selected existing model; show its findings in the case context | Core imaging goal, expressed as distinct input, processing and output requirements. Formats and labels remain unresolved. |
| Laboratory input | Supply laboratory information; validate required representation; display the Laboratory Agent's case findings | Core Laboratory Agent capability. No invented ranges, diagnoses or document formats. |
| Medication context | Supply or inspect medication information; present Medication Safety Agent findings linked to the case | Core Medication Safety capability; exact knowledge resource remains unresolved. |
| Case preparation and memory | Retrieve the selected patient's relevant history; combine it with current inputs; retain the temporal/source relationship | Core memory and Clinical Case capabilities. Internal storage design stays in 4.9. |
| Evidence | Retrieve relevant guideline material; display citations and supporting passages with the clinical draft | Core evidence/RAG capability. No guaranteed correctness from citation presence. |
| Reasoning and critic review | Produce a draft diagnosis/treatment plan; run critic review before physician presentation; display review findings | Core reasoning and critic goals. Failure/status responses are specified explicitly. |
| Physician decision | Approve; modify; approve the modified draft; reject; record only approved clinical decisions | Core physician-control goal, with distinct action and state outcomes. |
| Audit | Record each decision-related action with its actor/time/context; show the encounter's action history | Core audit goal. Do not invent a secure append-only implementation. |
| Research requirements | Configure and compare the single-LLM, memory-augmented and full-system variants; preserve the shared-case comparison conditions | Separate research capability inside the existing section, with a distinct table/identifier convention for approval. It is not another physician use case or another clinical interface role. |

FR wording will be atomic and observable, following the samples' direct "shall" statements. Patient navigation will be expressed as separate requirements:

- The system shall allow the physician to view a list of all patients.
- The system shall allow the physician to select a patient from the patient list.
- The system shall display the selected patient's information.
- The system shall allow the physician to view the selected patient's encounter history.

The use-case names will be direct, such as "View All Patients", "View Patient Information" and "View Encounter History". Their flows describe actor actions and system responses for the complete system. Verification plans remain separate from requirement wording. Neither a "shall" requirement nor a use-case flow claims that development or testing has already occurred.

Use a compact FR table with ID, user/trigger and requirement. Keep a separate traceability register in the planning/handoff material so that each row does not become a dense objective/component/design matrix. Preserve useful existing IDs where meanings remain the same; document every split, replacement and retired identifier before Fatima/Esha depend on them. Do not silently reuse an old identifier for a different requirement.

### Quality attributes and NFRs

Quality Attributes will explain what quality means for Zeest using conventional categories. Non-Functional Requirements will make these qualities assessable through explicit constraints and planned checks. They will not repeat the FR list.

| Quality category | Zeest-specific meaning | Candidate constraint/check for the rewrite |
|---|---|---|
| Usability | Clear patient context, navigation and draft/approved distinctions | Consistent labels and visible selected patient/encounter; evaluate representative workflow tasks. Step/time targets require agreement. |
| Reliability and integrity | Consistent associations and persisted review state | Failure must not create a falsely approved record; repeated submission must not create contradictory decision state. Exact recovery behaviour must be specified. |
| Security and confidentiality | Appropriate access and careful handling of permitted clinical information | If authentication is approved, protected actions require an authenticated session. Use de-identified/synthetic cases. Do not claim regulatory compliance or invent a full permission system. |
| Performance | Transcription and case processing usable in the consultation workflow | Define separate transcription delay, history retrieval time and analysis duration measurements; thresholds remain TBD until resources and targets are agreed. |
| Maintainability and reusability | Replaceable integrations with understandable interfaces | Specialist components expose agreed input/output contracts; replacement is checked against those contracts. |
| Extensibility | Additional supported data/model domains without changing physician-control rules | Additions require compatible data, models and interface contracts. No promise of universal coverage. |
| Traceability | Inputs, retrieved evidence, generated drafts and actions can be related | Each presented citation/action retains a recoverable source/context relationship; verify linkage on controlled cases. |

Move explicit approval, displaying evidence, accepting inputs and running evaluation variants to functional/research requirements. Model reuse and permitted clinical domains also appear as design/scope constraints; they are not automatically software quality attributes. Do not force every requirement into only one category if it has both a behaviour and an integrity constraint, but state the distinction explicitly.

Do not copy the samples' five-second response limits, 24/7 availability, user counts, diagnostic accuracy or resilience guarantees. Proposed numerical acceptance targets can be reviewed later as targets; no invented values will be presented as established requirements or results.

## 8. Chapter 4: use cases, GUI and data design

### Proposed use-case inventory

Describe each significant user goal separately in the existing template table format. Final IDs follow approval of coverage.

1. Log in and log out, if approved.
2. View All Patients and select a patient.
3. View patient information and encounter history.
4. Open/select the current encounter; create one only if approved.
5. Record the consultation and obtain structured notes.
6. Review/correct structured notes, if editing is approved.
7. Supply an imaging input and inspect its findings.
8. Supply laboratory information and inspect its findings.
9. Supply/review medication context and inspect safety findings.
10. Request and review a draft diagnosis/treatment plan.
11. Inspect supporting evidence and critic findings.
12. Approve a clinical draft.
13. Modify a clinical draft and approve the revision explicitly.
14. Reject a clinical draft.
15. Inspect audit history.

This inventory will result in approximately 15-18 descriptions depending on where distinct goals need separate tables. Do not write a separate use case for every agent invocation or click. Agents inside Zeest are internal components, not additional human actors.

Each table must include the existing Name, Actors, Summary, Pre-Conditions, Post-Conditions, Special Requirements, Basic Flow and Alternative Flow fields. Flows alternate concrete actor actions and system responses. Examples of relevant alternatives: invalid credentials, empty patient list, unavailable encounter, missing audio permission, unsupported image, incomplete laboratory input, failed analysis, unavailable evidence, failed record save and modification without approval. These are proposed behaviours to agree, not observed incidents. A failed save must not produce a success message or an approved record.

### GUI coverage

Preserve the calm visual style of the recently approved HTML designs. Rework their coverage only after requirements and use cases are settled.

| View | Planned work |
|---|---|
| Login | Add only if access scope is approved; no fabricated institutional branding or registration workflow. |
| Patient list | Show the patient list and selection controls, linked to View All Patients and View Patient Information; searching/filtering remains optional. |
| Patient history | Retain the encounter list and clinical sections; connect it to the selected patient and current encounter. |
| Consultation | Make input actions explicit: audio controls, notes review, supported image/lab/medication inputs and analysis/review navigation. Current passive rows are not enough to show those tasks. |
| Review and audit | Preserve pending draft, evidence, critic review and decision actions; clarify modification/edit state and the explicitly approved content. |
| Empty/error states | Cover material failures in the use-case descriptions; add a separate figure only where necessary to explain a distinct interface. |

Five main views are an initial design recommendation, not a forced screen count. Controls/dialogues may cover several use cases. Each figure caption identifies the physician user, function and mapped use cases; the mapping table covers every approved use case. Keep placeholders, planned status and accessible descriptive captions.

PlantUML remains the source for use-case, navigation and ER diagrams. HTML remains the source for GUI images. Sources stay in kashaf/diagrams/ and rendered report images in Report template/Figures/ with kashaf_ prefixes. Keep existing figure labels where possible. Do not create new organizational layers or export images of tables.

### Database and other retained sections

| Location | Rewrite action |
|---|---|
| Assumptions | State operating assumptions about physician use, selected patient context, supported inputs, permitted data and external services. Separate assumptions from unsettled model/version choices. |
| Hardware Requirements | Describe the need for compute, storage, consultation audio and interface access directly. Final hardware capacities depend on chosen models; no invented RAM/GPU baseline. |
| Software Requirements | Keep the named stack and explain its actual intended roles concisely. LangGraph/ADK responsibility remains an open integration decision. |
| Database Design | Explain what must persist to support the approved workflow and how patient, encounter, inputs, drafts, evidence and physician actions relate. |
| ER Diagram | Review existing nine entities against the completed use cases; add physician identity/session concepts only if authentication is approved and the chosen approach requires persistence. Do not automatically model login/signup as separate domain entities. |
| Data Dictionary | Give consistent entity/field/type/key/nullability/meaning information. Preserve source and time relationships; review revision handling and whether current uniqueness constraints unnecessarily restrict amended drafts. |
| Risk Analysis | Explain each risk, its effect on a requirement and a realistic planned response. Include data/model dependencies, transcription, misleading evidence, patient-context mistakes, approval-state integrity, integration and evaluation resources. No invented scores or successful mitigations. |
| Chapter ending | Summarize the resulting workflow and its role in subsequent methodology/design with connected prose. Do not repeat an entire paragraph of non-implementation disclaimers. |

## 9. Executive Summary, Appendix and references

Executive Summary: one to two pages of plain prose for business/non-specialist readers, explaining the problem, proposed solution, intended value, scope and current deliverable. Write after the chapters agree; do not invent literature findings, completed experiments or performance.

Appendix: replace tutorial examples with approved supporting material. Recommended content is extended requirements/verification traceability or design-support material that would interrupt the chapters. The current appendix chapter title and subsections are explicit demonstrations, but changes still need an approved outline checked against the original template. If they must remain verbatim under the heading rule, flag that conflict before editing. Never retain irrelevant E=mc^2/C-program examples as Zeest content or manufacture algorithms to fill headings.

References: verify primary sources before citing clinical background, model capabilities, limitations or SDG claims. Source-document traceability stays in this plan/handoff rather than repetitive narrative citations. Coordinate canonical citation keys with Fatima; never edit her bibliography. Do not remove example references while another member's unchanged chapter or appendix still uses them. Do not write categorical superiority/novelty claims without evidence.

## 10. Writing and status rules

- Write Zeest with a capital Z; do not use em dashes.
- Main prose paragraphs contain 150-250 words; tables, captions and one-line bullets are not padded to that length.
- Begin paragraphs with their substantive point and build connected reasoning.
- Avoid repeated heading definitions, administrative narration and generic filler.
- Preserve every required heading and order; add no packages or fake subsection headings.
- Describe requirements with "shall" and future design with appropriate proposed wording.
- Write FRs, NFRs and use-case flows for the complete intended system; exclude development-status disclaimers from their statements.
- Retain red PLANNED notices for prospective implementation/testing/results where needed.
- Group status notices sensibly; do not attach the same warning to every paragraph.
- Keep numerical results, screenshots, citations and access claims truthful.
- Refer to every figure and table; keep descriptive captions and automatic numbering.

## 11. Order of implementation and approval

1. Approve this plan and its supporting workflow additions. No report-content rewrite occurs before approval.
2. Review revised outlines for Chapters 1 and 2 together, using the exact retained headings.
3. Draft/review and save those two chapters using the user's approved workflow. Show chat drafts only if requested; otherwise confirm the desired saving step before proceeding.
4. Agree the Chapter 4 action inventory, access assumptions and FR/QA/NFR split before full prose.
5. Rewrite Chapter 4 first half: opening, Features, FRs, QA, NFRs, Assumptions and Use Cases. Present the concrete portion for approval as requested.
6. Rewrite Chapter 4 second half: Resources, GUI, Database and Risks; update its diagrams and dictionary from the settled first half.
7. Record old-to-new IDs and contracts in Kashaf's handoff so Fatima and Esha can align their work.
8. Finish Executive Summary and approved Appendix after the necessary shared chapter information is available.
9. Compile and visually check the new PDF, preserve required headings, check paragraph lengths and source support, and scan for prohibited/repetitive phrasing.

Acceptance checks: complete physician workflow coverage; distinct functional and quality requirements; use cases linked to FRs and screens; database relationships matching persisted outcomes; approval retained after modification; no fabricated metrics or clinical results; no source-document narration throughout the body; exact heading/order preservation; readable figures/tables; no new undefined references or oversized content.

## 12. Approval decisions and assumptions

| Status | Decision / assumption |
|---|---|
| [Certain] | Kashaf's assignment is Chapters 1/2/4, Executive Summary and Appendix. Other member files and shared assembly stay unchanged. |
| [Certain] | The current submission is R&D Deliverable II, Chapters 1-6. The prototype is unbuilt. |
| [Certain] | The source document defines Zeest's core scope; samples guide writing/detail and do not establish additional project facts. |
| [Certain] | The final Introduction paragraph must summarize the included chapters despite the request to remove unnecessary report narration. |
| [Likely] | A physician login/logout flow with pre-provisioned access is the simplest access addition. Account setup/identity mechanism must be approved; no signup/admin module is assumed. |
| [Likely] | View All Patients, patient selection and View Patient Information are needed to explain entry into the clinical workflow. Search/filter is optional. |
| [Likely] | Opening/selecting a current encounter is needed; whether physicians create a new encounter requires approval. |
| [Likely] | Review and correction of generated consultation notes is a useful supporting requirement but is not an explicit source-document commitment. |
| [Guessing] | Five principal views and approximately 15-18 use-case descriptions will cover the approved workflow. Final counts depend on the agreed tasks. |
| [Certain] | Formats, clinical domains, models, performance thresholds, available resources and reviewer arrangements remain unresolved. |
| [Certain] | Source-based technical/clinical claims need verified references; results and evaluation outcomes cannot be predetermined. |

Approve or adjust login/logout, View All Patients, patient selection, current-encounter handling and note correction as part of this plan. Once their scope is approved, write their requirements and use cases directly as complete-system behaviour. Keep source traceability and actual development/evaluation status in separate notes rather than repeating them inside requirements.


### Implemented presentation adjustment

User requested paragraphs near the 150-word minimum, correctly bold template headings, sequential FR numbering and numbered QA descriptions. Applied within Chapters 1/2/4. Current FR IDs are FR01–FR38 in workflow order; HANDOFF.md records the migration. QA01–QA07 now correspond to seven numbered subsections. Historical plan IDs above are superseded. GUI remains pending separate review.
