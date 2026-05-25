# Note Template

path: 00_index/Note-Template.md
folder: 00_index
filename: Note-Template.md
repository: DDF
type: research_note

# Note Template for DDF Research Notes

This file defines the **canonical structure** for all technical notes in the Dual Domain Framework (DDF).  
When creating or refactoring notes, rearrange existing content into this structure without deleting any material.

---

# Title

Use the format:

- `F# — Descriptive Title` for foundational notes, or  
- `N# — Descriptive Title` for operator / quantum / geometric notes.

Example:

- `# F1 — Projection Ontology`  
- `# N1 — Propagation Rigidity`

---

## Purpose

State the high‑level goal of the note:

- What concept is being introduced?  
- What structure or result is being derived?  
- How does it fit into the global derivation chain?

Keep this descriptive; do not replace any technical content elsewhere.

---

## Definitions

List and define all symbols, objects, and key terms used in the note.

Guidelines:

- Reference `ddf_notation.md` for framework‑wide symbols (Ω, U, P, A, c, ℏ, G, D, etc.).  
- If new symbols are introduced, define them here **and** add an entry to `ddf_notation.md`.  
- Do not remove older or alternative definitions; instead, move them here or to `## Notes / Working Material` with appropriate comments.

---

## Core Statement / Theorem

State the main structural statement, theorem, or key principle proved or argued in this note.

Examples:

- A rigidity statement (e.g. existence of a unique propagation cone under given constraints).  
- A factorisation result (e.g. hyperbolic operator factorises into a Dirac operator).  
- A structural equivalence (e.g. projection constraints imply a particular curvature response).

If the note is exploratory and has no single clean theorem yet, use this section to summarise the current target statement and its status (e.g. PROVED / PARTIAL / CONJECTURE).

---

## Derivation / Explanation

Place **all detailed reasoning** here:

- Step‑by‑step derivations.  
- Intermediate lemmas.  
- Calculations and algebraic manipulations.  
- Argument chains and structural reasoning.

Rules:

- Do **not** delete or compress existing derivations; they may be re‑ordered but not removed.  
- If multiple derivations exist, keep them all, clearly marked (e.g. “First derivation”, “Alternative derivation”).  
- Any moved or merged material must preserve all original equations and logical steps.

---

## Consequences

List consequences, corollaries, and direct applications of the core statement:

- Links to other notes where these consequences are developed.  
- Brief structural description (not replacement) of how the result feeds into later constructions.

If consequences are conjectural or incomplete, that fact should be noted here and the detailed work kept in `## Notes / Working Material`.

---

## Dependencies

Explicitly list the notes that must be understood before this one.

Format:

- `Requires F1 — Projection Ontology`  
- `Requires F2 — Admissibility and Spectral Moderation`  
- `Requires N1 — Propagation Rigidity`

Include both label and title where possible.  
If a dependency is missing from the repository, do **not** delete the reference; instead, ensure a stub or TODO exists somewhere and note this under `## Notes / Working Material`.

---

## Next Notes

List the notes that logically follow from this one.

Format:

- `Leads to N2 — Dirac Factorisation`  
- `Leads to N3 — Spin Structure`

This defines outgoing edges in the global derivation DAG (see `framework_map.md`).

---

## Notes / Working Material

Use this section for:

- Exploratory calculations.  
- Partially developed ideas.  
- Alternative formulations and abandoned routes.  
- Questions, TODOs, and status tags (PROVED / PARTIAL / CONJECTURE).

Key rule:

- **Never** delete material; move it here if it is not part of the main derivation.  
- When merging redundant or overlapping material from different files, keep the fullest version in the main sections and move the others here as “Historical version” or “Alternative derivation”.

---

## Instructions for Editors and AI Systems

- Preserve all equations and derivations exactly.  
- Do not summarise proofs in place of the original; summarise only in addition to them.  
- When restructuring, track original order in comments or short remarks if that history is important.  
- Update `master_index.md`, `framework_map.md`, and `ddf_notation.md` when adding new labelled notes or new symbols.  
- If uncertain about where content belongs, place it under `## Notes / Working Material` and add a short remark describing the issue.