# T1 + T3: Boxcar Extraction and Ostrowski Certificate

**Status:** finite-cutoff theorem package.  
**Purpose:** make the first Goldbach spline stage exact before adding fractional Riesz transport, topology, or spectral estimates.

---

## 1. Why begin with the boxcar pair

The OFI spline hierarchy begins with the boxcar \(B_1\), its convolution powers \(B_n\), and the exact semigroup
\[
B_m*B_n=B_{m+n}.
\]

The lowest nontrivial Goldbach synthesis is therefore
\[
B_1*B_1=B_2,
\]
where \(B_2\) is the triangular B-spline. This case is special because its Gram matrix is explicitly tridiagonal and uniformly well conditioned. It gives a concrete exact coefficient extractor instead of an abstract promise of a dual frame.

We use the centered normalization
\[
b_1(x)=\mathbf 1_{[-1/2,1/2]}(x),
\qquad
b_2=b_1*b_1=(1-|x|)_+.
\]
Thus \(b_2\) is supported on \([-1,1]\), has unit integral, and is centered at zero.

---

## 2. Prime measures on the half-shift lattice

For a finite cutoff \(N\) and a residue branch \(\sigma\in\{+,-\}\), let
\[
\mu_{\sigma,N}
=
\sum_{r\le N}\theta_\sigma(r)\,\delta_{r+1/2}.
\]
The boxcar synthesis is
\[
\Phi_{\sigma,N}=b_1*\mu_{\sigma,N}
=
\sum_{r\le N}\theta_\sigma(r)
 b_1\left(x-\left(r+\frac12\right)\right).
\]

For two branches \(\sigma,\tau\), put
\[
H_{\sigma,\tau,N}
:=\Phi_{\sigma,N}*\Phi_{\tau,N}.
\]
By associativity, the half-shift identity, and \(b_1*b_1=b_2\),
\[
\boxed{
H_{\sigma,\tau,N}(x)
=
\sum_E
\mathfrak G^{(N)}_{\sigma,\tau}(E)
\,b_2\bigl(x-(E+1)\bigr),
}
\]
where
\[
\mathfrak G^{(N)}_{\sigma,\tau}(E)
=
\sum_{a+b=E}\theta_\sigma(a)\theta_\tau(b).
\]

This is an exact identity. The target Goldbach coefficient is literally the coefficient of the translate centered at \(E+1\).

---

## 3. Exact finite Gram extraction

Choose a finite consecutive index set \(I\) containing all relevant sums \(E\). Write
\[
g_E=\mathfrak G^{(N)}_{\sigma,\tau}(E),
\qquad
c_k=\left\langle H_{\sigma,\tau,N},b_2(\cdot-(k+1))\right\rangle_{L^2(\mathbb R)}.
\]
Then
\[
c=Ag,
\]
where \(A=(A_{kE})_{k,E\in I}\) is the Gram matrix
\[
A_{kE}
=
\left\langle b_2(\cdot-(E+1)),b_2(\cdot-(k+1))\right\rangle.
\]

A direct integration gives
\[
A_{kE}=
\begin{cases}
\frac23,&k=E,\\[4pt]
\frac16,&|k-E|=1,\\[4pt]
0,&|k-E|\ge2.
\end{cases}
\]

Hence \(A\) is symmetric tridiagonal Toeplitz. If \(|I|=M\), its eigenvalues are
\[
\lambda_j
=
\frac23+\frac13\cos\!\left(\frac{j\pi}{M+1}\right),
\qquad j=1,\dots,M.
\]
Therefore
\[
\frac13<\lambda_j<1,
\qquad
\|A^{-1}\|_2<3.
\]
Strict diagonal dominance also yields
\[
\|A^{-1}\|_\infty\le3.
\]

### Theorem T1 (exact boxcar coefficient extraction)

For every finite cutoff \(N\) and every sector pair \((\sigma,\tau)\),
\[
\boxed{
 g=A^{-1}c.
}
\]
In particular, the Goldbach coefficient is recovered exactly from the triangular-spline correlation with no continuum approximation and no number-theoretic assumption.

---

## 4. A B-spline-weighted Ostrowski estimate

Let \(H\) be any Lipschitz function. Since \(b_2\) is nonnegative, has unit integral, and is centered at \(0\),
\[
\left|
\int_{\mathbb R}H(x)b_2(x-y)\,dx-H(y)
\right|
\le
\operatorname{Lip}(H)
\int_{-1}^{1}|u|b_2(u)\,du.
\]
The triangular moment is
\[
\int_{-1}^{1}|u|(1-|u|)\,du=\frac13.
\]
Thus
\[
\boxed{
\left|
c_k-H(k+1)
\right|
\le
\frac13\operatorname{Lip}(H).
}
\]

This is the correct local Ostrowski role: it compares the B-spline weighted local average \(c_k\) to the center sample \(H(k+1)\). It does not claim that point samples alone are Goldbach coefficients.

---

## 5. Exact descent from samples to Goldbach coefficients

Let
\[
h_k=H(k+1).
\]
Combining \(c=Ag\) with the weighted Ostrowski estimate gives
\[
\|c-h\|_\infty
\le
\frac13\operatorname{Lip}(H).
\]
Hence
\[
\|g-A^{-1}h\|_\infty
\le
\|A^{-1}\|_\infty\|c-h\|_\infty
\le
\operatorname{Lip}(H).
\]

### Theorem T3 (finite boxcar descent certificate)

For every \(E\in I\),
\[
\boxed{
\mathfrak G^{(N)}_{\sigma,\tau}(E)
\ge
(A^{-1}h)_E-\operatorname{Lip}(H_{\sigma,\tau,N}).
}
\]

More generally, suppose a continuous or spectral procedure supplies an approximation \(\widehat h\) satisfying
\[
\|\widehat h-h\|_\infty\le\varepsilon.
\]
Then
\[
\boxed{
\mathfrak G^{(N)}_{\sigma,\tau}(E)
\ge
(A^{-1}\widehat h)_E
-\operatorname{Lip}(H_{\sigma,\tau,N})
-3\varepsilon.
}
\]

A strictly positive right-hand side is a rigorous finite-cutoff certificate of a prime-pair representation in that sector.

---

## 6. What this does and does not solve

### It does solve

- the exact half-shifted B-spline encoding of the sector coefficient;
- stable finite reconstruction of that coefficient;
- a concrete local average-to-sample error bound;
- the first precise place where an Ostrowski inequality belongs in the OFI Goldbach program.

### It does not solve

- a useful asymptotic upper bound on \(\operatorname{Lip}(H)\) small enough to certify all large \(E\);
- the minor-arc or twisted-character cancellation problem;
- the prime-power subtraction when replacing \(\theta\) by \(\Lambda\);
- the global lower bound required for strong Goldbach.

The estimate is a bridge theorem, not the final arithmetic inequality.

---

## 7. Next refinement: fractional order

The appropriate continuation is not to jump immediately to topology or Ricci flow. First replace \(b_2\) by a centered fractional B-spline \(\beta^\alpha\), while retaining:

1. a finite Gram matrix with a lower spectral bound;
2. an explicit or computable dual/reconstruction operator;
3. a weighted Ostrowski moment
\[
\int |u|\,\beta^\alpha(u)\,du;
\]
4. a controlled continuum limit toward the symmetric Riesz OFI kernel.

This is the exact place where the OFI semigroup and the B-spline semigroup can be fused without losing the discrete Goldbach coefficient.
