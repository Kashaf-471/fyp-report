# Zeest use-case coverage audit

Status: approved revision completed. Physician records are restricted to their own patients. GUI, navigation, Chen-style ER diagrams and the matching dictionary are now integrated into Chapter 4.

The inventory was checked against the nine project objectives, clinical scope, current FRs, and the SynapSure/RecruitEase/ParkEase sample tables. Sample account and browsing patterns guide presentation; unrelated sample features were not copied.

| Area | Current coverage |
|---|---|
| Accounts | UC01 Sign Up, UC02 Log In, UC21 Log Out; invalid/missing registration data, duplicate email and invalid credentials are alternative flows. |
| Patient context | UC03?UC06: own patient list and selection, patient information, encounter history and opening an existing encounter. Ownership is checked throughout. |
| Consultation | UC07 recording/transcription; UC08 review and correction of notes. |
| Clinical inputs | UC09?UC11 imaging, laboratory and medication context; UC12 specialist findings. Unsupported input and failed processing are alternatives. |
| Reasoning and review | UC13 generation and review; UC14 evidence; UC15 critic findings; UC16 modification; UC17 approval; UC18 rejection. |
| Persistent outcomes | UC19 approved decisions; UC20 audit history. Approval binds the saved revision, and modification alone never approves it. |
| Research | UC22 comparative evaluation covers RR01?RR04; Research team is an evaluation actor, not an added clinical application role. |

## Objective coverage

| Objective | Use cases / included behaviour |
|---|---|
| O1 hybrid memory | UC05 and relevant-history retrieval included by UC13. |
| O2 transcription | UC07?UC08. |
| O3 specialised agents | UC09?UC13. |
| O4 existing imaging model | UC09, UC12. |
| O5 cited guidelines | Evidence retrieval included by UC13; UC14. |
| O6 clinical reasoning | UC13. |
| O7 critic review | Critic review included by UC13; UC15. |
| O8 physician decisions and audit | UC16?UC20, including accepted-decision and action recording. |
| O9 ablation comparison | UC22 and RR01?RR04. |

## Open decisions before expanding scope

- Add Patient and Create Encounter: the current workflow starts from existing permitted patient/encounter records. Their entry/import and ownership-assignment workflow needs a user decision; no CRUD or external integration was invented.
- Password recovery, account profile editing, patient search, deletion, exporting decisions and notifications remain optional suggestions.
- Registration creates an application account; it does not imply a physician credential-verification service. No email verification or administrator approval was specified.
- Registration fields and physician ownership are now included in the logical schema, diagrams and dictionary. Implementation and patient/encounter creation or import remain separate work.

## Numbering

FR01?FR44 are sequential in the current workflow/table order. UC01?UC22 are sequential in the table order. Use-case names, captions, references and W01?W03 textual mappings use the current IDs. GUI, navigation and ERD sources/images were updated under the subsequent report-integration approval. Read diagrams/REPORT_VISUALS.md for current assets.
