# N6 Spin Structure From Propagation Cone Symmetry

path: 06_quantum_structure/N6-Spin-Structure-from-Propagation-Cone-Symmetry.md
folder: 06_quantum_structure
filename: N6-Spin-Structure-from-Propagation-Cone-Symmetry.md
repository: DDF
type: research_note

# Note ID

N6

# Title

Spin Structure from Propagation Cone Symmetry (Corrected)

# Folder

06_quantum_structure

# Status

Conditional derivation (depends on N1b and N2/N2c)

# Version

v2.0 (corrected)

# Date

March 2026

---

# Purpose

To analyse how **spinorial structure** arises from:

- propagation constraints (N1 / N1b)  
- symmetry of the propagation cone (N2)  
- existence of a first-order factorisation (Dirac structure)  

---

# Depends On

- N1 — Propagation Rigidity (conditional on N1b)  
- N1b — Admissibility ⇒ Hyperbolicity  
- N2 — Lorentz Invariance (requires quadratic invariant form)  
- N5 — Dirac Factorisation (existence assumed)

---

# Establishes

• Conditional emergence of Lorentz symmetry  
• Conditional emergence of Spin group  
• Spin-½ representations given Dirac structure  

---

# 1. Propagation Cone (Input)

From N1 / N1b:

Admissible dynamics are governed by a hyperbolic operator with characteristic set:

|ω| ≤ c|k|

Boundary:

ω² = c²|k|²

**Important:**

This result is conditional on:

→ admissibility implying hyperbolicity (N1b)

---

# 2. Lorentz Symmetry (Conditional)

If the propagation cone is defined by a quadratic form:

Q(ω, k) = ω² − c²|k|²

then admissible transformations must preserve:

Q(ω, k)

This yields:

→ Lorentz group O(1,3)

Restricting to physical transformations:

→ SO⁺(1,3)

**Important:**

This requires:

→ uniqueness of quadratic form (not yet proven in DDF)

---

# 3. Dirac Operator (Assumed Structure)

Suppose the wave operator admits a first-order factorisation:

D² = □

with:

D = γ^μ ∂_μ

Then D must transform consistently under Lorentz transformations.

---

# 4. Emergence of Clifford Algebra

Consistency with Lorentz invariance requires:

{γ^μ, γ^ν} = 2η^{μν}

This defines the Clifford algebra associated with the quadratic form.

---

# 5. Spin Group

The Lorentz group has a nontrivial topology:

→ not simply connected  

Thus:

→ representations on fields require a double cover  

This gives:

Spin(1,3) ≅ SL(2,C)

---

# 6. Spinor Representations

Fields transform as:

ψ' = S(Λ) ψ

where:

S(Λ) ∈ Spin(1,3)

Under a 2π rotation:

ψ → −ψ

This defines **spin-½ behaviour**

---

# 7. Interpretation in DDF

The structural chain becomes:

admissibility  
→ (N1b) hyperbolicity  
→ propagation cone  
→ (N2) Lorentz symmetry (conditional)  
→ (N5) Dirac operator (assumed/derived)  
→ Clifford algebra  
→ Spin group  
→ spinor representations  

---

# 8. Spin Structure Theorem (Corrected Form)

If:

1. admissible dynamics are governed by a hyperbolic operator (N1b),  
2. the propagation cone is defined by a quadratic invariant form (N2/N2c),  
3. the operator admits a first-order Clifford factorisation (Dirac structure),  

then:

→ admissible states include spinor representations transforming under Spin(1,3),  
→ and spin-½ structure arises naturally from the double cover of the symmetry group.

---

# 9. Limitations

This note does NOT yet prove:

- uniqueness of quadratic invariant form  
- necessity of Dirac factorisation  
- global existence of spin structure (topological conditions)  

In particular:

→ existence of spin structure requires vanishing of w₂(M), not derived here  

---

# 10. Open Problems

| ID   | Problem                                             |
| ---- | --------------------------------------------------- |
| OP1  | prove uniqueness of quadratic form (N2c)            |
| OP2  | derive Dirac operator from projection generator     |
| OP3  | prove global spin structure from projection mapping |
| OP4  | incorporate mass term consistently                  |
| OP5  | extend to interacting/gauge-coupled fields          |

---

# 11. Role in DDF

This note provides the bridge:

propagation structure  
→ symmetry structure  
→ algebraic structure of fields  

It connects:

- operator geometry  
- Lorentz invariance  
- spinorial representation theory  

---

# 12. Key Insight

Spin is not introduced independently.

It arises from:

→ the algebraic structure required to represent the symmetry of propagation  

given:

- hyperbolic dynamics  
- quadratic invariant form  
- first-order operator structure  

---

# 13. Summary

Spin-½ structure is not assumed.

It follows conditionally from:

- propagation constraints  
- symmetry requirements  
- algebraic consistency  

The full derivation becomes complete once:

→ quadratic form uniqueness  
→ Dirac emergence  

are rigorously established.