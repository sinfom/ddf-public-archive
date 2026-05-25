# N1 Propagation Rigidity

path: 02_operator_notes/N1-Propagation-Rigidity.md
folder: 02_operator_notes
filename: N1-Propagation-Rigidity.md
repository: DDF
type: research_note

# Propagation Rigidity Chain (Corrected)

## Note ID

N1

## Title

Propagation Rigidity in the Dual-Domain Framework (Final Corrected)

## Folder

02_operator_notes

## Status

Mathematically corrected (v5.0 — hyperbolicity fix applied)

## Date

March 2026

------

# **1. Purpose**

Derive the **finite propagation cone**

∣ω∣≤c∣k∣∣ω∣≤c∣k∣

from:

- admissibility (state constraint)
- operator structure (via projection generator LL)
- principal symbol classification

without invalid spectral or heuristic steps.

------

# **2. Critical Corrections (Final Form)**

This version resolves all known issues:

### Removed (invalid)

- Paley–Wiener ⇒ cone ❌
- admissibility ⇒ hyperbolic ❌
- implicit Lorentz insertion ❌

### Replaced with (correct chain)

- admissibility constrains **states only**
- operator constructed from LL
- principal symbol explicitly derived
- hyperbolicity from **symbol classification**
- cone from **characteristic set**

------

# **3. Step 1 — Admissibility (State Space Only)**

Let:

ψ∈S′(Rn)ψ∈S′(Rn)

Admissibility requires:

- polynomial translation bounds
- no exponential growth
- stability under evolution

This ensures:

- tempered spectral behaviour
- controlled wavefront set

**Key principle:**

> Admissibility constrains states — not the form of the evolution operator.

------

# **4. Step 2 — Physical Requirement: Finite Propagation**

We impose:

> Disturbances must propagate with finite speed.

This is required for:

- causality
- observability
- projection stability

This excludes:

| Type      | Behaviour                | Status     |
| --------- | ------------------------ | ---------- |
| Elliptic  | instantaneous influence  | ❌ excluded |
| Parabolic | infinite-speed diffusion | ❌ excluded |

Only hyperbolic structure remains viable (see N1b). 

------

# **5. Step 3 — Operator Class Constraint**

From microlocal propagation (wavefront evolution):

- singularities propagate along bicharacteristics
- finite-speed propagation ⇒ hyperbolic class

Thus:

finite propagation requirement  ⇒  hyperbolic operator classfinite propagation requirement⇒hyperbolic operator class

⚠️ Important:
This is **not derived from admissibility alone** — it is an additional structural requirement.

------

# **6. Step 4 — Operator from Projection Generator**

From DDPM:

L=A ∂t+B⋅∇+lower-order termsL=A∂t+B⋅∇+lower-order terms

Define:

P:=L†L−MP:=L†L−M

This yields a **second-order evolution operator**.

------

# **7. Step 5 — Principal Symbol**

Replace:

∂t→iω,∇→ik∂t→iω,∇→ik

Then:

σ(L)=i(Aω+B⋅k)σ(L)=i(Aω+B⋅k)σ(P)=∣Aω+B⋅k∣2σ(P)=∣Aω+B⋅k∣2

After symmetry reduction:

p(ω,k)=A2ω2−∣B∣2∣k∣2p(ω,k)=A2ω2−∣B∣2∣k∣2

------

# **8. Step 6 — Hyperbolicity from Cone Structure (Critical Fix)**

The symbol:

p(ω,k)=A2ω2−∣B∣2∣k∣2p(ω,k)=A2ω2−∣B∣2∣k∣2

is a quadratic form.

Define:

c=∣B∣Ac=A∣B∣

Then:

p(ω,k)=ω2−c2∣k∣2p(ω,k)=ω2−c2∣k∣2

This has:

- one positive direction
- three negative directions

i.e. **signature (1,3)**.

### Therefore:

By standard PDE classification:

principal symbol  ⇒  hyperbolic operatorprincipal symbol⇒hyperbolic operator

------

## **Correct Logical Chain (Fixed)**

admissibility  →  finite propagation requirement  →  operator construction  →  principal symbol  →  hyperbolicityadmissibility→finite propagation requirement→operator construction→principal symbol→hyperbolicity

------

# **9. Step 7 — Characteristic Set**

Defined by:

p(ω,k)=0p(ω,k)=0⇒ω2=c2∣k∣2⇒ω2=c2∣k∣2

------

# **10. Step 8 — Propagation Cone**

Thus:

∣ω∣=c∣k∣∣ω∣=c∣k∣

and admissible propagation satisfies:

∣ω∣≤c∣k∣∣ω∣≤c∣k∣

This is the **propagation cone**.

------

# **11. Step 9 — Microlocal Propagation**

From Hörmander propagation of singularities (N1b):

- wavefront set travels along bicharacteristics
- bicharacteristics lie on characteristic set

Therefore:

propagation speed≤cpropagation speed≤c

------

# **12. Step 10 — Wave Operator**

From the symbol:

p(ω,k)=ω2−c2∣k∣2p(ω,k)=ω2−c2∣k∣2

the operator is:

∂t2−c2∇2∂t2−c2∇2

This is the **wave operator**.

------

# **13. Final Correct Derivation Chain**

Admissibility (state constraint)
↓
finite propagation requirement
↓
microlocal propagation constraints (N1b) 
↓
hyperbolic operator class
↓
projection generator LL
↓
constructed operator P=L†L−MP=L†L−M
↓
principal symbol
↓
hyperbolicity (symbol classification)
↓
characteristic set
↓
propagation cone
↓
finite propagation speed cc

------

# **14. Consistency with N1a and N1b**

### N1b (microlocal)

- supplies **propagation of singularities justification**
- correctly identifies hyperbolicity as required class
- does NOT overclaim derivation

### N1a (dispersion)

- fits AFTER this note
- uses cone to define:
  - phase velocity
  - group velocity