# Kashaf: start here

You are Member A. Your exclusive working folder is `kashaf/`.

## Read first

Read `../README.md`, `../AGENTS.md`, `../PLAN.md`, `../Rules.txt`, `../F26-098.docx`, and the template/class instructions. Sample reports guide presentation only. The proposal alone supplies project facts. Current assumptions are FYP-1 and Research and Development; no prototype has been built.

## Your files

- `01_introduction.tex`
- `02_project_vision.tex`
- `04_software_requirement_specifications.tex`
- `08_user_manual.tex`
- `10_conclusions.tex`
- `appendix_a_template_examples.tex`
- `executive_summary.tex`
- `references.bib`: your bibliography, integrated automatically with the other two.
- `diagrams/`: your PlantUML sources (create them when diagram work is requested).
- `HANDOFF.md`: your coordination notes, decisions and unresolved dependencies.

Existing chapter text is template examples/guidance, not completed Zeest prose. Required headings are governed by PLAN.md and the template. Keep your chapter commands, order and section hierarchy. The demo appendix is preserved until an explicit content decision.

## First work and dependencies

Start with Introduction, Project Vision and proposal-grounded requirements. Give Fatima and Esha stable objective/FR/use-case IDs, data terms and physician approval semantics. Wait for design and implementation status before User Manual; write Conclusions and Executive Summary last.

Owned visuals: D01 doctor use cases; D02 navigation; D03 hybrid-memory ER; W01?W03 proposed history, consultation and review/audit views; template SDG caption. Consult PLAN.md for exact placement, owners of tables, descriptions and defense questions. Render images into `../Report template/Figures/` with `kashaf_` filename prefixes; use descriptive captions and reference every image. Do not modify another person's image.

## Agent prompt

> I am Kashaf, Member A. Read my START_HERE.md, root README.md/AGENTS.md, PLAN.md, Rules.txt and F26-098.docx before writing. Work only in kashaf/ and my prefixed figure assets. Preserve all required template headings and formatting. Never edit main.tex, FastFyp.cls, add packages or edit another member's files. The prototype is unbuilt: mark future implementation/testing/results with \textcolor{red}{PLANNED: ...}. Never invent numbers, outputs, screenshots, data access or references. Record dependencies and decisions in my HANDOFF.md. Complete only the chapter/diagram work I request.

## Work and check

Use a separate clone and branch `report/kashaf`. Consult others' HANDOFF.md files, keep your own updated, commit only owned changes and open a PR for review. Follow root README for compilation from `Report template/`. Leave shared assembly and coordination files alone during ordinary member work.
