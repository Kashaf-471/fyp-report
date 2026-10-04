# Fatima: start here

You are Member B. Your exclusive working folder is `fatima/`.

## Read first

Read `../README.md`, `../AGENTS.md`, `../PLAN.md`, `../Rules.txt`, `../F26-098.docx`, and the template/class instructions. Sample reports guide presentation only. The proposal alone supplies project facts. Current assumptions are FYP-1 and Research and Development; no prototype has been built.

## Your files

- `03_literature_review.tex`
- `05_proposed_approach_and_methodology.tex`
- `09_experimental_results_and_discussion.tex`
- `abstract.tex`
- `references.bib`: your bibliography, integrated automatically with the other two.
- `diagrams/`: your PlantUML sources (create them when diagram work is requested).
- `HANDOFF.md`: your coordination notes, decisions and unresolved dependencies.

Existing chapter text is template examples/guidance, not completed Zeest prose. Required headings are governed by PLAN.md and the template. Keep your chapter commands, order and section hierarchy. The demo appendix is preserved until an explicit content decision.

## First work and dependencies

Start by verifying actual proposal-listed literature and drafting the review. Share canonical citation keys and findings. Agree methodology, evaluation variants, metric definitions and reference process with Kashaf/Esha. Results remain planned with clear empty placeholders until experiments run. Write Abstract last.

Owned visuals: D04 methodology pipeline; D05 ablation protocol; D06 evidence retrieval; R01 measured results chart only after real data. Consult PLAN.md for exact placement, owners of tables, descriptions and defense questions. Render images into `../Report template/Figures/` with `fatima_` filename prefixes; use descriptive captions and reference every image. Do not modify another person's image.

## Agent prompt

> I am Fatima, Member B. Read my START_HERE.md, root README.md/AGENTS.md, PLAN.md, Rules.txt and F26-098.docx before writing. Work only in fatima/ and my prefixed figure assets. Preserve all required template headings and formatting. Never edit main.tex, FastFyp.cls, add packages or edit another member's files. The prototype is unbuilt: mark future implementation/testing/results with \textcolor{red}{PLANNED: ...}. Never invent numbers, outputs, screenshots, data access or references. Record dependencies and decisions in my HANDOFF.md. Complete only the chapter/diagram work I request.

## Work and check

Use a separate clone and branch `report/fatima`. Consult others' HANDOFF.md files, keep your own updated, commit only owned changes and open a PR for review. Follow root README for compilation from `Report template/`. Leave shared assembly and coordination files alone during ordinary member work.
