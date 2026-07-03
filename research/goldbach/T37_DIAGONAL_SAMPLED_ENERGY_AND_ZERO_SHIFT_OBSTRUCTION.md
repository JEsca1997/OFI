# T37: Diagonal Sampled Energy and the Zero-Shift Obstruction

**Status:** exact large-sieve baseline and zero-shift reduction for a corrected Type-II product component; no power saving is claimed.  
**Purpose:** test the diagonal sampled-energy target from the near-diagonal gate and identify the irreducible arithmetic quantity that generic spacing estimates retain.

---

## 1. Product coefficient sequence

For a Type-II component pair, write
\[
T(\alpha)
:=\mathcal B_1(\alpha)\mathcal B_2(\alpha)
=
\sum_t C(t)e(\alpha t),
\]
where
\[
C(t)
:=
\sum_{mn+uv=t}a_{m,n}b_{u,v}.
\]

If
\[
MN_1\asymp X,
\qquad UV\asymp X,
\]
then \(C(t)\) is supported in an interval of length \(L\asymp X\) after fixed dyadic localization.

For a \(\delta\)-separated sample set
\[
\mathcal A=\{\alpha_1,\ldots,\alpha_J\},
\]
set
\[
\mathscr L(\mathcal A)
:=
\sum_{j=1}^J|T(\alpha_j)|^2.
\]

---

## 2. Exact coefficient-energy identity

By Parseval on the full circle,
\[
\boxed{
\sum_t|C(t)|^2
=
\int_0^1|\mathcal B_1(\alpha)|^2|\mathcal B_2(\alpha)|^2d\alpha.
}
\]

Expanding in the original Type-II variables gives
\[
\boxed{
\sum_t|C(t)|^2
=
\sum_{mn+uv=m'n'+u'v'}
 a_{m,n}b_{u,v}
 \overline{a_{m',n'}b_{u',v'}}.
}
\]

This is the exact zero-output-shift collision energy for the component pair.

---

## 3. Generic separated-frequency baseline

The standard large-sieve inequality gives the generic bound
\[
\boxed{
\mathscr L(\mathcal A)
\ll
(L+\delta^{-1})
\sum_t|C(t)|^2.
}
\]

Since \(L\asymp X\),
\[
\boxed{
\mathscr L(\mathcal A)
\ll
(X+\delta^{-1})
\mathcal E_0(\mathcal B_1,\mathcal B_2),
}
\]
where
\[
\mathcal E_0(\mathcal B_1,\mathcal B_2)
:=
\sum_t|C(t)|^2.
\]

This estimate uses separation but does not use that all samples lie in a far-minor set.

---

## 4. The scale required by T34--T36

The sampling target inherited from the joint-large-values route is schematically
\[
\mathscr L(\mathcal A)
\ll
\delta^{-1}X^{3-\eta}.
\]

In the natural regime
\[
\delta^{-1}\gtrsim X,
\]
the generic large sieve would require
\[
\boxed{
\mathcal E_0(\mathcal B_1,\mathcal B_2)
\ll X^{3-\eta}.
}
\]

Thus a power saving in the diagonal sampled-energy theorem cannot come from frequency spacing alone. It requires a power saving in the zero-shift collision energy, or a genuinely far-minor-sensitive replacement for the generic large sieve.

---

## 5. Why raw zero-shift energy is not expected to save automatically

The collision equation
\[
mn+uv=m'n'+u'v'
\]
has a positive diagonal family
\[
(m,n,u,v)=(m',n',u',v').
\]

Consequently,
\[
\mathcal E_0
ge
\sum_{m,n,u,v}|a_{m,n}|^2|b_{u,v}|^2.
\]

More broadly, the additive output variable \(t=mn+uv\) ranges over \(O(X)\) values while the two-factor input set may have total mass of size about \(X^2\) up to logarithmic/coefficient factors. A random-distribution heuristic then places the collision energy near the cubic scale \(X^3\), not below it by a fixed power.

This is a heuristic diagnostic, not a lower-bound theorem for every coefficient family. The exact conclusion is only that the positive diagonal prevents a cancellation argument inside \(\mathcal E_0\).

---

## 6. Consequence: the direct diagonal route is too strong in raw form

The desired inequality
\[
\mathcal E_0\ll X^{3-\eta}
\]
asks for a power saving against a positive collision energy before the far-minor restriction has entered.

That is generally the wrong place to seek the saving.

The far-minor condition must be used **before** collapsing to the full-circle coefficient norm. In particular, a viable route must keep at least one of:

\[
\chi_{\mathfrak F}(\alpha),
\qquad
\Omega(\alpha),
\qquad
\text{a rational-approximation parameter for }\alpha,
\qquad
\text{a bilinear phase prior to the final absolute square}.
\]

---

## 7. Correct revised theorem target

The right target is not a naked bound on \(\mathcal E_0\). It is a far-minor-localized estimate
\[
\boxed{
\int_0^1
\chi_{\mathfrak F}(\alpha)|\Omega(\alpha)|^2
|\mathcal B_1(\alpha)|^2|\mathcal B_2(\alpha)|^2d\alpha
\ll X^{3-\eta}.
}
\]

Equivalently, any discrete sampling theorem must contain a hypothesis that records the far-minor geometry beyond mere \(\delta\)-separation.

A generic large-sieve inequality cannot distinguish a far-minor sample set from an equally separated sample set concentrated near a rational arc.

---

## 8. Outcome

The diagonal attack produces a decisive result:
\[
\boxed{
\text{generic large sieve }+
\text{ raw zero-shift energy }
\text{ cannot supply the needed power saving.}
}
\]

The next attack must be localized from the start. The productive object is the weighted far-minor fourth moment of the Type-II pair, not its full-circle collision energy.