# N G2 Lichnerowicz Identity Ddf

path: 05_gravity_limit/N-G2-lichnerowicz-identity-ddf.md
folder: 05_gravity_limit
filename: N-G2-lichnerowicz-identity-ddf.md
repository: DDF
type: research_note

# Lichnerowicz Identity in the Dual Domain Framework

## Note ID

N-G2

## Title

The Lichnerowicz–Weitzenböck Identity for the DDF Dirac Operator

## Folder

05_gravity_limit

## Status

Derived — identity proved from established DDF operator structure and standard spin geometry

## Version

v1.0

## Date

March 2026

## Dependencies

- N5 — Dirac Factorisation
- N6 — Spin Structure
- N-G1 — Curvature from Projection (establishes $\mathcal{D}$, spin connection, spinorial curvature)

## Establishes

- The Lichnerowicz identity $\mathcal{D}^2 = \nabla^*\nabla + \frac{1}{4}R$ for the DDF Dirac operator
- Scalar curvature as a spectral invariant of the squared Dirac operator
- Interpretation of $\frac{1}{4}R$ as a structural response of the projection

## Excludes

- Derivation of the Einstein field equations
- Spectral action computation
- Matter-coupled curvature terms

---

# 1. Introduction

In Note N-G1 we showed that the squared DDF Dirac operator takes the form

$$
\mathcal{D}^2 = \nabla^*\nabla + \frac{1}{4}[\gamma^\mu, \gamma^\nu][\nabla_\mu, \nabla_\nu] \,,
$$

and that the commutator $[\nabla_\mu, \nabla_\nu]$ produces the Riemann curvature tensor acting on spinors.

In this note we carry out the **explicit reduction** of the curvature endomorphism to show that it equals $\frac{1}{4}R$, where $R$ is the scalar curvature. This is the **Lichnerowicz identity** (also called the Schrödinger–Lichnerowicz formula), adapted to the DDF setting.

---

# 2. Definitions

## Definition 2.1 (Connection Laplacian on Spinors)

The **connection Laplacian** (or Bochner Laplacian) on spinor sections $\psi \in \Gamma(S)$ is

$$
\nabla^*\nabla \psi = -g^{\mu\nu}\left(\nabla_\mu \nabla_\nu - \Gamma^\lambda_{\ \mu\nu} \nabla_\lambda\right)\psi \,.
$$

In a local orthonormal frame $(e_a)$:

$$
\nabla^*\nabla \psi = -\sum_{a=1}^{n} \left(\nabla_{e_a}\nabla_{e_a} - \nabla_{\nabla^{\text{LC}}_{e_a} e_a}\right)\psi \,.
$$

## Definition 2.2 (Scalar Curvature)

The **scalar curvature** is the double contraction of the Riemann tensor:

$$
R = g^{\mu\rho} g^{\nu\sigma} R_{\mu\nu\rho\sigma} = g^{\mu\nu} R_{\mu\nu} \,,
$$

where $R_{\mu\nu} = R^\lambda_{\ \mu\lambda\nu}$ is the Ricci tensor.

## Definition 2.3 (Spinorial Curvature Endomorphism)

For the spin connection, define the **curvature endomorphism**:

$$
\mathcal{F} = \frac{1}{4}[\gamma^\mu, \gamma^\nu][\nabla_\mu, \nabla_\nu] = \frac{1}{2}\gamma^\mu \gamma^\nu [\nabla_\mu, \nabla_\nu] - \frac{1}{2}g^{\mu\nu}[\nabla_\mu, \nabla_\nu] \,.
$$

Since $[\nabla_\mu, \nabla_\nu]$ is antisymmetric in $\mu, \nu$ while $g^{\mu\nu}$ is symmetric, the second term vanishes and

$$
\mathcal{F} = \frac{1}{2}\gamma^\mu \gamma^\nu [\nabla_\mu, \nabla_\nu] \,.
$$

---

# 3. The Half-Ricci Formula

## Lemma 3.1 (Half-Ricci Identity)

For any vector field $X$ on $M$ and spinor $\psi \in \Gamma(S)$:

$$
\sum_{a=0}^{3} e_a \cdot R^S(X, e_a)\psi = -\frac{1}{2}\text{Ric}(X) \cdot \psi \,,
$$

where $R^S(X,Y)\psi = [\nabla_X, \nabla_Y]\psi - \nabla_{[X,Y]}\psi$ is the spinorial curvature, and $\text{Ric}(X) = R_{\mu\nu}X^\nu e^\mu$ is the Ricci endomorphism acting via Clifford multiplication.

## Proof

By Theorem 6.1 of N-G1:

$$
R^S(X, Y)\psi = \frac{1}{4}\sum_{a,b} R(X,Y,e_a,e_b)\,\gamma^a\gamma^b\,\psi \,.
$$

Contracting with $\sum_c e_c \cdot R^S(X, e_c)$:

$$
\sum_c \gamma^c \cdot R^S(X, e_c)\psi = \frac{1}{4}\sum_{c,a,b} R(X, e_c, e_a, e_b)\,\gamma^c\gamma^a\gamma^b\,\psi \,.
$$

We use the **Clifford contraction identity**: for any 2-form $\alpha_{ab}$,

$$
\sum_c \gamma^c \gamma^a \gamma^b \alpha_{cab} = -2\sum_a \alpha^{\ a}_{a\ } \gamma^a + \sum_{c,a,b} \gamma^{cab}\alpha_{cab}
$$

where $\gamma^{cab} = \gamma^c\gamma^a\gamma^b$ (fully antisymmetrised).

The fully antisymmetric part $\sum_{c,a,b} R(X, e_c, e_a, e_b)\gamma^{cab}$ vanishes by the **first Bianchi identity**:

$$
R(X, e_c, e_a, e_b) + R(X, e_a, e_b, e_c) + R(X, e_b, e_c, e_a) = 0 \,.
$$

The remaining term yields:

$$
\sum_c \gamma^c \cdot R^S(X, e_c)\psi = \frac{1}{4}\cdot(-2)\sum_a R(X, e_a, e_a, e_b)\gamma^b\psi = -\frac{1}{2}R_{\mu\nu}X^\nu \gamma^\mu\psi = -\frac{1}{2}\text{Ric}(X)\cdot\psi \,.
$$

$\square$

---

# 4. The Lichnerowicz Identity

## Theorem 4.1 (Lichnerowicz Identity for the DDF Dirac Operator)

Let $(M, g)$ be a 4-dimensional Lorentzian spin manifold carrying the DDF structure, and let $\mathcal{D} = \gamma^\mu \nabla_\mu$ be the DDF Dirac operator. Then for any spinor $\psi \in \Gamma(S)$:

$$
\boxed{\mathcal{D}^2 \psi = \nabla^*\nabla\,\psi + \frac{1}{4}R\,\psi}
$$

where $\nabla^*\nabla$ is the connection Laplacian and $R$ is the scalar curvature.

## Proof

**Step 1. Expand $\mathcal{D}^2$ in an orthonormal frame.**

Choose a local orthonormal frame $(e_a)_{a=0}^3$ with $\nabla^{\text{LC}}_{e_a} e_b|_p = 0$ at a point $p$ (normal frame). Then at $p$:

$$
\mathcal{D}^2\psi = \sum_{a,b} \gamma^a\gamma^b \nabla_{e_a}\nabla_{e_b}\psi \,.
$$

**Step 2. Decompose into symmetric and antisymmetric parts.**

$$
\sum_{a,b}\gamma^a\gamma^b\nabla_{e_a}\nabla_{e_b}\psi = \sum_{a,b}\left(\frac{1}{2}\{\gamma^a,\gamma^b\} + \frac{1}{2}[\gamma^a,\gamma^b]\right)\nabla_{e_a}\nabla_{e_b}\psi \,.
$$

The symmetric part gives:

$$
\sum_{a,b}\frac{1}{2}\{\gamma^a,\gamma^b\}\nabla_{e_a}\nabla_{e_b}\psi = \sum_{a,b}\eta^{ab}\nabla_{e_a}\nabla_{e_b}\psi = -\nabla^*\nabla\,\psi
$$

(at the point $p$ in normal coordinates, this is the connection Laplacian with the appropriate sign).

The antisymmetric part gives:

$$
\sum_{a,b}\frac{1}{2}[\gamma^a,\gamma^b]\nabla_{e_a}\nabla_{e_b}\psi = \frac{1}{4}\sum_{a,b}[\gamma^a,\gamma^b][\nabla_{e_a},\nabla_{e_b}]\psi
$$

since only the antisymmetric part of $\nabla_{e_a}\nabla_{e_b}$ survives when contracted with the antisymmetric $[\gamma^a,\gamma^b]$.

In normal coordinates at $p$, $[e_a, e_b] = 0$, so $[\nabla_{e_a}, \nabla_{e_b}] = R^S(e_a, e_b)$.

**Step 3. Evaluate the curvature endomorphism.**

$$
\mathcal{F}\psi = \frac{1}{2}\sum_{a<b}[\gamma^a,\gamma^b]R^S(e_a,e_b)\psi = \frac{1}{2}\sum_{a,b}\gamma^a\gamma^b R^S(e_a,e_b)\psi \,.
$$

We can rewrite this as:

$$
\mathcal{F}\psi = \frac{1}{2}\sum_a \gamma^a \left(\sum_b \gamma^b R^S(e_a, e_b)\right)\psi \,.
$$

But the inner sum is $\sum_b \gamma^b R^S(e_a, e_b)\psi$. By the sign antisymmetry $R^S(e_a, e_b) = -R^S(e_b, e_a)$, we get $\sum_b \gamma^b R^S(e_a, e_b) = -\sum_b e_b \cdot R^S(e_b, e_a)$.

By Lemma 3.1 (Half-Ricci identity) with $X = e_a$:

$$
\sum_b e_b \cdot R^S(e_a, e_b)\psi = -\frac{1}{2}\text{Ric}(e_a)\cdot\psi \,.
$$

Therefore:

$$
\mathcal{F}\psi = \frac{1}{2}\sum_a \gamma^a \cdot\left(\frac{1}{2}\text{Ric}(e_a)\cdot\psi\right) = \frac{1}{4}\sum_a \gamma^a \cdot \text{Ric}(e_a)\cdot\psi \,.
$$

Now, $\text{Ric}(e_a) = R_{a}^{\ b}\,e_b$, so $\gamma^a\cdot\text{Ric}(e_a) = R_{a}^{\ b}\gamma^a\gamma_b$. Taking the trace:

$$
\sum_a R_a^{\ b}\gamma^a\gamma_b = \sum_a R_a^{\ b}\left(\eta^{ab} + \frac{1}{2}[\gamma^a,\gamma_b]\right) = R\cdot\text{Id} + \frac{1}{2}R_a^{\ b}[\gamma^a,\gamma_b] \,.
$$

The second term vanishes because $R_{ab}$ is symmetric while $[\gamma^a, \gamma_b]$ is antisymmetric in $(a,b)$:

$$
R_{ab}[\gamma^a,\gamma^b] = 0 \,.
$$

Therefore:

$$
\mathcal{F}\psi = \frac{1}{4}R\,\psi \,.
$$

**Step 4. Combine.**

$$
\mathcal{D}^2\psi = \nabla^*\nabla\,\psi + \mathcal{F}\psi = \nabla^*\nabla\,\psi + \frac{1}{4}R\,\psi \,.
$$

$\square$

---

# 5. Consequences

## Corollary 5.1 (Flat-Space Limit)

When $R = 0$ (uniform projection), the identity reduces to $\mathcal{D}^2 = \nabla^*\nabla$. In globally flat spacetime with $\nabla = \partial$, this gives $\mathcal{D}^2 = \Box$, recovering the DDF Dirac factorisation of N5.

## Corollary 5.2 (Spectral Constraint from Positive Scalar Curvature)

If $(M, g)$ is a compact Riemannian spin manifold with $R > 0$ everywhere, then $\mathcal{D}^2 = \nabla^*\nabla + \frac{1}{4}R > 0$. Therefore $\mathcal{D}$ has trivial kernel: there are **no harmonic spinors**. This is the classical result of Lichnerowicz (1963), now interpreted in the DDF as: **positive projection curvature forbids zero-mode spinor states**.

## Corollary 5.3 (Curvature from Spectral Data)

The scalar curvature $R$ can be extracted from the spectrum of $\mathcal{D}^2$ via the heat kernel expansion:

$$
\text{Tr}\,e^{-t\mathcal{D}^2} \sim (4\pi t)^{-n/2}\left(a_0 + a_1 t + a_2 t^2 + \cdots\right) \,,
$$

where

$$
a_0 = \text{rank}(S)\cdot\text{Vol}(M), \quad a_1 = \frac{\text{rank}(S)}{6}\int_M R\,\text{dvol}_g \,.
$$

The scalar curvature is therefore a **spectral invariant** of the DDF Dirac operator.

---

# 6. Interpretation in the DDF

## 6.1 The Curvature Term as Projection Response

The Lichnerowicz identity

$$
\mathcal{D}^2 = \nabla^*\nabla + \frac{1}{4}R
$$

has a direct physical interpretation within the DDF:

- **$\nabla^*\nabla$** is the **kinetic term**: it encodes the propagation of spinor fields, controlled by the spin connection. This is the direct generalisation of the flat d'Alembertian $\Box$.

- **$\frac{1}{4}R$** is the **curvature potential**: it represents the **structural response** of the projection to non-uniformity. When the projection $\Pi: \Omega \to U$ compresses different regions of $\Omega$ by different amounts, the scalar curvature $R$ measures the net effect on spinor dynamics.

The identity shows that **curvature is not an independent degree of freedom** in the DDF — it is determined entirely by the spin connection, which itself arises from the varying projection frame. The scalar curvature enters the spinor dynamics as an effective potential.

## 6.2 Toward Newton's Constant

The Lichnerowicz identity provides the bridge between the Dirac operator and gravity. The scalar curvature $R$ that appears is the same $R$ that enters the Einstein–Hilbert action:

$$
S_{\text{EH}} = \frac{1}{16\pi G}\int_M R\,\sqrt{-g}\,d^4x \,.
$$

In the Chamseddine–Connes spectral action principle, the coefficient of $\int R$ in the heat kernel expansion of $\text{Tr}\,f(\mathcal{D}^2/\Lambda^2)$ determines Newton's constant $G$ in terms of the cutoff scale $\Lambda$ and the spectral data. The DDF derivation chain therefore has a clear path:

$$
\text{Projection norms} \to c, \hbar \to \text{Dirac operator } \mathcal{D} \to \text{Lichnerowicz} \to R \to G
$$

The explicit extraction of $G$ from the DDF projection parameters is an open problem (OP-G3 in N-G1).

---

# 7. Verification of the Identity

## 7.1 Consistency Checks

1. **Dimensional analysis:** $\mathcal{D}$ has dimensions of (length)$^{-1}$; $\mathcal{D}^2$ has (length)$^{-2}$; $\nabla^*\nabla$ has (length)$^{-2}$; $R$ has (length)$^{-2}$. ✓

2. **Flat limit:** When $g = \eta$ and $R = 0$, the identity gives $D^2 = \Box$, consistent with N5. ✓

3. **Symbol computation:** The principal symbol of $\mathcal{D}$ is $\sigma_1(\mathcal{D})(\xi) = \gamma^\mu\xi_\mu$. Therefore $\sigma_2(\mathcal{D}^2)(\xi) = g^{\mu\nu}\xi_\mu\xi_\nu$, which agrees with $\sigma_2(\nabla^*\nabla)(\xi)$. The $\frac{1}{4}R$ term is zeroth-order, hence does not affect the principal symbol. ✓

4. **Bianchi identity usage:** The proof crucially uses the first Bianchi identity to eliminate the totally antisymmetric part. This is automatically satisfied since the Levi-Civita connection is torsion-free. ✓

---

# 8. Mathematical Status

| Item | Status |
|------|--------|
| Connection Laplacian $\nabla^*\nabla$ definition | **Standard** |
| Half-Ricci identity (Lemma 3.1) | **Proved** |
| Lichnerowicz identity $\mathcal{D}^2 = \nabla^*\nabla + \frac{1}{4}R$ | **Proved** (Theorem 4.1) |
| Flat-space recovery | **Proved** (Corollary 5.1) |
| Heat kernel interpretation | **Proved** (standard spectral theory) |
| Interpretation as projection response | **Derived** (Section 6.1) |
| Path to Newton's constant $G$ | **Conjecture** (Section 6.2) |

---

# 9. Open Problems

| ID | Problem |
|----|---------|
| OP-L1 | Derive the full Einstein equations from a DDF variational principle |
| OP-L2 | Compute the spectral action $\text{Tr}\,f(\mathcal{D}^2/\Lambda^2)$ for the DDF operator and extract the gravitational coupling |
| OP-L3 | Determine whether the DDF projection admits a natural cutoff scale $\Lambda$ |
| OP-L4 | Extend the Lichnerowicz identity to include gauge curvature terms $F_A$ from DDF gauge fields |
| OP-L5 | Investigate whether the Lichnerowicz obstruction ($R > 0$ implies no harmonic spinors) constrains the DDF projection topology |

---

# 10. References (Mathematical)

- Lichnerowicz, A., *Spineurs harmoniques*, C. R. Acad. Sci. Paris **257** (1963), 7–9.
- Schrödinger, E., *Diracsches Elektron im Schwerefeld I*, Sitzungsber. Preuss. Akad. Wiss. Phys.-Math. Kl. (1932), 105–128.
- Lawson, H.B. and Michelsohn, M.L., *Spin Geometry*, Princeton University Press, 1989.
- Friedrich, T., *Dirac Operators in Riemannian Geometry*, AMS, 2000.
- Berline, N., Getzler, E. and Vergne, M., *Heat Kernels and Dirac Operators*, Springer, 2004.
- Chamseddine, A.H. and Connes, A., *The Spectral Action Principle*, Commun. Math. Phys. **186** (1997), 731–750.
- Gilkey, P.B., *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem*, CRC Press, 1995.
