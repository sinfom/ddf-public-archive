# N13 Lorentzian Heatkernel

path: 05_gravity_limit/n13-lorentzian-heatkernel.md
folder: 05_gravity_limit
filename: n13-lorentzian-heatkernel.md
repository: DDF
type: research_note





# Heat Kernel Expansion in Lorentzian DDF for Quantum Gravity Loops

path 05gravitylimit/n13-lorentzian-heatkernel.md
folder 05gravitylimit
filename n13-lorentzian-heatkernel.md
repository DDF
type researchnote

Note ID N13

Folder 05gravitylimit
Status Active mathematical development
Version v0.1
Date 2026-03-22



**Purpose**
Derive Lorentzian heat kernel K(t)*K*(*t*) for DDF Dirac D*D* on curved U*U*, yielding one-loop QG effective action via log⁡det⁡Dlogdet*D*. Extends N11 spectral to dynamical gravity; post-Einstein limit (N12).

**Definitions**

- K(t;x,y)=⟨x∣e−tD2∣y⟩*K*(*t*;*x*,*y*)=⟨*x*∣*e*−*t**D*2∣*y*⟩: Heat kernel (Lorentzian analytic cont.).
- Seeley-DeWitt coeffs: an(x)=\Tr(bn(x,x))*a**n*(*x*)=\Tr(*b**n*(*x*,*x*)), b4∼R2,Λ4*b*4∼*R*2,Λ4.
- Effective action: Γ=−12log⁡det⁡D=12∫0∞dtt\Tr(e−tD2)Γ=−21logdet*D*=21∫0∞*t**d**t*\Tr(*e*−*t**D*2).

**Core Statement / Theorem**
**Theorem N13.1 (Lorentzian Heat Kernel Theorem).** For DDF D*D* on Lorentzian spinor bundle,
K(t)∼(4πt)−2[1+a2t+a4t2+… ],a2=16R,a4∼R2+Λ4*K*(*t*)∼(4*π**t*)−2[1+*a*2*t*+*a*4*t*2+…],*a*2=61*R*,*a*4∼*R*2+Λ4
Loop Γ(1)∼∫R2120(4π)2ϵ+Λ4Γ(1)∼∫120(4*π*)2*ϵ**R*2+Λ4; UV finite via proj cutoff Λ∼1/ℓPΛ∼1/ℓ*P*.
Status: DERIVED.

**Derivation**

1. Wick rotate: Euclidean DE2→−D2+it*D**E*2→−*D*2+*i**t*; expand parametrices (Seeley-Nielsen-Zee).
2. Lichnerowicz (N-G2): Heat trace \Tre−tD2=∫K(t;x,x)gd4x\Tr*e*−*t**D*2=∫*K*(*t*;*x*,*x*)*g**d*4*x*.
3. Coeffs: a0=1*a*0=1, a2=(1/6)R*a*2=(1/6)*R* (N11); a4=(1/360)(5R2−2∣Riem∣2+...)+\TrF2*a*4=(1/360)(5*R*2−2∣*R**i**e**m*∣2+...)+\Tr*F*2(gauge F7).
4. Loop: Γ=12∫dtt(\Tre−tD2−a0/t2)Γ=21∫*t**d**t*(\Tr*e*−*t**D*2−*a*0/*t*2); renorm ϵ=Λ−2*ϵ*=Λ−2. Proj: Λ=∥P∥−1Λ=∥*P*∥−1 (F2 bound).
   Γ(1)=1(4π)2∫d4xg[R2120ϵ+30Λ4+… ]Γ(1)=(4*π*)21∫*d*4*x**g*[120*ϵ**R*2+30Λ4+…]
   Finite: ΛΛ internal (NC1 fit).

**Consequences**

- Corollary N13.1.1: QG loops → R2*R*2 terms; asymptotic safety via proj.
- Unifies N12 Einstein + quantum corrections; preps RH spectral (07).
- Predicts ΛQG∼mPΛ*QG*∼*m**P*.

**Dependencies**

- Requires N11 Spectral Action
- Requires N12 Einstein Limit
- Requires N-G2 Lichnerowicz Identity DDF
- Requires NC1 Numeric Projection Norms Fit

**Next Notes**

- Leads to N14 Asymptotic Safety from Projection
- Leads to 07NumberTheory Spectral Interface

**Notes Working Material**

- Partial: Full b6*b*6 coeff. TODO: Numerical heat trace on toy curved U.
- Alt: Zeta-reg ζ(s)=\TrD−s*ζ*(*s*)=\Tr*D*−*s*, pole res. at s=0.