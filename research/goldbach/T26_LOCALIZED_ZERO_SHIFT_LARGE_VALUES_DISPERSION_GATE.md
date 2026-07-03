# T26: Localized Zero-Shift Large-Values / Dispersion Gate

**Status:** exact level-set reduction and a concrete localized theorem target for the zero-shift energy in T24; no large-values or dispersion estimate is claimed.  
**Purpose:** state the discrete-sieve route in a form that preserves far-minor localization instead of replacing it by a full-circle absolute collision count.

---

## 1. Localized bilinear product

Fix one required Type-I/II pair and write
\[
F(\alpha):=\mathcal B_1(\alpha)\mathcal B_2(\alpha).
\]

Let
\[
w(\alpha):=\chi_{\mathfrak F}(\alpha)\Omega_K(\alpha)^2,
\qquad 0\le w\le1.
\]

The zero-shift gate from T24 is the localized positive energy
\[
\boxed{
\mathcal E_{\rm loc}(F;w)
:=
\int_0^1w(\alpha)|F(\alpha)|^2d\alpha.
}
\]

The target is
\[
\mathcal E_{\rm loc}(F;w)\ll X^{3-\eta}.
\]

No full-circle coefficient energy is substituted for this quantity.

---

## 2. Exact weighted level-set formula

For \(T\ge0\), define the weighted large-values distribution
\[
V_w(T)
:=
\int_{\{\alpha:\ |F(\alpha)|>T\}}w(\alpha)\,d\alpha.
\]

The layer-cake identity gives
\[
\boxed{
\mathcal E_{\rm loc}(F;w)
=
2\int_0^\infty T\,V_w(T)\,dT.
}
\]

For a dyadic threshold sequence \(T_j=2^jT_0\), truncated at any valid uniform bound for \(|F|\),
\[
\boxed{
\mathcal E_{\rm loc}(F;w)
\ll
\sum_jT_j^2V_w(T_j).
}
\]

Thus a localized energy saving is equivalent to sufficiently strong control of the weighted measure of the far-minor large-value sets.

---

## 3. A usable large-values theorem target

Choose dyadic threshold intervals \(\mathcal T\) covering the possible values of \(|F|\). A sufficient theorem is
\[
\boxed{
\sum_{T\in\mathcal T}T^2V_w(T)
\ll X^{3-\eta}.
}
\]

A stronger pointwise form is
\[
\boxed{
V_w(T)
\ll X^{3-\eta}T^{-2}(\log X)^{-A}
}
\]
for enough threshold ranges and some bookkeeping exponent \(A>0\), with the remaining ranges handled separately.

The exponent and threshold segmentation must be derived from the actual bilinear ranges; neither bound is asserted here.

---

## 4. Separation into moderate and genuinely large values

Fix a threshold \(T_*\). Then
\[
\mathcal E_{\rm loc}(F;w)
\le
T_*^2\int_0^1w(\alpha)d\alpha
+
2\int_{T_*}^{\infty}T V_w(T)dT.
\]

This creates two independent tasks:

\[
\text{moderate values: }T_*^2\int w,
\qquad
\text{large values: }\int_{T_*}^{\infty}T V_w(T)dT.
\]

The first is governed by the geometric support mass of the far-minor weight. The second is where bilinear dispersion must enter.

Choosing \(T_*\) too large makes the moderate-value term useless; choosing it too small asks for an unrealistically strong large-values theorem. The threshold is a real optimization parameter, not a formal symbol.

---

## 5. Lattice-fiber organization of the discrete side

The T23 zero-shift geometry writes the product-difference collisions through
\[
(m,n)=(da,b\ell),
qquad
(m',n')=(db,a\ell),
qquad (a,b)=1.
\]

For a dyadic gcd block \(d\sim D\) and slope blocks \(a\sim A\), \(b\sim B\), define the corresponding fiber sum schematically by
\[
\mathcal L_{D,A,B}(\alpha)
:=
\sum_{\substack{d\sim D\\a\sim A,\ b\sim B\\(a,b)=1}}
\sum_{\ell\in\mathcal I(d,a,b)}
\gamma_{d,a,b,\ell}\,
 e\bigl(\alpha\,d a\,b\ell\bigr),
\]
where \(\gamma\) carries the actual coefficients inherited from the decomposition and the interval \(\mathcal I(d,a,b)\) enforces the original dyadic supports.

This display is organizational, not an equality for every decomposition piece: a valid implementation must derive the exact coefficient map \(\gamma\) from the chosen Vaughan/Heath--Brown identity.

The discrete route must prove that these structured lattice-fiber sums cannot be simultaneously large on a set of far-minor frequencies with enough weighted measure to violate Section 3.

---

## 6. Finite separated-set formulation

A standard large-values reduction begins with a \(\delta\)-separated set
\[
\mathcal A\subset\operatorname{supp}(w),
\qquad
\|\alpha-\beta\|_{\mathbb T}\ge\delta
\quad(\alpha\ne\beta).
\]

A sufficient localized large-values theorem can be stated as:

\[
\boxed{
\#\{\alpha\in\mathcal A:\ |F(\alpha)|\ge T\}
\ll
\delta^{-1}X^{3-\eta}T^{-2},
}
\]

uniformly for the admissible far-minor separated sets and required threshold ranges, with a covering argument converting this into a bound for \(V_w(T)\).

The precise relationship between \(\delta\), the arc widths, and the smooth collar has to be chosen so that the covering multiplicity is controlled. This is the place for a genuine large-sieve spacing or dispersion inequality.

---

## 7. What the dispersion estimate must actually see

After duality/Cauchy--Schwarz, a real proof will encounter sums over distinct frequencies \(\alpha,\beta\in\mathcal A\) of the schematic type
\[
\sum_{m,n,m',n'}
\mathfrak a_{m,n}\overline{\mathfrak a_{m',n'}}
 e\bigl((\alpha-\beta)(mn-m'n')\bigr),
\]
or the analogous T23 lattice coordinates.

The far-minor condition is valuable only if it yields cancellation in these frequency differences after the actual coefficient structure is retained. Replacing the phase by its absolute value collapses the argument back to the full-circle collision energy and loses the desired saving.

Thus the arithmetic deliverable is a dispersion bound that uses both:

\[
\text{the product/lattice coefficient structure},
\qquad
\text{and far-minor spacing of the frequency set}.
\]

---

## 8. A two-ledger theorem package

A rigorous density-one advance from the discrete route would follow from the pair:

### Z-M (moderate values)
\[
T_*^2\int_0^1w(\alpha)d\alpha
\le\frac12X^{3-\eta}.
\]

### Z-L (large values)
\[
\sum_{T\ge T_*}^{\rm dyadic}T^2V_w(T)
\le\frac12X^{3-\eta}.
\]

Together,
\[
\mathcal E_{\rm loc}(F;w)\ll X^{3-\eta}.
\]

This turns the T24 zero-shift obstruction into two auditable numerical budgets rather than one opaque request.

---

## 9. OFI decision rule

An OFI-based operator can participate only by proving a stronger instance of Z-M or Z-L under the same far-minor partition and the same output-locality ledger. Examples of legitimate improvements are:

\[
\text{a better weighted support mass }\int w,
\]

or
\[
\text{a stronger separated-set large-values estimate for the actual lattice-fiber sums}.
\]

Renaming the weight, or replacing the localized energy by a full-circle collision count, does not advance this gate.

---

## 10. Outcome

The discrete-sieve route is now a precise research program:
\[
\text{T23 gcd-lattice fibers}
\to
\text{far-minor separated-frequency dispersion}
\to
\text{weighted large-values bound}
\to
\text{T24 localized zero-shift energy}
\to
\text{T18 density-one conclusion}.
\]

The first genuinely proof-moving inequality is Z-L: a nontrivial far-minor large-values estimate that retains both the bilinear coefficients and the frequency spacing.