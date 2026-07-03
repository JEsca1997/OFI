# T14: Sector Major-Arc Residuals Reduce to Arithmetic-Progression Discrepancy

**Status:** exact reduction by residue decomposition and partial summation; no new prime-distribution estimate is claimed.  
**Purpose:** identify the precise analytic input needed to control the residuals in T13.

---

## 1. Sector sum on a rational arc

Let
\[
L=[q,6],\qquad \alpha=\frac aq+\beta,\qquad (a,q)=1.
\]
For \(\sigma\in\{+,-\}\),
\[
T_{\sigma,N}(\alpha)
=
\sum_{\substack{n\le N\\n\equiv\sigma\,({\rm mod}\,6)}}
\Lambda(n)e\!\left(\frac{an}{q}\right)e(\beta n).
\]

Because \(L\) is divisible by \(q\), the rational phase is constant on each residue class modulo \(L\). Thus, after separating the finitely many non-coprime residue classes (which only contain contributions from prime powers supported on primes dividing \(L\)),
\[
T_{\sigma,N}(\alpha)
=
\sum_{\substack{r\bmod L\\(r,L)=1\\r\equiv\sigma\,({\rm mod}\,6)}}
 e\!\left(\frac{ar}{q}\right)
\sum_{\substack{n\le N\\n\equiv r\,({\rm mod}\,L)}}
\Lambda(n)e(\beta n)
+\mathcal X_{\sigma}(a,q,\beta;N),
\]
where \(\mathcal X_\sigma\) is an explicit finite-prime exceptional term.

---

## 2. Arithmetic-progression discrepancy

Define
\[
\psi(x;L,r):=
\sum_{\substack{n\le x\\n\equiv r\,({\rm mod}\,L)}}\Lambda(n),
\]
and, for \((r,L)=1\),
\[
D(x;L,r):=\psi(x;L,r)-\frac{x}{\varphi(L)}.
\]

The exact sector discrepancy aggregate is
\[
\mathscr D_{\sigma}(x;a,q)
:=
\sum_{\substack{r\bmod L\\(r,L)=1\\r\equiv\sigma\,({\rm mod}\,6)}}
 e\!\left(\frac{ar}{q}\right)D(x;L,r).
\]

The corresponding principal amplitude is
\[
\mathfrak a_\sigma(a,q)
=
\frac{1}{\varphi(L)}
\sum_{\substack{r\bmod L\\(r,L)=1\\r\equiv\sigma\,({\rm mod}\,6)}}
 e\!\left(\frac{ar}{q}\right).
\]

This recovers the T13 main amplitude directly from AP equidistribution.

---

## 3. Partial summation identity

For any function \(F(x)=\sum_{n\le x}c_n\),
\[
\sum_{n\le N}c_ne(\beta n)
=e(\beta N)F(N)-2\pi i\beta\int_1^N e(\beta x)F(x)\,dx.
\]

Applying this residue class by residue class gives
\[
T_{\sigma,N}\!\left(\frac aq+\beta\right)
=
\mathfrak a_\sigma(a,q)V_N(\beta)
+\mathcal R^{\rm AP}_{\sigma}(a,q,\beta;N)
+\mathcal X_{\sigma}(a,q,\beta;N),
\]
where
\[
\mathcal R^{\rm AP}_{\sigma}
=e(\beta N)\mathscr D_{\sigma}(N;a,q)
-2\pi i\beta\int_1^N e(\beta x)\mathscr D_{\sigma}(x;a,q)\,dx.
\]

Consequently,
\[
\boxed{
|\mathcal R^{\rm AP}_{\sigma}(a,q,\beta;N)|
\le
(1+2\pi N|\beta|)
\sup_{x\le N}|\mathscr D_{\sigma}(x;a,q)|.
}
\]

This is the exact T13 residual reduction.

---

## 4. Safe bound for the finite exceptional term

Every non-coprime residue class modulo \(L\) contributing to the sector sum is supported on prime powers of primes dividing \(L\). Hence, crudely,
\[
|\mathcal X_{\sigma}(a,q,\beta;N)|
\ll \omega(L)(\log N)^2,
\]
where \(\omega(L)\) is the number of distinct prime divisors of \(L\).

This term is negligible relative to an order-\(N\) major model for fixed or slowly growing \(q\), but it must be carried explicitly in a fully quantitative proof.

---

## 5. Character decomposition of the discrepancy

The sector aggregate can be written through the ordinary and \(\chi_3\)-twisted progressions:
\[
\Lambda_\pm=\frac12(A_\Lambda\pm B_\Lambda),
\qquad
A_\Lambda=\Lambda-\Lambda_3,
\quad B_\Lambda=\chi_3\Lambda.
\]

Therefore the two needed discrepancy families are:

\[
\sum_{n\le x}\Lambda(n)e\!\left(\frac{an}{q}\right)
-\text{principal term},
\]

and

\[
\sum_{n\le x}\chi_3(n)\Lambda(n)e\!\left(\frac{an}{q}\right)
-\text{twisted principal term}.
\]

The second is the χ\(_3\)-twisted requirement encoded by \(-L'/L(s,\chi_3)\). It cannot be dropped in the \(2\) and \(4\pmod6\) channels.

---

## 6. T14 major-arc input target

A sufficient input for T13 is a bound, uniform for all rational centers in the chosen major arcs,
\[
\boxed{
\sup_{q\le Q}\sup_{(a,q)=1}\sup_{x\le N}
|\mathscr D_{\sigma}(x;a,q)|
\le N^{1-\delta}
}
\]
for some \(\delta>0\), together with a choice of widths satisfying
\[
N|\beta|\ll N^{o(1)}
\quad\text{on }\mathfrak M(Q,W;N).
\]

Then
\[
\mathcal R_{\sigma}(a,q,\beta;N)
\ll N^{1-\delta+o(1)},
\]
and the exact T13 major-arc error ledger may be estimated.

This is a target specification, not a claim that such a uniform estimate has been proved here.

---

## 7. What OFI can and cannot affect

The Fejér/OFI multiplier enters the major-arc integral only after these AP residuals are formed:
\[
\Omega_K(\alpha)
\bigl(P_\sigma\mathcal R_\tau+
\mathcal R_\sigma P_\tau+
\mathcal R_\sigma\mathcal R_\tau\bigr).
\]

Because \(0\le\Omega_K\le1\), it never enlarges the absolute residual bound. But it does not improve the AP discrepancy itself.

So the next true arithmetic question is:
\[
\boxed{
\text{Can the sector AP discrepancy be bounded uniformly on a major-arc range strong enough for T13?}
}
\]

Until then, the major-model lower bound remains conditional.