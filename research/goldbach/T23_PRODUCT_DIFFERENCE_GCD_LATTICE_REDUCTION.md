# T23: Product-Difference Correlations on GCD Lattices

**Status:** exact solvability, parametrization, and divisor-stratified reduction for the four-variable correlations in T22; no cancellation estimate is claimed.  
**Purpose:** make the arithmetic geometry of
\[
mn-m'n'=s
\]
explicit, so a later dispersion or OFI-derived estimate has a concrete divisor-lattice target.

---

## 1. The product-difference correlation

Consider one factor from T22:
\[
\mathcal R_A(s)
=
\sum_{\substack{m\sim M,\ n\sim L\\m'\sim M,\ n'\sim L\\mn-m'n'=s}}
 a_{m,n}\overline{a_{m',n'}}.
\]

All coefficient restrictions—Möbius weights, logarithms, divisor sums, dyadic supports, and any sector conditions—remain inside \(a_{m,n}\). The reduction below is purely algebraic and does not alter them.

---

## 2. GCD solvability condition

Fix \(m,m'\), and let
\[
d=(m,m'),\qquad m=da,\qquad m'=db,\qquad (a,b)=1.
\]

Then
\[
mn-m'n'=s
\]
is equivalent to
\[
a n-b n'=\frac{s}{d}.
\]

Therefore:
\[
\boxed{
\text{A solution exists only if }d\mid s.
}
\]

When \(d\nmid s\), the entire \((m,m')\)-fiber contributes zero.

For \(s=0\), every gcd stratum is admissible. For a fixed nonzero short shift \(s\), only common divisors of \(|s|\) can occur. This is a real structural distinction, but it is not yet a power-saving estimate.

---

## 3. Exact one-dimensional lattice parametrization

Assume \(d\mid s\), and write
\[
h:=\frac{s}{d}.
\]

Since \((a,b)=1\), choose one integer solution \((n_0,n'_0)\) to
\[
a n_0-b n'_0=h.
\]

Then every integer solution is exactly
\[
\boxed{
 n=n_0+b\ell,
 \qquad
 n'=n'_0+a\ell,
 \qquad \ell\in\mathbb Z.
}
\]

Hence the fixed-\((m,m')\) contribution is a one-dimensional weighted lattice sum:
\[
\sum_{\ell\in\mathbb Z}
 a_{da,\,n_0+b\ell}
 \overline{a_{db,\,n'_0+a\ell}},
\]
with the convention that coefficients vanish outside their prescribed supports.

---

## 4. Exact divisor-stratified expansion

Let \(m=da\), \(m'=db\) as above. Then
\[
\boxed{
\mathcal R_A(s)
=
\sum_{d\mid s}
\sum_{\substack{a,b\\(a,b)=1\\da\sim M,\ db\sim M}}
\sum_{\ell\in\mathbb Z}
 a_{da,\,n_0(a,b;s/d)+b\ell}
 \overline{a_{db,\,n'_0(a,b;s/d)+a\ell}}.
}
\]

For \(s=0\), interpret the outer sum as a sum over all admissible \(d\) in the dyadic range rather than divisors of zero.

This is an exact rewriting of the product-difference correlation. It identifies the natural strata:

\[
\boxed{
 d=(m,m'),
 \qquad
(a,b)=1,
 \qquad
\ell\text{-lattice along }a n-bn'=s/d.
}
\]

---

## 5. Support-length bound for a lattice fiber

Suppose the inner variables lie in intervals of length \(\asymp L\). The conditions
\[
n=n_0+b\ell\asymp L,
\qquad
n'=n'_0+a\ell\asymp L
\]
restrict \(\ell\) to the intersection of two intervals. Its cardinality is bounded by
\[
\boxed{
\#\{\ell:\ n,n'\asymp L\}
\ll
1+\frac{L}{\max(a,b)}.
}
\]

Thus the geometry itself gives the crude fiber count
\[
\#\{(n,n')\asymp L:\ mn-m'n'=s\}
\ll
\mathbf 1_{d\mid s}
\left(1+\frac{L}{\max(a,b)}\right).
\]

This count is often useful for separating very unbalanced and balanced outer-variable ranges. It is not sufficient by itself for the T22 power-saving target once general arithmetic coefficients are inserted.

---

## 6. The zero-shift exceptional geometry

At \(s=0\), the equation becomes
\[
a n=b n'.
\]
Since \((a,b)=1\), it forces
\[
n=b\ell,
\qquad n'=a\ell.
\]

So the zero-shift correlation has the exact form
\[
\boxed{
\mathcal R_A(0)
=
\sum_{d}
\sum_{\substack{a,b\\(a,b)=1\\da,db\sim M}}
\sum_{\ell}
 a_{da,b\ell}\overline{a_{db,a\ell}}.
}
\]

The literal diagonal \((m,n)=(m',n')\) is only the subfamily \(a=b=1\) after the gcd normalization. The remaining coprime \((a,b)\) families are genuine multiplicative collisions and must be included in any diagonal ledger.

---

## 7. Nonzero short shifts and divisor sparsity

For \(0<|s|\le H\), only divisors \(d\mid s\) contribute. Thus the number of possible gcd strata is bounded by
\[
\tau(|s|),
\]
not by the full dyadic range of possible gcds.

When the final sector shifts are \(s=6r\), this becomes
\[
d\mid6r.
\]

This divisor sparsity is a possible source of a saving for **nonzero** shifts after summing over \(r\), but it cannot control the \(s=0\) term and does not alone control the signed coefficient sums on each surviving lattice.

---

## 8. What a valid next estimate must control

T22 needs a weighted convolution of \(\mathcal R_A\) and \(\mathcal R_B\). T23 reduces each factor to gcd-lattice strata. A useful theorem must now bound one of:

\[
\sum_{d\mid s}
\sum_{\substack{a,b\\(a,b)=1}}
\left|
\sum_{\ell}
 a_{da,n_0+b\ell}
\overline{a_{db,n'_0+a\ell}}
\right|,
\]

or a signed/averaged version compatible with the T22 convolution.

Potential mechanisms include bilinear dispersion across \((a,b)\), cancellation in the \(\ell\)-sum from the actual coefficients, or a spectral statement that applies to these explicit lattice correlations. A spline or semigroup identity alone does not bound them.

---

## 9. Outcome

The product-difference side of the density-one branch is now organized as
\[
\text{short output shift }s
\to
\text{divisor strata }d\mid s
\to
\text{coprime slope pair }(a,b)
\to
\text{one-dimensional lattice sum in }\ell.
\]

The zero shift is structurally exceptional; nonzero shifts have divisor sparsity. Any genuine improvement must exploit this split quantitatively in the T22 weighted convolution.