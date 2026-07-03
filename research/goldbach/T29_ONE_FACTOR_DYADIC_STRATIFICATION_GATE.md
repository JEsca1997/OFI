# T29: One-Factor Dyadic Stratification Gate

**Status:** exact dyadic decomposition of the T28 sampled product energy and explicit threshold budgets; no one-factor large-values estimate is claimed.  
**Purpose:** make route P-D2 in T28 auditable without replacing either bilinear factor by an uncontrolled global supremum.

---

## 1. Separated far-minor sample energy

Let
\[
\mathcal A=\{\alpha_1,\dots,\alpha_J\}
\subset\operatorname{supp}(w)
\]
be \(\delta\)-separated, and write
\[
A_j:=A_{\alpha_j}=\mathcal B_1(\alpha_j),
\qquad
B_j:=B_{\alpha_j}=\mathcal B_2(\alpha_j).
\]

The quantity required by T26–T28 is
\[
\mathcal S(\mathcal A)
:=
\sum_{j=1}^J|A_jB_j|^2.
\]

No estimate in this file treats \(\max_j|B_j|\) as harmless.

---

## 2. Exact dyadic partition by the second factor

Choose a base threshold \(U_0>0\). For dyadic \(U=2^rU_0\), define
\[
\mathcal A_U
:=
\{\alpha_j\in\mathcal A:\ U<|B_j|\le2U\}.
\]

Let
\[
\mathcal A_{\le U_0}
:=
\{\alpha_j\in\mathcal A:\ |B_j|\le U_0\}.
\]

These sets partition \(\mathcal A\). Hence
\[
\begin{aligned}
\mathcal S(\mathcal A)
&=
\sum_{\alpha_j\in\mathcal A_{\le U_0}}|A_jB_j|^2
+
\sum_U\sum_{\alpha_j\in\mathcal A_U}|A_jB_j|^2\\
&\le
\boxed{
U_0^2\sum_{\alpha_j\in\mathcal A}|A_j|^2
+
4\sum_UU^2
\sum_{\alpha_j\in\mathcal A_U}|A_j|^2.
}
\end{aligned}
\]

This is exact up to the displayed factor \(4\).

---

## 3. Moderate-​\(B\) ledger

By the ordinary separated-set large sieve applied only to \(A\),
\[
\sum_{\alpha_j\in\mathcal A}|A_j|^2
\ll
(X+\delta^{-1})\sum_x|A(x)|^2,
\]
where
\[
A( x )=
\sum_{mn=x}a_{m,n}.
\]

Therefore the moderate contribution is bounded by
\[
\boxed{
\mathcal S_{\rm mod}
\ll
U_0^2(X+\delta^{-1})\sum_x|A(x)|^2.
}
\]

To fit the density-one target, a sufficient budget condition is
\[
\boxed{
U_0^2(X+\delta^{-1})\sum_x|A(x)|^2
\le
\frac14\delta^{-1}X^{3-\eta}.
}
\]

This determines how low the baseline threshold \(U_0\) must be. It is a genuine constraint, not a free choice.

---

## 4. Large-​\(B\) strata require more than cardinality

For each \(U\), the naive estimate gives
\[
\sum_{\alpha_j\in\mathcal A_U}|A_j|^2
\ll
(X+\delta^{-1})\sum_x|A(x)|^2,
\]
which is independent of \(|\mathcal A_U|\). Thus a mere bound on the number of large \(B_j\) values does not automatically yield a saving if one uses only the generic large sieve.

The needed input is one of the following stronger statements.

### B1. Restricted-set sampling estimate for \(A\)
\[
\boxed{
\sum_{\alpha_j\in\mathcal A_U}|A_j|^2
\ll
\mathfrak L_A(U;\mathcal A)
}
\]
with
\[
\sum_U U^2\mathfrak L_A(U;\mathcal A)
\ll
\delta^{-1}X^{3-\eta}.
\]

### B2. Joint product large-values estimate
\[
\boxed{
\sum_{\alpha_j\in\mathcal A_U}|A_jB_j|^2
\ll
\mathfrak J(U;\mathcal A),
\qquad
\sum_U\mathfrak J(U;\mathcal A)
\ll
\delta^{-1}X^{3-\eta}.
}
\]

### B3. A conditional correlation estimate
Use the fact that membership in \(\mathcal A_U\) is defined by \(B\) itself, and prove a bilinear correlation estimate stronger than generic sampling. This is the natural bridge back to T28's kernel \(\mathscr K_B\).

---

## 5. A weighted counting formulation

Define the restricted \(A\)-energy
\[
E_A(U;\mathcal A)
:=
\sum_{\alpha_j\in\mathcal A_U}|A_j|^2.
\]

Then the exact dyadic task is
\[
\boxed{
U_0^2E_A(\mathcal A)
+
4\sum_UU^2E_A(U;\mathcal A)
\ll
\delta^{-1}X^{3-\eta}.
}
\]

This is more informative than the scalar count
\[
N_B(U):=|\mathcal A_U|,
\]
because it records whether the large values of \(B\) correlate with large sampled energy of \(A\).

The difficulty is exactly that the two factors may concentrate on the same far-minor frequencies. Any proof must rule out that joint concentration.

---

## 6. Symmetric two-sided decomposition

One may also dyadically partition both factors:
\[
\mathcal A_{U,V}
:=
\{\alpha_j:\ U<|A_j|\le2U,\ V<|B_j|\le2V\}.
\]

Then
\[
\boxed{
\mathcal S(\mathcal A)
\ll
\sum_{U,V}U^2V^2|\mathcal A_{U,V}|.
}
\]

This is exact up to fixed dyadic constants. A proof-moving theorem is therefore a joint large-values bound
\[
\boxed{
\sum_{U,V}U^2V^2|\mathcal A_{U,V}|
\ll
\delta^{-1}X^{3-\eta}.
}
\]

The two-sided form is the cleanest statement of the avoided-concentration requirement, but it is usually harder than the one-factor conditional route.

---

## 7. Relation to the T28 kernel

For a fixed \(U\), the set \(\mathcal A_U\) depends on the \(B\)-values. The restricted \(A\)-energy expands as
\[
\sum_{\alpha_j\in\mathcal A_U}|A_j|^2
=
\sum_{m,n,m',n'}
a_{m,n}\overline{a_{m',n'}}
K_{\mathcal A_U}(mn-m'n'),
\]
where
\[
K_{\mathcal A_U}(h)
:=
\sum_{\alpha_j\in\mathcal A_U}e(\alpha_jh).
\]

Thus the large-​\(B\) condition changes the sampling kernel itself. A valid proof must use the arithmetic structure that selected \(\mathcal A_U\); treating it as an arbitrary subset throws away the correlation between the kernel and \(B\).

This is precisely why T28's preconvolution kernel remains the central object.

---

## 8. Decision rule and next theorem

The one-factor route succeeds only if it establishes a budget of the form
\[
\boxed{
\sum_UU^2E_A(U;\mathcal A)
\ll
\delta^{-1}X^{3-\eta},
}
\]
with the moderate term separately paid.

A scalar estimate for \(N_B(U)\) is insufficient unless combined with a restricted-set estimate for \(A\) that genuinely improves as \(N_B(U)\) decreases.

The next hard subproblem is therefore a **joint concentration exclusion theorem** for Type-II sums on far-minor separated sets: large \(B\)-values cannot carry too much sampled \(A\)-energy.