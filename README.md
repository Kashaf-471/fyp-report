# Zeest report: team and agent handoff

This is the shared FAST-NUCES FYP report workspace for **Zeest: An Agentic Medical Copilot**. Phase 1 planning and Phase 2 mechanical setup are complete. **Chapter writing has not started:** the `.tex` files still contain the original template instructions and examples.

## Start here — prompt for your agent

Copy this, replacing the member letter:

> I am Member [A/B/C]. Read AGENTS.md, README.md, PLAN.md, Rules.txt, the original template at Report template/baseline/sources/main.tex, and F26-098.docx before writing. Use the proposal as the sole source of project facts. Work only in my assigned files and my diagram assets. Do not edit main.tex, FastFyp.cls, another member's files, or the baseline. Follow the exact required headings and formatting. The prototype is not built: mark prospective implementation, tests and results with `\textcolor{red}{PLANNED: ...}` and never invent outputs, numbers, screenshots or references. First identify dependencies on other members and record unresolved items in my own handoff note. Complete only the report work I explicitly request.

Read [PLAN.md](PLAN.md) for the exact heading inventory, diagram/table specifications, objective traceability, workload estimates, defense questions and dependencies. [PHASE2_SETUP.md](PHASE2_SETUP.md) contains the setup audit and compiler limitations.

## Project facts and boundaries

The only authoritative project source is [F26-098.docx](F26-098.docx); the supplied [PDF](F26-098.pdf) is its reading companion. Advisor: Miss Umm-e-Ammarah. Working assumptions authorized for setup: **FYP-1**, **Research and Development**, and member assignments in proposal name order. These assumptions are not independently confirmed departmental facts.

Zeest proposes a physician-controlled, multimodal clinical decision support prototype with longitudinal relational and semantic patient memory. Its nine proposal objectives cover:

1. Hybrid relational and semantic patient memory.
2. Real-time consultation transcription into structured notes.
3. Patient Memory, Clinical Case, Imaging, Laboratory and Medication Safety agents.
4. Integration of an existing validated pre-trained imaging classification model.
5. Evidence and RAG retrieval of relevant guidelines with citations.
6. Clinical Reasoning output of a reviewable proposed diagnosis; scope also includes physician-reviewed treatment plans.
7. Safety and Critic review before presentation.
8. Physician approval, modification or rejection and a full audit log; approval is required before recording a clinical decision.
9. Ablation comparing a single LLM, a memory-augmented variant and the full system. The Introduction also asks about critic and multimodal contributions.

The proposal names FastAPI, Next.js, LangGraph, Google ADK, Gemini, PyTorch, PostgreSQL and pgvector. It discusses MIMIC-IV/MIMIC-CXR, PubMed, Synthea and imaging dataset/model candidates. Names in the proposal do not establish approved data access, a final model/domain selection or a completed integration. Do not invent the LangGraph/ADK division, hardware, numerical targets, languages, reviewers, sample counts or reference labels.

Use de-identified or synthetic data and supported domains with both suitable data and validated models. Exclusions include training diagnostic models from scratch, autonomous treatment/prescribing, real clinical deployment, regulatory approval, unsupported domains, patient chat/mobile apps, knowledge graphs and emergency/ICU systems. `context.txt` is old brainstorming, **not** an authoritative project specification. Sample reports guide presentation only; their headings, claims, results and citations do not override this template or become Zeest facts.

## Who owns what

Every listed chapter filename is under `Report template/chapters/`; summary files are under `Report template/frontmatter/`.

| Member / assumed student | Exclusive files |
|---|---|
| **A — Kashaf Ali, 23L-0691** | `01_introduction.tex`, `02_project_vision.tex`, `04_software_requirement_specifications.tex`, `08_user_manual.tex`, `10_conclusions.tex`, `appendix_a_template_examples.tex`; `executive_summary.tex`; `Report template/fypbib_A.bib` |
| **B — Fatima Malik, 23L-0826** | `03_literature_review.tex`, `05_proposed_approach_and_methodology.tex`, `09_experimental_results_and_discussion.tex`; `abstract.tex`; `Report template/fypbib_B.bib` |
| **C — Eesha Irfan, 23L-0836** | `06_high_level_and_low_level_design.tex`, `07_implementation_and_test_cases.tex`; `Report template/fypbib_C.bib` |

Owner names are already in comments at the top of the extracted files. One editor per chapter. Reviews happen through comments/PRs or handoff notes; reviewers do not rewrite someone else's file. A coordinates assembly reviews but **does not edit the frozen main.tex**.

Diagram ownership from PLAN.md:

- **A:** D01 doctor use cases, D02 navigation, D03 hybrid-memory ER; W01 history, W02 consultation, W03 review/audit proposed views; template SDG asset/caption.
- **B:** D04 method pipeline, D05 ablation protocol, D06 evidence retrieval; R01 results chart only after real measurements.
- **C:** D07 system architecture, D08 agent subsystem, D09 domain/class model, D10 consultation sequence, D11 physician approval state, D12 memory update sequence. Follow PLAN.md for exact descriptions/placement.

Keep PlantUML sources in `Report template/diagrams/` and rendered images in `Report template/Figures/`, with matching unique basenames and the assigned owner. Do not create diagrams during a setup-only task. Tables stay selectable LaTeX text. UI wireframes must be visibly identified as proposed designs; they cannot masquerade as prototype screenshots. PlantUML is unsuitable for measured plots and official artwork; use the alternatives described in PLAN.md when authorized.

**Final summaries:** A writes Conclusions and Executive Summary; B writes Abstract; C supplies design/implementation/test status. Write summaries last, after all chapters agree.

## Rules agents must preserve

- `main.tex` is frozen. Never edit `FastFyp.cls` or add packages. Main already inputs all files and all three bibliographies with `ieeetr`.
- Preserve every required heading, sequence, hierarchy and front-matter item. Genuine example headings can be replaced during authorized writing as specified in PLAN.md; do not import additional sample-report sections. Keep the appendix unchanged until a later explicit content decision.
- Ordinary prose paragraphs: 150–250 words. Abstract: one paragraph, 50–125 words, three to five sentences. Executive Summary: one to two pages of plain prose.
- Number body headings; no fake bold headings or decorative emphasis. Keep bullets within one rendered line.
- Reference every figure and use one descriptive accessible caption; no subcaptions or forced placement. Use labels, references and citations, not hand-written numbering.
- Analyze at least 15 distinct relevant verified works. B starts with proposal-listed candidates, reads actual sources, verifies metadata and flags any eligibility shortfall. Sample citations are not evidence for Zeest.
- A's bibliography currently holds six original template examples to reproduce the baseline; B/C initially have owner comments only. Replace examples only when their corresponding example content is replaced. Do not delete an entry still cited by another chapter.
- Use unique citation prefixes `zeestA:`, `zeestB:`, `zeestC:`. Assign one canonical entry owner when a source is shared; other members cite its existing key, without duplicating it.
- All unbuilt or unexecuted implementation/testing/results must use `\textcolor{red}{PLANNED: ...}`. Expected behavior is not an observed result. Numerical fields remain TBD / NOT MEASURED; test status remains NOT EXECUTED.

## How to work at the same time

Use **one clone/worktree per member**, not three agents writing into one shared folder. Each member works on a separate branch and changes only owned files.

```sh
git clone <repository-url>
cd <repository-folder>
git switch -c report/member-a
# B uses report/member-b; C uses report/member-c.
```

Before each new work session, fetch and merge the repository's actual shared branch (do not assume its name is `main`). Pull other members' completed handoffs before using them. Commit owned source changes, open a PR, and ask another member to review. Build the combined report after merging. Never force-push the shared branch or resolve conflicts by overwriting another member's chapter.

Use `handoffs/A.md`, `handoffs/B.md`, or `handoffs/C.md` as your own coordination file. Each member may create/edit only their own note. Include the branch/commit, completed work, stable terms/IDs, decisions needed by others, unresolved dependencies and references to relevant files. This avoids everyone updating one shared status document. Root README/PLAN/setup/tooling changes are coordinator-managed and should be made in a separate agreed PR; read them during normal chapter work.

### First parallel tasks and handoffs

| Member | Safe first task | What others need before dependent writing |
|---|---|---|
| A | Proposal-grounded scope, Introduction, Vision and initial requirements | Stable objective/FR/use-case IDs, user/approval semantics, data terminology; no fabricated targets |
| B | Verify actual proposal-listed literature and draft its review | Verified source keys/findings; proposed evaluation variants, reference process and metric definitions, with unresolved choices clearly marked |
| C | Read proposal and draft a proposed component inventory/design skeleton | Wait for A's requirement/data meanings and B's method/evaluation contracts before treating design as settled; tests must map to the stable IDs |

A's requirements and B's literature can start concurrently. C can prepare proposed design but must mark unsettled contracts. Methodology, architecture and planned tests must agree before their prose is finalized. No one assumes that another member's planned feature already exists. See PLAN.md's handoff table for detailed dependent assumptions.

## Files to keep and files Git ignores

| Folder/file | Why it exists / repository treatment |
|---|---|
| `README.md`, `AGENTS.md`, `PLAN.md`, `Rules.txt` | Shared context and automatic agent instructions; commit |
| `PHASE2_SETUP.md` | Audit, baseline proof, assumptions and compiler limitations; commit |
| Proposal DOCX/PDF and `Sample Reports/` | Supplied source material; retained, never deleted as generated clutter |
| `context.txt` | Supplied historical discussion; retained but not project authority |
| `Report template/main.tex`, class, chapters, summaries, bibliographies, original figures | Editable project sources and frozen assembly; commit |
| `Report template/baseline/` | Preserved original sources/PDF and compact build evidence; commit, never edit |
| `.phase2/setup.py`, `build.ps1`, `bootstrap.py`, `split_manifest.json`, `verification/comparison.json`, `verification/split-build.log` | Reproducible build/freeze checks and evidence; commit |
| `.phase2/tools/`, `.phase2/cache/` | Machine-local compiler/Python dependencies and cached LaTeX resources; **ignored**, downloaded when needed |
| `Report template/build/`, `Report template/main.pdf` | Regenerated working output; **ignored**, keep locally or attach PDF to a PR/release |
| Verification PNGs and Python bytecode | Disposable visual checks; **ignored**, regenerate when needed |

`.gitignore` is supplied. Do not use `git add -f` on ignored compiler/cache/build files. Diagram images in `Figures/` remain tracked because the report needs them to compile. The preserved baseline PDF is tracked separately from the ignored working PDF.

## Compile and checks

On Windows with Python and PowerShell, from the workspace root:

```powershell
& '.phase2/build.ps1'
```

The script installs the pinned portable compiler inside ignored `.phase2/tools/` if missing (internet needed on the first build), checks frozen `main.tex` and class hashes, runs compilation and refreshes `Report template/main.pdf`. It does not install packages into or modify the document. Run this build after your chapter edits and after integrating other branches.

For a normal TeX installation or Overleaf, compile `Report template/main.tex` as the root document using the existing class/assets and all three `.bib` files; run LaTeX, BibTeX, LaTeX, LaTeX as needed. Keep relative paths intact when uploading. A pdfLaTeX build is the route to investigate the intended Times typography without changing the class/packages; it has **not** been verified in this workspace yet.

Setup-only checks:

```powershell
python '.phase2/setup.py' freeze
python '.phase2/setup.py' verify
& '.phase2/build.ps1' -CompareBaseline
```

`freeze` remains applicable during writing. `verify` and `-CompareBaseline` deliberately require original template bodies and are **not** acceptance checks for newly written chapters. Baseline comparison is also date-sensitive because the unchanged template uses `\today`.

The local Phase 2 baseline and split PDFs both have 39 pages and matched pixel-for-pixel at 144 DPI, with identical text positions, links, bibliography and generated lists. Preserved warnings include an unresolved SDG reference, header-height/box diagnostics and XeTeX font substitutions. This proves the mechanical split, not that the final typography is submission-ready. Read PHASE2_SETUP.md before making a broader fidelity claim.

## Repository readiness and remaining work

**Ready:** non-overlapping owner files, bibliography integration, diagram naming/ownership plan, complete context for agents, source-freeze checks and a build path with ignored local tools. All three can start authorized writing in separate clones/branches using the handoffs above.

**Remaining:** create/connect the Git repository, agree on its shared branch/reviewer workflow, write the chapters, verify literature, create planned diagrams, settle unresolved proposal choices, and verify the intended font rendering. The prototype and measured evaluation remain future work. Ownership/type/stage are documented assumptions and can be corrected if the team chooses differently.

At preparation time this folder was not a Git repository and no remote URL was supplied. To publish the initial workspace yourself:

```sh
git init -b main
git add .
git status --short
git commit -m "Prepare Zeest report sources and team handoff"
git remote add origin <repository-url>
git push -u origin main
```

Inspect the staged files before committing: tool/cache/build files must be absent. If the remote already has history, use a clone of that repository and copy these prepared files into it instead of creating competing history. No commit, remote configuration or push was performed by this cleanup task.
