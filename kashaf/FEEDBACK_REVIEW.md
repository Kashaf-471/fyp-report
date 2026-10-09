# Kashaf feedback audit

Reviewed 8 October 2026 against all three pages of FYP-I_Feedback_Summary.pdf.
Scope: Chapters 1, 2 and 4; supplementary owned files and shared front matter checked read-only. No report content changed.

## Confirmed issues

| Finding | Evidence | Proposed correction |
|---|---|---|
| Chapter 2 has no concluding paragraph summarising the vision. | 02_project_vision.tex:120?124. | Add closing prose; retain headings unless a Conclusion heading exception is approved. |
| Chapter 4 ends with Risk Analysis and a planned-status note, without a substantive conclusion. | End of 04_software_requirement_specifications.tex. | Add a chapter-ending paragraph after the risk table. |
| SDG image shows all seventeen goals and has a lengthy caption. | 02_project_vision.tex:74?84; PDF page 22, printed page 8. | Show only SDG 3 and use a concise accessible caption. Preserve the original asset. |
| Problem Statement partly describes what Zeest should do. | 02_project_vision.tex:16. | Focus on the problem and its consequences; keep solution descriptions in appropriate other sections. |
| GUI dumps have large blank backgrounds and inefficient page use. | Example PDF pages 56?57; recurring clearpage calls. | Crop unnecessary margins, pair related screens when readable and keep only necessary float boundaries. |
| GUI raster resolution is below 300 DPI at current print size. | 1366-pixel images placed at 6.02 inches: approximately 227 DPI. | Render at higher pixel density; merely changing DPI metadata does not solve this. |
| ERD labels are too small at print size despite sharp vector export. | PDF page 73, printed page 59. | Improve printable label size/page use, retaining the complete model and readable enlargements. |
| Several GUI/navigation/ER captions are long. | Chapter 4 captions reach 38 words. | Shorten while retaining user/UC coverage and accessible descriptions. |
| Nullable repeats No throughout several individual dictionary tables. | Physician and Encounter tables, for example. | Merge nullability into constraints consistently, preserving optional and conditional-source rules. Values do vary across the complete schema. |
| Website access dates lack square brackets. | references.bib: zeestA:unSDG3 and zeestA:owaspPasswords. | Format bracketed access dates after website links. |
| RAG is used in the Introduction before its expansion in the glossary. | 01_introduction.tex:10. | Expand at first substantive use without repeated prose definitions. |

## Checks that pass

- Chapter 1 Conclusion is one paragraph with the roadmap, no bullets or citations.
- Required headings are present and numbered; no per-use-case subsection headings.
- No em dashes, bold pseudo-headings or unnecessary bold prose.
- FR01?FR44 and UC01?UC22 are consecutive.
- Use-case tables are centred, captioned above and follow actor/system flow columns. Most pages fit two or three use cases; the final single table is a remainder.
- GUI captions and coverage tables identify users and UCs.
- Both thumbnail and Physician/Zeest swimlane navigation are present.
- ERD is under ER Diagram, has a white background and matches the dictionary entities/attributes. It is not a DFD.
- FR tables finish before QA; ER diagrams finish before the dictionary; dictionary tables finish before Risk Analysis.
- No test cases or sequence diagrams were added to Chapter 4. Research requirements are specifications, not invented results.
- ieeetr is used. Latest compile has no overfull boxes, oversized floats, missing characters or undefined references/citations.

## Conflicts with existing approvals/template

- Feedback requires 150?250 words, but the user approved 100?120 words. Keep that approval unless the user changes it. One current ER introductory paragraph is about 87 words and should be brought into the chosen range.
- Feedback discourages abbreviation definitions in headings. The retained SDG heading contains (SDG), and Database Design has an instructional parenthesis. These are inherited template headings; changing them needs a template exception.
- Feedback says use-case diagrams should not be in Chapter 4; the user explicitly requested and approved this placement. Do not remove or relocate it silently, or edit Esha's files.
- Feedback suggests landscape for large ERDs. That changes the approved layout; do not add packages or modify the class/main.tex without a specific exception.
- Stakeholders Summary uses a table; feedback prefers stakeholder prose. Other stakeholder subsections already use paragraphs. This summary can be converted to prose while preserving its heading if approved.
- Feedback chapter numbering differs from this submission's methodology/design chapters; do not reorder chapters based on it.

## Separate submission blockers

- executive_summary.tex still contains template instructions instead of Zeest content.
- appendix_a_template_examples.tex still contains demonstration text, equations and unrelated references.
- Shared main.tex has placeholder title, supervisor/student details and declaration date/signature blanks. Its declaration layout also needs a coordinator check. It is frozen and was not edited.
- main.pdf must be exported as a single submission PDF with the required title/dash naming convention.
- Other members' chapters were not revised or certified by this audit.

## Proposed correction order

1. Resolve feedback/template conflicts, retaining short paragraphs unless instructed otherwise.
2. Fix problem-statement wording, first-use abbreviation, SDG visual/caption and chapter-ending conclusions.
3. Shorten captions and consolidate dictionary columns without losing information.
4. Improve GUI crops, page packing and raster density; improve ERD print legibility while retaining both navigation flows and section float boundaries.
5. Compile and visually verify all affected pages and cross-references.
6. Complete owned Executive Summary/Appendix under an approved content scope, and coordinate frozen shared front matter before submission.
