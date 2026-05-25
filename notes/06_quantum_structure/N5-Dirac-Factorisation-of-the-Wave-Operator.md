# N5 Dirac Factorisation Of The Wave Operator

path: 06_quantum_structure/N5-Dirac-Factorisation-of-the-Wave-Operator.md
folder: 06_quantum_structure
filename: N5-Dirac-Factorisation-of-the-Wave-Operator.md
repository: DDF
type: research_note

# Note ID

N5

# Title

Dirac Factorisation of the Wave Operator

# Folder

06_quantum_structure

# Status

Active mathematical development

# Version

v1.0

# Date

March 2026

# Purpose

Show that the wave operator emerging from propagation rigidity admits a first-order square root.

This produces the **Dirac operator**, which leads to fermionic fields.

---

# Depends On

N1 — Propagation Rigidity

---

# Establishes

• factorisation of the wave operator  
• first-order propagation operator  
• Clifford algebra structure

---

# 1 Wave Operator

Propagation rigidity yields the wave operator

$$
\Box = \partial_t^2 - c^2 \nabla^2
$$

---

# 2 Factorisation Principle

We seek an operator

$$
D = \gamma^\mu \partial_\mu
$$

such that

$$
D^2 = \Box
$$

---

# 3 Clifford Relations

This requires matrices satisfying

$$
\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}
$$

which define the **Clifford algebra**.

---

# 4 Dirac Operator

Thus

$$
D = \gamma^\mu \partial_\mu
$$

is the **first-order rigidity operator**.

---

# 5 Physical Meaning

This produces

• fermionic propagation  
• spin-½ structure  
• relativistic quantum wave equations

---

# 6 Result

## Dirac Factorisation Theorem

If admissible propagation obeys the hyperbolic wave operator

$$
\Box
$$

then it admits a first-order square root

$$
(\gamma^\mu \partial_\mu)^2 = \Box .
$$