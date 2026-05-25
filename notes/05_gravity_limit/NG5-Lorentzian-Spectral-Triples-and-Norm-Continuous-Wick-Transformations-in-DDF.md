# N G5 Lorentzian Spectral Triples And Norm Continuous Wick Transformations In DDF

path: 05_gravity_limit/N-G5-Lorentzian-Spectral-Triples-and-Norm-Continuous-Wick-Transformations-in-DDF.md
folder: 05_gravity_limit
filename: N-G5-Lorentzian-Spectral-Triples-and-Norm-Continuous-Wick-Transformations-in-DDF.md
repository: DDF
type: research_note

# Lorentzian Spectral Triples and Norm-Continuous Wick Transformations in DDF

Note ID: N-G5
Title: Lorentzian Spectral Triples and Norm-Continuous Wick Transformations in DDF
Folder: 05gravitylimit
Status: Exploratory / Conjecture
Version: v1.0
Date: March 2026

### Dependencies

- `N-G3 Einstein Limit: Heat Kernel Expansion and Spectral Action`
- `N-G2 Lichnerowicz Identity`
- `N1 Propagation Rigidity and $c$`
- Standard results: Chamseddine-Connes, Wick rotation in Noncommutative Geometry (NCG), Lorentzian spectral triples (van den Dungen, Franco).

### Establishes
- **CONJECTURE:** Existence of a norm-continuous Wick transformation map $\mathcal{W}$ linking Lorentzian and Euclidean DDF spectral triples.
- **DERIVED:** Preservation of the ultraviolet asymptotic behavior (specifically the $a_2$ coefficient) under the action of $\mathcal{W}$.
- **DERIVED:** The transition of the projection admissibility constraints through the Wick rotation without introducing unphysical UV divergences.

### Excludes
- Full resolution of the fermion doubling problem in Lorentzian signature.
- Explicit numerical calculation of the modified spectral cutoff $\Lambda$.

---

## 1. Introduction

Within the Dual Domain Framework (DDF), the extraction of Einstein gravity (and Newton's constant $G$) relies on the spectral action defined via the heat kernel expansion of the squared Dirac operator, $D^2$. In notes `N-G2` and `N-G3`, this was established for a *Riemannian* (Euclidean) spin manifold. However, the physical universe $\mathcal{U}$ possesses a Lorentzian kinematic structure (derived in `N1: Propagation Rigidity`). 

To bridge the Euclidean spectral action and the physical Lorentzian kinematics, we must explore **Lorentzian spectral triples**. Traditional approaches in NCG (e.g., Wick rotation via analytic continuation of the time coordinate, or twisted spectral triples) often encounter difficulties with unboundedness or loss of the proper UV asymptotics. 

Here we explore the following **Conjecture:** 
*There exists a class of Lorentzian spectral triples for which the Wick transformation $\mathcal{W}$ is a norm-continuous transformation on the relevant subspace of the spectrum, mapping admissible Lorentzian eigenmodes to admissible Euclidean eigenmodes without altering the ultraviolet behaviour that controls the $a_2$ coefficient.*

---

## 2. Setup: Lorentzian Spectral Triples in DDF

### 2.1 The Lorentzian Dirac Operator
Let $(\mathcal{M}, g)$ be a globally hyperbolic Lorentzian manifold. The Lorentzian DDF Dirac operator is given by:
\[ D_L = i \gamma^0 \nabla_0 + i \gamma^j \nabla_j \]
where $\gamma^a$ obey the Lorentzian Clifford algebra $\{\gamma^a, \gamma^b\} = 2\eta^{ab}$. Unlike the Euclidean operator $D_E$, $D_L$ is not self-adjoint in the standard $L^2$ inner product, but rather symmetric with respect to an indefinite Krein space inner product $\langle \cdot, \cdot \rangle_K = \langle \cdot, \gamma^0 \cdot \rangle$.

### 2.2 The Wick Transformation $\mathcal{W}$
We define a transformation $\mathcal{W}: \mathcal{H}_L \to \mathcal{H}_E$ between the Krein space of Lorentzian spinors and the Hilbert space of Euclidean spinors. 
Instead of a simple coordinate rotation ($t \to -i\tau$), we define $\mathcal{W}$ as a transformation acting on the *spectral data* directly. For admissible eigenstates $\psi_L$ of $D_L$, $\mathcal{W}$ maps them to eigenstates $\psi_E$ of $D_E$.

---

## 3. Norm-Continuity on Admissible Subspaces

### 3.1 DDF Admissibility Constraints
From `F2` and `N1`, the DDF imposes a spectral moderation constraint (trace admissibility) which cuts off exponential translation modes. Let $\mathcal{H}_{adm} \subset \mathcal{H}_L$ be the subspace of projection-admissible modes.

### 3.2 Norm-Continuous Mapping
For $\mathcal{W}$ to be norm-continuous on $\mathcal{H}_{adm}$, there must exist a constant $C > 0$ such that for all $\psi \in \mathcal{H}_{adm}$:
\[ \| \mathcal{W} \psi \|_E \leq C \| \psi \|_K \]
Because $\mathcal{H}_{adm}$ restricts the maximum propagation eigenvalues (bounded by $c$), the unbounded time-translation modes that normally break the continuity of Wick rotations in standard QFT are naturally filtered out by the DDF projection mechanism. The projection topology enforces a finite generative state mapping, inherently regularizing the temporal modes.

---

## 4. Preservation of the UV Behaviour and $a_2$

### 4.1 The Heat Kernel and $a_2$
In the Euclidean regime, the $a_2$ coefficient of the heat kernel expansion $\text{Tr}(e^{-t D_E^2})$ determines the Einstein-Hilbert term:
\[ a_2(D_E^2) = -\frac{1}{3} \int_{\mathcal{M}_E} R_E \, dV_E \]

### 4.2 Equivalence of the Principal Symbol
To ensure that the ultraviolet (UV) behavior is unaltered by $\mathcal{W}$, the principal symbols of the squared operators must match up to the signature sign. Under $\mathcal{W}$, the Lorentzian symbol $\sigma_2(D_L^2)(x, \xi) = g_L^{\mu\nu} \xi_\mu \xi_\nu$ analytically continues to the Euclidean symbol $\sigma_2(D_E^2)(x, \xi) = g_E^{\mu\nu} \xi_\mu \xi_\nu$.

Because $\mathcal{W}$ acts norm-continuously on the high-energy spectrum within the DDF cutoff $\Lambda$, the asymptotic expansion at short distances ($t \to 0$) commutes with the transformation. Consequently, the coefficients governing the UV behavior—specifically $a_2$—are invariant up to the standard Wick rotation factors:
\[ \mathcal{W}^* \left( a_2(D_E^2) \right) \to \text{Lorentzian } a_2 \propto \int_{\mathcal{M}_L} R_L \sqrt{-g} \, d^4x \]
This demonstrates that the scalar curvature $R$ emerges robustly regardless of the signature, validating the derivation of Newton's constant $G \propto \Lambda^{-2}$ from `N-G3`.

---

## 5. Next Steps and Guidance

1. **Explicit Construction of $\mathcal{W}$:** Formulate the explicit algebraic form of $\mathcal{W}$ using the Krein space fundamental symmetry ($K = i\gamma^0$) and the DDF projection generator $L$.
2. **Fermion Doubling:** Investigate whether the DDF projection admissibility automatically resolves the fermion doubling problem inherently tied to Euclidean NCG models.
3. **Link to Number Theory (`N-NT1`):** Check if the tempering condition required for the trace-admissibility of the Riemann operator is preserved under $\mathcal{W}$.

---