# QM EXT 003 Toy Model Projection Fibres

path: 06_quantum_structure/QM-EXT-003-toy-model-projection-fibres.md
folder: 06_quantum_structure
filename: QM-EXT-003-toy-model-projection-fibres.md
repository: DDF
type: research_note

# Toy Model for Projection Fibres and Entanglement in the Dual Domain Framework
**Note ID:** QM-EXT-003  
**Title:** Toy Model for Projection Fibres and Entanglement in the Dual Domain Framework  
**Folder:** 06_quantum_structure/entanglement_projection/  
**Status:** Toy model — finite illustrative construction  
**Version:** 0.1  
**Date:** 2026-03-15  

---

# Dependencies

- DDF projection ontology \( \Omega \to U \)
- DDF-QM-EXT-001 — Projection Degeneracy and Hidden Multiplicity
- DDF-QM-EXT-002 — Entanglement from Projection Fibres

---

# Establishes

- A finite toy construction of projection fibres
- A concrete distinction between separable and entangled fibre structure
- A coarse-graining mechanism showing how joint hidden structure can be lost in subsystem descriptions

---

# Excludes

- No claim of physical completeness
- No Bell inequality calculation
- No Schrödinger dynamics
- No measurement theory beyond illustrative restriction

---

# 1. Purpose

The aim of this note is not to prove a full quantum theory.

It is to build the smallest mathematically clear example showing how:

- multiple generative states may project to one observable state,
- separable states may have product-like fibres,
- entangled states may have irreducibly joint fibres.

---

# 2. Observable System

Take two qubits \(A\) and \(B\).

Their observable Hilbert spaces are

$$
\mathcal{H}_A \cong \mathbb{C}^2,
\qquad
\mathcal{H}_B \cong \mathbb{C}^2,
$$

with computational basis

$$
|0\rangle,\ |1\rangle.
$$

The joint observable space is

$$
\mathcal{H}_{AB} = \mathcal{H}_A \otimes \mathcal{H}_B.
$$

We compare:

1. a separable state
   $$
   |00\rangle = |0\rangle_A \otimes |0\rangle_B,
$$
2. an entangled Bell state
$$
|\Phi^+\rangle = \frac{1}{\sqrt{2}}\bigl(|00\rangle + |11\rangle\bigr).
$$
---

# 3. Finite Generative Sets

Let the generative subsystem sets be finite:
$$
\Omega_A = \{a_0^{(1)}, a_0^{(2)}, a_1^{(1)}, a_1^{(2)}\},
$$

$$
\Omega_B = \{b_0^{(1)}, b_0^{(2)}, b_1^{(1)}, b_1^{(2)}\}.
$$
Define subsystem projections
$$
P_A(a_0^{(1)}) = P_A(a_0^{(2)}) = |0\rangle_A,
$$

$$
P_A(a_1^{(1)}) = P_A(a_1^{(2)}) = |1\rangle_A,
$$
and similarly
$$
P_B(b_0^{(1)}) = P_B(b_0^{(2)}) = |0\rangle_B,
$$

$$
P_B(b_1^{(1)}) = P_B(b_1^{(2)}) = |1\rangle_B.
$$
Thus each basis state has a 2-element degeneracy fibre.

---

# 4. Separable-State Fibre

For the observable product state \( |00\rangle \), define the joint fibre by direct product:
$$
\mathcal{F}_{AB}(|00\rangle)
=
\{(a_0^{(i)}, b_0^{(j)}) : i,j \in \{1,2\}\}.
$$
Explicitly,
$$
\mathcal{F}_{AB}(|00\rangle)
=
\{
(a_0^{(1)}, b_0^{(1)}),
(a_0^{(1)}, b_0^{(2)}),
(a_0^{(2)}, b_0^{(1)}),
(a_0^{(2)}, b_0^{(2)})
\}.
$$
This fibre factorises as
$$
\mathcal{F}_{AB}(|00\rangle)
\cong
\mathcal{F}_A(|0\rangle_A)\times \mathcal{F}_B(|0\rangle_B).
$$
So the separable state has a product-like fibre.

---

# 5. Entangled-State Fibre

Now define the Bell-state fibre not as a product, but as a constrained compatibility set.

Let
$$
\mathcal{F}_{AB}(|\Phi^+\rangle)
=
\{
(a_0^{(1)}, b_0^{(1)}),
(a_0^{(2)}, b_0^{(2)}),
(a_1^{(1)}, b_1^{(1)}),
(a_1^{(2)}, b_1^{(2)})
\}.
$$
This is **not** equal to
$$
\mathcal{F}_A \times \mathcal{F}_B
$$
for any separate fibres over \(A\) and \(B\), because mixed pairings such as
$$
(a_0^{(1)}, b_0^{(2)}), \qquad (a_1^{(2)}, b_1^{(1)})
$$
are deliberately excluded.

Thus the fibre is irreducibly joint.

---

# 6. Projection Rule for the Toy Model

Define a joint projection map \(P_{AB}\) by declaring:

- any element of \(\mathcal{F}_{AB}(|00\rangle)\) projects to \( |00\rangle \),
- any element of \(\mathcal{F}_{AB}(|\Phi^+\rangle)\) projects to \( |\Phi^+\rangle \).

This makes projection many-to-one.

It also shows two different structural classes:

- product fibre for a separable state,
- constrained joint fibre for an entangled state.

---

# 7. Coarse-Graining to Subsystems

Consider the Bell fibre
$$
\mathcal{F}_{AB}(|\Phi^+\rangle)
=
\{
(a_0^{(1)}, b_0^{(1)}),
(a_0^{(2)}, b_0^{(2)}),
(a_1^{(1)}, b_1^{(1)}),
(a_1^{(2)}, b_1^{(2)})
\}.
$$
Projecting only to subsystem \(A\), the visible possibilities are:
$$
a_0^{(1)},\ a_0^{(2)},\ a_1^{(1)},\ a_1^{(2)}.
$$
If we ignore which \(b\)-state each was paired with, we lose the compatibility pattern.

From the subsystem viewpoint, the hidden data has been coarse-grained away.

This is the toy-model analogue of the reduced state becoming mixed.

---

# 8. Toy Reduced-State Interpretation

For \( |\Phi^+\rangle \), standard quantum mechanics gives
$$
\rho_A = \frac{1}{2}|0\rangle\langle 0| + \frac{1}{2}|1\rangle\langle 1|,
$$

and likewise for \(B\).

In the toy model, this mixedness is not derived by amplitudes, but mirrored structurally:

- at the joint level, the fibre contains strict compatibility pairings,
- at the subsystem level, those pairings are forgotten,
- what remains is an unresolved set of possible subsystem labels.

Thus the reduced mixture is represented as **loss of joint compatibility information**.

---

# 9. Graph Interpretation

The toy fibre can be represented as a bipartite graph.

For the separable state \( |00\rangle \):

- every \(a_0^{(i)}\) connects to every \(b_0^{(j)}\),
- the graph is a complete \(2 \times 2\) product block.

For the Bell state \( |\Phi^+\rangle \):

- \(a_0^{(1)}\) connects only to \(b_0^{(1)}\),
- \(a_0^{(2)}\) connects only to \(b_0^{(2)}\),
- \(a_1^{(1)}\) connects only to \(b_1^{(1)}\),
- \(a_1^{(2)}\) connects only to \(b_1^{(2)}\).

So entanglement corresponds, in this toy model, to a **compatibility graph that is not a Cartesian product graph**.

This gives a useful visual and combinatorial representation.

---

# 10. What the Toy Model Achieves

This model does not reproduce amplitudes, interference, or Bell violations.

What it does achieve is narrower but important:

1. It gives a concrete realisation of projection degeneracy.  
2. It distinguishes product fibres from irreducibly joint fibres.  
3. It shows how subsystem coarse-graining can lose joint compatibility information.  
4. It provides a base for more advanced algebraic or probabilistic models.

---

# 11. Natural Generalisation

A more serious model could replace finite sets by:

- finite-dimensional fibre vector spaces,
- probability measures on fibres,
- sheaf-like compatibility structures,
- graph or category-valued fibres.

The most natural next step is probably a **weighted fibre graph model**, where:

- edges carry amplitudes or weights,
- separable states correspond to factorisable weight matrices,
- entangled states correspond to non-factorisable weight matrices.

---

# 12. Mathematical Status

| Component | Status |
|-----------|--------|
| finite subsystem fibres | defined |
| product-fibre separable example | consistent |
| non-factorisable Bell-fibre example | consistent |
| reduced-state coarse-graining analogy | heuristic but clear |
| physical completeness | absent by design |

---

# 13. Open Problems

1. Add weights or amplitudes to the compatibility graph.  
2. Define a fibre entropy and compare it with von Neumann entropy.  
3. Extend from basis states to arbitrary superpositions.  
4. Determine whether interference can be represented by phase data on fibre edges.  
5. Test whether a probabilistic Bell-type model can be constructed without contradicting the Bell-aware constraints of DDF-QM-EXT-002.

---

# 14. Main Result

The toy model shows explicitly that DDF projection fibres can be organised so that:

- separable states correspond to product-like fibres,
- entangled states correspond to irreducibly joint compatibility fibres,
- subsystem reduction corresponds to forgetting joint compatibility structure.

This is enough to justify the projection-fibre programme as a serious line of DDF development.

---

# Summary

This note provides the first concrete toy model for projection degeneracy and entanglement in DDF.

It does not yet produce full quantum dynamics.

But it does show that the core idea is mathematically workable and structurally nontrivial.
