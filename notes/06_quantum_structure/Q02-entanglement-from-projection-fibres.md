# QM EXT 002 Entanglement From Projection Fibres

path: 06_quantum_structure/QM-EXT-002-entanglement-from-projection-fibres.md
folder: 06_quantum_structure
filename: QM-EXT-002-entanglement-from-projection-fibres.md
repository: DDF
type: research_note

# Entanglement from Projection Fibres in the Dual Domain Framework

**Note ID:** DDF-QM-EXT-002  
**Title:** Entanglement from Projection Fibres in the Dual Domain Framework  
**Folder: 06_quantum_structure/entanglement_projection/ 
**Status:** Exploratory — kinematic framework with toy-derivation targets  
**Version:** 0.1  
**Date:** 2026-03-15  

---

# Dependencies

- DDF projection ontology \( \Omega \to U \)
- Propagation rigidity and propagation cone
- Dirac/spin structure in \(U\)
- DDF-QM-EXT-001 — Projection Degeneracy and Hidden Multiplicity

---

# Establishes

- A fibre-based reinterpretation of entangled states
- Joint fibres over bipartite observable states
- A clean separation between observable entanglement in \(U\) and hidden multiplicity in \( \Omega \)
- Bell-aware consistency conditions for any future dynamical extension

---

# Excludes

- No Bell inequality derivation
- No claim that locality in \( \Omega \) reproduces all quantum correlations
- No decoherence timescale model
- No modification of standard observable-state quantum mechanics in \(U\)

---

# 1. Introduction

DDF-QM-EXT-001 introduced the idea that the projection

$$
P : \Omega \to \mathcal{H}_U
$$

may be many-to-one, with each observable state \( \psi_U \) possessing a degeneracy fibre

$$
\mathcal{F}(\psi_U) = P^{-1}(\psi_U).
$$

The present note asks whether this fibre structure can provide a structural interpretation of **entanglement**.

The key idea is simple:

- entanglement remains an observable property of the projected state in \(U\),
- but the generative domain \( \Omega \) may contain additional multiplicity and compatibility structure over that state,
- and this hidden structure may help explain why multipartite states behave differently from separable ones.

This note remains deliberately conservative: it does **not** replace standard entanglement theory in \(U\); it only proposes a compatible DDF extension above it.

---

# 2. Observable Bipartite States

Let two subsystems \(A\) and \(B\) have observable Hilbert spaces

$$
\mathcal{H}_A, \qquad \mathcal{H}_B.
$$

The observable joint space is

$$
\mathcal{H}_{AB} = \mathcal{H}_A \otimes \mathcal{H}_B.
$$

A pure state \( \psi_{AB} \in \mathcal{H}_{AB} \) is **separable** if

$$
\psi_{AB} = \psi_A \otimes \psi_B,
$$

and **entangled** otherwise.

This standard distinction remains unchanged in DDF.

---

# 3. Joint Projection Fibres

We extend the projection map to multipartite states:

$$
P_{AB} : \Omega_{AB} \to \mathcal{H}_{AB}.
$$

---

## Definition 3.1 — Joint Fibre

For any observable bipartite state \( \psi_{AB} \in \mathcal{H}_{AB} \), define the joint fibre

$$
\mathcal{F}_{AB}(\psi_{AB}) := P_{AB}^{-1}(\psi_{AB}).
$$

This is the set of all generative configurations in \( \Omega_{AB} \) that project to the same observable state.

---

## Definition 3.2 — Fibre-Factorisable State

A bipartite observable state \( \psi_{AB} \) is **fibre-factorisable** if there exist fibres
$$
\mathcal{F}_A(\psi_A), \qquad \mathcal{F}_B(\psi_B)
$$
such that
$$
\mathcal{F}_{AB}(\psi_{AB}) \cong \mathcal{F}_A(\psi_A) \times \mathcal{F}_B(\psi_B)
$$
for some observable factorisation
$$
\psi_{AB} = \psi_A \otimes \psi_B.
$$

If no such factorisation exists, we call the fibre **irreducibly joint**.

---

# 4. DDF Reinterpretation of Entanglement

This leads to the following structural proposal.

---

## Definition 4.1 — Fibre Entanglement Criterion

An observable state \( \psi_{AB} \) is said to have **irreducible fibre entanglement structure** if:

1. \( \psi_{AB} \) is entangled in the standard quantum sense, and  
2. its joint fibre \( \mathcal{F}_{AB}(\psi_{AB}) \) does not admit a natural product decomposition into separate subsystem fibres.

Symbolically:

$$
\mathcal{F}_{AB}(\psi_{AB}) \not\cong \mathcal{F}_A \times \mathcal{F}_B.
$$

This does not define entanglement in \(U\); rather it proposes a DDF **generative signature** of entanglement.

---

# 5. Structural Consequence

In this framework:

- separable states correspond naturally to factorisable fibre structure,
- entangled states correspond to non-factorisable fibre structure.

Thus the distinction between product and entangled states in \(U\) is mirrored by a distinction between:

- product fibres,
- irreducibly joint fibres.

This gives entanglement a possible structural home in \( \Omega \) without changing observable quantum mechanics.

---

# 6. Reduced States and Hidden Correlation

Let \( \rho_{AB} = |\psi_{AB}\rangle \langle \psi_{AB}| \).

The reduced states are

$$
\rho_A = \mathrm{Tr}_B(\rho_{AB}), \qquad
\rho_B = \mathrm{Tr}_A(\rho_{AB}).
$$

In standard quantum mechanics, entanglement is detectable because \( \rho_A \) and \( \rho_B \) may be mixed even when \( \rho_{AB} \) is pure.

In fibre language, this suggests:

- the full joint fibre may be coherent as a whole,
- but projections to subsystem descriptions discard internal compatibility data,
- so reduced observable states appear mixed.

This is not yet a derivation, but it suggests a clear DDF mechanism:

**mixed reduced states may arise because subsystem projection forgets generative compatibility relations present only at the joint-fibre level.**

---

# 7. Bell-Aware Consistency

Any DDF extension of entanglement must respect a crucial constraint.

If a future model aims to reproduce standard Bell-violating quantum correlations, then it cannot simply be a standard local hidden-variable theory.

Therefore any successful DDF dynamical model must make at least one of the following explicit:

1. the relevant \(\Omega\)-level structure is nonlocal in the Bell sense, or  
2. the \(\Omega\)-level notion of locality is not the same as observable spacetime locality in \(U\), or  
3. the model does not claim to reproduce the full Bell correlation structure.

This note adopts option (2) as the cleanest provisional stance:

**locality in \(U\) is constrained by the propagation cone, but fibre relations in \( \Omega \) need not be expressible as spacetime-local relations in \(U\).**

---

# 8. Measurement Interpretation

A measurement on subsystem \(A\) updates the observable state assignment in \(U\).

In DDF language, this may be understood as:

- restricting the admissible joint fibre,
- thereby changing which joint generative configurations remain compatible with the observed outcome.

Observable collapse is therefore not interpreted here as a signal passing through spacetime, but as a **restriction of admissible joint-fibre structure**.

This is still only an interpretation; no dynamical collapse law is being asserted.

---

# 9. Minimal Mathematical Scheme

A minimal future scheme would contain:

1. a projection map
   $$
   P_{AB} : \Omega_{AB} \to \mathcal{H}_{AB},
$$
2. subsystem maps
$$
P_A : \Omega_A \to \mathcal{H}_A, \qquad
   P_B : \Omega_B \to \mathcal{H}_B,
$$
3. a compatibility relation
$$
\mathcal{C}_{AB} \subseteq \Omega_A \times \Omega_B
$$
   selecting which pairs of subsystem-generative states are admissible jointly,
4. a joint fibre representation
$$
\mathcal{F}_{AB}(\psi_{AB})
   \subseteq \mathcal{C}_{AB}
$$
   whose structure is product-like for separable states and irreducibly joint for entangled states.

This is the cleanest route toward a concrete model.

---

# 10. Mathematical Status

| Component | Status |
|-----------|--------|
| Joint fibre definition | mathematically consistent |
| Fibre-factorisation criterion | mathematically consistent |
| Entanglement reinterpretation | exploratory |
| Reduced-state interpretation | heuristic but coherent |
| Bell-aware consistency condition | necessary |

---

# 11. Open Problems

1. Construct explicit joint fibres for simple two-qubit states.  
2. Define a compatibility relation \( \mathcal{C}_{AB} \) that reproduces standard reduced-state behaviour.  
3. Determine whether entanglement entropy can be related to fibre cardinality, fibre dimension, or fibre connectivity.  
4. Specify whether \(\Omega\)-level relations are discrete, continuous, algebraic, or topological.  
5. Build a toy model that distinguishes separable vs Bell-pair fibres.

---

# 12. Next Step

The next natural step is a toy model.

That model should:

- assign finite fibres to simple qubit states,
- make separable states fibre-factorisable,
- make Bell-like states irreducibly joint,
- show explicitly how subsystem coarse-graining yields mixed reduced descriptions.

This is developed in:

**DDF-QM-EXT-003 — Toy Model for Projection Fibres and Entanglement**

---

# Summary

This note proposes that quantum entanglement in \(U\) may correspond, in DDF, to **non-factorisable joint fibre structure** in \( \Omega \).

The observable mathematics of entanglement is left unchanged.

The new contribution is a generative interpretation:

- separable states arise from product-like fibre structure,
- entangled states arise from irreducibly joint fibre structure,
- reduced mixedness may reflect loss of joint-fibre compatibility information under subsystem projection.
