# T2-A: Fractional Spline Frame-Stability Corridor

**Status:** proved for the centered symmetric Fourier-defined family below.  
**Purpose:** close the translate-stability half of T2 with explicit constants.

---

## 1. Centered fractional semigroup kernel

For a semigroup order \(u>0\), define the centered symmetric fractional B-spline \(\mathsf B_u\) by
\[
\widehat{\mathsf B_u}(\xi)
=
\left|\frac{2\sin(\xi/2)}{\xi}\right|^u,
\]
with value \(1\) at \(\xi=0\).

The order is chosen so that
\[
\mathsf B_s*\mathsf B_t=\mathsf B_{s+t}.
\]
At \(u=1\) it is the centered boxcar and at \(u=2\) the centered triangular spline.

This is the symmetric Fourier-side version of the fractional B-spline chain in OFI.

---

## 2. Translate Gram symbol

For integer translates, define
\[
P_u(\omega)
=
\sum_{k\in\mathbb Z}
\left|\widehat{\mathsf B_u}(\omega+2\pi k)\right|^2,
\qquad \omega\in[-\pi,\pi].
\]

The translate family is stable exactly when
\[
0<A_u\le P_u(\omega)\le B_u<\infty.
\]

---

## 3. Lower frame bound

For \(|\omega|\le\pi\), the \(k=0\) term alone gives
\[
P_u(\omega)
\ge
\left|\frac{2\sin(\omega/2)}{\omega}\right|^{2u}.
\]

The function
\[
q(x)=\frac{2\sin(x/2)}{x}
\]
is positive and decreasing on \([0,\pi]\), with \(q(0)=1\) and \(q(\pi)=2/\pi\). Hence
\[
\boxed{
P_u(\omega)\ge A_u:=\left(\frac2\pi\right)^{2u}>0.
}
\]

No cancellation estimate is needed: the frame lower bound follows from the central alias.

---

## 4. Upper frame bound

For \(k\ne0\), use \(|2\sin((\omega+2\pi k)/2)|=|2\sin(\omega/2)|\le2\), and, for \(|\omega|\le\pi\),
\[
|\omega+2\pi k|\ge\pi(2|k|-1).
\]
Therefore
\[
P_u(\omega)
\le
1+
2\sum_{k=1}^{\infty}
\left(\frac{2}{\pi(2k-1)}\right)^{2u}
=:B_u.
\]

The series converges exactly for
\[
\boxed{u>\frac12.}
\]

Thus, for every \(u>1/2\),
\[
\boxed{
\left(\frac2\pi\right)^{2u}
\le P_u(\omega)\le
1+2\left(\frac2\pi\right)^{2u}
\sum_{k=1}^{\infty}(2k-1)^{-2u}<\infty.
}
\]

Equivalently,
\[
B_u
=
1+2\left(\frac2\pi\right)^{2u}
\bigl(1-2^{-2u}\bigr)\zeta(2u).
\]

---

## 5. T2-A theorem

### Theorem (stable fractional translate corridor)

For every semigroup order
\[
u>\frac12,
\]
the integer translates
\[
\{\mathsf B_u(\cdot-k):k\in\mathbb Z\}
\]
form a stable Riesz sequence in their closed shift-invariant span. Its Gram symbol is bounded between \(A_u\) and \(B_u\) above.

Consequently, the canonical dual is defined by
\[
\widehat{\widetilde{\mathsf B}_u}(\omega)
=
\frac{\widehat{\mathsf B_u}(\omega)}{P_u(\omega)}
\]
periodically on the fundamental frequency cell, and has the biorthogonality relation
\[
\left\langle
\mathsf B_u(\cdot-E),
\widetilde{\mathsf B}_u(\cdot-k)
\right\rangle
=\delta_{Ek}.
\]

---

## 6. Goldbach consequence

Take synthesis orders \(s,t>0\) with
\[
u=s+t>\frac12.
\]
Then for the half-shifted prime spline field
\[
H^{(s,t)}_{\sigma,\tau,N}
=
\Phi^{(s)}_{\sigma,N}*\Phi^{(t)}_{\tau,N}
=
\sum_E\mathfrak G^{(N)}_{\sigma,\tau}(E)
\mathsf B_\nu(\cdot-(E+1)),
\]
the coefficient is recovered exactly by
\[
\boxed{
\mathfrak G^{(N)}_{\sigma,\tau}(E)
=
\left\langle
H^{(s,t)}_{\sigma,\tau,N},
\widetilde{\mathsf B}_\nu(\cdot-(E+1))
\right\rangle.
}
\]

Therefore T2-A is closed for the stated kernel convention.

---

## 7. What remains open: T2-B

Frame stability alone does not give the local Ostrowski constant
\[
M_\nu
=
\int_{\mathbb R}|x|\,
\left|\widetilde{\mathsf B}_\nu(x)\right|\,dx.
\]

The next theorem must either:

1. prove \(M_\nu<\infty\) on a useful subrange of \(\nu\); or
2. replace point-sampling Ostrowski descent with a bounded local functional whose dual window has a known finite first moment.

The second route may be better: use a compact test window to estimate the Gram coefficients first, then apply the stable inverse. This avoids requiring an unnecessarily strong global first moment from the canonical dual.

---

## 8. Safe order corridor

The exact extraction corridor is now
\[
\boxed{s+t>\frac12.}
\]

For the symmetric balanced choice \(s=t=r\), this is
\[
r>\frac14.
\]

Recommended first comparisons:

\[
(r,r)=(1,1)\quad(\nu=2),
\]
\[
(r,r)=\left(1+\frac1{24},1+\frac1{24}\right)
\quad\left(\nu=2+\frac1{12}\right),
\]
\[
(r,r)=\left(\frac12,\frac12\right)\quad(\nu=1),
\]
\[
(r,r)=\left(\frac13,\frac13\right)\quad\left(\nu=\frac23\right).
\]

All pass T2-A. They differ in locality, Fourier decay, and the still-unresolved T2-B local-descent constant.

---

## 9. Interpretation

This theorem provides exactly what the Goldbach program needs from OFI at this stage:

- a real-valued continuous order;
- semigroup composition;
- exact retention of the discrete prime correlation through stable extraction;
- an explicit lower frame bound preventing information loss under the fractional lift.

It does **not** yield a lower bound for prime correlations. That remains the arithmetic/spectral stage.