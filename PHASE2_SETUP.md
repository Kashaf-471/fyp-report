# Phase 2 setup — completed

Completed on 4 October 2026 after the students approved setup and authorized assumptions for unresolved questions. No Zeest chapter content, references, results, screenshots or diagrams were written.

## Assumptions

- **[Likely]** Report stage: FYP-1, following `Rules.txt`.
- **[Likely]** Project classification: Research and Development; retain every chapter and conditional section for this mechanical setup.
- **[Guessing]** Member A = Kashaf Ali; Member B = Fatima Malik; Member C = Eesha Irfan, following the proposal's name order. This mapping is stated as an assumption in the owner comments.
- **[Certain]** The prototype remains unbuilt. Model choices, dataset access, reviewers, hardware, numerical targets and execution evidence remain unspecified, rather than being invented.
- **[Certain]** Preserve the original title/student/supervisor/declaration placeholders and all demonstration text for the unchanged-PDF comparison. Main assembly is frozen after setup. Populating its metadata later would require an explicit exception to the user's freeze instruction.

The full Q1–Q12 working decisions are recorded at the top of [PLAN.md](PLAN.md).

## Deliverables

| Artifact | Location |
|---|---|
| Untouched original template PDF | [original-template.pdf](Report%20template/baseline/original-template.pdf) |
| PDF of the split assembly | [main.pdf](Report%20template/main.pdf) |
| Original source/figure snapshot | `Report template/baseline/sources/` |
| Original logs, bibliography and generated list evidence | `Report template/baseline/build/` |
| Preserved split build log | `.phase2/verification/split-build.log` |
| Original source SHA-256 hashes | `Report template/baseline/source_hashes.json` |
| Extraction and final assembly hashes | `.phase2/split_manifest.json` |
| All-page comparison results | [.phase2/verification/comparison.json](.phase2/verification/comparison.json) |
| Disposable verification images | Regenerate with the baseline comparison command; excluded from Git |

The original was successfully compiled and its PDF retained before the chapter extraction. Both builds use the same untouched class, assets, date and compiler.

## Exclusive file ownership

All files below are under `Report template/`. Each extracted file begins with a comment containing its owner's member letter and actual name.

| Owner | Files |
|---|---|
| A — Kashaf Ali | `chapters/01_introduction.tex`, `02_project_vision.tex`, `04_software_requirement_specifications.tex`, `08_user_manual.tex`, `10_conclusions.tex`, `appendix_a_template_examples.tex`; `frontmatter/executive_summary.tex`; `fypbib_A.bib` |
| B — Fatima Malik | `chapters/03_literature_review.tex`, `05_proposed_approach_and_methodology.tex`, `09_experimental_results_and_discussion.tex`; `frontmatter/abstract.tex`; `fypbib_B.bib` |
| C — Eesha Irfan | `chapters/06_high_level_and_low_level_design.tex`, `07_implementation_and_test_cases.tex`; `fypbib_C.bib` |

Chapter titles and contents were extracted verbatim, including their `\chapter` commands. Abstract and Executive Summary bodies were extracted; their original headings and page breaks remain in `main.tex`. Bibliography positioning, the appendix switch, front matter, preamble and formatting commands remain in the original order.

`main.tex` now inputs the extracted files and reads `\bibliography{fypbib_A,fypbib_B,fypbib_C}`. `\bibliographystyle{ieeetr}` is unchanged. For baseline fidelity, A's bibliography contains the original six example entries verbatim. B and C have owner/reservation comments and no invented entries. The original `fypbib.bib` remains unchanged.

## Verification result

**No final visible or layout differences were found. Both PDFs contain 39 pages.**

| Check | Result |
|---|---|
| Expand every `\input`, remove owner comments and restore the original bibliography database name | Exact original `main.tex` bytes recovered |
| Class, original bibliography and four original figure files | SHA-256 hashes unchanged |
| Page count and page dimensions | Identical |
| Extracted text on every page | Identical |
| Word positions on every page | Identical |
| Every rendered page at 144 DPI | Pixel-identical |
| Every page's hyperlinks/destinations | Identical after disregarding internal PDF object identifiers |
| Generated bibliography (`main.bbl`) | Byte-identical |
| Contents, figure list and table list (`main.toc`, `.lof`, `.lot`) | Byte-identical |

An intermediate build showed different word spacing on PDF page 24. Suppressing the extra newline after each `\input` with a trailing `%` corrected the mechanical boundary behavior. The final comparison passed for all 39 pages; no chapter text or class formatting was changed. The two PDF files need not have identical bytes because their internal metadata/identifiers differ.

Final frozen `main.tex` SHA-256:

```text
fb9d70d76c5bb08525ad975ec4bd317d5848f7c14536d204c51e7fddba8f39b0
```

## Preserved baseline warnings and comparison limits

The original and split final TeX logs each contain 64 warnings/box diagnostics recognized by the comparison script. Diagnostic file names and line numbers naturally move into chapter files after extraction. The rendered output and generated lists are unchanged.

- The SDG reference `fig:my_label` is undefined; the template defines `fig:1`. Its original unresolved reference remains present.
- `fancyhdr` reports insufficient `\headheight`; original settings are preserved.
- `tocloft` reports that `\@starttoc` was already redefined.
- Example paragraphs/tables produce underfull-box diagnostics; original wrapping is preserved.
- The workspace compiler is **Tectonic 0.17.0**, which uses XeTeX and runs BibTeX/reruns automatically. With the original `mathptmx` setup it reports unavailable `TU/ptm` normal/bold/italic font shapes and substitutes defaults in both builds. **The comparison proves fidelity between these two local builds; it does not certify the intended Times typography or equality to an unseen pdfLaTeX/Overleaf PDF.** No font package or class change was introduced to conceal this limitation.
- Compiler output also reports legacy encoding warnings in the bundled `algorithm2e.sty`, a Fontconfig configuration diagnostic, and a duplicate page destination during PDF conversion. These occur with the original template as well as the split version.

BibTeX successfully resolves the original entries, including the differently capitalized Guyon key; the final baseline BibTeX log reports no missing-entry warning. The database list changes from one file to three, as requested.

Existing template examples, empty sections and demonstration headings are intentionally retained. This setup PDF is a template, not a completed or submission-ready Zeest report. Any later content writing remains outside Phase 2.

## Build and freeze

No pre-existing `pdflatex`, `latexmk` or `bibtex` tool was found in the checked locations. A portable [official Tectonic release](https://github.com/tectonic-typesetting/tectonic/releases/tag/tectonic%400.17.0) and a Python PDF renderer were installed within `.phase2/tools/`; compiler dependency caches stay in `.phase2/cache/tectonic`. These are build tools, not additions to the document's package list.

From the workspace root, rebuild with:

```powershell
& '.phase2/build.ps1'
```

This verifies the frozen assembly/class, builds `Report template/build/main.pdf`, and refreshes `Report template/main.pdf`. To repeat the setup-only fidelity comparison while the extracted template text is still unchanged:

```powershell
& '.phase2/build.ps1' -CompareBaseline
```

The comparison is date-sensitive because the untouched template uses `\today`; rebuilding on a later date will change the title page relative to the preserved original. Later authorized chapter writing will also intentionally invalidate baseline text/layout equality. Neither requires editing the assembly.

**Nobody edits `main.tex` after this setup. Never edit `FastFyp.cls` or add packages.** Scoped instructions are saved in `Report template/AGENTS.md`. Owners may edit their chapter/summary/bibliography files only when a later writing task is authorized; other members provide review notes. No later phase has been started.

## Repository handoff and cleanup

[README.md](README.md) is the entry point for all three students and their agents. It provides an agent prompt, exclusive file ownership, diagram ownership, dependencies, citation rules, build instructions and separate-clone/branch collaboration. Root `AGENTS.md` and the scoped report instructions enforce the same boundaries.

Duplicate build PDFs, transient auxiliary files and disposable verification images were removed. Original sources, the original PDF, hashes, comparison JSON and compact build evidence remain. `.gitignore` excludes local compiler tools, caches, working PDFs and regenerated build output. The build script bootstraps its portable Windows compiler on a new machine; Python, internet access for initial downloads, and permission to run PowerShell scripts are prerequisites.

The workspace is not yet a Git repository and has not been committed or pushed. Follow the README repository instructions, or copy the tracked sources into an existing repository clone. Setup is ready for separate assigned writing tasks; the report content and final typography validation remain unfinished.
