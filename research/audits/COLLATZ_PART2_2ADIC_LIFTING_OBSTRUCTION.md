# Collatz Part 2 Audit: The 2-adic Lifting Obstruction

**Scope:** audit of the proposed `Generic odd-constant block lemma` used in the uploaded March 2026 Part 2 manuscript.  
**Outcome:** the non-stabilization conclusion does not follow from the displayed recurrence. Consequently this lemma cannot be imported as a proved p-adic mechanism into the Goldbach program.

---

## 1. Claimed generic setting

The manuscript considers an infinite affine block sequence
\[
2^{m_i}y_i=3^{s_i}y_{i-1}+D_i,
\qquad m_i\ge1,\ s_i\ge0,\ D_i\ \text{odd},
\]
with
\[
M_n=\sum_{i=1}^n m_i,
\qquad
S_n=\sum_{i=1}^n s_i,
\]
and recursively defined odd constants
\[
C_{n+1}=3^{s_{n+1}}C_n+2^{M_n}D_{n+1}.
\]

The exact composed identity is valid:
\[
2^{M_n}y_n=3^{S_n}y_0+C_n.
\]
It implies the compatible congruence
\[
y_0\equiv -3^{-S_n}C_n\pmod{2^{M_n}}.
\]

Let \(a_n\) denote the least nonnegative representative of the right-hand residue class modulo \(2^{M_n}\).

---

## 2. The invalid lift

From the recurrence one obtains
\[
-3^{-S_{n+1}}C_{n+1}
=
-3^{-S_n}C_n
-2^{M_n}3^{-S_{n+1}}D_{n+1}.
\]

This equality holds in the 2-adic integers. However, the manuscript replaces the first term by the integer representative \(a_n\) **modulo \(2^{M_{n+1}}\)**.

Only the weaker statement is known:
\[
-3^{-S_n}C_n\equiv a_n\pmod{2^{M_n}}.
\]

Because \(M_{n+1}>M_n\), there is an undetermined lift bit/block:
\[
-3^{-S_n}C_n
=
a_n+2^{M_n}k_n
quad (\bmod\ 2^{M_{n+1}})
\]
for some integer \(k_n\) known only modulo \(2^{m_{n+1}}\).

The correct relation is therefore
\[
a_{n+1}-a_n
\equiv
2^{M_n}\bigl(k_n-3^{-S_{n+1}}D_{n+1}\bigr)
\pmod{2^{M_{n+1}}}.
\]

There is no reason for the parenthesis to be odd. Thus one cannot conclude
\[
v_2(a_{n+1}-a_n)=M_n.
\]

---

## 3. Explicit counterexample

Take the constant sequence
\[
m_i=1,\qquad s_i=1,\qquad D_i=-1,\qquad y_i=1
\]
for all \(i\). Every block is a valid odd-constant affine block:
\[
2\cdot1=3\cdot1-1.
\]

The sequence is realized by the positive integer \(y_0=1\) at every level.

For this sequence:
\[
C_1=-1,
\qquad
C_2=3(-1)+2(-1)=-5,
\]
and
\[
a_1\equiv-3^{-1}(-1)\equiv1\pmod2,
\]
\[
a_2\equiv-3^{-2}(-5)\equiv1\pmod4.
\]
Taking canonical representatives gives
\[
a_1=a_2=1.
\]

But the claimed recurrence would force
\[
a_2-a_1\equiv-2\cdot3^{-2}(-1)\equiv2\pmod4,
\]
which is false because the left side is \(0\).

Hence the asserted generic conclusion that the canonical residues are never eventually constant is false.

---

## 4. What remains valid

The following pieces remain algebraically valid:

\[
2^{M_n}y_n=3^{S_n}y_0+C_n,
\]

\[
y_0\equiv-3^{-S_n}C_n\pmod{2^{M_n}},
\]

and the recurrence for \(C_n\).

What fails is the unqualified comparison of **canonical integer representatives across changing moduli**.

A corrected theorem would need an additional hypothesis that controls the lift variable \(k_n\), or a different invariant that is genuinely incompatible with compatible inverse-limit residues. The existing oddness assumption on \(D_n\) does not do this.

---

## 5. Consequence for Goldbach cross-pollination

No p-adic non-stabilization theorem from this source may be used in the Goldbach transition-annulus argument.

The Goldbach obstruction remains the independently derived arithmetic target:
\[
\sum_{Q<q\le2Q}\sum_{\chi\,([q,6])}^{*}
\int_{|\beta|\le W/(qX)}
|\mathsf R_X(\chi;\beta)|^4d\beta.
\]

The valid transferable lesson is methodological only:
\[
\text{separate exact congruence identities from estimates or incompatible-lift claims.}
\]

It does not produce a denominator-sensitive bound for twisted prime sums.