# N1b Admissibility Hyperbolicity Microlocal Formulation

path: 02_operator_notes/N1b-Admissibility-Hyperbolicity-Microlocal-Formulation.md
folder: 02_operator_notes
filename: N1b-Admissibility-Hyperbolicity-Microlocal-Formulation.md
repository: DDF
type: research_note

# N1b — Admissibility ⇒ Hyperbolicity (Microlocal Formulation)

## Status
Active development (core theorem not yet fully proven)

---

## 1. Purpose

This note reformulates propagation rigidity using **microlocal analysis**.

Goal:

→ replace invalid Fourier/Paley–Wiener arguments  
→ express admissibility in terms of **wavefront propagation**  
→ identify conditions under which admissibility forces **hyperbolic dynamics**

---

## 2. Admissible State Space

Let:

ψ ∈ S′(ℝⁿ)

be a tempered distribution.

Admissibility requires:

1. Polynomial translation control  
2. Absence of exponential growth  
3. Stability under evolution  

These conditions ensure:

- ψ has a well-defined **wavefront set**  
- ψ does not develop uncontrolled high-frequency amplification  

---

## 3. Wavefront Set

We use the standard definition:

WF(ψ) ⊂ T*ℝⁿ \ {0}

This encodes:

- location of singularities  
- directions of high-frequency concentration  

---

## 4. Propagation Principle (Microlocal)

For a differential or pseudodifferential operator P:

Pψ = 0

the wavefront set evolves according to:

→ bicharacteristics of the principal symbol p(x, ξ)

(Hörmander propagation of singularities theorem)

---

## 5. Admissibility as a Propagation Constraint

We impose the key physical/mathematical condition:

### Admissibility Principle (Propagation Form)

Admissible states must satisfy:

1. Singularities propagate along continuous curves  
2. Propagation occurs at **finite speed**  
3. No instantaneous global spread of WF(ψ)  

---

## 6. Operator Classification via Propagation

We analyse standard operator classes:

---

### 6.1 Elliptic Operators

Example:

Δψ = 0

Properties:

- WF(ψ) = ∅ (smooth solutions)
- Green’s function has global support

Implication:

→ disturbances affect entire domain instantly  

Status:

❌ violates admissibility (infinite propagation)

---

### 6.2 Parabolic Operators

Example:

∂tψ − Δψ = 0

Properties:

- smoothing behaviour  
- solutions become analytic instantly  

Implication:

→ arbitrarily fast propagation tails  

Status:

❌ violates admissibility (infinite-speed diffusion)

---

### 6.3 Hyperbolic Operators

Example:

∂t²ψ − c²∇²ψ = 0

Properties:

- finite domain of dependence  
- propagation along characteristic surfaces  
- WF(ψ) transported along bicharacteristics  

Implication:

→ finite propagation speed  

Status:

✅ compatible with admissibility

---

## 7. Main Structural Result (Conditional)

### Theorem (Admissibility ⇒ Hyperbolicity, Conditional Form)

If:

- admissible states require finite-speed propagation of singularities  
- evolution is governed by a local differential or pseudodifferential operator P  

then:

P must be of **hyperbolic (real principal type)**.

---

### Justification (Sketch)

- elliptic operators violate finite propagation  
- parabolic operators violate finite-speed constraints  
- only hyperbolic operators preserve causal propagation of WF  

Thus:

finite propagation ⇒ hyperbolic operator class

---

## 8. Characteristic Set and Cone

Let:

p(x, ξ) = principal symbol of P  

The characteristic set:

p(x, ξ) = 0  

defines the allowed directions of propagation.

For hyperbolic operators:

→ this set forms a **cone in frequency space**

Thus:

propagation cone arises from symbol geometry

---

## 9. Limitations

This note does NOT yet prove:

- that admissibility alone implies finite propagation  
- uniqueness of operator P  
- quadratic form of symbol  
- Lorentz invariance  

---

## 10. Open Problems

| ID   | Problem                                              |
| ---- | ---------------------------------------------------- |
| OP1  | prove admissibility ⇒ finite propagation rigorously  |
| OP2  | classify admissible pseudodifferential operators     |
| OP3  | derive quadratic symbol from symmetry/irreducibility |
| OP4  | extend to global manifold setting                    |

---

## 11. Role in DDF

This note replaces:

❌ spectral support / Paley–Wiener arguments  

with:

✅ microlocal propagation framework  

It provides the bridge:

admissibility  
→ wavefront propagation  
→ hyperbolicity  
→ propagation cone  

---

## 12. Summary

The correct route to propagation rigidity is:

→ not Fourier decay  
→ not spectral support  

but:

→ propagation of singularities  
→ operator classification  
→ characteristic geometry  

This establishes hyperbolicity as the only viable class of admissible dynamics (under stated conditions).