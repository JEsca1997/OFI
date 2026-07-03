# Correction: The Goldbach Operator Is a Reflected Additive Convolution

**Status:** exact correction of the core arithmetic/Fourier object.  
**Effect:** the former correlation-centered spine is quarantined as an auxiliary energy technology; it is not the Goldbach representation function itself.

---

## 1. Two different arithmetic objects

For a finitely supported arithmetic sequence \(f\), define
\[
\Gamma_f(E):=(f*f)(E)=\sum_{k\in\mathbb Z}f(k)f(E-k).
\]

For prime weights \(\theta(n)=\log p\) at primes and \(0\) otherwise,
\[
\boxed{
\Gamma_\theta(E)=\sum_{k=1}^{E-1}\theta(k)\theta(E-k).
}
\]

This is the weighted Goldbach representation function. It is an additive **Hankel/reflection pairing**: the second input is evaluated at \(E-k\).

By contrast, the shift correlation is
\[
\mathcal C_f(h):=\sum_kf(k)\overline{f(k+h)}.
\]

It is a **Toeplitz/translation pairing** and naturally measures prime pairs at gap \(h\). In particular,
\[
\Gamma_\theta(E)\ne\mathcal C_\theta(E)
\]
in general.

Example:
\[
\Gamma_{\mathbf1_{\mathbb P}}(8)=2
\quad\text{(ordered pairs \((3,5),(5,3)\))},
\]
while
\[
\mathcal C_{\mathbf1_{\mathbb P}}(8)\ge2
\quad\text{from \((3,11),(5,13)\)},
\]
and the terms count different prime configurations.

---

## 2. Correct Fourier identity

Let
\[
S_N(\alpha):=\sum_{n\le N}\theta(n)e(\alpha n).
\]
Then Fourier inversion gives the exact coefficient identity
\[
\boxed{
\Gamma_{\theta,N}(E)
=
\int_0^1S_N(\alpha)^2e(-E\alpha)\,d\alpha.
}
\]

The correlation identity is instead
\[
\mathcal C_{\theta,N}(h)
=
\int_0^1|S_N(\alpha)|^2e(-h\alpha)\,d\alpha.
\]

Therefore:
\[
\boxed{
S_N(\alpha)^2\text{ is the Goldbach integrand};
\qquad |S_N(\alpha)|^2\text{ is the prime-gap correlation integrand}.
}
\]

No argument may exchange these expressions without a separately proved transformation.

---

## 3. Ordered versus unordered counts

Let
\[
R(E):=\sum_{k=1}^{E-1}\mathbf1_{\mathbb P}(k)\mathbf1_{\mathbb P}(E-k).
\]
Then \(R(E)\) counts ordered representations. The unordered count is
\[
\boxed{
G(E)=\frac12\bigl(R(E)+\mathbf1_{\mathbb P}(E/2)\bigr)
}
\]
for even \(E\), because a noncentral pair is counted twice and the midpoint prime pair is counted once.

For Goldbach positivity it is enough to prove
\[
R(E)>0.
\]

---

## 4. Correct sector decomposition

Using
\[
\theta_\pm(n):=\theta(n)\mathbf1_{n\equiv\pm1\pmod6},
\]
the three nontrivial even residue classes are governed by the correct convolutions
\[
\Gamma_0:=\theta_+*\theta_-,
\qquad
\Gamma_2:=\theta_+*\theta_+,
\qquad
\Gamma_4:=\theta_-*\theta_-.
\]

Equivalently, with
\[
S_{\pm,N}(\alpha)=\sum_{n\le N}\theta_\pm(n)e(\alpha n),
\]
\[
\Gamma_{0,N}(E)=\int_0^1S_{+,N}(\alpha)S_{-,N}(\alpha)e(-E\alpha)d\alpha,
\]
\[
\Gamma_{2,N}(E)=\int_0^1S_{+,N}(\alpha)^2e(-E\alpha)d\alpha,
\]
\[
\Gamma_{4,N}(E)=\int_0^1S_{-,N}(\alpha)^2e(-E\alpha)d\alpha.
\]

This part of the prior sector notation survives, but every analysis must retain the product \(S_\sigma S_\tau\), not replace it with a modulus square.

---

## 5. Legitimate reflected OFI window

Let \(\Omega_u\) be a sector-preserving output multiplier, e.g.
\[
\Omega_u(\alpha+1/6)=\Omega_u(\alpha).
\]

Define the windowed Goldbach coefficient
\[
\boxed{
\Gamma^{\Omega_u}_{\sigma,\tau}(E)
:=
\int_0^1\Omega_u(\alpha)
S_{\sigma,N}(\alpha)S_{\tau,N}(\alpha)e(-E\alpha)\,d\alpha.
}
\]

If
\[
\Omega_u(\alpha)=\sum_h\omega_h e(\alpha h),
\]
then exactly
\[
\boxed{
\Gamma^{\Omega_u}_{\sigma,\tau}(E)
=
\sum_h\omega_h\Gamma_{\sigma,\tau}(E-h).
}
\]

Thus an OFI/Fourier multiplier still performs an output-side average of nearby Goldbach coefficients. It does **not** directly establish the point coefficient \(\Gamma(E)\) unless an extraction/local-deficit theorem is supplied.

---

## 6. What survives from T17--T30

The prior localized-energy framework may survive only after this correction.

For a correct Goldbach bilinear product
\[
F_{\sigma,\tau}(\alpha):=S_{\sigma,N}(\alpha)S_{\tau,N}(\alpha),
\]
the far-minor energy is
\[
\boxed{
\mathfrak Q^{\rm GB}_{\mathfrak F,\Omega}
:=
\int_0^1\chi_{\mathfrak F}(\alpha)|\Omega(\alpha)|^2
|S_{\sigma,N}(\alpha)S_{\tau,N}(\alpha)|^2d\alpha.
}
\]

This is a legitimate density-one control target because Parseval gives a mean square of the *windowed Goldbach coefficient errors*.

However, it is not the same object as a direct prime-gap autocorrelation. Any reuse of T21--T30 must rederive its coefficient expansion from \(S_\sigma S_\tau\) and verify every variable/sector restriction.

The following are retained only as methodological warnings:

\[
\text{positive final energy requires earlier cancellation},
\]
\[
\text{generic large sieve after full convolution loses structure},
\]
\[
\text{window smoothing cannot prove pointwise positivity by itself}.
\]

The following are **not** inherited as Goldbach theorems:

\[
\text{a shift-autocorrelation identity},
\qquad
\text{a T23 lattice expansion derived for a different coefficient problem},
\qquad
\text{any claimed OFIPrimeNormal implication based solely on nonnegative gap sums}.
\]

---

## 7. Correct analytic target

The density-one branch now starts from
\[
\Gamma_{\sigma,\tau}(E)
=
\mathcal M_{\sigma,\tau}(E)+\mathcal R_{\sigma,\tau}(E),
\]
where \(\mathcal M\) is the weighted singular-series major model and \(\mathcal R\) is the exact residual for the reflected convolution.

A valid mean-square target is
\[
\boxed{
\sum_{E\asymp X\atop E\equiv j(6)}
|\mathcal R_{\sigma_j,\tau_j}(E)|^2
\ll X^{3-\eta}.
}
\]

Together with a uniform positive major lower bound
\[
\mathcal M_{\sigma_j,\tau_j}(E)\ge cX,
\]
this yields a density-one conclusion by Chebyshev, subject to the existing prime-power and window-extraction ledgers.

This estimate is unproved. The correction identifies the right residual to estimate.

---

## 8. Immediate repository consequence

The next formalization files should establish only exact identities:

1. ordered reflected convolution equals the Fourier coefficient of \(S^2\);
2. unordered/ordered count conversion;
3. the sector products for residues \(0,2,4\pmod6\);
4. output-window convolution identity;
5. explicit separation of Goldbach convolution from prime-gap autocorrelation.

No Goldbach theorem should cite a shift-autocorrelation lemma unless a new bridge theorem is written and proved.

---

## 9. Outcome

The corrected spine is
\[
\text{reflected additive convolution}
\to
\text{sector Fourier product }S_\sigma S_\tau
\to
\text{major/minor residual for that product}
\to
\text{mean-square or pointwise control}
\to
\text{Goldbach positivity}.
\]

This is a reset of the core operator, not a proof of the missing arithmetic estimate.