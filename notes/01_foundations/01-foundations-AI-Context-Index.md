# 01 Foundations AI Context Index

path: 01_foundations/01-foundations-AI-Context-Index.md
folder: 01_foundations
filename: 01-foundations-AI-Context-Index.md
repository: DDF
type: research_note

This file guides AI systems working specifically with the foundations layer of the DDF.

---

## Folder Scope

`01_foundations` contains:

- Projection ontology and constraints (F1–F4).  
- Sector structure (fermionic/bosonic, gauge redundancy).  
- Projection generator.  
- Structural interpretation and progress on physical constants.  

It does **not** contain detailed operator‑chain proofs (those live in the operator folders) but provides their conceptual base.

---

## Local Note Labels and Files

Foundations notes (expected mapping):

- F1 — Harmonic Projection  
  - File: `F1-harmonic_projection.md`
- F2 — Projection Constraints  
  - File: `F2-projection_constraints.md`
- F3 — Spectral Selection  
  - File: `F3-spectral_selection.md`
- F3a — Algebraic Structure of the Generative Domain  
    - File: `F3a-Algebraic-Generative-Domain.md`  
    - Status: CONJECTURE / PROGRAMME  
    - Scope: Models Ω as an AF C*-algebra. Proposes Clifford representations emerge from  
      projection admissibility plus Lorentzian cone. Leads to N1a (Clifford Emergence).  
      Do not treat its conjectures as derived results. Not part of the minimal chain F1–F4.
- F4 — Particle Discreteness  
  - File: `F4-particle_discreteness.md`
- F5 — Structural Role of Physical Constants in DDF  
  - File: `F5-structural_constants.md` (merged structural + definition)
- F6 — Fermionic and Bosonic Sectors  
  - File: `F6-fermionic_and_bosonic_sectors.md`
- F7 — Gauge Redundancy from Projection  
  - File: `F7-gauge_redundancy_projection.md`
- F8 — Projection Generator  
  - File: `F8-projection_generator.md`

Status / meta note:

- N‑C0 — Progress on Deriving Fundamental Constants  
  - File: `N-C0-constants_progress_summary.md`

Conceptual background:

- TN‑010 — Conceptual Foundations of the Dual‑Domain Framework  
  - File: `TN-010-Conceptual-Foundations-of-the-Dual-Domain-Framework.md`  
  - Use only for conceptual context, never as a formal proof source.

---

## Dependency Chains Within 01_foundations

Minimal internal chain:

- F1 — Harmonic Projection  
  → F2 — Projection Constraints  
  → F3 — Spectral Selection  
  → F4 — Particle Discreteness

Additional branches:

- F3 → F6 (Fermionic/Bosonic Sectors)  
- F3 → F7 (Gauge Redundancy)  
- F1, F2, F8 → F5 (Structural Constants)  
- F5 → N‑C0 (progress on constants)

Each note should list its actual dependencies in its own `## Dependencies` section.

---

## Editing and Preservation Rules (Local to 01_foundations)

- Do not delete equations, derivations, or exploratory paragraphs.  
- When merging duplicates (e.g. multiple spectral‑selection files), keep:
  - the fullest version in the main sections,  
  - the others under `## Notes / Working Material`.

- Keep historical files (e.g. old stubs) in this folder or a `history/` subfolder, but make F‑notes the canonical entrypoints.

When adding a new foundations note:

1. Assign the next F‑label (or a dedicated N‑label if it is explicitly a status/meta note).  
2. Use the standard `note_template.md` structure.  
3. Update:
   - `01_foundations/master_index.md`  
   - `01_foundations/framework_map.md` (local foundations map)  
   - `ddf_notation.md` (if new symbols appear).

---

## Notes / Working Material

- Any ambiguity in label–filename mapping should be resolved by adding explicit lines here rather than renaming notes silently.  
- If a foundations note logically moves to an operator folder later, retain a short stub in `01_foundations` pointing to the new location.