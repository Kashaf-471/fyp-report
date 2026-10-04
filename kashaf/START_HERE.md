# Kashaf: start here

You are Member A. Your exclusive working folder is `kashaf/`.

## Read first

Read `../README.md`, `../AGENTS.md`, `../PLAN.md`, `../Rules.txt`, `../F26-098.docx`, and the template/class instructions. Sample reports guide presentation only. The proposal alone supplies project facts. Current deliverable is R&D Deliverable II: Chapters 1 through 6, Abstract, Executive Summary, References and Appendix. No prototype has been built.

## Your files

- `01_introduction.tex`
- `02_project_vision.tex`
- `04_software_requirement_specifications.tex`
- `appendix_a_template_examples.tex`
- `executive_summary.tex`
- `references.bib`: your bibliography, integrated automatically with the other two.
- `diagrams/`: your PlantUML sources (create them when diagram work is requested).
- `HANDOFF.md`: your coordination notes, decisions and unresolved dependencies.

Existing chapter text is template examples/guidance, not completed Zeest prose. Required headings are governed by PLAN.md and the template. Keep your chapter commands, order and section hierarchy. The demo appendix is preserved until an explicit content decision.

## First work and dependencies

Start with Introduction, Project Vision and proposal-grounded requirements. Give Fatima and Esha stable objective/FR/use-case IDs, data terms and physician approval semantics. Write Executive Summary last. Coordinate an Appendix outline for approval; template appendix examples are not final content.

Owned visuals: D01 doctor use cases; D02 navigation; D03 hybrid-memory ER; W01 through W03 proposed interface wireframes under Chapter 4; existing SDG figure/caption. Consult PLAN.md for exact placement, tables and defense questions. Put PlantUML sources in diagrams/ and rendered images in ../Report template/Figures/ with kashaf_ prefixes. No other owner may edit your files.

## Agent prompt

> I am Kashaf, Member A. Read my START_HERE.md, root README.md/AGENTS.md, PLAN.md, Rules.txt and F26-098.docx before writing. Work only in kashaf/ and my prefixed figure assets. Preserve all required template headings and formatting. Never edit main.tex, FastFyp.cls, add packages or edit another member's files. The prototype is unbuilt: mark future implementation/testing/results with \textcolor{red}{PLANNED: ...}. Never invent numbers, outputs, screenshots, data access or references. Record dependencies and decisions in my HANDOFF.md. Complete only the chapter/diagram work I request.

## Work and check

Use a separate clone and branch `report/kashaf`. Consult others' HANDOFF.md files, keep your own updated, commit only owned changes and open a PR for review. Follow root README for compilation from `Report template/`. Leave shared assembly and coordination files alone during ordinary member work.

## Kashaf approval and style rules

Review two chapters at a time. Obtain approval for the outline before drafting, then show the draft in chat and obtain explicit approval before saving. Do not change shared files during chapter writing. Use Zeest with capital Z; do not use em dashes in authored prose. This setup update does not authorize chapter prose.
