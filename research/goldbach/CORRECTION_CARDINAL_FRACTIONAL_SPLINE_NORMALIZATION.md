# Correction: Cardinal Fractional B-Spline Normalization

**Scope:** This correction supersedes the kernel-identification statements in `T2_FRACTIONAL_BSPLINE_GATE.md` and `T2A_FRACTIONAL_FRAME_BOUND.md` that identify
\[
\left|\frac{2\sin(\xi/2)}{\xi}\right|^u
\]
with the cardinal B-spline semigroup itself.

## 1. The issue

The centered cardinal boxcar has Fourier transform
\[
\widehat b_1(\xi)=\frac{2\sin(\xi/2)}{\xi},
\]
not its absolute value. Outside the first Nyquist cell, this multiplier changes sign.

Therefore the even nonnegative multiplier
\[
\left|\frac{2\sin(\xi/2)}{\xi}\right|^u
\]
is useful for magnitude and Gram estimates, but at \(u=1\) it is **not** the boxcar kernel. It must not be called the cardinal B-spline semigroup without qualification.

## 2. Correct cardinal semigroup family

Use the order parameter \(s>0\) and define the cardinal fractional B-spline by the principal-branch Fourier multiplier
\[
\widehat{\beta_s}(\xi)
=
\left(\frac{1-e^{-i\xi}}{i\xi}\right)^s.
\]
For integral \(s=n\), this is the standard degree-\(n-1\) cardinal B-spline. In particular,
\[
\beta_1=\mathbf 1_{[0,1]},
\qquad
\beta_2=\beta_1*\beta_1.
\]

The exact semigroup identity is
\[
\boxed{\beta_s*\beta_t=\beta_{s+t}.}
\]

A centered version is obtained by translation:
\[
\gamma_s(x)=\beta_s\left(x+\frac s2\right),
\]
so that
\[
\widehat{\gamma_s}(\xi)
=e^{is\xi/2}\left(\frac{1-e^{-i\xi}}{i\xi}\right)^s.
\]
At integer order this recovers the centered cardinal B-spline chain.

## 3. Why the previous frame estimates still apply

The translate Gram symbol depends on magnitude squared. For the corrected cardinal family,
\[
\left|\widehat{\beta_s}(\xi)\right|
=
\left|\widehat{\gamma_s}(\xi)\right|
=
\left|\frac{2\sin(\xi/2)}{\xi}\right|^s.
\]

Therefore the Gram symbol is exactly
\[
P_s(\omega)
=
\sum_{k\in\mathbb Z}
\left|\widehat{\beta_s}(\omega+2\pi k)\right|^2
=
\sum_{k\in\mathbb Z}
\left|\frac{2\sin((\omega+2\pi k)/2)}{\omega+2\pi k}\right|^{2s}.
\]

Hence the lower and upper frame estimates derived in T2-A remain valid for the **corrected cardinal fractional family**:
\[
\left(\frac2\pi\right)^{2s}
\le P_s(\omega)
\le
1+2\left(\frac2\pi\right)^{2s}(1-2^{-2s})\zeta(2s),
\qquad s>\frac12.
\]

What changes is only the interpretation of the primal kernel: it is a cardinal/centered fractional B-spline with a phase branch, not an even positive kernel.

## 4. Corrected Goldbach synthesis

For half-shifted prime coefficients, define
\[
\Phi^{(s)}_{\sigma,N}(x)
=
\sum_{r\le N}\theta_\sigma(r)
\gamma_s\left(x-\left(r+\frac12\right)\right).
\]
Then
\[
\Phi^{(s)}_{\sigma,N}*\Phi^{(t)}_{\tau,N}(x)
=
\sum_E
\mathfrak G^{(N)}_{\sigma,\tau}(E)
\gamma_{s+t}(x-(E+1)).
\]

The coefficient-extraction and frame arguments proceed using the Gram symbol above. The correct primal family now genuinely extends
\[
\text{boxcar}\to\text{triangle}\to\text{integer B-splines}\to\text{fractional cardinal B-splines}.
\]

## 5. Two distinct symmetric objects

Do not conflate:

1. **Centered fractional cardinal B-splines** \(\gamma_s\), which preserve the cardinal semigroup and exact B-spline ancestry; and
2. **Even modulus kernels** with multiplier \(|2\sin(\xi/2)/\xi|^s\), which are useful as symmetric spectral envelopes and for frame bounds.

The first belongs in the exact Goldbach representation. The second may be used as a symmetric OFI/Riesz diagnostic or energy weight, but not as a literal replacement for the boxcar chain.

## 6. Effect on the proof status

- T1 boxcar/triangle extraction remains valid.
- T2-A frame corridor remains valid after replacing the primal notation with \(\beta_s\) or \(\gamma_s\).
- T3 local-dual construction remains valid.
- No Goldbach positivity estimate has been altered or gained.

This correction improves the framework because the fractional extension now respects the exact cardinal B-spline semigroup at every integer anchor.