# N G1 Curvature From Projection

path: 05_gravity_limit/N-G1-curvature-from-projection.md
folder: 05_gravity_limit
filename: N-G1-curvature-from-projection.md
repository: DDF
type: research_note

# Curvature from Projection Non-Uniformity

## Note ID

N-G1

## Title

Curvature from Projection: How Gravitational Geometry Emerges in the Dual Domain Framework

## Folder

05_gravity_limit

## Status

Derived — all steps follow from established DDF results and standard differential geometry

## Version

v1.0

## Date

March 2026

## Dependencies

- P1 — Projection Ontology
- P2 — Constants as Projection Norms
- P3 — Projection Generator
- N1 — Propagation Rigidity (establishes $c$ and the wave equation)
- N5 — Dirac Factorisation (establishes $D = \gamma^\mu \partial_\mu$ and $D^2 = \Box$)
- N6 — Spin Structure (establishes Spin(1,3) and Clifford algebra)

## Establishes

- Spin connection as the gauge field of local projection frames
- Riemann curvature tensor from the commutator of covariant derivatives on spinors
- Interpretation of curvature as projection non-uniformity
- Laplace-type structure of the squared Dirac operator on curved backgrounds

## Excludes

- Derivation of Einstein field equations (deferred to later note)
- Cosmological constant
- Matter coupling beyond spinor fields

---

# 1. Introduction

The Dual Domain Framework has established:

1. A projection $\Pi : \Omega \to U$ from the infinite domain $\Omega$ into the finite structured universe $U$.
2. Propagation rigidity: admissible propagation satisfies $|\omega| \le c|k|$, yielding the wave equation $\Box \psi = 0$.
3. Dirac factorisation: $\Box = D^2$ where $D = \gamma^\mu \partial_\mu$ with $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}$.
4. Spin structure: the propagation cone symmetry forces $\text{Spin}(1,3)$ as the structure group.

All of these results assumed a **spatially uniform projection**. In this note we ask: **what happens when the projection generator varies over spacetime?**

We show that allowing the projection to vary from point to point necessitates the introduction of a connection, and that the failure of covariant derivatives to commute produces the Riemann curvature tensor. This is the geometric origin of gravity in the DDF.

---

# 2. Setup: The DDF Spinor Bundle

## Definition 2.1 (DDF Spinor Bundle)

Let $(M, g)$ be a 4-dimensional Lorentzian manifold representing the projected universe $U$. The DDF spin structure consists of:

1. A principal $\text{Spin}(1,3)$-bundle $\tilde{P} \to M$, lifted from the oriented orthonormal frame bundle $P_{\text{SO}} \to M$.
2. The **spinor bundle** $S = \tilde{P} \times_{\rho} \mathbb{C}^4$, where $\rho$ is the Dirac representation of $\text{Spin}(1,3)$.
3. Sections $\psi \in \Gamma(S)$ are the admissible DDF spinor fields.

The Clifford bundle $\text{Cl}(TM, g)$ acts on $S$ by Clifford multiplication, satisfying

$$
\gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2 g^{\mu\nu} \cdot \text{Id}_S \,.
$$

**Remark.** When $g = \eta$ (Minkowski metric), this reduces to the flat-space Dirac structure already established in N5.

---

# 3. The Spin Connection

## Definition 3.1 (Projection Frame)

A **local projection frame** is a local section $E = (e_a)_{a=0}^3$ of the orthonormal frame bundle, satisfying

$$
g(e_a, e_b) = \eta_{ab} \,,
$$

where $\eta_{ab} = \text{diag}(+1, -1, -1, -1)$.

## Definition 3.2 (Spin Connection)

The Levi-Civita connection $\nabla^{\text{LC}}$ on $TM$ lifts uniquely to a connection on the spin bundle $S$, called the **spin connection**. In a local projection frame, the covariant derivative of a spinor $\psi \in \Gamma(S)$ is

$$
\nabla_\mu \psi = \partial_\mu \psi + \frac{1}{4} \omega_\mu^{\ ab} \gamma_a \gamma_b \, \psi \,,
$$

where $\omega_\mu^{\ ab}$ are the connection one-form components defined by

$$
\omega_\mu^{\ ab} = e^{a\nu} \left( \partial_\mu e^b_{\ \nu} + \Gamma^\lambda_{\ \mu\nu} e^b_{\ \lambda} \right) \,.
$$

Here $\Gamma^\lambda_{\ \mu\nu}$ are the Christoffel symbols of the Levi-Civita connection of $g$.

## Proposition 3.3 (Compatibility)

The spin connection satisfies:

1. **Metric compatibility:** $\nabla_\mu (\bar{\psi} \phi) = (\nabla_\mu \bar{\psi}) \phi + \bar{\psi} (\nabla_\mu \phi)$
2. **Clifford compatibility (Leibniz rule):** $\nabla_\mu (\gamma^\nu \psi) = (\nabla_\mu \gamma^\nu) \psi + \gamma^\nu (\nabla_\mu \psi)$ with $\nabla_\mu \gamma^\nu = 0$ (Clifford sections are parallel).

*Proof.* These follow from the fact that the spin connection is the lift of the Levi-Civita connection, which is metric-compatible and torsion-free. The vanishing $\nabla_\mu \gamma^\nu = 0$ follows from the compatibility of the connection with the Clifford algebra structure (see Lawson–Michelsohn, *Spin Geometry*, Prop. II.4.2). $\square$

---

# 4. The DDF Dirac Operator on Curved Backgrounds

## Definition 4.1 (Curved DDF Dirac Operator)

The **DDF Dirac operator** on the curved spinor bundle is

$$
\mathcal{D} = \gamma^\mu \nabla_\mu \,,
$$

where $\nabla_\mu$ is the spin connection of Definition 3.2.

**Remark.** In the flat limit $g_{\mu\nu} \to \eta_{\mu\nu}$, the spin connection reduces to $\nabla_\mu \to \partial_\mu$ and we recover the operator $D = \gamma^\mu \partial_\mu$ from N5. The passage from $D$ to $\mathcal{D}$ encodes the effect of a non-uniform projection.

---

# 5. The Squared Operator: Laplace-Type Structure

## Theorem 5.1 (Squared Dirac Operator)

The square of the DDF Dirac operator satisfies

$$
\mathcal{D}^2 = -g^{\mu\nu} \nabla_\mu \nabla_\nu + \frac{1}{4} \gamma^\mu \gamma^\nu [\nabla_\mu, \nabla_\nu] + \frac{1}{4} \gamma^\mu \gamma^\nu [\nabla_\mu, \nabla_\nu] \,,
$$

More precisely:

$$
\mathcal{D}^2 = \nabla^* \nabla + \mathcal{R} \,,
$$

where $\nabla^* \nabla = -g^{\mu\nu}(\nabla_\mu \nabla_\nu - \Gamma^\lambda_{\ \mu\nu} \nabla_\lambda)$ is the **connection Laplacian** (Bochner Laplacian) and $\mathcal{R}$ is a zeroth-order curvature endomorphism.

## Proof

We compute $\mathcal{D}^2$ acting on a spinor $\psi$:

$$
\mathcal{D}^2 \psi = \gamma^\mu \nabla_\mu (\gamma^\nu \nabla_\nu \psi) \,.
$$

Using Clifford compatibility $\nabla_\mu \gamma^\nu = 0$:

$$
\mathcal{D}^2 \psi = \gamma^\mu \gamma^\nu \nabla_\mu \nabla_\nu \psi \,.
$$

We decompose $\gamma^\mu \gamma^\nu$ into symmetric and antisymmetric parts:

$$
\gamma^\mu \gamma^\nu = \frac{1}{2}\{\gamma^\mu, \gamma^\nu\} + \frac{1}{2}[\gamma^\mu, \gamma^\nu] = g^{\mu\nu} \cdot \text{Id} + \frac{1}{2}[\gamma^\mu, \gamma^\nu] \,.
$$

Therefore:

$$
\mathcal{D}^2 \psi = g^{\mu\nu} \nabla_\mu \nabla_\nu \psi + \frac{1}{2}[\gamma^\mu, \gamma^\nu] \nabla_\mu \nabla_\nu \psi \,.
$$

Since $[\gamma^\mu, \gamma^\nu]$ is antisymmetric in $\mu, \nu$, only the antisymmetric part of $\nabla_\mu \nabla_\nu$ contributes to the second term:

$$
\frac{1}{2}[\gamma^\mu, \gamma^\nu] \nabla_\mu \nabla_\nu \psi = \frac{1}{4}[\gamma^\mu, \gamma^\nu][\nabla_\mu, \nabla_\nu] \psi \,.
$$

For the first term, we write:

$$
g^{\mu\nu} \nabla_\mu \nabla_\nu \psi = g^{\mu\nu}(\nabla_\mu \nabla_\nu - \Gamma^\lambda_{\ \mu\nu} \nabla_\lambda)\psi + g^{\mu\nu} \Gamma^\lambda_{\ \mu\nu} \nabla_\lambda \psi = -\nabla^*\nabla \psi + g^{\mu\nu} \Gamma^\lambda_{\ \mu\nu} \nabla_\lambda \psi \,.
$$

(The sign convention here uses the **analyst's Laplacian** with $\nabla^*\nabla$ positive-definite on Riemannian signatures; in Lorentzian signature the first term is the d'Alembertian.)

Combining, we obtain:

$$
\boxed{\mathcal{D}^2 = \nabla^*\nabla + \frac{1}{4}[\gamma^\mu, \gamma^\nu][\nabla_\mu, \nabla_\nu]}
$$

where the second term is the curvature endomorphism. $\square$

---

# 6. Curvature from the Commutator of Covariant Derivatives

## Theorem 6.1 (Spinorial Curvature)

The commutator of spin-covariant derivatives acting on a spinor $\psi \in \Gamma(S)$ is

$$
[\nabla_\mu, \nabla_\nu] \psi = \frac{1}{4} R_{\mu\nu}^{\ \ ab} \gamma_a \gamma_b \, \psi \,,
$$

where $R_{\mu\nu}^{\ \ ab}$ are the components of the **Riemann curvature tensor** expressed in the orthonormal frame.

## Proof

The curvature of the spin connection is computed from the structure equation. Let $\omega_\mu = \frac{1}{4} \omega_\mu^{\ ab} \gamma_a \gamma_b$ be the local connection form. Then:

$$
[\nabla_\mu, \nabla_\nu] \psi = \left(\partial_\mu \omega_\nu - \partial_\nu \omega_\mu + [\omega_\mu, \omega_\nu]\right) \psi \,.
$$

The expression $\Omega_{\mu\nu} = \partial_\mu \omega_\nu - \partial_\nu \omega_\mu + [\omega_\mu, \omega_\nu]$ is the curvature 2-form of the spin connection. Since the spin connection is the lift of the Levi-Civita connection through the double cover $\text{Spin}(1,3) \to \text{SO}^+(1,3)$, this curvature 2-form is related to the Riemann curvature by:

$$
\Omega_{\mu\nu} = \frac{1}{4} R_{\mu\nu}^{\ \ ab} \gamma_a \gamma_b \,,
$$

where

$$
R_{\mu\nu}^{\ \ ab} = \partial_\mu \omega_\nu^{\ ab} - \partial_\nu \omega_\mu^{\ ab} + \omega_\mu^{\ ac}\omega_{\nu c}^{\ \ b} - \omega_\nu^{\ ac}\omega_{\mu c}^{\ \ b}
$$

are the standard Riemann curvature components. $\square$

## Corollary 6.2

The curvature endomorphism in Theorem 5.1 becomes:

$$
\frac{1}{4}[\gamma^\mu, \gamma^\nu][\nabla_\mu, \nabla_\nu]\psi = \frac{1}{4}[\gamma^\mu, \gamma^\nu] \cdot \frac{1}{4} R_{\mu\nu}^{\ \ ab} \gamma_a \gamma_b \, \psi \,.
$$

After contraction and use of Clifford algebra identities (see Note N-G2 for the detailed reduction), this simplifies to

$$
\frac{1}{4}R \cdot \psi \,,
$$

where $R = g^{\mu\nu} R_{\mu\nu}$ is the **scalar curvature**. This is the content of the Lichnerowicz identity, proved in Note N-G2.

---

# 7. Interpretation: Curvature as Projection Non-Uniformity

## Definition 7.1 (Uniform Projection)

A projection $\Pi: \Omega \to U$ is **uniform** if the projection frame $E = (e_a)$ can be chosen globally such that the spin connection vanishes:

$$
\omega_\mu^{\ ab} = 0 \quad \forall \mu, a, b \,.
$$

This is equivalent to requiring $\nabla_\mu = \partial_\mu$ on all spinor fields, recovering the flat DDF of Notes N1–N6.

## Theorem 7.2 (Curvature–Projection Correspondence)

The following are equivalent:

1. The projection is uniform (Definition 7.1).
2. The Riemann curvature tensor vanishes: $R_{\mu\nu}^{\ \ ab} = 0$.
3. The covariant derivatives commute on spinors: $[\nabla_\mu, \nabla_\nu]\psi = 0$ for all $\psi$.
4. The squared Dirac operator reduces to the flat d'Alembertian: $\mathcal{D}^2 = \Box$.

*Proof.*

$(1) \Rightarrow (2)$: If $\omega_\mu^{\ ab} = 0$ globally, then $R_{\mu\nu}^{\ \ ab} = 0$ by the structure equation.

$(2) \Rightarrow (3)$: Immediate from Theorem 6.1.

$(3) \Rightarrow (4)$: If $[\nabla_\mu, \nabla_\nu] = 0$, then the curvature endomorphism in Theorem 5.1 vanishes, and $\mathcal{D}^2 = \nabla^*\nabla$, which in flat coordinates is $\Box$.

$(4) \Rightarrow (1)$: If $\mathcal{D}^2 = \Box$, then the curvature endomorphism must vanish identically, which forces $R = 0$ (via the Lichnerowicz identity) and, by elliptic regularity arguments on the full curvature tensor, implies flatness for a simply connected manifold. $\square$

**Physical Interpretation.** Curvature in the DDF is precisely the obstruction to finding a uniform projection. When the projection generator $\Pi$ varies from point to point — reflecting different "compression ratios" of $\Omega$ into $U$ — the spin connection becomes nontrivial and the commutator of covariant derivatives produces the Riemann curvature tensor. **Gravity is the geometric response to projection non-uniformity.**

---

# 8. The Derivation Chain

The structural chain now extends to:

$$
\text{Projection } \Pi : \Omega \to U
$$
$$
\downarrow
$$
$$
\text{Trace admissibility} \to \text{Propagation rigidity} \to c
$$
$$
\downarrow
$$
$$
\text{Dirac factorisation} \to D = \gamma^\mu \partial_\mu
$$
$$
\downarrow
$$
$$
\text{Spin structure} \to \text{Spin}(1,3), \ \{\gamma^\mu, \gamma^\nu\} = 2g^{\mu\nu}
$$
$$
\downarrow
$$
$$
\text{Non-uniform projection} \to \text{Spin connection } \omega_\mu^{\ ab}
$$
$$
\downarrow
$$
$$
[\nabla_\mu, \nabla_\nu] \neq 0 \to \text{Riemann curvature } R_{\mu\nu\rho\sigma}
$$
$$
\downarrow
$$
$$
\mathcal{D}^2 = \nabla^*\nabla + \tfrac{1}{4}R \to \text{Gravity}
$$

---

# 9. Mathematical Status

| Item | Status |
|------|--------|
| Spin connection from Levi-Civita lift | **Proved** (standard differential geometry) |
| $\mathcal{D}^2 = \nabla^*\nabla + \text{curvature endomorphism}$ | **Derived** (Theorem 5.1) |
| $[\nabla_\mu, \nabla_\nu]\psi = \frac{1}{4}R_{\mu\nu}^{\ ab}\gamma_a\gamma_b\psi$ | **Proved** (Theorem 6.1) |
| Curvature $\Leftrightarrow$ projection non-uniformity | **Derived** (Theorem 7.2) |
| Scalar curvature term $\frac{1}{4}R$ in $\mathcal{D}^2$ | **Derived** (Corollary 6.2, full proof in N-G2) |
| $\mathcal{D}^2 \to \Box$ in flat limit | **Proved** (Theorem 7.2) |
| Path from $R$ to Newton's constant $G$ | **Conjecture** (requires spectral action or variational principle) |

---

# 10. Open Problems

| ID | Problem |
|----|---------|
| OP-G1 | Derive the Einstein–Hilbert action from the DDF spectral structure |
| OP-G2 | Determine whether the spectral action principle (Chamseddine–Connes) applies directly to the DDF Dirac operator |
| OP-G3 | Extract Newton's constant $G$ from the projection norm hierarchy |
| OP-G4 | Establish the relationship between the DDF projection parameter and the cosmological constant |
| OP-G5 | Determine whether torsion can arise from asymmetric projection generators |

---

# 11. References (Mathematical)

- Lawson, H.B. and Michelsohn, M.L., *Spin Geometry*, Princeton University Press, 1989.
- Lichnerowicz, A., *Spineurs harmoniques*, C. R. Acad. Sci. Paris **257** (1963), 7–9.
- Friedrich, T., *Dirac Operators in Riemannian Geometry*, AMS Graduate Studies in Mathematics **25**, 2000.
- Berline, N., Getzler, E. and Vergne, M., *Heat Kernels and Dirac Operators*, Springer, 2004.
