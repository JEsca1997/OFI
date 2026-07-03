# T9-P2: Local Deficit Propagation Requires Arithmetic Regularity

**Status:** exact obstruction plus conditional propagation lemma.  
**Purpose:** determine what additional theorem would be required for the OFI local-window route to eliminate every exceptional Goldbach target.

---

## 1. The proposed P2 mechanism

Let
\[
g_E=(\theta_\sigma*\theta_\tau)(E)\ge0
\]
be the relevant prime-only Goldbach coefficient and let
\[
M(E)\asymp E
\]
be a positive model main term. Put
\[
r_E:=g_E-M(E).
\]

A zero coefficient gives a point deficit:
\[
g_{E_0}=0
\quad\Longrightarrow\quad
r_{E_0}=-M(E_0).
\]

P2 would need to turn this one deficit into a whole block of deficits, large enough to contradict the T8 mean-square budget.

---

## 2. No propagation from nonnegativity alone

There is no general implication
\[
g_{E_0}=0
\Longrightarrow
\sum_{|h|\le H}|r_{E_0+h}|^2\gg E_0^2H
\]
from nonnegativity of \(g\) alone.

Indeed, a nonnegative sequence can vanish at one coordinate and be arbitrarily large at adjacent coordinates. A positive local window then averages those neighboring spikes and may remain positive at the center.

Therefore neither:

- positivity of the Goldbach coefficient sequence,
- positivity of a spline/window average,
- compact support of the window, nor
- minimality of a hypothetical exceptional target

produces P2 automatically.

---

## 3. A valid conditional deficit-propagation lemma

### Lemma (discrete regularity propagates a point deficit)

Let \(r:\mathbb Z\to\mathbb R\) satisfy a local Lipschitz bound
\[
|r_{n+1}-r_n|\le L
\qquad\text{for }|n-E_0|\le H.
\]
Assume
\[
r_{E_0}\le-cE_0
\]
for some \(c>0\). Then for every integer \(h\) with
\[
|h|\le \frac{cE_0}{2L},
\]
we have
\[
r_{E_0+h}\le-\frac{c}{2}E_0.
\]
Consequently, for
\[
H\le\frac{cE_0}{2L},
\]
\[
\boxed{
\sum_{|h|\le H}|r_{E_0+h}|^2
\ge (2H+1)\frac{c^2}{4}E_0^2.
}
\]

### Proof

By telescoping,
\[
r_{E_0+h}\le r_{E_0}+L|h|
\le-cE_0+L|h|.
\]
The stated range gives the claimed negative bound. Squaring and summing proves the conclusion. \(\square\)

---

## 4. Why this does not yet apply to Goldbach

For Goldbach correlations, no known estimate of the required type
\[
|r_{E+1}-r_E|\ll E^{1-\varepsilon}
\]
uniformly in all admissible even targets follows from the spline construction or from standard prime estimates.

The coefficient sequence can fluctuate substantially because changing the target changes the entire additive prime-pair condition. In particular, smoothing the output after the fact does not prove regularity of the unsmoothed residual.

Thus the lemma is a **bridge specification**, not a completed Goldbach lemma.

---

## 5. Frequency-localized variant

A more OFI-native route is to split the residual into low and high output-frequency pieces:
\[
r=r^{\mathrm{low}}_B+r^{\mathrm{high}}_B,
\]
where \(r^{\mathrm{low}}_B\) is supported in output frequencies \(|\xi|\le B\).

A Bernstein-type estimate would then give schematically
\[
\|\Delta r^{\mathrm{low}}_B\|_\infty
\lesssim B\|r^{\mathrm{low}}_B\|_\infty.
\]

If one could prove simultaneously that:

1. a zero at \(E_0\) forces a negative low-frequency residual there; and
2. the high-frequency residual is uniformly smaller than a fixed fraction of \(M(E_0)\),

then the previous local-deficit lemma would apply to \(r^{\mathrm{low}}_B\).

This would make the OFI order relevant through its output-frequency partition. But both bullets are new arithmetic estimates; a B-spline multiplier alone proves neither.

---

## 6. Quantitative P2 target

A workable pointwise propagation theorem would be any statement of the following form.

For every admissible target \(E_0\) with \(g_{E_0}=0\), there exist parameters \(B,H\) and a residual decomposition such that
\[
\sum_{|h|\le H}|r_{E_0+h}|^2
\ge c_1E_0^2H,
\]
while the global T8 bound gives
\[
\sum_{E\in[X,2X]\cap2\mathbb Z}|r_E|^2
\le C X^{3-\eta}.
\]

To force a contradiction from a single zero at scale \(X\), the local block must consume more than the full available mean-square budget. That requires either:

- a block length comparable to or larger than \(X^{1-\eta}\) with order-\(X\) deficit; or
- a substantially stronger global moment estimate; or
- many linked deficit blocks generated from one zero.

This makes the burden explicit.

---

## 7. Consequence for OFI strategy

The right OFI task is not to claim that the local spline window itself propagates positivity. It is to seek a rigorous spectral decomposition in which:

\[
\text{high output frequencies are controlled strongly enough,}
\]
\[
\text{and a low-frequency deficit cannot remain isolated.}
\]

The required theorem must be formulated in terms of the actual Goldbach residual or an explicitly defined major/minor decomposition, not generic spline smoothness.

---

## 8. Decision rule

P2 should remain a research branch only if a candidate OFI/Riesz/heat/Ruelle construction produces a concrete estimate for one of:

\[
\|\Delta r^{\mathrm{low}}_B\|_\infty,
\qquad
\|r^{\mathrm{high}}_B\|_\infty,
\qquad
\text{or a zero}\Rightarrow\text{multi-block deficit law}.
\]

Without such an estimate, P2 does not advance beyond a conceptual possibility.

The primary proof spine remains P1: a pointwise post-extraction minor-arc bound.