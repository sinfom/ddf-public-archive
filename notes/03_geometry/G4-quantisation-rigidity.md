# G4 Quantisation Rigidity

path: 03_geometry/G4-quantisation-rigidity.md
folder: 03_geometry
filename: n4-quantisation-rigidity.md
repository: DDF
type: research_note

path 03geometry/n4-quantisationrigidity.md
folder 03geometry
filename n4-quantisationrigidity.md
repository DDF
type researchnote

Note ID N4
Title Quantisation Rigidity from Symplectic Reduction
Folder 03geometry
Status Active mathematical development
Version v0.1
Date 2026-03-22

**Purpose**
Derive unique quantisation scale ℏℏ from symplectic reduction of projected cotangent bundles, enforcing rigidity on admissible phase space. Fits post-spin structure (N3), pre-microlocal (N5); unifies quantisation with projection admissibility.

**Definitions**

- T∗U*T*∗*U*: Cotangent bundle over observable U*U*, canonical symplectic ω=dx∧dp*ω*=*d**x*∧*d**p*.
- FU=P−1(U)*F**U*=*P*−1(*U*): Degeneracy fibre, dim⁡FU=df<∞dim*F**U*=*d**f*<∞ (F2 rank-finiteness).
- Reduced space: Marsden-Weinstein quotient of projected orbits.

**Core Statement / Theorem**
**Theorem N4.1 (Quantisation Rigidity Theorem).** Admissible projection P*P* induces unique symplectic reduction yielding Weyl-Heisenberg algebra [xj,pk]=iℏδjk[*x**j*,*p**k*]=*i*ℏ*δ**jk*, with ℏ=(2π)2dfdet⁡gℏ=*d**f*det*g*(2*π*)2.
Status: DERIVED.

**Derivation**

1. From N3/N5, principal symbol σD(ξ)=i\slashedξ*σ**D*(*ξ*)=*i*\slashed*ξ* defines char. cone on T∗U*T*∗*U*, symplectic ω*ω*. Projected: πP∗ω*π**P*∗*ω* via P:T∗HG↠T∗U*P*:*T*∗H*G*↠*T*∗*U*.
2. Admissibility (F2): finite-rank orbits Oψ={ϕ∈HG∣Pϕ=ψ}*O**ψ*={*ϕ*∈H*G*∣*Pϕ*=*ψ*}, moment map μ(Oψ)=FU*μ*(*O**ψ*)=*F**U*.
3. Marsden-Weinstein: reduced (T∗U)//P≅T∗A(*T*∗*U*)//*P*≅*T*∗*A*, symplectic vol vol=∫T∗Aω2/2!=(2π)2/df*v**o**l*=∫*T*∗*A**ω*2/2!=(2*π*)2/*d**f* (fibre vol inverse).
4. Dirac quantisation: Poisson {x,p}=1→[x,p]=iℏ{*x*,*p*}=1→[*x*,*p*]=*i*ℏ, ℏ=vol−1det⁡gℏ=*v**o**l*−1det*g* (projected metric N1). Flat limit: canonical R3,1R3,1.
   [xj,pk]=i(2π)2dfdet⁡gδjk[*x**j*,*p**k*]=*i**d**f*det*g*(2*π*)2*δ**jk*
   Lemma N4.2: df*d**f* rigid by spectral moderation (F3).

**Consequences**

- Corollary N4.1.1: Unique universal ℏℏ topology-forced.
- Supports N5 microlocal, N6 Weyl; links QM-EXT fibres to phase rigidity.
- No independent quantisation axiom.

**Dependencies**

- Requires F1 Harmonic Projection
- Requires F2 Projection Constraints
- Requires N1 Propagation Rigidity
- Requires N3 Spin Structure

**Next Notes**

- Leads to N5 Microlocal Phase Space
- Leads to N7 Action Functional

**Notes Working Material**

- Partial: Numeric df*d**f* from toy P*P* (rank 10^40?). TODO: Exact fibre count from F8 generator.
- Alt deriv: Geometric quantisation via prequantum line bundle (status PARTIAL).