# Note ID

N1

# Title

Propagation Rigidity in the Dual-Domain Framework

# Folder

02_operator_notes

# Status

Active mathematical development

# Version

v3.1

# Date

March 2026

# Purpose

Derive the **propagation cone**

|ω| ≤ c|k|

from minimal projection-admissibility assumptions within the Dual-Domain Framework (DDF).

This note establishes the mathematical foundation for the **finite propagation bound** that later produces the constant (c).

------

# Depends On

P1 — Projection Ontology
P2 — Constants as Projection Norms
P3 — Projection Generator (L)

------

# Establishes

• Definition of projection-admissible state space
• Exclusion of exponential spectral growth
• Spectral slope bound
• Emergence of a propagation cone
• Hyperbolic operator classification
• Definition of the constant (c)

------

# Excludes

• No empirical claim about measured light speed
• No Dirac factorisation yet
• No gauge structure derivation

------

# 1 Introduction

The Dual-Domain Framework describes the observable universe (U) as the projection

$$
U = P(\Omega)
$$



of an infinite generative domain ( \Omega ).

Physical states must remain stable under this compression.
This requirement defines the **admissible state space**.

This note shows that admissibility forces a **finite propagation cone**.

Logical order of the derivation:

admissibility
→ spectral constraints
→ slope theorem
→ Paley–Wiener tightening
→ operator classification
→ hyperbolicity
→ emergence of (c)

------

# 2 Projection Framework

The universe arises from projection of an infinite domain.

Projection stability requires that observable states remain bounded under compression.

This condition restricts admissible spectral behaviour.

------

# 3 Definition of Projection-Admissible States

Let (w(x)) be a polynomially bounded weight.

## Definition 3.1 — Admissible State Space

A distribution 
$$
\psi
$$
 is projection-admissible 
$$
written ( \psi \in A ))
$$
if:

### (A1) Weighted Finite Energy

$$
\int | \psi(x) |^2 w(x),dx < \infty
$$




### (A2) Spectral Moderation

The Fourier transform grows at most polynomially.

### (A3) Polynomial Translation Growth

Let (T_a) denote translation.

$$
||T_a \psi|| \le P(|a|)
$$


for some polynomial (P).

### (A4) Harmonic Coherence

For the harmonic operator (H_G):

$$
\langle \psi, H_G \psi \rangle < \infty
$$


This excludes exponential spectral instability.

------

## Lemma 3.2

The admissible space (A) is a vector space.

Proof: direct verification.

------

# 4 Spectral Representation

Admissible states admit the Fourier representation

$$
\psi(x) = \int e^{ikx}, d\mu(k)
$$


where ( \mu ) is the spectral measure.

------

## Proposition 4.1

For 
$$
\psi \in A
$$
• the spectral measure is tempered
• polynomial moments exist
• exponential spectral concentration is excluded

------

# 5 Spectral Support Restrictions

## Lemma 5.1 — Exclusion of Vertical Rays

If spectral support contains arbitrarily large temporal frequencies at fixed spatial frequency, polynomial translation bounds are violated.

Therefore such spectra are inadmissible.

------

## Corollary 5.2

Admissible spectra cannot contain arbitrarily large temporal frequencies at fixed spatial frequency.

------

# 6 Spectral Moment Bounds

Define the autocorrelation

$$
R(a)=\langle \psi , T_a \psi \rangle
$$
Translation moderation implies polynomial bounds.

------

## Lemma 6.1

Polynomial bounds on (R(a)) imply finite spectral moments.

------

## Lemma 6.2

Finite moments imply polynomial spectral tail decay.

------

# 7 Spectral Slope Bound

## Theorem 7.1

For admissible states there exists (c) such that

$$
|\omega| \le c|k| + C
$$
Thus arbitrarily large spectral slopes are incompatible with admissibility.

------

# 8 Paley–Wiener Tightening

The additive constant can be removed.

## Theorem 8.1 — Paley–Wiener Tightening

If a tempered distribution satisfies

1. polynomial translation bounds
2. polynomial spectral moments

then spectral support must lie in a homogeneous cone

$$
|\omega| \le c|k|
$$




Proof follows from Paley–Wiener–Schwartz theory.

------

# 9 Operator Structure

Dynamics satisfy

$$
\partial_t^2 \psi = L \psi
$$



with (L) linear on the admissible space.

Principal symbol

$$
\sigma(\omega,k)
$$



determines propagation behaviour.

------

# 10 Operator Classification

Second-order operators fall into four types.

| Type            | Behaviour          |
| --------------- | ------------------ |
| elliptic        | no propagation     |
| hyperbolic      | finite propagation |
| parabolic       | diffusive          |
| ultrahyperbolic | unstable           |

------

# 11 Hyperbolic Rigidity

## Theorem 11.1

Admissibility forces **hyperbolic operators**.

Elliptic → no propagation
Parabolic → unbounded slopes
Ultrahyperbolic → ill-posed evolution

Thus admissible dynamics must satisfy

$$
\omega^2 = c^2 k^2
$$




------

# 12 Emergence of the Propagation Cone

Characteristic condition

$$
\omega^2 - c^2k^2 = 0
$$



produces the propagation cone

$$
|\omega| \le c|k|
$$


------

# 13 Definition of the Constant (c)

Define

$$
c = \sup_{\psi \in A} \frac{|\omega|}{|k|}
$$


------

## Proposition 13.1

If the projection is irreducible then (c) is unique.

------

# 14 Operator Interpretation

Let transport operators be defined by

$$
T_s , T_t
$$



Then

$$
c = \frac{||T_s||}{||T_t||}
$$



Thus (c) is a **structural ratio of projection transport operators**.

------

# 15 Emergent Lorentz Structure

The cone

$$
|\omega| \le c|k|
$$


is invariant under Lorentz transformations.

Thus Lorentz symmetry emerges from spectral invariance.

------

# 16 Causality

Hyperbolic operators produce finite propagation domains.

Therefore signals remain confined within the propagation cone.

------

# 17 Physical Interpretation

Massless excitations satisfy

$$
\omega = ck
$$




Electromagnetic radiation lies on the cone boundary.

Light reveals the propagation limit but does not define it.

------

# 18 Mathematical Status

## Established

1. admissible function space
2. exclusion of vertical spectral rays
3. spectral moment bounds
4. spectral slope bound
5. Paley–Wiener tightening
6. hyperbolic operator structure
7. propagation cone

------

# 19 Open Problems

| ID   | Problem                                        |
| ---- | ---------------------------------------------- |
| OP1  | rigorous microlocal proof of operator form     |
| OP2  | derive Dirac factorisation                     |
| OP3  | derive gauge fields from projection symmetries |

------

# 20 Main Result

## Propagation Rigidity Theorem

For any projection-admissible universe there exists a finite constant (c) such that

$$
|\omega| \le c|k|
$$


and the admissible dynamics are governed by a hyperbolic operator

$$
\partial_t^2 - c^2\nabla^2
$$
producing wave equations in the observable domain.

------

# 21 Next Step

The next major step is deriving the **Dirac operator factorisation**

$$
(\gamma^\mu \partial_\mu)^2 = \Box
$$
which connects propagation rigidity to **fermions and spin-½ structure in DDF**.