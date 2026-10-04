# Esha (Eesha Irfan in proposal): start here

You are Member C. Your exclusive working folder is `esha/`.

## Read first

Read `../README.md`, `../AGENTS.md`, `../PLAN.md`, `../Rules.txt`, `../F26-098.docx`, and the template/class instructions. Sample reports guide presentation only. The proposal alone supplies project facts. Current assumptions are FYP-1 and Research and Development; no prototype has been built.

## Your files

- `06_high_level_and_low_level_design.tex`
- `07_implementation_and_test_cases.tex`
- `references.bib`: your bibliography, integrated automatically with the other two.
- `diagrams/`: your PlantUML sources (create them when diagram work is requested).
- `HANDOFF.md`: your coordination notes, decisions and unresolved dependencies.

Existing chapter text is template examples/guidance, not completed Zeest prose. Required headings are governed by PLAN.md and the template. Keep your chapter commands, order and section hierarchy. The demo appendix is preserved until an explicit content decision.

## First work and dependencies

Start with a proposed component inventory and design skeleton based on the proposal. Obtain requirement/data meanings from Kashaf and methodology/evaluation contracts from Fatima before treating design as settled. Map planned test cases to stable requirement IDs. Implementation and test execution are not completed.

Owned visuals: D07 architecture; D08 agent subsystem; D09 domain/class model; D10 consultation sequence; D11 physician approval state; D12 memory update sequence. Consult PLAN.md for exact placement, owners of tables, descriptions and defense questions. Render images into `../Report template/Figures/` with `esha_` filename prefixes; use descriptive captions and reference every image. Do not modify another person's image.

## Agent prompt

> I am Esha (Eesha Irfan in proposal), Member C. Read my START_HERE.md, root README.md/AGENTS.md, PLAN.md, Rules.txt and F26-098.docx before writing. Work only in esha/ and my prefixed figure assets. Preserve all required template headings and formatting. Never edit main.tex, FastFyp.cls, add packages or edit another member's files. The prototype is unbuilt: mark future implementation/testing/results with \textcolor{red}{PLANNED: ...}. Never invent numbers, outputs, screenshots, data access or references. Record dependencies and decisions in my HANDOFF.md. Complete only the chapter/diagram work I request.

## Work and check

Use a separate clone and branch `report/esha`. Consult others' HANDOFF.md files, keep your own updated, commit only owned changes and open a PR for review. Follow root README for compilation from `Report template/`. Leave shared assembly and coordination files alone during ordinary member work.
