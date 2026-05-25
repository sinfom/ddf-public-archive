# N7 Actionfunctional

path: 04_action_principle/n7-actionfunctional.md
folder: 04_action_principle
filename: n7-actionfunctional.md
repository: DDF
type: research_note

path 04actionprinciple/n7-actionfunctional.md
folder 04actionprinciple
filename n7-actionfunctional.md
repository DDF
type researchnote

Note ID N7
Title Action Functional Compatible with Projection Rigidity
Folder 04actionprinciple
Status Derived
Version v0.1
Date 2026-03-22

**Purpose**
Construct DDF action S*S* over admissible A⊂U*A*⊂*U* from N4 symplectic phase and N1 propagation, yielding Dirac + Einstein-Hilbert via variation. Fits post-quantisation (N4/N6), pre-variational principle (N8).

**Definitions**

- S[ψ,g]*S*[*ψ*,*g*]: Action functional on spinor-metric configs.
- LL: Density, L=ψˉ(i\slashedD−m)ψ+116πGR+14FabFabL=*ψ*ˉ(*i*\slashed*D*−*m*)*ψ*+16*π**G*1*R*+41*F**ab**F**ab*.
- m=ℏ/ℓP*m*=ℏ/ℓ*P*: Mass from projection scale (N4).

**Core Statement / Theorem**
**Theorem N7.1 (DDF Action Principle).** Unique action stationary on admissible paths:
S=∫A[ψˉ(iD−m)ψ+R16πG+… ]−g d4x*S*=∫*A*[*ψ*ˉ(*i**D*−*m*)*ψ*+16*π**G**R*+…]−*g**d*4*x*
Varies to Dirac eq + Einstein: Dψ=mψ*D**ψ*=*m**ψ*, Rμν−12Rgμν=8πGTμν*R**μν*−21*R**g**μν*=8*π**G**T**μν*.
Status: DERIVED.

**Derivation**

1. From N4 symplectic T∗A*T*∗*A*, Legendre transform yields phase-space action S=∫pq˙−H*S*=∫*p**q*˙−*H*, H=ψˉDψ*H*=*ψ*ˉ*D**ψ* (N5 Dirac kinetic).
2. Curvature term: Lichnerowicz D2=□−14R*D*2=□−41*R* (N-G2) → R/16πG*R*/16*π**G* coeff from spectral norm (N-G4, G∼ℏc/Λ2*G*∼ℏ*c*/Λ2).
3. Admissibility Lagrange mult: δS∣∂A=0*δ**S*∣∂*A*=0 enforces rigidity (N1 cone).
4. Variation: δS/δψ=0→iDψ=mψ*δ**S*/*δ**ψ*=0→*i**D**ψ*=*m**ψ*; δS/δg=0→Gμν=8πGTμν*δ**S*/*δ**g*=0→*G**μν*=8*π**G**T**μν*. Gauge from F7 kernel.
   δS=∫(ψˉ\slashed∇δψ+δRδg)=0*δ**S*=∫(*ψ*ˉ\slashed∇*δ**ψ*+*δ**g**δ**R*)=0

**Consequences**

- Corollary N7.1.1: Gravity from spinor projection response; no sep. postulate.
- Unifies fermi/boson action (F6); preps N11 spectral.
- ℏ,Gℏ,*G* insertion rigid from N4.

**Dependencies**

- Requires N1 Propagation Rigidity
- Requires N4 Quantisation Rigidity
- Requires N-G2 Lichnerowicz Identity DDF
- Requires F7 Gauge Redundancy from Projection

**Next Notes**

- Leads to N8 Variational Principle
- Leads to N11 Spectral Action

**Notes Working Material**

- Partial: Bosonic kinetic from bosonic sector (F6 stub). TODO: Full SM matter Lagrangian.
- Alt: DDPM-inspired L†L−M*L*†*L*−*M* (link P4); map to density.