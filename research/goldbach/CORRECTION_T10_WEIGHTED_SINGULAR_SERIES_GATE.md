# Correction: T10 Requires a Weighted Singular Series, Not Broad Rational Preservation

**Scope:** This correction refines `T10_RATIONAL_PRESERVATION_AND_ARC_BUDGET.md`.

## 1. The issue

T10 correctly noted that an additive output multiplier
\[
\Omega_H(\alpha)=\sum_{|h|\le H}\omega_h e(\alpha h)
\]
cannot be judged only near \(\alpha=0\): major arcs occur around many rationals \(a/q\).

However, the blanket design target
\[
\Omega_H(\alpha)\approx1
\quad\text{on every major arc}
\]
is usually too strong for a nontrivial short local window. It should not be treated as the default route.

The correct major-arc condition is instead a lower bound for the **weighted singular series** produced by the actual values \(\Omega_H(a/q)\).

---

## 2. Exact rational-preservation obstruction for positive windows

Assume \(\omega_h\ge0\), \(\sum_h\omega_h=1\), and \(\operatorname{supp}\omega\subset[-H,H]\cap\mathbb Z\).

### Lemma

If
\[
\Omega_H(a/q)=1
\]
for every reduced rational \(a/q\) with \(1\le q\le Q\), then every point in \(\operatorname{supp}\omega\) is divisible by
\[
L_Q:=\operatorname{lcm}(1,2,\dots,Q).
\]

In particular, if \(H<L_Q\), then
\[
\omega=\delta_0.
\]

### Proof

For fixed \(a/q\),
\[
\Omega_H(a/q)=\sum_h\omega_h e(ah/q)
\]
is a convex combination of points on the unit circle. Its value can equal the unit-modulus point \(1\) only when every phase carrying positive mass equals \(1\). Thus every support point obeys
\[
ah\equiv0\pmod q.
\]
Taking \(a=1\), every support point is divisible by \(q\). Repeating for all \(q\le Q\) gives divisibility by \(L_Q\). If \(|h|\le H<L_Q\), only \(h=0\) remains. \(\square\)

### Consequence

\[
\boxed{
\text{A genuinely local positive output window cannot exactly preserve all low-denominator major rationals.}
}
\]

The same phenomenon persists approximately: demanding very small distortion at many rational centers forces a severe locality/selectivity tradeoff.

---

## 3. Correct major-arc object

Let \(\mathcal A_q(a;E,j)\) denote the arithmetic local factor arising in the sector-\(j\) major-arc approximation at the rational center \(a/q\). The OFI-weighted major contribution has the schematic form
\[
\mathcal M^{\Omega}_{j}(E)
=
E
\sum_{q\ge1}\sum_{\substack{1\le a\le q\\(a,q)=1}}
\Omega_H(a/q)
\mathcal A_q(a;E,j)
+
\mathcal E^{\mathfrak M}_{\Omega,j}(E).
\]

Define the corresponding weighted singular series
\[
\mathfrak S^{\Omega}_{j}(E)
:=
\sum_{q\ge1}\sum_{\substack{1\le a\le q\\(a,q)=1}}
\Omega_H(a/q)
\mathcal A_q(a;E,j).
\]

For a symmetric real output kernel
\[
\omega_{-h}=\omega_h\in\mathbb R,
\]
we have
\[
\Omega_H(-\alpha)=\Omega_H(\alpha)\in\mathbb R,
\]
which is the natural setting for seeking a real lower bound.

---

## 4. Correct major-arc gate

The required theorem is not \(\Omega_H\approx1\) everywhere. It is
\[
\boxed{
\mathfrak S^{\Omega}_{j}(E)\ge c_{\Omega,j}>0
\qquad\text{for every admissible }E,
}
\]
together with a controlled approximation error
\[
|\mathcal E^{\mathfrak M}_{\Omega,j}(E)|
\le \varepsilon_{\Omega,j}E
\]
small enough that
\[
\mathcal M^{\Omega}_{j}(E)
\ge \frac12c_{\Omega,j}E.
\]

This is the lawful replacement for broad rational preservation.

---

## 5. Consequence for OFI design

An OFI output window has to be evaluated as a coupled arithmetic filter:

\[
\boxed{
\text{weighted major singular series remains positive}
\quad+\quad
\text{weighted minor-arc budget improves}
\quad+\quad
\text{local extraction error is paid}.
}
\]

The triangle/delta-like baseline may preserve the ordinary singular series more transparently. A fractional/local window earns promotion only by proving that its modified singular series stays uniformly positive and that it buys enough minor-arc improvement to offset the extra structure.

---

## 6. What this changes

- The locality-versus-frequency Bernstein inequality in T10 remains valid.
- Denominator-stratified minor-arc budgeting remains valid.
- The blanket rational-preservation requirement is demoted to a sufficient special case, not the default target.
- The primary new arithmetic gate is positivity of \(\mathfrak S^{\Omega}_{j}(E)\).

Until this weighted singular-series bound is proved, an OFI multiplier cannot be claimed to preserve the Goldbach major term.