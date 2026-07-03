# T15: Polylogarithmic Major-Arc Package

**Status:** reduction to the classical Siegel–Walfisz scale plus a conditional assembly estimate.  
**Purpose:** separate the small-denominator major arcs, where prime distribution in progressions is the relevant input, from the genuinely hard large-denominator/minor-arc problem.

---

## 1. A deliberately conservative major-arc choice

Fix constants \(B,C>0\) and take
\[
Q=(\log N)^B,
\qquad
W=(\log N)^C.
\]

Use the T13 major arcs
\[
\mathfrak M(Q,W;N)
=
\bigcup_{q\le Q}\ \bigcup_{\substack{1\le a\le q\\(a,q)=1}}
\left\{\frac aq+\beta:\ |\beta|\le\frac{W}{qN}\right\}.
\]

This range is intentionally small. It is not intended to solve the Goldbach problem by itself; it isolates the portion where classical uniform arithmetic-progression estimates are naturally applicable.

---

## 2. Progression input at the polylogarithmic scale

For every prescribed \(A>0\), the needed classical input has the form
\[
\max_{m\le (\log N)^{B'}}\
\max_{(r,m)=1}\
\max_{x\le N}
\left|
\psi(x;m,r)-\frac{x}{\varphi(m)}
\right|
\ll_{A,B'}\frac{N}{(\log N)^A}.
\]

Here one takes \(B'\) large enough to cover
\[
L=[q,6]\le6(\log N)^B.
\]

This is the exact scale required by the sector residual in T14. The mod-\(6\) restriction is encoded by selecting residue classes modulo \(L\); the \(\chi_3\)-twisted formulation is an equivalent character decomposition of the same finite-modulus information.

---

## 3. Consequence for the T14 sector discrepancy

There are at most \(\varphi(L)\) residue classes in the sector aggregate, and the coefficient phases have modulus one. The crude bound
\[
|\mathscr D_\sigma(x;a,q)|
\le
\sum_{\substack{r\bmod L\\(r,L)=1\\r\equiv\sigma\,({\rm mod}\,6)}}
|D(x;L,r)|
\]
therefore gives, after requesting enough logarithmic saving in the AP input,
\[
\sup_{q\le Q}\sup_{(a,q)=1}\sup_{x\le N}
|\mathscr D_\sigma(x;a,q)|
\ll_A \frac{N}{(\log N)^A}.
\]

The loss from summing over residue classes is at most polylogarithmic because \(L\ll(\log N)^B\).

---

## 4. Partial-summation cost on these arcs

On the selected major arcs,
\[
N|\beta|\le\frac{W}{q}\le W=(\log N)^C.
\]

Thus T14 yields
\[
|\mathcal R_\sigma^{\rm AP}(a,q,\beta;N)|
\ll_A
\frac{N}{(\log N)^{A-C}}.
\]

After choosing the AP saving exponent larger than every bookkeeping loss, one may record the compact form
\[
\boxed{
\sup_{\alpha\in\mathfrak M(Q,W;N)}
|\mathcal R_\sigma(\alpha)|
\ll_{D,B,C}\frac{N}{(\log N)^D}
}
\]
for any predetermined \(D>0\), subject to the stated classical progression input and the explicit finite-prime term from T14.

---

## 5. Crude total-measure ledger

The total measure satisfies
\[
\begin{aligned}
|\mathfrak M(Q,W;N)|
&\le
\sum_{q\le Q}\varphi(q)\frac{2W}{qN}\\
&\ll\frac{WQ}{N}\\
&\ll\frac{(\log N)^{B+C}}{N}.
\end{aligned}
\]

The principal sector sums obey the trivial bound
\[
|P_\sigma(\alpha)|\ll N.
\]

Consequently, inserting the residual estimate from Section 4 into the exact T13 error ledger gives a schematic bound
\[
\mathcal E_{j,K}^{\mathfrak M}(n;Q,W)
\ll_D
\frac{N(\log N)^{B+C}}{(\log N)^D}
+
\frac{N(\log N)^{B+C}}{(\log N)^{2D}}
+
text{finite-prime contribution}.
\]

Choosing \(D\) sufficiently large relative to \(B+C+A_0\) gives
\[
\boxed{
\mathcal E_{j,K}^{\mathfrak M}(n;Q,W)
\ll_{A_0}\frac{N}{(\log N)^{A_0}}.
}
\]

The displayed line is a bookkeeping implication of the stated uniform residual bound; it is not a substitute for proving the weighted major-model lower bound.

---

## 6. What this does and does not settle

This package says:

\[
\boxed{
\text{For polylogarithmic denominators, the sector major-arc residual is not the core obstruction.}
}
\]

But it does **not** establish:

1. positivity of the full Fejér-weighted major model \(\mathcal M_{j,K}^{(N)}\);
2. control of rational regions with denominators beyond the chosen \(Q\);
3. a pointwise minor-arc bound; or
4. descent from the Fejér-windowed coefficient to the exact Goldbach coefficient.

Those remain separate gates.

---

## 7. Correct revised architecture

The proof spine now separates into:

\[
\text{small }q\le(\log N)^B
\quad\Rightarrow\quad
\text{AP-controlled major arcs},
\]

\[
(\log N)^B<q\lesssim N^{\vartheta}
\quad\Rightarrow\quad
\text{transition / large-denominator analysis},
\]

\[
\text{far minor arcs}
\quad\Rightarrow\quad
\text{Type-I/II cancellation problem}.
\]

The OFI/Fejér multiplier may be compared across the latter two regions, but it should not be credited for the classical polylogarithmic major-arc package.

---

## 8. Next theorem target

The next honest target is a positive lower bound for the **assembled** Fejér-weighted major model on the polylogarithmic arcs:
\[
\mathcal M_{j,K}^{(N)}(n;Q,W)\ge c_jN.
\]

That is a weighted singular-series problem. Once it is isolated, the remaining global difficulty is visibly concentrated in the transition and minor-arc regimes.