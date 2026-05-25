# Note ID

N1b

# Title

Wave Dispersion and Phase Velocity from Propagation Rigidity

# Folder

02_operator_notes

# Status

Active mathematical development

# Version

v0.1

# Date

March 2026

# Purpose

Derive the classical wave relation

$$
v = f \lambda
$$

from the propagation cone established in propagation rigidity, and clarify how the homogeneity of the cone boundary implies a constant phase velocity for massless modes in the Dual-Domain Framework (DDF). This note corrects earlier claims by distinguishing finite propagation, dispersion, and phase velocity rigidity.

---

# Depends On

- N1 — Propagation Rigidity in the Dual-Domain Framework (propagation cone and hyperbolic operator)[file:18]
- P1 — Projection Ontology
- P2 — Constants as Projection Norms[file:11]
- P3 — Projection Generator (L)[file:5][file:19]

---

# Establishes

- Plane-wave analysis inside the DDF propagation cone
- Derivation of the wave operator from the cone
- Derivation of the linear dispersion relation on the cone boundary
- Phase velocity relation \( v_p = \omega/k \)
- Classical identity \( v = f \lambda \) from Fourier relations
- Explanation that constancy of \( f \lambda \) arises from homogeneity of the cone boundary, not from Paley–Wiener excluding dispersion

---

# Excludes

- Any empirical identification of \( c \) with a measured light speed
- Dirac factorisation and spinor structure
- Gauge interactions and quantisation
- Gravitational or curved-background generalisations

---

# 1 Introduction

The Propagation Rigidity note N1 establishes that projection-admissible states in DDF satisfy Paley–Wiener type bounds that confine spectral support to a homogeneous cone

$$
|\omega| \le c |k|
$$

for some finite structural constant \( c \).[file:18]

The present note refines the wave-theoretic consequences of this cone by:

1. deriving the wave operator from the cone,
2. analysing plane waves that saturate the cone boundary,
3. extracting the dispersion relation and phase velocity,
4. and expressing the classical wave identity \( v = f \lambda \) in DDF language.

A key correction to earlier reasoning is that Paley–Wiener bounds enforce a finite propagation cone but do **not** themselves forbid dispersive relations; the constancy of the ratio \( f \lambda \) for massless modes is instead tied to the **homogeneity** of the cone boundary.

---

# 2 Propagation Cone and Hyperbolic Operator

We recall the established structural chain from N1:[file:18]

> admissibility  
> \( \rightarrow \) spectral constraints  
> \( \rightarrow \) slope theorem  
> \( \rightarrow \) Paley–Wiener tightening  
> \( \rightarrow \) operator classification  
> \( \rightarrow \) hyperbolicity  
> \( \rightarrow \) emergence of \( c \)

## 2.1 Propagation Cone

From spectral moderation and Paley–Wiener–Schwartz theory, admissible states have spectral support contained in a homogeneous cone

$$
|\omega| \le c |k|
$$

for some finite \( c > 0 \).[file:18]

We interpret this cone in the \((\omega,k)\) plane as the **propagation cone**, with its boundary

$$
\omega^2 = c^2 k^2
$$

representing the extremal propagation slope allowed by projection admissibility.[file:18]

## 2.2 Hyperbolic Operator

N1 further shows that admissible dynamics are governed by a second-order hyperbolic operator whose principal symbol vanishes precisely on the cone boundary:[file:18]

$$
\sigma(\omega,k) = \omega^2 - c^2 k^2.
$$

In configuration space this corresponds to the wave operator

$$
\partial_t^2 \psi - c^2 \nabla^2 \psi = 0.
$$

This operator is **established** as the effective description of propagation in the massless sector of DDF, independent of any empirical identification of \( c \).[file:18]

---

# 3 Plane Waves and the Dispersion Relation

We now analyse plane-wave solutions of the wave equation and connect them to the cone boundary.

## 3.1 Plane-Wave Ansatz

Consider a plane-wave mode in one spatial dimension

$$
\psi(x,t) = A \exp\big(i(kx - \omega t)\big),
$$

with complex amplitude \( A \), wave number \( k \in \mathbb{R} \), and angular frequency \( \omega \in \mathbb{R} \).

Substituting into the wave equation

$$
\partial_t^2 \psi - c^2 \partial_x^2 \psi = 0
$$

yields

$$
(-\omega^2) \psi - c^2 (-k^2) \psi = 0,
$$

and hence the **dispersion relation**

$$
\omega^2 = c^2 k^2.
$$

This is consistent with the cone boundary condition from N1 and should be understood as the plane-wave saturation of that boundary, not an independent postulate.[file:18]

## 3.2 Homogeneity of the Dispersion Relation

The dispersion relation

$$
\omega^2 = c^2 k^2
$$

is **homogeneous of degree 2** in \((\omega,k)\). Equivalently, the relation

$$
\omega = \pm c k
$$

is homogeneous of degree 1: scaling \( (\omega,k) \mapsto (\lambda \omega, \lambda k) \) preserves the equality. This homogeneity is the spectral reflection of the homogeneous cone \( |\omega| \le c |k| \).[file:18]

The homogeneity property will be crucial in explaining why the phase velocity and the classical ratio \( f \lambda \) are constant for massless modes.

---

# 4 Phase Velocity and Fourier Relations

We now translate from spectral variables \( (\omega,k) \) to the classical frequency and wavelength, and derive the phase velocity relation.

## 4.1 Frequency and Wavelength

For a plane wave \( \psi(x,t) = A e^{i(kx - \omega t)} \), the standard Fourier identifications are:

- temporal frequency

  $$
  f = \frac{\omega}{2\pi},
  $$

- spatial wavelength

  $$
  \lambda = \frac{2\pi}{|k|}.
  $$

These relations are purely Fourier-theoretic and are adopted unchanged inside DDF, interpreted as the coordinate representation of spectral parameters in the observable domain.

## 4.2 Phase Velocity

The **phase velocity** \( v_p \) of a plane wave is defined as the speed at which a fixed phase point \( kx - \omega t = \text{constant} \) propagates. Solving

$$
kx - \omega t = \text{constant}
$$

for \( x(t) \) gives

$$
x(t) = \frac{\omega}{k} t + \text{constant},
$$

so the phase velocity is

$$
v_p = \frac{dx}{dt} = \frac{\omega}{k}.
$$

Using the Fourier relations, we can rewrite this in terms of \( f \) and \( \lambda \). We have

$$
\omega = 2\pi f, \qquad k = \frac{2\pi}{\lambda},
$$

so

$$
v_p = \frac{\omega}{k}
    = \frac{2\pi f}{2\pi / \lambda}
    = f \lambda.
$$

Thus, **for any plane wave**, the phase velocity satisfies the classical identity

$$
v_p = f \lambda.
$$

This is a simple algebraic consequence of the definitions of \( f \), \( \lambda \), and \( v_p \) in terms of \( \omega \) and \( k \).

---

# 5 Constant Phase Velocity from Homogeneous Cone Boundary

We now specialise to modes that lie on the cone boundary and show how homogeneity enforces constant phase velocity.

## 5.1 Linear Dispersion on the Cone Boundary

On the cone boundary, the dispersion relation reduces to

$$
\omega = \pm c k.
$$

Here \( c \) is the structural constant appearing in the cone inequality \( |\omega| \le c |k| \).[file:18]

Substituting into the phase velocity definition yields

$$
v_p = \frac{\omega}{k} = \pm c.
$$

For a chosen time orientation and sign convention, we select the forward-propagating branch \( \omega = c k \), giving

$$
v_p = c.
$$

Thus, **all monochromatic plane waves that lie on the cone boundary propagate with the same phase velocity** \( c \).

## 5.2 Constancy of \( f \lambda \) from Homogeneity

Using \( v_p = f \lambda \) and \( v_p = c \) on the boundary, we obtain

$$
f \lambda = c
$$

for forward-propagating massless modes.

The **constancy** of this product does not arise from Paley–Wiener bounds directly, but from the **homogeneity** of the boundary dispersion relation

$$
\omega = c k.
$$

Homogeneity implies that for any scaling \( (\omega,k) \mapsto (\lambda \omega, \lambda k) \), the ratio

$$
\frac{\omega}{k}
$$

remains invariant and equal to \( c \). Since \( f \propto \omega \) and \( \lambda \propto 1/k \), we have

$$
f \lambda = \frac{\omega}{2\pi} \cdot \frac{2\pi}{|k|}
         = \frac{\omega}{|k|}
         = c
$$

(up to the sign convention for \( k \)). The structural statement is:

> For massless modes saturating the homogeneous cone boundary \( \omega = c k \), the product \( f \lambda \) is **rigidly fixed** to the structural constant \( c \), independent of the particular frequency or wavelength.

This is the DDF reinterpretation of the classical wave relation \( v = f \lambda \): constancy of \( f \lambda \) expresses **spectral homogeneity on the cone boundary**, not an empirical law about a particular physical field.

---

# 6 Logical Chain in Corrected Form

In light of the above derivation, the corrected DDF logical chain is:

1. **Projection admissibility**: defines the admissible state space with polynomial translation bounds and spectral moderation.[file:18]

2. **Spectral moderation**: excludes vertical spectral rays and enforces polynomial spectral tails.[file:18]

3. **Propagation cone**: Paley–Wiener–Schwartz yields a homogeneous cone \( |\omega| \le c |k| \) for the spectral support.[file:18]

4. **Hyperbolic operator**: admissible dynamics correspond to a hyperbolic operator whose symbol vanishes on the cone boundary, giving the wave operator.[file:18]

5. **Homogeneous dispersion relation**: the characteristic equation \( \omega^2 = c^2 k^2 \) is homogeneous, and its first-order form \( \omega = c k \) on the boundary has degree 1.

6. **Constant phase velocity**: homogeneity implies the ratio \( \omega/k \) is constant along the boundary, so the phase velocity \( v_p = \omega/k = c \) is fixed; via Fourier relations this yields \( f \lambda = c \).

---

# 7 Status of Results

- **Established (from N1 and standard Fourier analysis)**  
  - Existence of the homogeneous propagation cone \( |\omega| \le c|k| \).[file:18]  
  - Hyperbolic wave operator \( \partial_t^2 - c^2 \nabla^2 \).[file:18]  
  - Plane-wave dispersion relation \( \omega^2 = c^2 k^2 \) on the cone boundary.  
  - Phase velocity definition \( v_p = \omega/k \).  
  - Fourier relations \( f = \omega/2\pi \), \( \lambda = 2\pi/k \) and \( v_p = f \lambda \).

- **Derived consequences (within this note)**  
  - Constancy of phase velocity \( v_p = c \) for boundary modes.  
  - Constancy of \( f \lambda = c \) for massless boundary modes, as a direct consequence of homogeneity.

- **Conjectural / not addressed here**  
  - Whether all physically relevant massless excitations in DDF must lie exactly on the cone boundary (rather than within the interior) in all regimes.  
  - Detailed microlocal analysis of cone boundary modes beyond the plane-wave approximation.

---

# 8 Next Step

The natural continuation of this note is to analyse how **nonlinear** dispersion relations compatible with the cone (e.g. massive or effective medium corrections) modify phase and group velocities, and how this affects wave packet evolution within the admissible space. This is the subject of the companion note:

> N2b — Dispersion and Wave Packet Behaviour in DDF (Folder: 03_globalisation).

---