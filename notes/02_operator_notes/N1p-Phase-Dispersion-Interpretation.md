# Note ID

N1p

# Title

N1p. Phase / Dispersion Interpretation 

# Folder

02_operator_notes

# Status

Active mathematical development (corrected)

# Version

v1.0

# Date

March 2026

---

# Correction Note

This note has been updated to remove earlier reliance on Paley–Wiener arguments.

The propagation cone is now derived from operator structure (see N0/N1), not from Fourier growth bounds.

---

# Purpose

Derive the classical wave relation

v = f λ

from the propagation cone established in propagation rigidity, and clarify how the homogeneity of the cone boundary implies a constant phase velocity for massless modes in the Dual-Domain Framework (DDF).

---

# Depends On

- N0 — Operator Emergence and Hyperbolic Cone  
- N1 — Propagation Rigidity  
- F5 — Structural Role of Physical Constants  

---

# Establishes

- Plane-wave analysis inside the DDF propagation cone  
- Dispersion relation from the hyperbolic operator  
- Phase velocity relation v_p = ω/k  
- Classical identity v = f λ  
- Constancy of fλ from homogeneity of the cone boundary  

---

# Excludes

- Dirac factorisation and spin  
- Gauge interactions  
- Curved spacetime  
- Any Paley–Wiener arguments  

---

# 1. Introduction

From N0/N1, admissible dynamics in DDF are governed by a hyperbolic operator with principal symbol:

p(ω, k) = ω² − c²|k|²

The characteristic set:

p(ω, k) = 0

defines the propagation cone:

|ω| ≤ c |k|

This note explores the **wave-theoretic consequences** of this structure.

---

# 2. Propagation Cone and Hyperbolic Operator (Corrected)

The propagation cone arises from the operator:

P = L†L − M

with principal symbol:

p(ω, k) = ω² − c²|k|²

The boundary:

ω² = c² k²

defines the extremal propagation modes.

In configuration space, this corresponds to:

∂t² ψ − c² ∇² ψ = 0

This is the wave operator.

---

# 3. Plane Waves and Dispersion

## 3.1 Plane-Wave Ansatz

ψ(x,t) = A exp(i(kx − ωt))

Substitute into wave equation:

∂t² ψ − c² ∂x² ψ = 0

⇒

−ω² + c² k² = 0

Thus:

ω² = c² k²

---

## 3.2 Interpretation

This is not assumed — it is:

→ the condition p(ω,k)=0

Thus plane waves correspond to **characteristic modes of the operator**.

---

# 4. Frequency and Wavelength

Using Fourier definitions:

f = ω / (2π)  
λ = 2π / |k|

---

# 5. Phase Velocity

Definition:

v_p = ω / k

Substitute:

v_p = (2π f) / (2π / λ) = f λ

Thus:

v_p = f λ

---

# 6. Constant Phase Velocity from Cone Boundary

On the cone boundary:

ω = c k

Thus:

v_p = ω / k = c

So:

f λ = c

---

# 7. Role of Homogeneity

The relation:

ω = c k

is homogeneous:

(ω, k) → (λω, λk)

⇒ ratio ω/k unchanged

Thus:

v_p = constant

This is the **true reason** for constant phase velocity.

---

# 8. Interpretation in DDF

- c is the slope of the characteristic set  
- v_p = c is structural, not empirical  
- fλ = c reflects operator geometry  

---

# 9. Correct Logical Chain

Operator L  
→ hyperbolic operator  
→ characteristic set  
→ dispersion relation  
→ phase velocity  
→ v = f λ  

---

# 10. Status of Results

### Established

- Hyperbolic operator  
- Cone structure  
- Dispersion relation  
- Phase velocity  

### Derived

- Constant phase velocity  
- Classical wave relation  

### Not addressed

- Dispersion inside cone  
- Wave packets  
- Massive modes  

---

# 11. Key Insight

The classical relation:

v = f λ

is not a physical law.

It is:

→ a consequence of homogeneity of the propagation cone

---

# 12. Next Step

Study:

- dispersive systems (inside cone)  
- group velocity  
- wave packet evolution  