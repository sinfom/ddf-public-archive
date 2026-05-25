---
path: 02_operator_notes/N2d-Schrodinger-Limit-from-Klein-Gordon.md
folder: 02_operator_notes
filename: N2d-Schrodinger-Limit-from-Klein-Gordon.md
repository: DDF
type: research_note
status: active
depends_on:
  - N2c-Klein-Gordon-Emergence
  - N2b-Dispersion-and-Admissibility
  - N1-Propagation-Rigidity
---

# N2d — Schrödinger Limit from Klein–Gordon

## Status

Active development (non-relativistic limit derivation)

---

# 1. Purpose

This note derives Schrödinger evolution as the non-relativistic limit of the Klein–Gordon equation obtained in N2c.

Goal:

→ recover non-relativistic quantum evolution  
→ derive Schrödinger dynamics from admissible relativistic propagation  
→ connect DDF projection structure to low-energy quantum mechanics  

This note shows that Schrödinger evolution is not fundamental within DDF.

Instead:

it emerges as an approximation to relativistic admissible propagation.

---

# 2. Starting Point

From N2c:

admissible scalar projected modes satisfy the Klein–Gordon equation:

\[
\left(
\frac{1}{c^2}\partial_t^2
-
\nabla^2
+
\frac{m^2c^2}{\hbar^2}
\right)\phi
=
0
\]

where:

- \(c\) is the admissible propagation speed
- \(m\) is spectral mass displacement
- \(\phi\) is an admissible projected scalar mode

---

# 3. Physical Interpretation

The Klein–Gordon equation describes fully relativistic propagation.

However:

many admissible projected states evolve far below the cone boundary:

\[
v \ll c
\]

In this regime:

- relativistic corrections become small
- rest-energy oscillation dominates
- propagation becomes approximately non-relativistic

Schrödinger evolution emerges in this low-energy limit.

---

# 4. Separation of Rest-Energy Oscillation

The dominant oscillatory phase of a massive relativistic mode is:

\[
e^{-imc^2 t/\hbar}
\]

Factor this from the field:

\[
\phi(x,t)
=
e^{-imc^2 t/\hbar}
\psi(x,t)
\]

where:

\[
\psi(x,t)
\]

is assumed to vary slowly compared with the rapid rest-energy phase oscillation.

Interpretation:

- the exponential factor represents intrinsic relativistic phase rotation
- \(\psi\) represents the slowly varying admissible envelope

---

# 5. Time Derivatives

Compute derivatives:

\[
\partial_t\phi
=
e^{-imc^2 t/\hbar}
\left(
\partial_t\psi
-
\frac{imc^2}{\hbar}\psi
\right)
\]

and:

\[
\partial_t^2\phi
=
e^{-imc^2 t/\hbar}
\left(
\partial_t^2\psi
-
\frac{2imc^2}{\hbar}\partial_t\psi
-
\frac{m^2c^4}{\hbar^2}\psi
\right)
\]

Spatial derivatives satisfy:

\[
\nabla^2\phi
=
e^{-imc^2 t/\hbar}
\nabla^2\psi
\]

---

# 6. Substitute into Klein–Gordon Equation

Substitute into:

\[
\left(
\frac{1}{c^2}\partial_t^2
-
\nabla^2
+
\frac{m^2c^2}{\hbar^2}
\right)\phi
=
0
\]

After cancellation of the rest-mass terms:

\[
\frac{1}{c^2}\partial_t^2\psi
-
\frac{2im}{\hbar}\partial_t\psi
-
\nabla^2\psi
=
0
\]

---

# 7. Non-Relativistic Approximation

In the low-energy regime:

\[
v \ll c
\]

the envelope evolves slowly.

Therefore:

\[
\frac{1}{c^2}\partial_t^2\psi
\]

is negligible compared with:

\[
\frac{m}{\hbar}\partial_t\psi
\]

Thus:

\[
-
\frac{2im}{\hbar}\partial_t\psi
-
\nabla^2\psi
=
0
\]

Rearranging:

\[
i\hbar\partial_t\psi
=
-\frac{\hbar^2}{2m}\nabla^2\psi
\]

This is the free-particle Schrödinger equation.

---

# 8. Inclusion of Potential

If the admissible environment contains a scalar potential \(V(x)\), the equation becomes:

\[
i\hbar\partial_t\psi
=
\left(
-\frac{\hbar^2}{2m}\nabla^2
+
V(x)
\right)\psi
\]

This is the standard Schrödinger equation.

---

# 9. Interpretation Inside DDF

| Standard Physics         | DDF Interpretation                         |
| ------------------------ | ------------------------------------------ |
| Schrödinger wavefunction | slowly varying admissible envelope         |
| quantum phase evolution  | residual relativistic phase structure      |
| kinetic operator         | low-energy propagation approximation       |
| rest-energy oscillation  | intrinsic relativistic spectral rotation   |
| non-relativistic limit   | propagation deep inside admissibility cone |

---

# 10. Structural Consequence

This note establishes:

\[
\text{Admissibility}
\Rightarrow
\text{Relativistic Cone}
\Rightarrow
\text{Klein–Gordon Equation}
\Rightarrow
\text{Low-Energy Limit}
\Rightarrow
\text{Schrödinger Evolution}
\]

Thus:

Schrödinger evolution appears as an emergent approximation to relativistic admissible propagation.

---

# 11. Why Schrödinger Is Not Fundamental in DDF

Within DDF:

the fundamental structure is relativistic propagation.

Schrödinger evolution appears only after:

- extracting the dominant relativistic phase
- neglecting higher-order relativistic corrections
- restricting propagation deep inside the cone

Therefore:

the Schrödinger equation is emergent rather than fundamental.

---

# 12. Relationship to Dirac Structure

N3 derives the Dirac equation as the admissible first-order relativistic factorisation of Klein–Gordon propagation.

N2d instead derives the non-relativistic scalar limit.

Thus:

\[
N2d
=
\text{low-energy scalar limit}
\]

\[
N3
=
\text{first-order relativistic factorisation}
\]

These are parallel consequences of N2c.

---

# 13. Theorem (Conditional Form)

## Theorem — Schrödinger Emergence from Klein–Gordon Limit

Let admissible scalar projected modes satisfy:

\[
\left(
\frac{1}{c^2}\partial_t^2
-
\nabla^2
+
\frac{m^2c^2}{\hbar^2}
\right)\phi
=
0
\]

Assume:

1. propagation occurs far below the admissibility cone boundary
2. envelope evolution is slow relative to rest-energy oscillation
3. higher-order relativistic corrections are negligible

Then:

the slowly varying projected envelope satisfies:

\[
i\hbar\partial_t\psi
=
-\frac{\hbar^2}{2m}\nabla^2\psi
\]

Therefore:

Schrödinger evolution emerges as the non-relativistic approximation to admissible relativistic projection dynamics.

---

# 14. Open Problems

| ID   | Open Problem                               |
| ---- | ------------------------------------------ |
| OP1  | derivation of probabilistic interpretation |
| OP2  | emergence of Hilbert space structure       |
| OP3  | emergence of measurement theory            |
| OP4  | derivation of gauge coupling               |
| OP5  | extension to interacting many-body systems |
| OP6  | emergence of quantum decoherence           |

---

# 15. Limitations

This derivation does not yet establish:

- Born rule
- measurement collapse
- quantum statistics
- entanglement structure
- operator quantisation

The note only derives Schrödinger evolution as a low-energy propagation approximation.

---

# 16. Summary

DDF admissibility produces:

- hyperbolic relativistic propagation
- Klein–Gordon scalar dynamics
- finite cone structure

Factoring out the dominant rest-energy oscillation and taking the low-energy limit yields:

\[
i\hbar\partial_t\psi
=
-\frac{\hbar^2}{2m}\nabla^2\psi
\]

which is precisely the Schrödinger equation.

Therefore:

Schrödinger evolution emerges naturally as the non-relativistic limit of admissible relativistic propagation within DDF projection theory.