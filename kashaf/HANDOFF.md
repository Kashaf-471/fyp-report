# Kashaf: coordination

Status: Chapters 1 and 2 drafted on 4 October 2026 after outline approval and explicit permission to write directly into owned files. Both halves of Chapter 4 are drafted with explicit approval. Chapters 1, 2 and 4 await Kashaf's review; Executive Summary and Appendix remain to be written.

## Completed work

Introduction and Project Vision now contain proposal-grounded prose, terminology/objective/scope/stakeholder tables, and the existing SDG image with a descriptive caption. Template headings are unchanged. No prototype results or screenshots were added.

## Decisions and stable IDs

O1 through O9 in Chapter 2 follow the nine proposal objectives in order. They are objective IDs, not implemented requirement IDs. Kashaf approved SDG 3 alignment. Citation keys: zeestA:proposal (supplied internal proposal) and zeestA:unSDG3 (official UN page). No shared or other-member source files were edited.

## Dependencies and open questions

See START_HERE.md and PLAN.md. No dependency is assumed resolved.

## Approved current assignment

Chapters 1, 2 and 4; Executive Summary and Appendix. All owners maintain their own references. Current submission is six-chapter R&D Deliverable II; Chapters 7 through 10 are excluded. No chapter writing was done during this scope update.

## Draft verification and next work

Combined report compiled with the archived Tectonic toolchain. New citations resolve and no overfull boxes were reported. Main prose paragraphs are 150 to 250 words. The figure reference is corrected locally in Chapter 2. Table/figure rendering was visually checked. Existing XeTeX Times substitutions and template diagnostics remain.

Kashaf explicitly changed the draft-in-chat workflow for the approved Chapter 1/2 task: write these chapters directly into their files. Approval is still required before starting a new chapter task. Chapter 4 sections 4.7 through 4.10, Executive Summary and Appendix remain template material. The SDG source is https://sdgs.un.org/goals/goal3, accessed 4 October 2026.

## Chapter 4 first-half handoff

Sections 4.1 through 4.6 are drafted. Every original heading and every byte from Hardware and Software Requirements onward is preserved. No second-half content or other member's files was written. Review the first half before authorizing 4.7 through 4.10. A float-clearing boundary keeps the first-half tables before the untouched second half.

Stable proposed IDs: F01-F10 feature groups; FR01-FR16 functional requirements; QA01-QA06 quality attributes; NFR01-NFR08 non-functional requirements; A01-A07 unresolved dependencies; UC01-UC08 physician use cases. They are proposed specification IDs, not verified implementation outcomes.

| Use case | Related functional requirements |
|---|---|
| UC01 Review longitudinal history | FR01, FR02 |
| UC02 Transcribe consultation | FR03, FR05 |
| UC03 Supply clinical inputs | FR04-FR08 |
| UC04 Review proposal and evidence | FR09-FR11 |
| UC05 Approve a proposal | FR12, FR15 |
| UC06 Modify and approve a proposal | FR13, FR12, FR15 |
| UC07 Reject a proposal | FR14, FR15 |
| UC08 Inspect audit history | FR15 |

FR16 describes the project team's evaluation framework, not a physician-facing clinical use case. Pending/rejected proposals are excluded as final approved clinical decisions; audit retention is distinct from clinical approval. Alternative flows are proposed design interpretations, not observed failures.

Diagram source: diagrams/kashaf_D01_doctor_use_cases.puml. Rendered asset: ../Report template/Figures/kashaf_D01_doctor_use_cases.png. Render with the official PlantUML jar (local ignored copy in .tools/, version 1.2026.8):

```powershell
java -jar .tools/plantuml-1.2026.8.jar -tpng -o '../../Report template/Figures' kashaf/diagrams/kashaf_D01_doctor_use_cases.puml
```

The command is run from the repository root; the output directory is resolved relative to the .puml source. Official renderer download: https://plantuml.com/download. No LaTeX packages or shared assembly changes were made.

Confirmed assumptions remain unresolved: dataset access, selected imaging/transcription/embedding models, clinical domain, medication knowledge base, LangGraph/ADK division, hardware, reference judgments, sample counts and numeric thresholds. Fatima and Esha may rely on the proposed requirement meanings but must not infer those choices or implemented behaviour.

Final first-half verification: report compilation passed; headings and sections 4.7 through 4.10 are preserved exactly. All eight use-case tables render before section 4.7. No undefined citations/references or overfull boxes were reported. Main prose paragraphs contain 161 to 165 words; table/diagram layout was visually reviewed. Existing local font substitutions and underfull-box diagnostics remain.

## Chapter 4 second-half handoff

The user approved sections 4.7 through 4.10. They now contain proposed hardware/software resources, physician view mappings, navigation, three labelled placeholder-only wireframes, an ER model and data dictionary, risk analysis and a closing paragraph. Original chapter/section/subsection headings and ordering are retained. First-half report content is unchanged; obsolete comments and line endings were updated. Shared assembly/class and other members' files remain unchanged.

New PlantUML sources: diagrams/kashaf_D02_doctor_navigation.puml and diagrams/kashaf_D03_hybrid_memory_er.puml. New editable wireframe sources: diagrams/kashaf_W01_history_view.svg, kashaf_W02_consultation_view.svg and kashaf_W03_review_audit_view.svg. Matching PNG images are in ../Report template/Figures/. The wireframes visibly state PLANNED and NOT A PROTOTYPE SCREENSHOT; they contain no real patient data or outputs.

The nine candidate entities are Patient, Encounter, ClinicalInput, Proposal, EvidenceItem, ProposalEvidence, PhysicianAction, ClinicalDecision and SemanticMemory. Names, fields, UUID types, nullability, uniqueness and cardinalities are proposed design choices, not proposal facts or implemented tables. Esha should review them against Chapter 6 before treating them as settled contracts. The ER image shows key fields; the dictionary supplies the complete field list.

Proposed integrity rules: ClinicalDecision requires an explicit approve action for the same proposal and the matching approved content. Modification alone does not approve a decision. Pending/rejected proposals stay separate from approved clinical decisions. Audit history retains modification, approval and rejection actions. SemanticMemory requires exactly one source: an input or an approved decision. Transactions, physical storage, retention, model and vector dimension are TBD.

W01 maps to UC01 and FR01/FR02; W02 to UC02/UC03 and FR03-FR08; W03 to UC04-UC08 and FR09-FR15. Risks R01-R08 link to established requirements/dependencies without probabilities or measured mitigation. Hardware values, models, domains, thresholds, references and access conditions remain unresolved.

Verification: report compiled successfully; no overfull boxes, oversized floats, undefined citations or undefined references. New main prose paragraphs contain 152 to 166 words. New figures/wireframes/tables were visually reviewed. Existing local font substitutions and underfull-box warnings remain. No prototype implementation/testing, commits or pushes occurred.

## Approved HTML wireframe replacement

The user authorized polishing the imported HTML designs and inserting them into Chapter 4. Current editable sources are `diagrams/stitch_zeest_clinical_copilot_wireframes/patient_history/code.html`, `consultation/code.html` and `review_and_audit/code.html`. Each view keeps its rendered `screen.png`; the existing `clinical_cockpit/DESIGN.md` records current design rules and requirement mappings. Open an HTML file in a browser to review it. Navigation links work; clinical controls are static design illustrations, with no recording, retrieval, approval or audit processing.

The HTML is self-contained with local CSS and system fonts. External CDN dependencies, hidden simulated clinical actions, unsupported verification claims, invented identifiers and redundant technical labels were removed. The three owner-prefixed report PNGs now render these HTML sources. Existing SVG sources are earlier drafts, preserved for reference; edit the HTML for the current designs. Keep the current owner folder structure and stable report asset names.

Chapter 4 retains its section headings and figure labels. Captions describe the revised panels and identify physician users, use cases and requirement mappings. The larger review figure remains within the existing template formatting. The PLANNED notice remains. No main.tex, class, packages, root documentation or other member files were changed.

Final verification: the report compiled to 68 pages; GUI figures appear on PDF pages 45 through 47 (printed pages 32 through 34). These pages were visually reviewed, including continuation controls and the empty audit table. No overfull boxes, oversized floats or undefined citations/references were reported. Existing font substitutions and template warnings remain. No commits or pushes were made.

## Rewrite review requested on 5 October 2026

The user rejected the current writing style and requested a sample-based deep review and implementation plan before a complete rewrite. Read `REWRITE_PLAN.md` for the sample evidence, section-by-section changes, proposed functional coverage, quality/NFR distinctions, use-case and GUI inventory, database review, and approval sequence. This review used extracted sample text rather than screenshots alone. Relevant Introduction/Vision chapters of four research-oriented samples and SRS chapters of the three with that chapter were closely read. No current chapter, bibliography or visual was changed during this planning step.

Supporting login/logout, permitted patient browsing/selection, current-encounter handling and note correction are explicitly proposed for approval. Do not treat these as previously established source facts or implemented features. Keep current IDs until the revised inventory is approved; record every split/retired identifier when rewriting. The current chapters are drafts awaiting complete revision, not finalized contracts for other members.

User correction: FRs, NFRs and use-case flows must describe the complete intended system directly, following the samples' shall statements. Use View All Patients, patient selection, View Patient Information and View Encounter History; do not qualify these as prototype-only records or insert not-implemented/not-executed disclaimers into requirements. REWRITE_PLAN.md was corrected accordingly. Actual development/testing status remains separate and truthful. Chapter content has not yet been rewritten.


## Approved rewrite completed on 5 October 2026

This entry supersedes the planning-only status above. The user explicitly authorized complete rewrites of Chapters 1, 2 and 4. Their original headings and order are preserved. Introduction and Vision use fuller connected prose, generally 150?190 words per paragraph, without repeated document-proposal narration or em dashes. Zeest keeps its capitalization. Complete-system requirements and use cases use direct functional wording; planned implementation/evaluation notices remain separate.

Chapter 4 now contains 38 functional requirements, four research requirements, seven quality attributes, 16 non-functional requirements and 17 use cases. Supporting account access, patient browsing/selection, opening an existing encounter and note correction follow the approved rewrite scope. Account provisioning, public registration and encounter creation are not specified. Actual implementation or test results are not claimed.

Identifier coordination: FR04's combined input requirement is retired and replaced by FR29?FR32. FR16's evaluation content is retired from clinical functions and replaced by RR01?RR04. FR01?FR03 and FR05?FR15 retain their principal functions; approval persistence is clarified by FR12/FR37, modification by FR13 and audit display by FR38. New supporting functions use FR17?FR40. UC03's combined input case is retired in favour of UC15?UC17. UC01/UC02/UC04?UC08 retain their principal meanings. UC09?UC14 add account/patient/encounter/note interactions; UC18 covers evidence inspection. QA and NFR tables replace the previous taxonomy completely, so downstream chapters must use these current definitions rather than old identifier meanings.

The logical data design adds Physician account ownership and explicit draft revisions, action snapshots and approved-decision references. Esha should align Chapter 6 to the current Chapter 4 tables and ER diagram. Fatima should align the methodology to RR01?RR04 and the approved workflow. These are intended design contracts, not evidence of a built database.

The three PlantUML diagrams and their owner-prefixed rendered assets are updated. GUI HTML, existing W01/W02/W03 images, shared main.tex/class and all Fatima/Esha files are unchanged. GUI captions identify current coverage; missing access/patient-selection controls will be addressed in the separate GUI review. Four verified primary-source bibliography entries support background and credential storage. The assembled PDF compiles to 70 pages with no overfull boxes, oversized floats or undefined references/citations. Existing font substitutions and underfull warnings remain. No commit or push was made.


## Presentation and numbering revision

The user requested shorter paragraphs while retaining the 150-word minimum, bold template headings and separate QA headings. Prose was tightened toward the minimum, with most paragraphs around 150–159 words. Seven numbered QA subsections replace the combined summary table. Their descriptions retain QA01–QA07 meanings in that order. No unnumbered substitute headings were added.

The class already specifies bold Times headings. The XeTeX build had fallen back from unsupported TU/ptm font shapes. A local T1 font-encoding group in each owned chapter restores the template's Times body, bold headings and bold captions. The group ends within each chapter, leaving other members' files and the shared class/assembly unchanged. No packages were added.

FR identifiers now run consecutively from FR01 to FR38 in workflow/table order. This supersedes the prior identifier-preservation notes. Use-case references and owned chapter mappings have been updated. Migration from the preceding draft: FR17 → FR01, FR18 → FR02, FR19 → FR03, FR20 → FR04, FR21 → FR05, FR22 → FR06, FR23 → FR07, FR24 → FR08, FR25 → FR09, FR26 → FR10, FR03 → FR11, FR27 → FR12, FR28 → FR13, FR29 → FR14, FR30 → FR15, FR31 → FR16, FR32 → FR17, FR01 → FR18, FR02 → FR19, FR05 → FR20, FR06 → FR21, FR07 → FR22, FR08 → FR23, FR33 → FR24, FR39 → FR25, FR40 → FR26, FR09 → FR27, FR10 → FR28, FR34 → FR29, FR11 → FR30, FR35 → FR31, FR36 → FR32, FR12 → FR33, FR13 → FR34, FR14 → FR35, FR37 → FR36, FR15 → FR37, FR38 → FR38. Other members must consult the current Chapter 4 IDs when aligning their chapters. GUI HTML and rendered screen images remain unchanged for separate review.


Feature-list presentation: at the user's request, Chapter 4 List of Features now uses concise one-line bullets instead of the explanatory paragraph and feature table. Feature coverage and FR identifiers are unchanged. The removed table reference was removed with its paragraph.
