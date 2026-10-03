# Shared report workspace

Read `README.md` before editing. It is the team/agent handoff: current status, proposal facts, ownership, dependencies, Git workflow, build commands and limitations. Read `PLAN.md`, `Rules.txt` and `F26-098.docx` for the full task constraints. `Report template/AGENTS.md` adds scoped editing rules.

Use the member letter supplied by the user to select owned files. If none is supplied, inspect/read and ask which member's work is requested before making chapter edits. Do not infer ownership merely from which tab is open.

Keep one owner per chapter. Never edit `Report template/main.tex` after setup or edit `FastFyp.cls`/add packages, except an explicit user exception to the assembly freeze. Do not edit other members' chapters, summaries, bibliography or diagram assets. Each member can create their own `handoffs/A.md`, `B.md` or `C.md` for coordination.

The prototype is unbuilt. The proposal is the sole source of project facts. Never invent results, references, resources or data access. Mark future implementation/testing/results `\textcolor{red}{PLANNED: ...}`. Template example content is not Zeest content.

Keep compiler dependencies, caches and generated working builds ignored by Git. Preserve supplied source documents and the original baseline. Root coordination documentation/tooling changes belong in a separate agreed coordinator change; normal member tasks only read these files.
