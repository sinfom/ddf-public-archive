# Admissibility Balance Equation (Corrected Form)

## Dimensionless Formulation and Lock Condition

------

## 1. Overview

This document refines the **Admissibility Balance Equation** by:

- Ensuring **dimensionless consistency**
- Introducing a **lock-selection condition**
- Formalising the **finite solution requirement**

The purpose is to convert the balance concept into a mathematically valid and testable structure.

------

## 2. Dimensionless Variables

To ensure consistency, all variables must be normalised:

[
\tilde{T} = \frac{T}{T_*}, \quad
\tilde{C} = \frac{C}{C_*}, \quad
\tilde{G} = \frac{G}{G_*}
]

[
\tilde{\hbar} = \frac{\hbar}{\hbar_*}, \quad
\tilde{\Lambda} = \frac{\Lambda}{\Lambda_*}, \quad
\tilde{S} = \frac{S}{S_*}
]

Where:

- (T_*, C_*, G_*, \hbar_*, \Lambda_*, S_*) are reference scales
- All variables are now **dimensionless**

------

## 3. Corrected Balance Equation

[
\mathcal{B} =
\frac{\tilde{S}^{2}\tilde{G}\tilde{\Lambda}}
{\tilde{C}^{2}\tilde{T}^{2}\tilde{\hbar}}
+
\frac{\tilde{C}\tilde{T}\tilde{\hbar}}
{\tilde{G}\tilde{\Lambda}\tilde{S}^{3}}
-1 = 0
]

------

## 4. Interpretation of Terms

### Term 1 — Contraction Component

[
\Pi_+ =
\frac{\tilde{S}^{2}\tilde{G}\tilde{\Lambda}}
{\tilde{C}^{2}\tilde{T}^{2}\tilde{\hbar}}
]

Represents:

- Coupled effect of:
  - spatial expansion ((\tilde S))
  - curvature ((\tilde G))
  - global expansion term ((\tilde \Lambda))

Opposed by:

- propagation ((\tilde C))
- time-rate ((\tilde T))
- quantisation ((\tilde \hbar))

------

### Term 2 — Expansion Component

[
\Pi_- =
\frac{\tilde{C}\tilde{T}\tilde{\hbar}}
{\tilde{G}\tilde{\Lambda}\tilde{S}^{3}}
]

Represents:

- propagation and quantum-driven expansion

Opposed by:

- curvature
- cosmological expansion term
- spatial volume scaling

------

### Balance Condition

[
\Pi_+ + \Pi_- = 1
]

This enforces:

- coupling across all variables
- exclusion of independent divergence
- existence of a finite equilibrium

------

## 5. Pre-Admissible Behaviour

As:

[
\tilde{T}, \tilde{C} \to \infty
]

Then:

[
\Pi_+ \to 0
]

[
\Pi_- \to \infty
]

So:

[
\mathcal{B} \to \infty \neq 0
]

**Conclusion:**

- Infinite propagation is inadmissible
- Infinite time-rate is inadmissible
- No balance exists in the unbounded regime

------

## 6. Finite Admissible Solution

A valid solution requires:

[
\mathcal{B} = 0
]

This implies:

[
\tilde{T}, \tilde{C}, \tilde{G}, \tilde{\hbar}, \tilde{\Lambda}, \tilde{S}
\rightarrow \text{finite values}
]

------

## 7. Lock Selection Condition (New)

To ensure a **unique physical solution**, impose:

[
\frac{d\mathcal{B}}{d\tilde{C}} = 0
]

Together with:

[
\mathcal{B} = 0
]

This defines:

- the **Admissibility Lock Point**
- not just any root, but the **stable equilibrium**

------

## 8. Emergent Propagation Limit

From the finite solution:

[
\tilde{C} \rightarrow \tilde{c}
]

Restoring units:

[
C \rightarrow c
]

Then:

[
|\omega| \leq c|k|
]

**Result:**

- finite propagation emerges from balance
- the light cone is a consequence of admissibility

------

## 9. Key Result

> A finite propagation limit and stable physical constants arise as a necessary consequence of the admissibility balance equation, provided a lock-selection condition is applied.

------

## 10. Summary

This corrected formulation:

- fixes dimensional consistency
- preserves the infinite → finite collapse
- introduces a stability condition
- supports emergence of the propagation cone

------

## 11. Next Step

The next development stage is to:

1. Solve the coupled system:
   [
   \mathcal{B}=0,\quad \frac{d\mathcal{B}}{d\tilde{C}}=0
   ]
2. Determine:
   - existence and uniqueness of solution
   - dependence between constants
   - sensitivity to scaling choices

------

**End of File**