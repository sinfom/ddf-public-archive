# Note ID

N1

# Title

Propagation Rigidity in the Dual-Domain Framework

# Folder

02_operator_notes

# Status

Active mathematical development

# Version

v4.0

# Date

March 2026

# Purpose

Derive the **finite propagation cone**

|ω| ≤ c|k|

from projection-admissibility constraints in the Dual-Domain Framework (DDF).

This establishes the structural origin of the universal wave equation and the
existence of a maximal propagation speed.

---

# Depends On

P1 — Projection Ontology  
P2 — Constants as Projection Norms  
P3 — Projection Generator

---

# Establishes

• Projection-admissible state space  
• Exclusion of exponential spectral growth  
• Spectral slope bound  
• Emergence of propagation cone  
• Hyperbolic wave operator  
• Dispersion relation  
• Phase velocity rigidity  
• Group velocity and signal propagation  
• Localised wave packets

---

# Excludes

• spin structure  
• fermions  
• gauge fields  
• quantum commutation relations

(these appear in later notes)

---

# 1 Introduction

The Dual-Domain Framework describes the observable universe

\[
U = P(\Omega)
\]

as the projection of an infinite generative domain.

For the projected universe to remain stable, admissible states must satisfy
certain **trace-stability conditions** under translations.

These conditions impose strict constraints on the spectral behaviour of
admissible modes.

We show that these constraints force a **linear spectral bound**, producing a
finite propagation cone and the universal wave equation.

---

# 2 Trace Admissibility

Let \( \psi(x) \) be a field and \( f(x) \) a Schwartz test function.

Define the trace pairing

\[
\langle \psi , f \rangle =
\int \psi(x)f(x) dx
\]

Projection admissibility requires stability of this trace under translations.

Thus

\[
|\langle \psi(x+a),f(x) \rangle|
\]

must remain bounded for admissible states.

This excludes modes with **exponential spectral growth**.

---

# 3 Spectral Moderation

Let the Fourier transform of the field be

\[
\tilde{\psi}(k,\omega)
\]

Trace stability requires polynomial spectral bounds

\[
|\tilde{\psi}(k,\omega)| \le C(1+|k|+|\omega|)^N
\]

This prevents arbitrarily steep spectral slopes.

As a result admissible modes must satisfy a **linear spectral relation**.

---

# 4 Propagation Cone

The spectral moderation constraint implies

\[
|\omega| \le c|k|
\]

for some universal constant \(c\).

This defines the **propagation cone**

\[
\omega^2 \le c^2 k^2
\]

The boundary

\[
\omega^2 = c^2 k^2
\]

represents maximal propagation modes.

---

# 5 Wave Equation

The quadratic cone boundary corresponds to the hyperbolic operator

\[
\Box = \partial_t^2 - c^2\nabla^2
\]

Admissible fields therefore satisfy

\[
\Box \psi = 0
\]

This is the universal **wave equation**.

---

# 6 Dispersion Relation

Fourier modes of the wave equation satisfy

\[
\omega^2 = c^2 k^2
\]

which yields

\[
\omega = \pm ck
\]

This establishes the fundamental relation between frequency and wavelength.

---

# 7 Classical Wave Relation

Using

\[
k = \frac{2\pi}{\lambda}, \quad
\omega = 2\pi f
\]

we obtain

\[
f \lambda = c
\]

or equivalently

\[
v = f\lambda
\]

Thus the classical wave relation emerges directly from the propagation cone.

---

# 8 Phase Velocity

The phase velocity of a monochromatic mode is

\[
v_p = \frac{\omega}{k}
\]

Using the dispersion relation

\[
v_p = c
\]

Thus phase propagation occurs along the boundary of the cone.

---

# 9 Wave Packets and Localisation

Real signals require localisation.

A general wave field can be written

\[
\psi(x,t) =
\int A(k)e^{i(kx-\omega t)}dk
\]

If the spectrum is concentrated near \(k_0\) the field forms a **wave packet**

\[
\psi(x,t) \approx
A(x-v_g t)e^{i(k_0x-\omega_0 t)}
\]

The slowly varying envelope describes the localised signal.

---

# 10 Group Velocity

The envelope propagates with

\[
v_g = \frac{d\omega}{dk}
\]

For the linear dispersion relation

\[
\omega = ck
\]

we obtain

\[
v_g = c
\]

Thus both phase and signal propagation occur at the same velocity.

---

# 11 Interpretation in DDF

The derivation chain becomes

projection admissibility  
→ spectral moderation  
→ propagation cone  
→ wave equation  
→ dispersion relation  
→ classical wave behaviour

Thus the existence of a finite propagation speed arises purely from
projection-admissibility constraints.

The constant \(c\) is therefore interpreted as a **structural bound of the
projection** rather than a free parameter.

---

# 12 Mathematical Status

Established

1. spectral moderation from admissibility
2. propagation cone
3. hyperbolic wave operator
4. classical dispersion relation
5. group velocity propagation

---

# 13 Open Problems

| ID   | Problem                                          |
| ---- | ------------------------------------------------ |
| OP1  | relation of propagation cone to Lorentz symmetry |
| OP2  | derivation of first-order rigidity operator      |
| OP3  | connection to Dirac operator                     |
| OP4  | emergence of spin structure                      |

---

# 14 Next Step

The propagation rigidity operator admits a **first-order square root**

\[
(\gamma^\mu \partial_\mu)^2 = \Box
\]

which leads to the Dirac operator and spin structure.

This is derived in

**N5 — Dirac Factorisation**