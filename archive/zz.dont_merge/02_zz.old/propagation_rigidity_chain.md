# Propagation Rigidity Chain

**Note ID:** N1  
**Location:** 02_operator_notes  
**Role:** Mathematical chain from admissibility to wave propagation  

---

# 1. Overview

This note combines three structural steps of the operator framework into a single derivation chain:

1. Trace admissibility  
2. Cone stability  
3. Propagation rigidity  

Together these establish that admissible propagation must satisfy a **linear spectral bound**, producing the universal wave equation and the maximal propagation speed.

---

# 2. Step 1 — Trace Admissibility

Trace admissibility defines the stability condition for projection-admissible modes.

Let \( \psi(x) \) be a field and \( f(x) \) a Schwartz test function.

Define the trace pairing

\[
\langle \psi , f \rangle = \int \psi(x)f(x)\,dx
\]

Translations act as

\[
T_a\psi(x) = \psi(x+a)
\]

Admissibility requires polynomial boundedness:

\[
|\langle \psi , f(x+a) \rangle| \le C(1+|a|)^N
\]

This forbids exponential growth.

Therefore modes of the form

\[
e^{\lambda a}
\]

with \( \lambda>0 \) are inadmissible.

**Conclusion**

Exponential spectral envelopes cannot exist.

Only polynomially bounded harmonic modes survive.

---

# 3. Step 2 — Cone Stability

Consider a propagating mode

\[
\psi(x,t)=\int A(k)e^{i(kx-\omega t)}dk
\]

If the dispersion relation grows faster than linearly

\[
|\omega(k)| \sim |k|^{1+\epsilon}
\]

then phase translation generates exponential envelopes.

This violates trace admissibility.

Therefore the dispersion relation must satisfy

\[
|\omega| \le c|k|
\]

This inequality defines a **spectral cone**.

All admissible propagation lies within this cone.

The boundary

\[
|\omega| = c|k|
\]

represents maximal admissible propagation.

---

# 4. Step 3 — Propagation Rigidity

Because admissible spectra are confined to the cone,

Fourier duality yields the operator relation

\[
\omega^2 = c^2 |k|^2
\]

which transforms to the differential equation

\[
\partial_t^2 \psi - c^2\nabla^2\psi = 0
\]

This is the **wave equation**.

The constant \(c\) is therefore identified as the maximal propagation speed.

---

# 5. Physical Interpretation

This derivation shows:

Propagation limits are not postulated.

They arise from spectral admissibility.

The constant \(c\) emerges as the **slope of the admissible propagation cone**.

Boundary modes of the cone correspond to:

- massless propagation
- electromagnetic waves
- relativistic light-speed transport

---

# 6. Structural Chain

The operator framework now contains the following derivation:

Trace admissibility
↓
exponential modes forbidden
↓
linear spectral bound
↓
propagation cone
↓
wave equation
↓
maximal propagation speed c

---

# 7. Role in the Operator Framework

This chain forms the first propagation result of the operator theory.

It provides the mathematical basis for:

- Lorentz symmetry
- Maxwell wave propagation
- Dirac factorisation
- spin structure

Later notes show that the wave operator can be factorised into a first-order operator, producing the Dirac structure.

---

# 8. Summary

Trace admissibility forbids exponential spectral growth.

This forces dispersion relations to remain inside a linear cone.

The cone boundary defines the maximal propagation speed and yields the wave equation.

Propagation rigidity therefore follows directly from spectral admissibility.