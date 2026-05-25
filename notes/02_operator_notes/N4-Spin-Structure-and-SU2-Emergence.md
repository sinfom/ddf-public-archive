# N4 Spin Structure And SU2 Emergence

path: 02_operator_notes/N4-Spin-Structure-and-SU2-Emergence.md
folder: 02_operator_notes
filename: N4-Spin-Structure-and-SU2-Emergence.md
repository: DDF
type: research_note

# N4 — Spin Structure and SU(2) Emergence

## Status
Core structural derivation

---

## 1. Purpose

Derive:

- why spinors arise
- why spin = 1/2
- why SU(2) symmetry appears

from the Dirac factorisation and Lorentz invariance.

---

## 2. Starting Point

From N3:

γ^μ ∂_μ ψ = mψ

with:

{γ^μ, γ^ν} = 2η^{μν}

This requires ψ to be multi-component.

---

## 3. Rotations in Physical Space

Spatial rotations act on coordinates:

x → R x

with:

R ∈ SO(3)

This preserves:

|x|²

---

## 4. Requirement for ψ

The equation must remain invariant under rotations.

Thus ψ must transform under a representation of rotations.

---

## 5. Clifford Algebra → Spin Representation

The γ-matrices generate the Clifford algebra.

From these we construct:

Σ^{μν} = (1/4)[γ^μ, γ^ν]

These generate transformations on ψ.

---

## 6. Spatial Rotation Generators

Define:

J^i = (1/2) ε^{ijk} Σ^{jk}

These satisfy:

[J^i, J^j] = i ε^{ijk} J^k

---

## 7. SU(2) Algebra

The above commutation relations define:

→ SU(2)

Thus:

spin transformations are SU(2) transformations

---

## 8. Why SU(2), Not SO(3)

Key fact:

- SO(3): rotations of space  
- SU(2): double cover of SO(3)

Spinors transform under SU(2), not SO(3)

---

## 9. Emergence of Spin-1/2

Representation theory of SU(2):

Smallest nontrivial representation = 2-dimensional

This gives:

ψ = (ψ₁, ψ₂)

This is a spinor.

---

## 10. 2π Rotation Property

Under full rotation:

θ = 2π

Spinor transforms as:

ψ → −ψ

Only after:

θ = 4π

does ψ return to original value.

---

## 11. Interpretation

Thus:

- spin is NOT classical rotation  
- it is representation of symmetry group  

Spin-1/2 arises because:

→ Dirac algebra forces SU(2) structure  
→ smallest representation is 2-component  

---

## 12. Pauli Matrices

In non-relativistic limit:

γ-structure reduces to:

σ^i (Pauli matrices)

These satisfy:

σ^i σ^j = δ^{ij} + i ε^{ijk} σ^k

---

## 13. Physical Meaning

Spin corresponds to:

- intrinsic angular momentum  
- internal degree of freedom  
- symmetry of the projection operator  

---

## 14. Key Result

### Spin Emergence Theorem (DDF)

Given:

- Lorentz-invariant Dirac operator  
- Clifford algebra structure  

then:

ψ transforms under SU(2), and the minimal representation yields spin-1/2.

---

## 15. Position in DDF Chain

L → symbol → cone → Lorentz → Dirac → spin

---

## 16. Key Insight

Spin is not added.

It is:

→ forced by the algebra required to factorise Lorentz-invariant propagation