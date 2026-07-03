# T20: Smooth Arc Partition and Fourier-Tail Ledger

**Status:** explicit cutoff construction, derivative accounting, and exact tail reduction; no arithmetic correlation estimate is claimed.  
**Purpose:** replace the placeholder smooth partition in T19 with a quantitative construction that preserves the sector Fejér structure while charging every collar and Fourier-tail cost.

---

## 1. Rational neighborhoods through the transition endpoint

Let
\[
Q_0=(\log N)^B,
\qquad
Q_1\le N^\vartheta,
\qquad
r_q:=\frac{W}{qN}.
\]

For every reduced \(a/q\) with \(q\le Q_1\), write
\[
I_{a/q}:=\left\{\alpha\in\mathbb T:\ \left|\alpha-\frac aq\right|_{\mathbb T}\le r_q\right\}.
\]

Choose a fixed even bump \(\rho\in C^\infty(\mathbb R)\) satisfying
\[
0\le\rho\le1,
\qquad
\rho(t)=1\ (|t|\le1),
\qquad
\rho(t)=0\ (|t|\ge1+\varepsilon),
\]
for a fixed collar parameter \(0<\varepsilon<1\).

Define the arc cutoff
\[
\chi_{a/q}(\alpha)
:=
\rho\!\left(\frac{\alpha-a/q}{r_q}\right),
\]
periodically interpreted on \(\mathbb T\).

When the enlarged arcs are disjoint, set
\[
\chi_{\le Q_1}(\alpha)
:=
\sum_{q\le Q_1}\sum_{(a,q)=1}\chi_{a/q}(\alpha),
\qquad
\chi_{\mathfrak F}(\alpha):=1-\chi_{\le Q_1}(\alpha).
\]

If they overlap, use a normalized partition
\[
\chi_{\mathfrak F}:=
1-\frac{\sum_{a/q}\chi_{a/q}}{\max\{1,\sum_{a/q}\chi_{a/q}\}},
\]
or first choose parameters ensuring bounded overlap. Any overlap multiplicity must appear in every estimate below.

---

## 2. Support and collar ledger

The cutoff obeys
\[
\chi_{a/q}=1\quad\text{on }I_{a/q},
\]
and is supported in the enlarged arc
\[
I^+_{a/q}:=
\left\{\alpha:\ \left|\alpha-\frac aq\right|_{\mathbb T}
\le(1+\varepsilon)r_q\right\}.
\]

The collar is
\[
\mathcal C_{a/q}:=I^+_{a/q}\setminus I_{a/q},
\]
with measure
\[
|\mathcal C_{a/q}|\le2\varepsilon r_q.
\]

Summing over reduced rationals gives the global collar estimate
\[
\begin{aligned}
|\mathcal C_{\le Q_1}|
&\ll
\varepsilon\sum_{q\le Q_1}\varphi(q)\frac{W}{qN}\\
&\ll
\boxed{\varepsilon\frac{WQ_1}{N}}.
\end{aligned}
\]

This collar mass is not automatically negligible when \(Q_1\) is large. Its contribution belongs in the transition/far-minor ledger rather than being discarded as “smoothing.”

---

## 3. Derivative cost of the rational partition

For every integer \(s\ge1\),
\[
\|\chi_{a/q}^{(s)}\|_{L^1(\mathbb T)}
\le
C_{s,\rho}r_q^{1-s}.
\]

Therefore, under bounded overlap,
\[
\begin{aligned}
\|\chi_{\le Q_1}^{(s)}\|_1
&\ll_{s,\rho}
\sum_{q\le Q_1}\varphi(q)
\left(\frac{qN}{W}\right)^{s-1}\\
&\ll_{s,\rho}
\boxed{
\left(\frac{N}{W}\right)^{s-1}Q_1^{s+1}
}.
\end{aligned}
\]

The same estimate holds for \(\chi_{\mathfrak F}^{(s)}\) up to the bounded-overlap normalization constants.

This is the quantitative price of a smooth separation through denominator \(Q_1\): high Fourier decay requires derivatives, and derivatives grow rapidly with \(Q_1\).

---

## 4. Fejér multiplier derivative ledger

Recall
\[
\Omega_K(\alpha)
=
\left|
\frac1{K+1}\sum_{r=0}^{K}e(6r\alpha)
\right|^2.
\]

For each fixed integer \(t\ge0\), termwise differentiation gives
\[
\|\partial_\alpha^t\Omega_K^2\|_\infty
\le C_t(6K)^t.
\]

Define the smooth far-minor weight
\[
W^{\rm sm}_{\mathfrak F,K}(\alpha)
:=
\chi_{\mathfrak F}(\alpha)\Omega_K(\alpha)^2.
\]

Leibniz gives, for every \(s\ge1\),
\[
\boxed{
\|\partial_\alpha^sW^{\rm sm}_{\mathfrak F,K}\|_1
\ll_s
\sum_{t=0}^s
(6K)^{s-t}
\|\chi_{\mathfrak F}^{(t)}\|_1.
}
\]

Combining with Section 3 yields an explicit smoothness norm
\[
\mathcal N_{s,K}(N,W,Q_1)
:=
C_s\sum_{t=0}^s
(6K)^{s-t}
\left(
\mathbf1_{t=0}
+
\mathbf1_{t\ge1}
\left(\frac{N}{W}\right)^{t-1}Q_1^{t+1}
\right).
\]

---

## 5. Fourier decay and finite-shift reduction

Write
\[
\widehat W^{\rm sm}_{\mathfrak F,K}(h)
:=
\int_0^1W^{\rm sm}_{\mathfrak F,K}(\alpha)e(\alpha h)\,d\alpha.
\]

For \(h\ne0\), integration by parts gives
\[
\boxed{
|\widehat W^{\rm sm}_{\mathfrak F,K}(h)|
\le
\frac{\mathcal N_{s,K}(N,W,Q_1)}{(2\pi|h|)^s}.
}
\]

Hence, for every \(s>1\),
\[
\boxed{
\sum_{|h|>H}
|\widehat W^{\rm sm}_{\mathfrak F,K}(h)|
\ll_s
\mathcal N_{s,K}(N,W,Q_1)H^{1-s}.
}
\]

Thus T19's shifted-correlation functional splits exactly into
\[
\sum_h\widehat W^{\rm sm}_{\mathfrak F,K}(h)\mathcal C_C(h)
=
\sum_{|h|\le H}\widehat W^{\rm sm}_{\mathfrak F,K}(h)\mathcal C_C(h)
+
\mathcal T_H,
\]
where the tail satisfies
\[
|\mathcal T_H|
\le
\left(\sup_h|\mathcal C_C(h)|\right)
\sum_{|h|>H}|\widehat W^{\rm sm}_{\mathfrak F,K}(h)|.
\]

A stronger, often more realistic version uses a weighted bound for the correlations rather than the crude supremum. Either way, the tail is now an explicit budget item.

---

## 6. What this does not give for free

The construction gives smooth Fourier tails, but it does **not** prove that
\[
\mathcal C_C(h)=\sum_nC(n)\overline{C(n-h)}
\]
has cancellation. It only reduces the far-minor fourth-moment theorem to:

1. finitely many short shifts \(|h|\le H\), with explicit coefficients; and
2. a tail controlled by the chosen regularity order \(s\), cutoff geometry, and a separate correlation estimate.

Large \(Q_1\), tiny transition width, or large Fejér radius \(K\) can inflate \(\mathcal N_{s,K}\). Smoothing is therefore a tradeoff, not a free localization device.

---

## 7. T20 theorem target

Choose \(s,H,K,W,Q_1\) so that the collar and tail costs are each below a predetermined fraction of the density-one error budget. Then prove
\[
\boxed{
\sum_{|h|\le H}
\left|
\widehat W^{\rm sm}_{\mathfrak F,K}(h)
\right|
\left|
\mathcal C_C(h)
\right|
\le X^{3-\eta}
}
\]
for each required Type-I/II coefficient sequence \(C\), with compatible bounds for the finite-prime and decomposition remainders.

This is the first finite, fully parameterized shifted-correlation subproblem produced by the Fejér/OFI program.

---

## 8. Decision rule for fractional OFI windows

A candidate sector-preserving OFI multiplier \(\Omega_u\) must be compared after the same smooth partition is applied. It is better than Fejér only if it improves the **total** certified functional:
\[
\text{short-shift correlation cost}
+
\text{Fourier tail cost}
+
\text{collar cost}
+
\text{major/extraction costs}.
\]

A faster-decaying multiplier that requires a much larger local radius or worsens the cutoff derivative norm is not automatically an improvement.