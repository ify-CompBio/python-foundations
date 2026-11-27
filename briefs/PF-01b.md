Brief set by AI mentor; all code and notes are my own.

# PF-01b: Data Shape Inspector v2 (rewrite from memory, then extend)

Approved by Ify, 27 November 2026.

**Track / workstream:** Foundations / Python Foundations
**Tier:** Build. It produces new code, involves design decisions, and is the "write, debug, explain" diagnostic for area 1 of the Skill Ledger.
**Skills it gives evidence for:** Python and software engineering practice (core). Tooling such as Git, Bash and VS Code (supporting).
**Time-box (estimate):** 4–6 hours over 2–3 sessions. If it runs past a week, review it and split it.

## Why this task matters

Ify can now explain length, `None`, and print versus return. This task tests whether she can produce that understanding without help, and adds three properties the original task asked for: mutability, iterability and truthiness.

The biological reason: a line like `if count:` treats a gene with 0 reads the same as a gene with no count recorded. Those mean very different things scientifically, and the bug produces no error.

## Rules for using help

| Part | What can be used |
|---|---|
| A: rewrite from memory | Nothing. No original file, no walkthrough, no Python docs, no AI. |
| B–D | Official Python documentation allowed. No AI-written code. If stuck, ask for a hint; hints start at level 1. |

Record every bit of help used in the AI-help log.

## Part A: rewrite from memory (time-box 30 minutes)

1. Create `01b_data_shape_inspector.py`. Leave the original file untouched (it is the evidence for PF-01).
2. Rebuild the v1 behaviour from memory: type, length or "not applicable", and value, for at least five objects.
3. Commit straight away, even if broken or incomplete.
4. Compare with the original: `git diff --no-index 01_data_shape_inspector.py 01b_data_shape_inspector.py`
5. Write three notes: what was remembered, what was forgotten, what was done differently on purpose.

## Part B: extend the inspector

For each object, report: type; mutable (yes/no); iterable (yes/no); length or "not applicable"; truthiness (True/False); value.

Design requirements (justify each):
1. Separate finding from showing. One function returns the findings and prints nothing; something separate handles printing. The structure of the findings is Ify's choice.
2. Choose a function name that does not shadow a standard library module, and say why.
3. How to decide mutability and iterability is part of the challenge: research it in the docs. A hard-coded rule by type is acceptable if its limitations are stated.

Required test objects, in this order: `0`, `42`, `3.14`, `""`, `"ACTG"`, `[]`, `[[]]`, `[1, 2, 3]`, `(1, 2)`, `{"gene": "TP53"}`, `{1, 2}`, `None`, `True`, plus one biological record of Ify's own design.

## Part C: predict, then explain

1. Before running the finished version, write predicted truthiness and mutability for every test object. Run it and mark which predictions were wrong.
2. In `notes/01b_concepts.md`, answer in plain language:
   - Why is `bool([])` False but `bool([[]])` True?
   - How are `None`, `0`, `""` and `[]` different? Why is `if count:` dangerous for read counts?
   - Why does the inspector return its findings instead of printing them, and what does that make possible?
   - What were the choices for the function name and the structure of the findings, and why?

## Part D: deliberate failure

Find one input the inspector handles wrongly or misleadingly. Record what it does, why, and whether to fix it or document it as a limitation. Fixing is not required.

## Git, Bash and VS Code requirements

- Run from the terminal (`python3 01b_data_shape_inspector.py`).
- At least three commits with specific messages: after Part A, after Part B, after the notes.
- Turn on VS Code's "Files: Insert Final Newline" before starting.

## Acceptance criteria

- [ ] Part A commit exists before any extension work, with the diff and three notes.
- [ ] Script runs from the terminal without errors and covers every required test object.
- [ ] Findings function returns results and does not print; printing is separate.
- [ ] All six properties reported for every object.
- [ ] Predictions written before running, mismatches marked.
- [ ] `notes/01b_concepts.md` answers all four questions in Ify's own words.
- [ ] One limitation found and explained.
- [ ] At least 3 commits with specific messages; AI-help log completed.

## Review and evidence

- Self-review first against the criteria, then AI review (meaningful Build and diagnostic).
- Evidence: commits, notes file, prediction log. Gets an Evidence Log entry.
- Skill Ledger: informs the area 1 baseline; does not change the level automatically.

**Out of scope:** classes, recursion (optional stretch: inspect nested objects recursively), performance.

## AI-help log

- Part A: 
- Parts B–D:
