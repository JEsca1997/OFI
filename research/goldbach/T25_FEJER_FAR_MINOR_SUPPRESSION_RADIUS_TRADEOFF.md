# T25: Fejér Far-Minor Suppression Versus Window Radius

**Status:** exact pointwise attenuation bound for the sector-preserving Fejér multiplier outside its low-denominator peak neighborhoods; no prime-sum estimate is claimed.  
**Purpose:** quantify how much far-minor suppression Fejér can provide by itself, and record the window-radius cost required for a polynomial gain.

---

## 1. Sector Fejér multiplier and its peaks

Recall the rescaled Fejér multiplier
\[
\Omega_K(\alpha)
=
F_K(6\alpha),
\qquad
F_K(x)
:=
\frac{1}{(K+1)^2}
\left(
\frac{\sin(\pi(K+1)x)}{\sin(\pi x)}
\right)^2.
\]

It satisfies
\[
0\le F_K(x)\le1,
\qquad
F_K(x+1)=F_K(x).
\]

Therefore \(\Omega_K\) has its unit-height peaks at
\[
\alpha\in\frac16\mathbb Z/\mathbb Z.
\]

These six points are exactly the rational centers of denominators dividing \(6\):
\[
0,\ \frac16,\ \frac13,\ \frac12,\ \frac23,\ \frac56.
\]

---

## 2. Elementary Fejér off-peak bound

For \(\|x\|_{\mathbb T}\le1/2\),
\[
|\sin(\pi x)|\ge2\|x\|_{\mathbb T}.
\]

Since the numerator of \(F_K\) has modulus at most one,
\[
\boxed{
F_K(x)
\le
\min\left\{
1,
\frac{1}{4(K+1)^2\|x\|_{\mathbb T}^2}
\right\}.
}
\]

Consequently,
\[
\boxed{
\Omega_K(\alpha)
\le
\min\left\{
1,
\frac{1}{4(K+1)^2\|6\alpha\|_{\mathbb T}^2}
\right\}.
}
\]

This is purely deterministic; no arithmetic input appears.

---

## 3. Separation on the far-minor region

Assume the smooth partition from T20 is built from rational neighborhoods that include all reduced rationals with denominator at most \(6\), with core radii
\[
r_q=\frac{W}{qN}.
\]

If \(\alpha\) lies outside the union of the six core neighborhoods around the points in \(\frac16\mathbb Z/\mathbb Z\), then
\[
\operatorname{dist}\left(\alpha,\frac16\mathbb Z\right)
\ge\frac{W}{6N}.
\]

Therefore
\[
\|6\alpha\|_{\mathbb T}\ge\frac{W}{N}.
\]

On this far region,
\[
\boxed{
\Omega_K(\alpha)
\le
\min\left\{
1,
\frac{N^2}{4(K+1)^2W^2}
\right\}.
}
\]

Squaring gives the corresponding energy-weight bound
\[
\boxed{
\Omega_K(\alpha)^2
\le
\min\left\{
1,
\frac{N^4}{16(K+1)^4W^4}
\right\}.
}
\]

The same estimate applies on the support of a far-minor cutoff \(\chi_{\mathfrak F}\) that is supported outside those core arcs. Enlarged collars must be accounted for separately, as in T20.

---

## 4. Radius required for a prescribed power attenuation

Suppose one seeks the deterministic energy attenuation
\[
\Omega_K(\alpha)^2\le N^{-\eta}
\]
throughout the far-minor support, for some \(\eta>0\).

The bound in Section 3 requires
\[
\frac{N^4}{16(K+1)^4W^4}\le N^{-\eta}.
\]

Hence a sufficient radius condition is
\[
\boxed{
K+1\ge\frac{1}{2W}N^{1+\eta/4}.
}
\]

Even to obtain only a fixed constant attenuation \(\Omega_K^2\le c<1\), one needs
\[
K\gg_c \frac{N}{W}.
\]

Thus Fejér suppression is controlled by the dimensionless ratio
\[
\boxed{
\frac{KW}{N}.
}
\]

---

## 5. Locality consequence

The rescaled Fejér window has support \(|k|\le K\), corresponding to physical output shifts
\[
h=6k,
\qquad |h|\le6K.
\]

If \(W\) is polylogarithmic, as in T15,
\[
W=(\log N)^C,
\]
then the radius needed for polynomial attenuation is
\[
K\gtrsim\frac{N^{1+\eta/4}}{(\log N)^C}.
\]

For every fixed \(\eta>0\), this eventually exceeds the natural target scale \(N\). Such a window is not a local average in the T9 sense and cannot be used as a local coefficient-surrogate without a separate global boundary and descent analysis.

Therefore:
\[
\boxed{
\text{Fejér alone cannot provide polynomial far-minor suppression while remaining genuinely local at polylogarithmic arc width.}
}
\]

This is a radius tradeoff, not a disproof of a weighted-energy theorem: arithmetic cancellation in the bilinear product could still yield a saving. It says only that the multiplier's deterministic decay cannot supply that saving by itself.

---

## 6. Consequence for the T24 zero-shift energy

On the far-minor support,
\[
\int\chi_{\mathfrak F}\Omega_K^2|
\mathcal B_1\mathcal B_2|^2
\le
\left(
\sup_{\operatorname{supp}\chi_{\mathfrak F}}\Omega_K^2
\right)
\int\chi_{\mathfrak F}|
\mathcal B_1\mathcal B_2|^2.
\]

By Section 3, the scalar prefactor is at most
\[
\min\left\{1,\frac{N^4}{16(K+1)^4W^4}\right\}.
\]

For a local radius \(K\ll N/W\), this estimate gives at best a constant-level reduction. Therefore the required T24 power saving
\[
\int\chi_{\mathfrak F}\Omega_K^2|
\mathcal B_1\mathcal B_2|^2
\ll N^{3-\eta}
\]
cannot be obtained solely from the pointwise Fejér envelope in that local regime.

A genuine arithmetic large-values, dispersion, or bilinear-energy estimate remains necessary.

---

## 7. Fractional OFI comparison rule

A fractional sector-preserving candidate \(\Omega_u\) may improve this tradeoff only by proving a stronger off-peak envelope under comparable localization constraints. The comparison must state all three quantities:

\[
\text{peak separation scale},
\qquad
\text{window/output radius},
\qquad
\text{far-region attenuation exponent}.
\]

A candidate that improves Fourier decay only by using a window with effective radius comparable to the target scale has not solved the local-output problem.

---

## 8. Outcome

T25 adds a hard deterministic constraint to the density-one spine:
\[
\text{local Fejér window}
\not\Rightarrow
\text{polynomial far-minor suppression by envelope decay alone}.
\]

The remaining viable route is exactly the one isolated in T24:
\[
\text{localized bilinear arithmetic energy saving},
\]
possibly helped by a multiplier whose gain survives the full radius/collar/extraction ledger.