# Esha (Eesha Irfan in proposal): coordination

Status: Chapter 6 and all six assigned design diagrams drafted on 8 October 2026.

## Completed work

- **Chapter 6 Design Prose & Tables:** Fully drafted in `esha/06_high_level_and_low_level_design.tex`. All required template section headings and ordering are strictly preserved. Every single prose paragraph is calibrated to between 150 and 173 words. The text uses `Zeest` with capital Z and zero em dashes. Prospective implementation, hardware targets, and model evaluations are explicitly marked with `\textcolor{red}{PLANNED: ...}`.
- **Component Contracts & Design Decisions Tables:**
  - `tab:esha:contracts` (T14): Formal contracts defining inputs, outputs, persistence layers, and recipient components for each of the eight specialist agents.
  - `tab:esha:decisions` (T15): Explicit architectural trade-offs, supported framework choices, and unresolved technical parameters.
- **PlantUML Diagram Sources:** Created under `esha/diagrams/`:
  - `esha_D07_system_architecture.puml`: High-level system architecture across client, gateway, orchestration, specialist agents, model inference runtimes, and persistence stores.
  - `esha_D08_agent_subsystems.puml`: Specialist agent topology organized into intake, diagnostic, and governance pipeline stages.
  - `esha_D09_domain_classes.puml`: Unified domain class diagram implementing the Chapter 4 data dictionary entities, value objects, and service layer controllers.
  - `esha_D10_consultation_sequence.puml`: End-to-end clinical recommendation sequence across consultation capture, history retrieval, specialist inference, and critic review.
  - `esha_D11_approval_states.puml`: State transition diagram for clinical drafts, modeling pending review, revision iterations, explicit approvals, and rejection audit logging.
  - `esha_D12_memory_update_sequence.puml`: Sequence diagram modeling transactional approval boundaries, audit logging, and asynchronous vector indexing.
- **Rendered Figure Assets:** Rendered directly to `Report template/Figures/` using standard PlantUML specifications:
  - `Report template/Figures/esha_D07_system_architecture.png`
  - `Report template/Figures/esha_D08_agent_subsystems.png`
  - `Report template/Figures/esha_D09_domain_classes.png`
  - `Report template/Figures/esha_D10_consultation_sequence.png`
  - `Report template/Figures/esha_D11_approval_states.png`
  - `Report template/Figures/esha_D12_memory_update_sequence.png`
- **Bibliography:** Populated `esha/references.bib` with verified keys: `zeestC:fastapi`, `zeestC:nextjs`, `zeestC:langgraph`, `zeestC:pytorch`, `zeestC:pgvector`, and `zeestC:gemini`.

## Decisions and alignment with upstream contracts

- Aligned with Kashaf's Chapter 4 specifications: traces directly to requirements `FR01` through `FR38` and use cases `UC01` through `UC08`.
- Reuses all 10 entities from Kashaf's Data Dictionary: `Physician`, `Patient`, `Encounter`, `ClinicalInput`, `Proposal`, `EvidenceItem`, `ProposalEvidence`, `PhysicianAction`, `ClinicalDecision`, and `SemanticMemory`.
- Strict Clinical Governance Boundary: No AI agent has permission to write directly to `ClinicalDecision` or `SemanticMemory`. All generated drafts enter a `PENDING` status. Only explicit physician approval (`UC05`/`UC06`) triggers an atomic transaction that records a `ClinicalDecision` and initiates asynchronous semantic memory vector indexing.
- Audit Trail Immutability: Every physician interaction (`MODIFY`, `APPROVE`, `REJECT`) instantiates an immutable `PhysicianAction` record capturing the actor, timestamp, draft revision, and reviewed content snapshot.

## Assumptions and open dependencies

- The prototype is unbuilt; all system operations represent proposed design specifications.
- Exact model checkpoint selection for the PyTorch radiology classifier and speech-to-text engine remains to be finalized.
- The concrete division of workflow roles between LangGraph and Google Agent Development Kit (ADK) remains an ongoing research exploration.
- Production vector dimensionality and HNSW indexing parameters for pgvector depend on final embedding model selection.
- Hardware specifications, server concurrency limits, and live clinical data integrations remain TBD.
