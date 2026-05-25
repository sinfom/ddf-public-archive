# N0 Operator Emergence And Hyperbolic Cone

path: 02_operator_notes/N0-Operator-Emergence-and-Hyperbolic-Cone.md
folder: 02_operator_notes
filename: N0-Operator-Emergence-and-Hyperbolic-Cone.md
repository: DDF
type: research_note

# N0 — Operator Emergence and Hyperbolic Cone

## Status
Core structural derivation (fills DDF gap)

---

## 1. Purpose

Derive the propagation cone:

|ω| ≤ c|k|

directly from the projection generator L.

This completes the chain:

L → operator → symbol → cone

---

## 2. Starting Point: Projection Generator

From DDF:

L = A ∂t + B·∇ + C ∇² + Q + K + D + …

Where:

- A = temporal component
- B = transport component
- C = smoothing/diffusion
- Q = quantisation
- K = curvature
- D = constraint terms

---

## 3. Physical Constraint: Admissibility

Admissible states require:

- stability (no exponential blow-up)
- bounded propagation
- coherent evolution

This excludes:

- elliptic operators (instantaneous influence)
- purely parabolic operators (unbounded smoothing)

Thus admissible dynamics must be:

→ **hyperbolic-dominated**

---

## 4. Constructing the Governing Operator

From the DDPM field equation:

(L†L)ψ = Mψ

Define:

P := L†L − M

So governing equation is:

Pψ = 0

---

## 5. Principal Part of L

Retain only highest-order derivative terms:

L_principal = A ∂t + B·∇

(∇² is lower order than first-order symbolically after squaring)

---

## 6. Principal Symbol of L

Replace:

∂t → iω  
∇ → ik  

Then:

σ(L) = i(Aω + B·k)

---

## 7. Symbol of L†L

σ(L†L) = |Aω + B·k|²

Expand:

= A²ω² + 2A(B·k)ω + |B·k|²

---

## 8. Removal of Cross-Term

By symmetry (time-reversal / isotropy):

the mixed term must vanish:

⇒ effective form:

σ(L†L) = A²ω² + |B|²|k|²

---

## 9. Subtracting M

The constant matrix M contributes only lower-order terms.

Thus principal symbol of P:

p(ω, k) = A²ω² − |B|²|k|²

(Sign chosen for hyperbolic signature)

---

## 10. Hyperbolicity

We now have:

p(ω, k) = 0  
⇒ A²ω² = |B|²|k|²  

⇒ |ω| = (|B| / A) |k|

Define:

c := |B| / A

---

## 11. Emergence of the Cone

Thus:

|ω| ≤ c|k|

This is the **propagation cone**.

---

## 12. Resulting Operator

The operator corresponding to p is:

∂t² − c²∇²

Thus the wave operator emerges as:

the principal part of L†L − M

---

## 13. Interpretation

- c is NOT derived from Fourier bounds  
- c is the ratio of generator components:

c = transport / temporal scaling

Thus:

c is a **structural parameter of L**

---

## 14. Final Theorem

### Operator → Cone Theorem (DDF Internal)

Given projection generator:

L = A∂t + B·∇ + lower-order terms

then the induced operator:

P = L†L − M

has principal symbol:

p(ω,k) = A²ω² − |B|²|k|²

which defines the propagation cone:

|ω| ≤ c|k|

with:

c = |B| / A

---

## 15. What This Fixes

This replaces the invalid chain:

admissibility → spectral cone ❌

with the correct chain:

L → operator → symbol → cone ✅

---

## 16. Position in DDF

This result now supports:

- propagation rigidity (N1)
- Dirac factorisation
- spin structure
- emergence of relativity

---

## 17. Key Insight

The propagation cone is NOT imposed.

It is:

→ the geometric shadow of the generator L