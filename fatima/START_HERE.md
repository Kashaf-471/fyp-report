# Fatima: start here

You are Member B. Your exclusive working folder is `fatima/`.

## Read first

Read `../README.md`, `../AGENTS.md`, `../PLAN.md`, `../Rules.txt`, `../F26-098.docx`, and the template/class instructions. Sample reports guide presentation only. The proposal alone supplies project facts. Current deliverable is R&D Deliverable II: Chapters 1 through 6, Abstract, Executive Summary, References and Appendix. No prototype has been built.

## Your files

- `03_literature_review.tex`
- `05_proposed_approach_and_methodology.tex`
- `abstract.tex`
- `references.bib`: your bibliography, integrated automatically with the other two.
- `diagrams/`: your PlantUML sources (create them when diagram work is requested).
- `HANDOFF.md`: your coordination notes, decisions and unresolved dependencies.

Existing chapter text is template examples/guidance, not completed Zeest prose. Required headings are governed by PLAN.md and the template. Keep your chapter commands, order and section hierarchy. The demo appendix is preserved until an explicit content decision.

## First work and dependencies

Start by verifying actual proposal-listed literature and drafting Chapter 3. Share canonical citation keys and findings. Agree Chapter 5 methodology, evaluation variants, proposed metric definitions and reference process with Kashaf/Esha. Describe evaluation as planned; no results chapter or measured chart belongs in this submission. Write Abstract last.

Owned visuals: D04 methodology pipeline; D05 planned ablation protocol; D06 evidence retrieval. Consult PLAN.md for exact placement, tables and defense questions. Put PlantUML sources in diagrams/ and rendered images in ../Report template/Figures/ with fatima_ prefixes. No other owner may edit your files.

## Agent prompt

> I am Fatima, Member B. Read my START_HERE.md, root README.md/AGENTS.md, PLAN.md, Rules.txt and F26-098.docx before writing. Work only in fatima/ and my prefixed figure assets. Preserve all required template headings and formatting. Never edit main.tex, FastFyp.cls, add packages or edit another member's files. The prototype is unbuilt: mark future implementation/testing/results with \textcolor{red}{PLANNED: ...}. Never invent numbers, outputs, screenshots, data access or references. Record dependencies and decisions in my HANDOFF.md. Complete only the chapter/diagram work I request.

## Work and check

Use a separate clone and branch `report/fatima`. Consult others' HANDOFF.md files, keep your own updated, commit only owned changes and open a PR for review. Follow root README for compilation from `Report template/`. Leave shared assembly and coordination files alone during ordinary member work.
