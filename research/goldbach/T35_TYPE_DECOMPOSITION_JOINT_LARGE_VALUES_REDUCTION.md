# T35: Type-Decomposition Joint Large-Values Reduction

**Status:** exact finite-component and pigeonhole reduction for the corrected T34 far-minor joint-large-values problem; no Type-I/II estimate is claimed.  
**Purpose:** move from joint large values of the full sector prime sums to a finite set of component-pair large-values problems with explicit losses.

---

## 1. Finite decomposition hypothesis

Fix a sector \(\rho\in\{+,-\}\). Assume a chosen Vaughan/Heath--Brown style identity has been organized on the far-minor support as
\[
S_\rho(\alpha)
=
\sum_{a=1}^{A_\rho}\mathcal B_{\rho,a}(\alpha)
+\mathcal E_\rho(\alpha),
\]
where:

\[
\mathcal B_{\rho,a}
\]
are the finitely many explicit Type-I/Type-II component sums, and
\[
\mathcal E_\rho
\]
is the total combinatorial remainder.

The number \(A_\rho\) may depend polylogarithmically on \(X\), but must be explicitly recorded.

---

## 2. Remainder exclusion set

Fix a threshold fraction \(0<\varepsilon<1/4\). For a dyadic level \(U\), define
\[
\mathfrak R_{\sigma}(U)
:=
\{\alpha\in\operatorname{supp}(w):|\mathcal E_\sigma(\alpha)|>\varepsilon U\},
\]
and analogously \(\mathfrak R_{\tau}(V)\).

On the complement of these remainder sets, if
\[
|S_\sigma(\alpha)|>U,
\]
then
\[
\left|\sum_{a=1}^{A_\sigma}\mathcal B_{\sigma,a}(\alpha)\right|
>(1-\varepsilon)U.
\]

By the triangle inequality, there exists an index \(a\) such that
\[
\boxed{
|\mathcal B_{\sigma,a}(\alpha)|
>
\frac{(1-\varepsilon)U}{A_\sigma}.
}
\]

Likewise, if \(|S_\tau(\alpha)|>V\) outside \(\mathfrak R_\tau(V)\), then some \(b\) satisfies
\[
\boxed{
|\mathcal B_{\tau,b}(\alpha)|
>
\frac{(1-\varepsilon)V}{A_\tau}.
}
\]

---

## 3. Exact containment of a full joint-large-value stratum

Let
\[
\mathfrak E_{U,V}
=
\{\alpha:\ U<|S_\sigma(\alpha)|\le2U,\ V<|S_\tau(\alpha)|\le2V\}
\]
be the T34 stratum. Define component-pair sets
\[
\mathfrak E^{a,b}_{U,V}
:=
\left\{
\alpha\in\operatorname{supp}(w):
|\mathcal B_{\sigma,a}(\alpha)|>
\frac{(1-\varepsilon)U}{A_\sigma},
\quad
|\mathcal B_{\tau,b}(\alpha)|>
\frac{(1-\varepsilon)V}{A_\tau}
\right\}.
\]

Then exactly
\[
\boxed{
\mathfrak E_{U,V}
\subseteq
\mathfrak R_\sigma(U)
\cup
\mathfrak R_\tau(V)
\cup
\bigcup_{1\le a\le A_\sigma\atop1\le b\le A_\tau}
\mathfrak E^{a,b}_{U,V}.
}
\]

Consequently,
\[
\boxed{
\mu_w(\mathfrak E_{U,V})
\le
\mu_w(\mathfrak R_\sigma(U))
+
\mu_w(\mathfrak R_\tau(V))
+
\sum_{a,b}\mu_w(\mathfrak E^{a,b}_{U,V}).
}
\]

This is the correct finite union reduction. No equality or independence between components is claimed.

---

## 4. Weighted dyadic budget after decomposition

Multiplying by \(U^2V^2\) and summing dyadically gives
\[
\begin{aligned}
\sum_{U,V}U^2V^2\mu_w(\mathfrak E_{U,V})
&\le
\sum_{U,V}U^2V^2\mu_w(\mathfrak R_\sigma(U))\\
&\quad+
\sum_{U,V}U^2V^2\mu_w(\mathfrak R_\tau(V))\\
&\quad+
\sum_{a,b}\sum_{U,V}U^2V^2\mu_w(\mathfrak E^{a,b}_{U,V}).
\end{aligned}
\]

Thus T34 follows if all three families of budgets are summable with total \(O(X^{3-\eta})\).

---

## 5. The remainder ledgers must use complementary factor control

The first remainder term cannot generally be bounded by its measure alone, because the factor \(V^2\) is still present. A direct sufficient estimate is
\[
\boxed{
\sum_{U,V}U^2V^2\mu_w(\mathfrak R_\sigma(U)\cap\{|S_\tau|\asymp V\})
\ll X^{3-\eta}.
}
\]

Equivalently, one may control it directly by energy:
\[
\boxed{
\int_0^1w(\alpha)|\mathcal E_\sigma(\alpha)|^2|S_\tau(\alpha)|^2d\alpha
\ll X^{3-\eta},
}
\]
and symmetrically for \(\mathcal E_\tau\).

This avoids the false move of treating an error term as negligible without accounting for its product with the other prime sum.

---

## 6. Component-pair theorem target

For every required pair \((a,b)\), a sufficient joint large-values theorem is
\[
\boxed{
\sum_{U,V}^{\rm dyadic}
U^2V^2
\mu_w\left(
\left\{
|\mathcal B_{\sigma,a}|>
\frac{(1-\varepsilon)U}{A_\sigma},
\quad
|\mathcal B_{\tau,b}|>
\frac{(1-\varepsilon)V}{A_\tau}
\right\}
\right)
\ll
\frac{X^{3-\eta}}{A_\sigma A_\tau(\log X)^B},
}
\]
for enough logarithmic slack \(B\) to absorb the finite component-pair sum and all dyadic sums.

A more natural formulation absorbs the threshold rescaling:
\[
\boxed{
\sum_{U',V'}^{\rm dyadic}
U'^2V'^2
\mu_w\{|​\mathcal B_{\sigma,a}|>U',\ |\mathcal B_{\tau,b}|>V'\}
\ll
X^{3-\eta}(\log X)^{-B}.
}
\]

The exact allocation over pairs may be nonuniform; it only needs to be summable.

---

## 7. Why this reduction is substantive

T35 does not prove a Type-I/II estimate. It does three necessary things:

\[
\text{it keeps the Goldbach product }S_\sigma S_\tau\text{ intact},
\]

\[
\text{it exhibits the exact component-count loss},
\]

\[
\text{it isolates remainder products instead of declaring them harmless.}
\]

The hard theorem is now finite and explicit: establish the joint large-values bound for each actual Type-I/II pair appearing in the decomposition.

---

## 8. Outcome

The corrected density-one far-minor route is
\[
S_\sigma,S_\tau
\to
\text{joint full-sum large values}
\to
\text{remainder energy + finite component pairs}
\to
\text{Type-I/II joint large-values theorem}
\to
X^{3-\eta}\text{ energy bound}.
\]

This is the final structural reduction before a genuine analytic estimate must enter.