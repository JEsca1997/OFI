# T30: Joint Large-Values Amplifier Gate

**Status:** exact amplification reduction for the T29 two-sided dyadic strata; no restricted bilinear Gram estimate is claimed.  
**Purpose:** convert joint concentration of two Type-II factors on far-minor samples into one phase-amplified operator inequality.

---

## 1. A joint large-value stratum

Let
\[
\mathcal S=\mathcal A_{U,V}
=
\{\alpha_j\in\mathcal A:
U<|A_j|\le2U,
\quad
V<|B_j|\le2V\},
\]
where \(\mathcal A\subset\operatorname{supp}(w)\) is \(\delta\)-separated.

For every \(\alpha_j\in\mathcal S\),
\[
|A_jB_j|>UV.
\]

The desired two-sided T29 bound is
\[
\sum_{U,V}U^2V^2|\mathcal A_{U,V}|
\ll
\delta^{-1}X^{3-\eta}.
\]

---

## 2. Phase alignment is exact

For each \(\alpha_j\in\mathcal S\), choose a unimodular phase
\[
z_j:=
\begin{cases}
\overline{A_jB_j}/|A_jB_j|,&A_jB_j\ne0,\\
0,&A_jB_j=0.
\end{cases}
\]

Then
\[
z_jA_jB_j=|A_jB_j|.
\]

Hence
\[
\sum_{\alpha_j\in\mathcal S}|A_jB_j|
=
\sum_{\alpha_j\in\mathcal S}z_jA_jB_j
\ge UV|\mathcal S|.
\]

Squaring gives the exact lower bound
\[
\boxed{
U^2V^2|\mathcal S|^2
\le
\left|
\sum_{\alpha_j\in\mathcal S}z_jA_jB_j
\right|^2.
}
\]

---

## 3. Amplified Gram expansion

Expand the right side:
\[
\begin{aligned}
\left|
\sum_{\alpha_j\in\mathcal S}z_jA_jB_j
\right|^2
&=
\sum_{i,j\in\mathcal S}
z_i\overline{z_j}
A_iB_i\overline{A_jB_j}\\
&=
\sum_{m,n,u,v\atop m',n',u',v'}
 a_{m,n}b_{u,v}
 \overline{a_{m',n'}b_{u',v'}}
 \mathcal K_{\mathcal S,z}
 \left(mn+uv-m'n'-u'v'\right),
\end{aligned}
\]
where the amplified sampling kernel is
\[
\boxed{
\mathcal K_{\mathcal S,z}(h)
:=
\sum_{\alpha_j\in\mathcal S}z_je(\alpha_jh).
}
\]

Unlike the unsigned kernel from T27,
\[
K_{\mathcal S}(h)=\sum_{\alpha_j\in\mathcal S}e(\alpha_jh),
\]
the phases \(z_j\) are chosen from the actual joint-large-value configuration. Any valid upper bound must hold uniformly in these phases.

---

## 4. Sufficient amplified operator inequality

A proof-moving theorem is:
\[
\boxed{
\left|
\sum_{\alpha_j\in\mathcal S}z_jA_jB_j
\right|^2
\ll
\delta^{-1}X^{3-\eta}|\mathcal S|
}
\]
for every \(\delta\)-separated far-minor subset \(\mathcal S\), every unimodular sequence \((z_j)\), and every required dyadic Type-I/II coefficient class.

Combining with Section 2 yields
\[
\boxed{
U^2V^2|\mathcal S|
\ll
\delta^{-1}X^{3-\eta}.
}
\]

This is precisely the individual-stratum estimate required by T29.

---

## 5. Dyadic summation ledger

If the amplified theorem in Section 4 holds uniformly across all dyadic strata, then
\[
\sum_{U,V}U^2V^2|\mathcal A_{U,V}|
\ll
(\#\text{ dyadic strata})\,\delta^{-1}X^{3-\eta}.
\]

Since the number of admissible dyadic ranges is polylogarithmic in \(X\), the theorem must carry enough logarithmic slack:
\[
\boxed{
\left|
\sum_{\alpha_j\in\mathcal S}z_jA_jB_j
\right|^2
\ll_A
\delta^{-1}X^{3-\eta}(\log X)^{-A}|\mathcal S|
}
\]
for sufficiently large \(A\), or an equivalent summable nonuniform budget must be supplied.

---

## 6. Relation to the preconvolution kernel

The Section 3 sum can be partially expanded in the \(B\)-factor exactly as in T28:
\[
\begin{aligned}
&\left|
\sum_{\alpha_j\in\mathcal S}z_jA_jB_j
\right|^2\\
&\qquad=
\sum_{m,n,m',n'}a_{m,n}\overline{a_{m',n'}}
\mathscr K_{B;\mathcal S,z}\big((m,n),(m',n')\big),
\end{aligned}
\]
with
\[
\mathscr K_{B;\mathcal S,z}\big((m,n),(m',n')\big)
:=
\sum_{u,v,u',v'}b_{u,v}\overline{b_{u',v'}}
\mathcal K_{\mathcal S,z}
\left(mn-m'n'+uv-u'v'\right).
\]

Therefore T30 does not introduce a new arithmetic object; it imposes the correct **uniform phase-amplified norm requirement** on T28's kernel.

---

## 7. Why scalar large-value counts are insufficient

A bound for
\[
|\mathcal S|
\]
alone does not account for the possibility that both \(A\) and \(B\) align in phase on the same far-minor sample set. The amplifier chooses those phases adversarially.

Thus a theorem that only controls unsigned frequency spacing, or only controls one factor independent of the other, does not imply the T30 bound unless it is explicitly strong enough to handle all \(z_j\).

The uniformity in \((z_j)\) is the mathematical form of excluding joint concentration.

---

## 8. GCD-lattice form of the required estimate

T23 may be inserted into the outer difference
\[
mn-m'n'=s,
\]
so that
\[
(m,m')=(da,db),
\qquad
an-bn'=s/d,
qquad(a,b)=1.
\]

A concrete proof route may therefore seek a uniform estimate for the amplified kernel after summation over
\[
d,\quad(a,b),\quad\ell,
\]
while the inner \(B\)-factor carries the product-difference phase and the far-minor amplifier \(\mathcal K_{\mathcal S,z}\).

This is the sharpest currently justified location for a spectral, dispersion, or OFI-derived transfer estimate.

---

## 9. Outcome

T30 turns the T29 qualitative phrase “large \(A\) and large \(B\) cannot concentrate together” into a single testable inequality:
\[
\boxed{
\sup_{|z_j|\le1}
\left|
\sum_{\alpha_j\in\mathcal S}z_jA_jB_j
\right|^2
\ll
\delta^{-1}X^{3-\eta}|\mathcal S|.
}
\]

Proving this uniformly on far-minor separated sets would immediately provide the joint dyadic large-values budget, then Z-L, then the T24 localized zero-shift energy bound.