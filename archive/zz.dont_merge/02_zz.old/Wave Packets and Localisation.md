# Wave Packets and Localisation

## Purpose

This note explains how **localized signals arise from superpositions of wave modes** and how such packets propagate within the admissible propagation cone.

---

## Superposition of Modes

A general wave field can be written as a Fourier superposition

\[
\psi(x,t) =
\int A(k) e^{i(kx-\omega t)} dk
\]

where

- \(A(k)\) is the spectral amplitude
- each mode satisfies the dispersion relation.

---

## Wave Packet Construction

If the spectrum \(A(k)\) is concentrated around a central wave number \(k_0\), the field forms a **wave packet**

\[
\psi(x,t)
\approx
A(x - v_g t)
e^{i(k_0 x - \omega_0 t)}
\]

where

\[
v_g = \frac{d\omega}{dk}
\]

is the group velocity.

---

## Envelope Propagation

The packet separates naturally into

- a rapidly oscillating **carrier wave**
- a slowly varying **envelope**

The envelope determines the location of the signal.

Thus signal propagation occurs at the group velocity.

---

## Linear Dispersion Case

For the propagation-rigidity dispersion relation

\[
\omega = ck
\]

the group velocity becomes

\[
v_g = c
\]

The entire packet therefore propagates rigidly without distortion.

---

## Localisation and Spectral Bounds

Localisation of a wave packet requires a **spread in wave numbers**.

However, admissibility conditions constrain spectral growth and prevent pathological localisation.

These constraints connect naturally to Paley–Wiener–type bounds on admissible spectra.

---

## Physical Interpretation

Wave packets represent:

- localized excitations
- signal propagation
- particle-like wave behaviour

They provide the bridge between:

- continuous wave fields
- localized physical phenomena.

---

## Leads To

- dirac_factorisation.md
- spin_structure.md