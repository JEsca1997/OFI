# T12: Fejer–B-Spline Factorization and the Major-Model Gate

**Status:** exact algebraic factorization and conditional major-model transfer.  
**Purpose:** make the sector-preserving Fejer baseline a literal discrete B-spline construction, then state precisely what it proves and what remains arithmetic.

---

## 1. The normalized discrete boxcar

On the rescaled lattice \(n\in\mathbb Z\), define
\[
b^{(K)}(k):=\frac{1}{K+1}\mathbf 1_{\{0,1,\dots,K\}}(k).
\]
Let its reflection be
\[
\widetilde b^{(K)}(k):=b^{(K)}(-k).
\]

Both are probability kernels:
\[
b^{(K)}\ge0,
\qquad
\sum_k b^{(K)}(k)=1.
\]

---

## 2. Exact discrete B-spline / Fejer identity

Their convolution is
\[
\begin{aligned}
(b^{(K)}*\widetilde b^{(K)})(k)
&=\frac{1}{(K+1)^2}
\#\{(r,s)\in\{0,\dots,K\}^2:r-s=k\}\\
&=
\begin{cases}
\dfrac{K+1-|k|}{(K+1)^2},& |k|\le K,\\[6pt]
0,&|k|>K.
\end{cases}
\end{aligned}
\]

Therefore
\[
\boxed{\nu^{(K)}=b^{(K)}*\widetilde b^{(K)}.}
\]

This is the exact discrete triangle/B-spline factorization behind T11.

Its Fourier multiplier factors as
\[
\widehat\nu_K(\beta)
=
\left|\widehat b^{(K)}(\beta)\right|^2,
\]
where
\[
\widehat b^{(K)}(\beta)
=\frac1{K+1}\sum_{r=0}^{K}e(r\beta).
\]

Thus Fejer is not foreign to the OFI spline spine: it is the positive discrete order-two spline energy kernel on the sector lattice.

---

## 3. Sector-safe original-coordinate form

Lift \(b^{(K)}\) to the Goldbach target coordinate by support on \(6\mathbb Z\):
\[
B^{(K)}(6k)=b^{(K)}(k),
\qquad
B^{(K)}(h)=0\quad(h\notin6\mathbb Z).
\]

Then
\[
\omega^{(K)}=B^{(K)}*\widetilde B^{(K)},
\]
and its multiplier is
\[
\Omega_K(\alpha)=\left|\widehat B^{(K)}(\alpha)\right|^2
=\left|
\frac1{K+1}\sum_{r=0}^{K}e(6r\alpha)
\right|^2.
\]

Hence
\[
0\le\Omega_K(\alpha)\le1,
\qquad
\Omega_K(\alpha+1/6)=\Omega_K(\alpha).
\]

The mod-\(6\) sector is preserved by construction.

---

## 4. Exact positive major-model transfer

Fix a sector \(j\) and suppose a model sequence \(\mathcal M_j(n)\) has a uniform local lower bound
\[
\mathcal M_j(m)\ge m_0(n)>0
\qquad(|m-n|\le K).
\]

Because \(\nu^{(K)}\) is a probability kernel,
\[
\begin{aligned}
(\nu^{(K)}*\mathcal M_j)(n)
&=\sum_{|k|\le K}\nu^{(K)}_k\mathcal M_j(n-k)\\
&\ge m_0(n)\sum_k\nu^{(K)}_k\\
&=m_0(n).
\end{aligned}
\]

Thus:
\[
\boxed{
\text{positive model main term on a sector window}
\Longrightarrow
\text{positive Fejer-windowed model main term.}
}
\]

No rational-by-rational preservation assertion is needed for this coefficient-side statement.

---

## 5. Conditional Goldbach major-model instance

Suppose the sector major model has the form
\[
\mathcal M_j(n)=\mathfrak S_j(6n+j)(6n+j),
\]
where, on the desired target range and sector,
\[
\mathfrak S_j(6m+j)\ge s_j>0.
\]

For \(n>K\), every \(m\in[n-K,n+K]\) satisfies
\[
6m+j\ge 6(n-K)+j.
\]
Hence
\[
\boxed{
(\nu^{(K)}*\mathcal M_j)(n)
\ge s_j\,[6(n-K)+j].
}
\]

This is a conditional lower bound for the **windowed model main term**. It does not prove the corresponding asymptotic formula for the actual prime correlation; that remains the circle-method major-arc theorem.

---

## 6. Factorization does not bypass the energy barrier

For any sequence \(f\),
\[
\nu^{(K)}*f
= B^{(K)}*\widetilde B^{(K)}*f.
\]
The multiplier is nonnegative because it is a modulus square, but that does not provide a power-saving minor-arc bound. T7 still applies:
\[
\left|\int_{\mathfrak m}\Omega_K T_\sigma T_\tau e(-E\alpha)d\alpha\right|
\]
cannot be made \(o(E)\) from boundedness of \(\Omega_K\) and global \(L^2\) energy alone.

The Fejer/B-spline factorization supplies a stable positive benchmark, not a cancellation theorem.

---

## 7. Correct OFI comparison criterion

Let \(\omega_u\) be a candidate sector-preserving OFI output kernel at the same physical radius \(6K\). It earns promotion over the Fejer/B-spline baseline only after proving all three:

1. **Major-model gate:** its coefficient-side weighted main model is bounded below by a positive order-\(E\) quantity;
2. **Minor-arc gate:** its denominator-stratified weighted minor-arc budget is strictly smaller by a quantified margin;
3. **Extraction gate:** its dual/truncation cost is smaller than that margin.

Symbolically, for a target sector \(j\),
\[
\mathfrak E^{\mathrm{minor}}_{u,j}
+\mathfrak E^{\mathrm{major}}_{u,j}
+\mathfrak E^{\mathrm{dual}}_{u,j}
<
\mathfrak E^{\mathrm{minor}}_{\mathrm{Fej},K,j}
+\mathfrak E^{\mathrm{major}}_{\mathrm{Fej},K,j}
+\mathfrak E^{\mathrm{dual}}_{\mathrm{Fej},K,j}.
\]

Without this post-ledger comparison, the fractional order is an alternative parametrization, not a proved advance.

---

## 8. Next arithmetic theorem

The next nontrivial theorem is now sharply stated:
\[
\boxed{
\text{Prove a sectorwise major-arc approximation for the Fejer-windowed Mangoldt correlation,
with a positive model lower bound and an explicit error.}
}
\]

Only after that should a candidate OFI/Riesz window be compared against the Fejer baseline on the same sector lattice.