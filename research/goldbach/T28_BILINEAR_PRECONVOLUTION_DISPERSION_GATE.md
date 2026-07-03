# T28: Bilinear Preconvolution Dispersion Gate

**Status:** exact partial Gram reduction for T27 and a sufficient preconvolution operator theorem; no dispersion estimate is claimed.  
**Purpose:** identify the stage at which a proof must gain before the full additive-convolution energy \(\sum_n|C(n)|^2\) is formed.

---

## 1. Why T27 must be improved before convolution

Let
\[
A_\alpha:=\mathcal B_1(\alpha)
=\sum_{m,n}a_{m,n}e(\alpha mn),
\qquad
B_\alpha:=\mathcal B_2(\alpha)
=\sum_{u,v}b_{u,v}e(\alpha uv),
\]
so that
\[
F(\alpha)=A_\alpha B_\alpha.
\]

The generic large sieve applied only after forming
\[
F(\alpha)=\sum_tC(t)e(\alpha t)
\]
returns a bound involving
\[
\sum_t|C(t)|^2.
\]

That is precisely the zero-shift collision energy isolated in T24. Consequently any proof that first compresses \(A_\alpha B_\alpha\) into \(C\) and then applies a generic sampling theorem has already lost the desired arithmetic structure.

The gain, if it exists, must occur at the bilinear level.

---

## 2. Exact partial Gram kernel

Let \(\mathcal A=\{\alpha_1,\dots,\alpha_J\}\) be the \(\delta\)-separated far-minor sample set of T27, and write
\[
K_{\mathcal A}(h):=\sum_{j=1}^Je(\alpha_j h).
\]

Expanding only the second factor defines the coefficient-sensitive kernel
\[
\boxed{
\mathscr K_B\big((m,n),(m',n')\big)
:=
\sum_{u,v,u',v'}
 b_{u,v}\overline{b_{u',v'}}
 K_{\mathcal A}\!\left(mn-m'n'+uv-u'v'\right).
}
\]

Then the sampled product energy has the exact representation
\[
\boxed{
\sum_{j=1}^J|A_{\alpha_j}B_{\alpha_j}|^2
=
\sum_{m,n,m',n'}
 a_{m,n}\overline{a_{m',n'}}
 \mathscr K_B\big((m,n),(m',n')\big).
}
\]

Interchanging the roles of \(A\) and \(B\) gives the symmetric alternate reduction.

---

## 3. Positivity and the correct kind of cancellation

The full matrix in Section 2 is positive semidefinite because it represents
\[
\sum_{j=1}^J|A_{\alpha_j}B_{\alpha_j}|^2\ge0.
\]

Therefore the required saving cannot come from claiming that the total energy has arbitrary sign cancellation. It must come from an upper bound for the operator norm of \(\mathscr K_B\) on the structured coefficient vector \(a\), or from a decomposition that proves the same bound.

The decisive difference from the generic large sieve is that \(\mathscr K_B\) still contains:

\[
\text{the second bilinear coefficients }b_{u,v},
\qquad
\text{the product-difference phase }uv-u'v',
\qquad
\text{the far-minor sample kernel }K_{\mathcal A}.
\]

---

## 4. A sufficient preconvolution dispersion theorem

For the relevant dyadic ranges, a proof-moving theorem would be an estimate of the form
\[
\boxed{
\sum_{m,n,m',n'}
 a_{m,n}\overline{a_{m',n'}}
 \mathscr K_B\big((m,n),(m',n')\big)
\ll
\delta^{-1}X^{3-\eta}.
}
\]

Uniformity must cover the actual coefficient classes produced by the chosen combinatorial identity for \(\Lambda\), including their divisor/logarithmic weights and sector restrictions.

This estimate directly implies the separated-frequency large-values input required in T26 after the standard maximal-separated-set covering step.

---

## 5. Diagonal/off-diagonal decomposition before convolution

Split the outer variables according to
\[
\Delta_1:=mn-m'n'.
\]
Then
\[
\mathscr K_B\big((m,n),(m',n')\big)
=
\sum_{u,v,u',v'}
 b_{u,v}\overline{b_{u',v'}}
 K_{\mathcal A}\big(\Delta_1+uv-u'v'\big).
\]

The literal outer diagonal \(\Delta_1=0\) is not enough to identify the dangerous mass: by T23 it includes the full gcd-lattice family
\[
(m,n)=(da,b\ell),
\qquad
(m',n')=(db,a\ell),
qquad(a,b)=1.
\]

The desired theorem must therefore control both:

\[
\Delta_1=0\text{ multiplicative-collision strata},
\qquad
\Delta_1\ne0\text{ product-difference strata},
\]
against the *same* inner bilinear sampling kernel.

---

## 6. Far-minor dependence cannot be dropped

A bound based only on
\[
|K_{\mathcal A}(h)|\le J
\]
or on absolute values of the \(u,v,u',v'\) sums recovers a collision count and does not yield the intended saving.

The far-minor location of the sample frequencies must enter before absolute values through an estimate for exponential sums of the schematic form
\[
\sum_{u,v,u',v'}
 b_{u,v}\overline{b_{u',v'}}
 e\bigl(\alpha(uv-u'v')\bigr),
\qquad
\alpha\in\operatorname{supp}(w),
\]
or through an equivalent dual/spectral formulation.

This is the precise point where a bilinear large-values theorem, a dispersion argument, or a spectral/Kloosterman mechanism could produce a power saving.

---

## 7. GCD-lattice insertion

Applying T23 to the outer difference \(\Delta_1=s\) gives
\[
(m,m')=(da,db),
qquad
an-bn'=s/d,
qquad(a,b)=1.
\]

Thus the left side of the target in Section 4 can be reorganized as a sum over
\[
\text{outer gcd }d,
\quad
\text{coprime slopes }(a,b),
\quad
\text{lattice coordinate }\ell,
\quad
\text{inner bilinear kernel }\mathscr K_B.
\]

The parameterization makes the arithmetic geometry explicit, but it does not by itself improve the operator norm. Any claimed OFI/Ruelle/Riesz contribution must supply a quantitative estimate for this reorganized kernel.

---

## 8. Two ways the theorem could be proved

A valid proof may take either route:

### P-D1. Direct bilinear dispersion
Prove the Section 4 bound directly by exploiting cancellation in the product-difference phases and the far-minor frequency spacing.

### P-D2. Conditional large-values for one factor
Partition the samples according to the size of \(|B_{\alpha_j}|\), prove a strong large-values estimate for \(B\) on each stratum, and apply a compatible sampling estimate for \(A\). The threshold losses must sum to \(\delta^{-1}X^{3-\eta}\).

Neither route permits replacing the second factor by a global supremum unless that supremum is independently strong enough to preserve a power saving.

---

## 9. Outcome

T28 places the first proof-moving inequality at the correct stage:
\[
\text{before }A*B\text{ is compressed into }C.
\]

The density-one branch now needs a coefficient-sensitive far-minor operator-norm gain for \(\mathscr K_B\), or its symmetric counterpart. This is narrower and more actionable than the full zero-shift energy request, while remaining exactly equivalent to the sampled bilinear energy.