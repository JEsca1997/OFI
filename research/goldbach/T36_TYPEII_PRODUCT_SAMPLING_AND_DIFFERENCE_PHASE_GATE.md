# T36: Type-II Product Sampling and Difference-Phase Gate

**Status:** exact expansion of a corrected Goldbach Type-II component-pair large-values functional; no cancellation estimate is claimed.  
**Purpose:** expose the concrete oscillatory sum that must be bounded to move T35.

---

## 1. A concrete Type-II pair

Let
\[
\mathcal B_1(\alpha)
:=
\sum_{m\sim M}\sum_{n\sim N_1}a_{m,n}e(\alpha mn),
\qquad MN_1\asymp X,
\]
and
\[
\mathcal B_2(\alpha)
:=
\sum_{u\sim U}\sum_{v\sim V}b_{u,v}e(\alpha uv),
\qquad UV\asymp X.
\]

The coefficients may contain sector restrictions, divisor weights, logarithms, or bounded combinatorial factors inherited from the chosen identity. Those restrictions must remain present in every subsequent estimate.

For a finite \(\delta\)-separated sample set
\[
\mathcal A=\{\alpha_1,\ldots,\alpha_J\}\subset\operatorname{supp}(w),
\]
define
\[
\mathscr L(\mathcal A)
:=
\sum_{j=1}^{J}
|\mathcal B_1(\alpha_j)|^2
|\mathcal B_2(\alpha_j)|^2.
\]

A restricted sampling bound of the form
\[
\mathscr L(\mathcal A)
\ll \delta^{-1}X^{3-\eta}
\]
would be a discrete analogue of the T34 joint-large-values target. Passing from a continuous weighted level set to such samples requires a separate discretization/stability lemma; it is not assumed here.

---

## 2. Exact eight-variable expansion

Let
\[
K_{\mathcal A}(h):=
\sum_{j=1}^{J}e(\alpha_j h).
\]

Then exactly
\[
\begin{aligned}
\mathscr L(\mathcal A)
&=
\sum_{m,n,u,v}\sum_{m',n',u',v'}
 a_{m,n}b_{u,v}\overline{a_{m',n'}b_{u',v'}}\\
&\qquad\qquad\times
K_{\mathcal A}\bigl(mn+uv-m'n'-u'v'\bigr).
\end{aligned}
\]

The zero-shift locus is
\[
mn+uv=m'n'+u'v'.
\]
It is a genuine positive-energy obstruction: a generic large sieve bound retains its full mass and therefore does not automatically yield a power saving.

---

## 3. Phase-amplified version

For arbitrary coefficients \(|z_j|\le1\), define
\[
K_{\mathcal A,z}(h):=
\sum_{j=1}^{J}z_je(\alpha_jh).
\]

Then
\[
\left|
\sum_{j=1}^Jz_j\mathcal B_1(\alpha_j)\mathcal B_2(\alpha_j)
\right|^2
\]
expands into the same eight-variable form with \(K_{\mathcal A,z}\) in place of \(K_{\mathcal A}\).

This is the sampling version of the T30 amplifier, now attached to a genuine Goldbach component pair.

---

## 4. Cauchy differencing in one bilinear factor

For a fixed \(m\), write
\[
B_{1,m}(\alpha):=\sum_{n\sim N_1}a_{m,n}e(\alpha mn).
\]

A Cauchy step in the \(m\)-variable introduces differences
\[
(m-m')n
\]
and leads to exponential sums whose phase frequencies depend on
\[
\alpha_j-\alpha_k.
\]

At the schematic level,
\[
\sum_j|\mathcal B_1(\alpha_j)|^2
\]
contains sums of the form
\[
\sum_{j,k}
\sum_{m,m',n,n'}
 c_{m,m',n,n'}
 e\bigl((\alpha_j-\alpha_k)(mn-m'n')\bigr).
\]

For the product functional, the corresponding phase is
\[
\boxed{
(\alpha_j-\alpha_k)
\bigl(mn+uv-m'n'-u'v'\bigr).
}
\]

Thus the arithmetic analysis is governed by **differences of sample frequencies**, not merely by each individual \(\alpha_j\).

---

## 5. Difference-phase instability

Even when every \(\alpha_j\) lies in the far-minor region,
\[
\alpha_j-\alpha_k
\]
may lie near \(0\) or near a low-denominator rational.

In particular:
\[
\alpha_j-\alpha_j=0,
\]
and two individually far-minor frequencies can have a difference in a major arc.

Therefore a valid proof must partition ordered sample pairs by the Diophantine type of
\[
\Delta_{jk}:=\alpha_j-\alpha_k,
\]
not claim that a far-minor point condition is preserved under subtraction.

---

## 6. Exact pair partition required by the method

Choose scales \(Q_0,Q_1,W\) appropriate to the **difference phase**. Partition pairs \((j,k)\) into:

\[
\Delta_{jk}\in\mathfrak D_0
quad\text{(near zero)},
\]
\[
\Delta_{jk}\in\mathfrak D_{\rm rat}(q)
:=
\left\{\Delta:
\left|\Delta-\frac aq\right|
\le\frac{W}{qX},\ (a,q)=1,\ q\le Q_1
\right\},
\]
\[
\Delta_{jk}\in\mathfrak D_{\rm far}
\quad\text{(remaining difference-far pairs)}.
\]

The three contributions need distinct controls:

1. **Near-zero pairs:** use \(\delta\)-separation and a local-density count.
2. **Rational-difference pairs:** use congruence/arithmetic progression structure of \(mn+uv\) modulo \(q\).
3. **Difference-far pairs:** seek cancellation in the bilinear exponential sum.

This partition is not optional: it is forced by the two-sample expansion.

---

## 7. The actual theorem target

For every allowed coefficient family, every \(\delta\)-separated sample set, and every \(|z_j|\le1\), prove a bound of the schematic form
\[
\boxed{
\left|
\sum_{j=1}^{J}z_j\mathcal B_1(\alpha_j)\mathcal B_2(\alpha_j)
\right|^2
\ll
\delta^{-1}X^{3-\eta}J
}
\]
with enough logarithmic slack for dyadic and component summation.

The proof must explicitly charge:

\[
\text{near-zero difference pairs},
\qquad
\text{rational-difference pairs},
\qquad
\text{difference-far cancellation},
\qquad
\text{coefficient norms and sector restrictions}.
\]

No such theorem is established here.

---

## 8. What this changes

T36 is the first place where the corrected Goldbach route hits an arithmetic object precise enough to attack:
\[
K_{\mathcal A,z}(mn+uv-m'n'-u'v').
\]

The obstacle is not an undefined OFI notion. It is the need for a power-saving estimate on this explicit Type-II product-difference sum, uniformly over phase-amplified far-minor samples.

A successful OFI contribution must appear as a proof of one of the three difference-phase controls above, not as an alternative name for the expansion.