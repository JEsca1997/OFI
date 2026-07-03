# T11: Sector-Preserving Fejer Window Benchmark

**Status:** exact window construction and benchmark ledger; no new prime-correlation estimate is claimed.  
**Purpose:** replace the abstract sector-preserving OFI output multiplier by a canonical, explicit positive window on the rescaled mod-6 lattice.

---

## 1. Rescaled sector lattice

Fix \(j\in\{0,2,4\}\) and write
\[
\mathcal G_j(n):=G_j(6n+j),
\qquad
\mathcal R_j(n):=R_j(6n+j).
\]

A sector-preserving output window acts by ordinary convolution on \(n\in\mathbb Z\):
\[
\mathcal A_j(n)=(\nu*\mathcal G_j)(n).
\]

In the original Goldbach coordinate this means shifts by \(6k\) only.

---

## 2. Canonical Fejer probability kernel

For an integer \(K\ge0\), define
\[
\nu^{(K)}_k
:=
\begin{cases}
\dfrac{K+1-|k|}{(K+1)^2},& |k|\le K,\\[6pt]
0,& |k|>K.
\end{cases}
\]

Then
\[
\nu^{(K)}_k\ge0,
\qquad
\nu^{(K)}_{-k}=\nu^{(K)}_k,
\qquad
\sum_{k\in\mathbb Z}\nu^{(K)}_k=1.
\]

The corresponding original-variable OFI output kernel is
\[
\omega^{(K)}_{6k}=\nu^{(K)}_k,
\qquad
\omega^{(K)}_h=0\quad(h\notin6\mathbb Z).
\]

Thus its physical additive radius is \(6K\).

---

## 3. Exact multiplier

On the rescaled unit circle, the multiplier is
\[
\widehat\nu_K(\beta)
=
\sum_{k=-K}^{K}\nu^{(K)}_k e(k\beta)
=
\frac1{(K+1)^2}
\left(\frac{\sin(\pi(K+1)\beta)}{\sin(\pi\beta)}\right)^2,
\]
with the continuous value \(\widehat\nu_K(0)=1\).

On the original frequency circle,
\[
\boxed{
\Omega_K(\alpha)=\widehat\nu_K(6\alpha).
}
\]

Consequently,
\[
0\le\Omega_K(\alpha)\le1,
\qquad
\Omega_K(\alpha+1/6)=\Omega_K(\alpha).
\]

This is a concrete sector-preserving nonnegative multiplier, not an unspecified filter.

---

## 4. Exact output and positivity of the model average

The Fejer-localized Goldbach output is
\[
\mathcal A_{j,K}(n)
=
\sum_{|k|\le K}
\frac{K+1-|k|}{(K+1)^2}
\mathcal G_j(n-k).
\]

For any nonnegative sequence \(f\),
\[
(\nu^{(K)}*f)(n)\ge0.
\]

Likewise, if a sector model main term \(\mathcal M_j(n)\) is positive on the whole window \([n-K,n+K]\), then
\[
(\nu^{(K)}*\mathcal M_j)(n)>0.
\]

This gives a lawful positive **windowed** main term. It does not imply positivity of the center coefficient \(\mathcal G_j(n)\); T9's positive-deconvolution obstruction still applies.

---

## 5. Weighted major term: correct definition

The safe major-term definition is coefficient-side:
\[
\mathcal M_{j,K}(n)
:=(\nu^{(K)}*\mathcal M_j)(n).
\]

If a conventional major-arc formula gives
\[
\mathcal R_j(n)=\mathcal M_j(n)+\mathcal E_j(n),
\]
then linearity gives the exact weighted identity
\[
\mathcal A^{\mathcal R}_{j,K}(n)
=
\mathcal M_{j,K}(n)
+(\nu^{(K)}*\mathcal E_j)(n).
\]

This formulation avoids prematurely treating the weighted major term as the old singular series times a scalar. The equivalent circle-method expression has multiplier \(\Omega_K\), but its rational contributions must sum to this same coefficient-side quantity.

---

## 6. Elementary distortion bound for slowly varying models

Let \(\Delta f(n)=f(n+1)-f(n)\). Then
\[
|(\nu^{(K)}*f)(n)-f(n)|
\le
\sum_{|k|\le K}\nu^{(K)}_k |f(n-k)-f(n)|.
\]

If \(|\Delta f(m)|\le L\) throughout \([n-K,n+K]\), then
\[
|(\nu^{(K)}*f)(n)-f(n)|
\le L\sum_k\nu^{(K)}_k|k|.
\]

For the Fejer probability kernel,
\[
\sum_k\nu^{(K)}_k|k|
=
\frac{K(K+2)}{3(K+1)}
<\frac K3+\frac13.
\]

Therefore
\[
\boxed{
|(\nu^{(K)}*f)(n)-f(n)|
\le
\frac{K(K+2)}{3(K+1)}L.
}
\]

This is an exact major-model distortion ledger once a genuine local variation bound for the chosen model has been proved.

---

## 7. Frequency selectivity is explicit

The first zeros of \(\widehat\nu_K\) occur at
\[
\beta=\frac{m}{K+1},
qquad m\in\mathbb Z\setminus (K+1)\mathbb Z.
\]

In the original variable they occur at
\[
\alpha=\frac{m}{6(K+1)}.
\]

Hence increasing \(K\):

\[
\text{widens additive averaging radius }6K
\]
while
\[
\text{narrowing the central frequency lobe on the sector lattice.}
\]

This makes the locality--frequency tradeoff calculable rather than rhetorical.

---

## 8. Honest role in the Goldbach program

The Fejer window supplies a fixed baseline satisfying all structural requirements:

- real and symmetric;
- nonnegative in output and frequency;
- supported on \(6\mathbb Z\), so no channel mixing;
- normalized at the target frequency;
- explicit physical radius and explicit multiplier.

It does **not** supply a pointwise minor-arc saving. By T7, even \(0\le\Omega_K\le1\) plus Parseval does not beat the binary energy barrier.

A fractional OFI window is worth pursuing only if it beats this Fejer benchmark in a proved post-extraction quantity:
\[
\text{weighted minor-arc budget}
+
\text{major-model distortion}
+
\text{dual/local tail}.
\]

---

## 9. Next concrete experiment/theorem

For each sector \(j\), compare a candidate OFI window with \(\nu^{(K)}\) under the same physical radius \(6K\). The required output is one of:

\[
\left|\mathcal I^{\mathfrak m}_{j,\Omega_u}(E)\right|
<
\left|\mathcal I^{\mathfrak m}_{j,\Omega_K}(E)\right|
\]
with a proved margin large enough to cover every reconstruction cost, or a stronger weighted mean-square inequality.

Without that comparison, the fractional branch remains a parametrization rather than an arithmetic improvement.