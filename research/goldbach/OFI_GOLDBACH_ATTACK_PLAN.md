# OFI Goldbach Attack Plan

**Status:** rigorous research program.  
**Goal:** force positivity of the prime-only sector coefficient
\[
\mathfrak G_j(E)>0
\]
for every admissible even integer \(E\), without confusing a smooth OFI representation with a prime-pair proof.

---

## 1. What the OFI PDF contributes

The proof spine uses only the OFI components that have a definite arithmetic job:

1. **Half-shift:** \(n+\tfrac12\) converts discrete sums into shifted integrals.
2. **Bernoulli splines:** encode the Euler--Maclaurin residual series.
3. **B-spline semigroup:** \(B_m*B_n=B_{m+n}\), giving exact convolutional synthesis.
4. **OFI/Riesz semigroup:** \(I^\alpha I^\beta=I^{\alpha+\beta}\), giving continuous-order transport.
5. **GL fractional differences:** provide the discrete fractional derivative interface.
6. **Character sectors:** \(\theta_\pm\) or equivalently the ordinary and \(\chi_3\)-twisted channels.

The 52-family catalogue is treated as a controlled library. It is not assumed that every family is relevant to Goldbach. The first proof route uses only four families:

- centered cardinal/fractional B-splines;
- Bernoulli splines;
- trigonometric L-splines as an oscillatory test branch;
- the Riesz/OFI limiting kernel.

---

## 2. The invariant arithmetic target

Let
\[
\theta(n)=\begin{cases}\log n,& n\text{ prime},\\0,&\text{otherwise},\end{cases}
\]
and, for primes larger than \(3\),
\[
\theta_+(n)=\theta(n)\mathbf 1_{n\equiv1\pmod6},
\qquad
\theta_-(n)=\theta(n)\mathbf 1_{n\equiv-1\pmod6}.
\]

Define the sector coefficients
\[
\mathfrak G_0=\theta_+*\theta_-,
\qquad
\mathfrak G_2=\theta_+*\theta_+,
\qquad
\mathfrak G_4=\theta_-*\theta_-.
\]

For every even \(E>6\), the one sector matching \(E\bmod6\) is positive if and only if \(E\) has a Goldbach representation by actual primes.

**Non-negotiable rule:** every OFI object in this program must eventually return a quantitative lower bound for this exact coefficient, or for a \(\Lambda\)-weighted version with an explicit prime-power subtraction.

---

## 3. The exact half-shift lift

For a finite cutoff \(N\), place the prime mass at
\[
x_n=n+\frac12.
\]
The half-shift gives
\[
\sum_{n=a}^{b}f(n)
=
\int_{a-1/2}^{b+1/2}f(x)\,dx
+\sum_{p\ge1}\frac{B_{2p}}{(2p)!}
\left[f^{(2p-1)}\right]_{a-1/2}^{b+1/2}
+R_P.
\]

Under this convention, the leading Bernoulli correction is
\[
\frac{B_2}{2!}=\frac1{12}.
\]

This is the convention used in OFI. Do not substitute a midpoint-rule coefficient from another normalization without reconciling the integration bounds.

---

## 4. B-spline coefficient engine

Let \(B_1\) be the centered boxcar and
\[
B_n=B_1^{*n}.
\]
Then
\[
B_m*B_n=B_{m+n}.
\]

For a branch \(\sigma\in\{+,-\}\), define the finite spline synthesis
\[
\Phi_{n,\sigma}^{(N)}(x)
=
\sum_{r\le N}\theta_\sigma(r)B_n\!\left(x-\left(r+\frac12\right)\right).
\]

By the convolution semigroup,
\[
\Phi_{m,\sigma}^{(N)}*\Phi_{n,\tau}^{(N)}
=
\sum_{E\le2N}\mathfrak G_{\sigma,\tau}^{(N)}(E)
B_{m+n}\left(x-(E+1)\right).
\]

### Gate A: exact extraction

Choose a dual family \(\widetilde B_{m+n}\) on the generated shift-invariant space and prove
\[
\left\langle
\Phi_{m,\sigma}^{(N)}*\Phi_{n,\tau}^{(N)},
\widetilde B_{m+n}(\cdot-(E+1))
\right\rangle
=
\mathfrak G_{\sigma,\tau}^{(N)}(E).
\]

Until this is proved, a spline correlation is only a visualization or estimator, not the Goldbach coefficient.

---

## 5. OFI transport operator

The B-spline multiplier is
\[
\widehat B_n(\xi)=\left(\frac{1-e^{-i\xi}}{i\xi}\right)^n.
\]
The OFI/Riesz multiplier is \(|\xi|^{-\alpha}\). Use the combined finite-cutoff test multiplier
\[
M_{n,\alpha}(\xi)
=
\left(\frac{1-e^{-i\xi}}{i\xi}\right)^n
|\xi|^{-\alpha}\chi_{|\xi|\ge\varepsilon},
\]
where the low-frequency cutoff \(\varepsilon>0\) is recorded explicitly and later removed only with a proof.

Define
\[
\widehat{\mathcal K_{n,\alpha,\varepsilon}f}(\xi)
=M_{n,\alpha}(\xi)\widehat f(\xi).
\]

The B-spline factor supplies compact-support reconstruction; the Riesz factor supplies fractional scale transport. The operator is not called prime-preserving until the coefficient extractor from Gate A has been applied.

### Gate B: semigroup consistency

Prove and numerically check the two identities separately:
\[
B_m*B_n=B_{m+n},
\qquad
I^\alpha I^\beta=I^{\alpha+\beta}.
\]
Then determine the exact composition law for \(\mathcal K_{n,\alpha,\varepsilon}\); do not assume it is a semigroup in both parameters without handling the cutoff.

---

## 6. Ostrowski descent estimate

The missing local link is an Ostrowski-type inequality controlling the descent from a continuous spline/OFI quantity to the exact dual coefficient.

Let
\[
H_{E,j}(x)
=
\bigl(\mathcal K\Phi_\sigma\bigr)*\bigl(\mathcal K\Phi_\tau\bigr)(x)
\]
for the sector \(j=(\sigma,\tau)\). Define a local window average around the Goldbach coordinate \(E+1\):
\[
\mathcal A_{E,j}(h)
=
\frac1h\int_{E+1-h/2}^{E+1+h/2}H_{E,j}(x)\,dx.
\]

The theorem to prove is an explicit bound
\[
\left|
\mathcal C_{E,j}-\mathcal A_{E,j}(h)
\right|
\le
\mathcal O_{n,\alpha}(h,E),
\]
where \(\mathcal C_{E,j}\) is the exact dual-extracted coefficient and \(\mathcal O\) is controlled by a derivative, variation norm, or fractional Sobolev norm of \(H_{E,j}\).

This is the sole role for Ostrowski: **local coefficient-versus-average control**. It does not prove prime density by itself.

### Gate C: certificate form

A continuous estimate certifies Goldbach only if
\[
\mathcal A_{E,j}(h)-\mathcal O_{n,\alpha}(h,E)>0.
\]
By Gate A this implies \(\mathfrak G_j(E)>0\).

---

## 7. Bernoulli/Euler--Maclaurin global correction

The local Ostrowski estimate controls sampling. Euler--Maclaurin controls the full finite sum-to-integral conversion. Keep the remainder ledger separate:
\[
\mathfrak G_j(E)
=
\mathcal M_j(E)
+\mathcal R^{\mathrm{EM}}_j(E)
+\mathcal R^{\mathrm{Ost}}_j(E)
+\mathcal R^{\mathrm{minor}}_j(E)
+\mathcal R^{\mathrm{pp}}_j(E).
\]

Here:

- \(\mathcal M_j\): major-arc or principal continuous term;
- \(\mathcal R^{\mathrm{EM}}_j\): Bernoulli/Euler--Maclaurin residual;
- \(\mathcal R^{\mathrm{Ost}}_j\): local spline descent error;
- \(\mathcal R^{\mathrm{minor}}_j\): oscillatory/minor-arc error;
- \(\mathcal R^{\mathrm{pp}}_j\): prime-power correction when using \(\Lambda\).

The \((-1,1/12)\) pair belongs only in the regularization and residual ledger. It cannot be inserted as a positive Goldbach contribution without a coefficientwise theorem.

---

## 8. Character-sector and spectral layer

Define
\[
A=\theta-\theta_3,
\qquad B=\chi_3\theta.
\]
Then
\[
\theta_+=\frac{A+B}{2},
\qquad
\theta_-=\frac{A-B}{2},
\]
and
\[
\mathfrak G_0=\frac14(A*A-B*B),
\]
\[
\mathfrak G_2=\frac14(A*A+2A*B+B*B),
\]
\[
\mathfrak G_4=\frac14(A*A-2A*B+B*B).
\]

For analytic estimates use the Mangoldt proxies
\[
-\frac{\zeta'}{\zeta}(s)=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},
\qquad
-\frac{L'}{L}(s,\chi_3)=\sum_{n\ge1}\frac{\chi_3(n)\Lambda(n)}{n^s}.
\]

The trigonometric and Euler-spline branches may be used to model the oscillatory Fourier-side objects, but the proof target remains a lower bound for the ordinary and twisted additive correlations—not merely an observed phase alignment.

---

## 9. Prime-power stripping

Let
\[
R_\Lambda(E)=\sum_{a+b=E}\Lambda(a)\Lambda(b),
\qquad G(E)=\sum_{a+b=E}\theta(a)\theta(b).
\]

A safe working requirement is
\[
R_\Lambda(E)-G(E)=O\!\left(\sqrt E\log^3E\right).
\]

Thus any \(\Lambda\)-based bound is adequate only if the positive main term dominates every other ledger term plus this prime-power allowance.

---

## 10. The theorem ladder

### T0 — exact arithmetic identity
Prove sector positivity is equivalent to a prime representation.

### T1 — B-spline reconstruction
Prove the dual-extraction identity in Gate A.

### T2 — OFI compatibility
Define \(\mathcal K\) on a rigorously specified finite-cutoff function space and prove all stated semigroup/adjointness properties.

### T3 — Ostrowski descent
Prove an explicit \(\mathcal O_{n,\alpha}(h,E)\) bound with constants and norm assumptions.

### T4 — Euler--Maclaurin residual
Prove a uniform or sectorwise bound for \(\mathcal R^{\mathrm{EM}}_j(E)\).

### T5 — spectral/major-minor theorem
Prove
\[
\mathcal M_j(E)
>
|\mathcal R^{\mathrm{EM}}_j(E)|
+|\mathcal R^{\mathrm{Ost}}_j(E)|
+|\mathcal R^{\mathrm{minor}}_j(E)|
+|\mathcal R^{\mathrm{pp}}_j(E)|.
\]

### T6 — finite completion
Verify every even target below the threshold from T5 by independent exact implementations.

Only T0 is complete as mathematics already written. T1--T4 are OFI-specific construction work. T5 is the true Goldbach bottleneck.

---

## 11. Experimental order

1. **Identity experiment:** \(B_1\), integer B-splines, exact integer convolution, no OFI reweighting.
2. **Bernoulli experiment:** verify half-shift and Euler--Maclaurin residuals on known sequences before primes.
3. **Dual-extraction experiment:** prove recovery for sparse artificial inputs, then \(\theta_\pm\).
4. **Ostrowski experiment:** measure candidate norm bounds for local descent and compare to exact errors.
5. **Fractional B-spline experiment:** vary order continuously while preserving the coefficient-extraction interface.
6. **Riesz limit experiment:** study the passage to nonlocal smoothing with a low-frequency control ledger.
7. **Character experiment:** run all tests separately in sectors \(0,2,4\bmod6\).
8. **Spectral experiment:** attach \(\Lambda\) and \(\chi_3\Lambda\) sums and test whether any OFI-derived estimate improves a provable error bound.

The experiment can reject bad branches quickly. A numerical pattern does not advance the proof unless it produces a deterministic estimate needed in T3--T5.

---

## 12. Family assignment

| OFI family | Goldbach assignment | Status |
|---|---|---|
| Bernoulli splines | Euler--Maclaurin residual and \(1/12\) ledger | core |
| Integer B-splines | exact convolution and dual extraction | core |
| Fractional/symmetric B-splines | continuous-order interpolation of core | core |
| GL family | discrete fractional difference checks | core |
| Riesz/OFI kernel | nonlocal limit and fractional scale transport | core |
| Trigonometric/Euler splines | oscillatory/Fourier test layer | secondary |
| Hyperbolic/E-splines | growth/decay stress tests | secondary |
| Chebyshev splines | optimal-node quadrature variant | secondary |
| Wavelet families | multiscale diagnostic, not proof coefficient | diagnostic |
| CAD/shape splines | no direct arithmetic role | excluded from proof spine |

---

## 13. Honest scorecard

- Exact sector target: complete.
- OFI architecture selection: complete.
- B-spline/Bernoulli/Ostrowski proof interfaces: specified, unproved.
- Uniform spectral lower bound: open.

The project is now a coherent OFI-native attack on Goldbach. Its next mathematical deliverable is **T1: exact dual B-spline coefficient extraction on the half-shift prime lattice**, followed immediately by **T3: an Ostrowski descent inequality for that extractor**.
