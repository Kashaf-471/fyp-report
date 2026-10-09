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


## Approved concise rewrite and complete use-case audit

The user approved the implementation plan and explicitly changed substantive paragraph length to 100?120 words, overriding the 150-word minimum for Kashaf's chapters. Chapters 1/2/4 now use concise relevant prose. The Introduction has two focused opening paragraphs and no detailed paper discussion. Definitions and stakeholder-summary sections use brief table references; unnecessary narration before requirement tables and design figures was removed. QA headings and the template's bold Times style remain. Original retained headings/order are preserved.

The user further specified that every physician has their own patient records. Requirements, confidentiality constraints and all patient/encounter use cases now restrict access and processing to that physician's records. Patient creation/import and assignment of ownership are open workflow decisions, documented in USE_CASE_AUDIT.md. No administrative or external data integration was invented.

The current inventory has 44 sequential FRs and 22 sequential UCs. Sign Up uses name/email/password, invalid/missing field validation, duplicate-email rejection and a subsequent login path. Separate cases cover analysis findings, critic findings and approved decisions. Modify is separate from Approve; saving never implies approval. Tables use actual Special Requirements constraints, paired actor/system steps and branch identifiers such as 4-A/4-B. A Research team actor covers comparative evaluation, without adding a clinical application role. The single-boundary PlantUML diagram includes mandatory processing and conditional review relationships; all actors are outside.

Read USE_CASE_AUDIT.md for objective coverage and unresolved additions. This audit does not assert that unspecified CRUD, password recovery, exporting, notifications or profile editing are required. Navigation, ERD/dictionary structure and GUI assets are unchanged for their later review. Textual GUI mappings use current UC IDs; the earlier navigation itself still requires alignment. Registration name/email storage and physician-to-patient ownership need data-design alignment before implementation.

FR migration from the immediately preceding draft: FR41 -> FR01, FR42 -> FR02, FR43 -> FR03, FR44 -> FR04, FR45 -> FR05, FR01 -> FR06, FR02 -> FR07, FR03 -> FR08, FR04 -> FR09, FR05 -> FR10, FR06 -> FR11, FR07 -> FR12, FR08 -> FR13, FR09 -> FR14, FR10 -> FR15, FR11 -> FR16, FR12 -> FR17, FR13 -> FR18, FR14 -> FR19, FR15 -> FR20, FR16 -> FR21, FR17 -> FR22, FR18 -> FR23, FR19 -> FR24, FR20 -> FR25, FR21 -> FR26, FR22 -> FR27, FR23 -> FR28, FR24 -> FR29, FR25 -> FR30, FR26 -> FR31, FR27 -> FR32, FR28 -> FR33, FR29 -> FR34, FR30 -> FR35, FR31 -> FR36, FR32 -> FR37, FR33 -> FR38, FR34 -> FR39, FR35 -> FR40, FR36 -> FR41, FR37 -> FR42, FR38 -> FR43, FR46 -> FR44. New registration and ownership rows were inserted before login; approved-decision browsing was added at the end.

UC migration: UC09 -> UC02, UC11 -> UC03, UC12 -> UC04, UC01 -> UC05, UC13 -> UC06, UC02 -> UC07, UC14 -> UC08, UC15 -> UC09, UC16 -> UC10, UC17 -> UC11, UC04 -> UC13, UC18 -> UC14, UC06 -> UC16, UC05 -> UC17, UC07 -> UC18, UC08 -> UC20, UC10 -> UC21. UC06 from the old draft now means Modify only (UC16); approval is UC17. New cases are listed in the audit. Downstream chapters must use the current identifiers and physician ownership rule.

Final assembly is 63 pages. Visual review covered shortened Introduction, use-case diagram and account/patient tables. Compilation has no overfull boxes, oversized floats, missing characters or undefined references/citations. Shared main.tex/class and Fatima/Esha files, navigation/ERD/GUI source and images are unchanged. No commit or push was made.


## Float placement correction, 6 October 2026

User reported FR tables after Quality Attributes and ER/data-dictionary floats crossing their headings. Added native LaTeX clearpage boundaries after float-bearing sections/subsections and before following headings in Kashaf's Chapters 1/2/4, including chapter-file endings. Tables and figures remain normal floats within their own sections and are not forced onto the prose page. No class/package/shared-file changes were needed. This is a layout correction, with content, numbering and diagram assets unchanged.


## Simplified imported GUI screens, 6 October 2026

User authorized editing all screens in diagrams/stitch_zeest_clinical_support_system/stitch_zeest_clinical_support_system to match the simple SynapSure/ImageSense sample presentation. Rebuilt all 11 imported HTML files and added the missing Login page: 12 HTML layouts including edit/approval/rejection variants. Kept the imported folder structure. Shared styles.css and preview.js are local, with working preview navigation and tabs. No clinical backend, authentication, recording, saving, approval or evaluation is simulated.

Removed invented ward/bed data, clinician identity, citations, clinical findings, numeric confidence scores, protocol banners, version strings and compliance claims. Screens use neutral sample references and empty clinical content. The restrained white/teal visual style uses plain forms, tables, two-column layouts and compact dialogs. Visually compared sample GUI pages (SynapSure PDF page 45 and ImageSense PDF page 45). Generated each screen.png at 1366 by 1000 and four additional tab screenshots for laboratory, medication, critic and audit coverage. SCREENS.md maps every UC01?UC22 to a screen; local link and asset targets verified.

This task updates HTML sources and their screenshots only. Report chapter/figure insertion, colourful navigation and ERD changes remain separate work. Previous three-screen report figures and main.tex/class/other member files are unchanged. Read the new folder SCREENS.md instead of the original generated design instructions. No commit or push made.

GUI visual refinement: user requested visuals. Added local SVG medical-record illustration to Sign Up/Login, task pictograms, tab icons, upload visual and symbolic empty states. Regenerated all screen PNGs and tab variants. Screens remain simple static prototype designs; no clinical imagery or results were invented. Report and other owners' files are unchanged.

User clarified that a prominent background image was required. Created decorative healthcare illustration using built-in image generation, saved under the new GUI folder assets/medical-background.png and applied visibly to Sign Up/Login. White forms sit on the left; physician illustration stays visible on the right. Regenerated and visually inspected screenshots. SCREENS.md records asset provenance and prompt. Report files remain unchanged.


## GUI, navigation and complete database section integrated, 6 October 2026

User approved report insertion of the visual screen designs, mapped users/use cases, colourful navigation and a complete Chen-style ERD/dictionary. Chapter 4 now includes sixteen owner-prefixed screen/state images, two navigation figures, four domain relationship views and six attribute sheets. Current template chapter/section/subsection headings and order remain unchanged. Each screen caption and coverage-table row identifies its actor and UC coverage. All UC01?UC22 are covered; input-screen generation controls also map to UC13. Decorative medical background is included on authentication pages. Designs remain explicitly PLANNED and contain no executed results or invented clinical information.

Schema is now complete at the logical design level: eighteen entities, ninety-one attributes, twenty-one relationships. Physician stores registration name/email/hash; Patient has physician ownership. ClinicalInput/InputRevision preserve corrected input versions; SpecialistFinding identifies analysed input revisions. Proposal/ProposalRevision preserve draft revisions; ProposalInput connects source input versions. CriticReview and ProposalEvidence identify the assessed/supported revision. PhysicianAction and ClinicalDecision enforce explicit revision-specific acceptance. SemanticMemory has exactly one source. EvaluationCase/EvaluationRun/EvaluationOutput support UC22 and RR01?RR04 without fabricated outputs. This supersedes the old ten-entity dictionary. Esha must align Chapter 6 to the current schema and constraints; Fatima should align research configuration/output descriptions. No changes were made to their files.

All diagram attributes and dictionary rows were checked against diagrams/kashaf_schema.json; all twenty-one relationships appear in the domain diagrams. Graphviz is used for the requested Chen appearance, with editable DOT and an alternative PlantUML model source. Source/asset details are in diagrams/REPORT_VISUALS.md. Patient creation, encounter creation and ownership-assignment UI remain separate open scope decisions; they were not invented.

Verification: final assembled PDF is 98 pages. Visual review covered screen mappings, illustrated signup, primary/research navigation, ER relationships, attribute sheets, dictionary tables and section transitions. No overfull boxes, oversized floats, missing characters or undefined references/citations. ER figures finish before Data Dictionary, and dictionary tables finish before Risk Analysis. Shared main.tex/class and all Fatima/Esha files are unchanged. Existing font substitutions, underfull warnings and duplicate front-matter page anchor remain template/build issues. No commit or push made.


## Navigation retained and ERD appearance corrected

User required keeping the swimlane along with the thumbnail flow and rejected separated entity/relationship and attribute diagrams. Report now includes both the primary thumbnail flow and the coloured Physician/Zeest swimlane. Research navigation also remains.

ERD is replaced with a single grouped conceptual model combining blue entity rectangles, green attribute ovals and amber relationship diamonds, following the supplied Hikari/coloured Chen examples. The complete model includes all eighteen entities, ninety-one attributes and twenty-one relationships. Four enlarged regions preserve readable labels; cross-region connections appear in the complete model. Primary keys remain underlined, FKs labelled and cardinalities shown. Native SVG sources and vector-PDF renderings provide predictable grouping and sharp zooming. Earlier Graphviz/separated sheets are superseded drafts. Data dictionary remains unchanged and was rechecked against schema JSON.

Final report compiles to 95 pages with no overfull boxes, oversized floats, missing characters or undefined references/citations. Main/class and other owners' files remain untouched. See diagrams/REPORT_VISUALS.md for current sources.


## Feedback audit, 8 October 2026

Read all three feedback pages and audited Chapters 1/2/4, with read-only checks of supplementary drafts/front matter. FEEDBACK_REVIEW.md records confirmed defects, passes, conflicts and proposed corrections. Several mistakes remain despite a clean compile. No report text, images, bibliography, shared files or other members' files changed during this audit.
