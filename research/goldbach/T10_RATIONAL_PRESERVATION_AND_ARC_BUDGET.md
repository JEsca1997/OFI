# T10: Rational Preservation and Denominator-Stratified Arc Budget

**Status:** exact design constraints; no binary-Goldbach estimate is claimed.  
**Purpose:** state what an OFI output multiplier must preserve on major arcs, what it must save on minor arcs, and why a short local window cannot be treated as a free sharp arc cutoff.

---

## 1. The OFI multiplier is an additive-output trigonometric polynomial

Let the compact local output kernel be supported in \([-H,H]\cap\mathbb Z\):
\[
\omega_h=0\qquad(|h|>H),
\qquad
\sum_h\omega_h=1.
\]
Its periodic multiplier is
\[
\Omega_H(\alpha)=\sum_{|h|\le H}\omega_h e(\alpha h),
\qquad
\Omega_H(0)=1.
\]

This multiplier acts on the additive Goldbach frequency variable. It is not an independently chosen circle-method cutoff.

---

## 2. Rational preservation is mandatory

The ordinary major-arc main term is assembled from neighborhoods of many rationals \(a/q\), not only from \(0\). Therefore a multiplier that is small at relevant \(a/q\) can erase part of the singular-series contribution.

For a standard major-arc set \(\mathfrak M(Q,N)\), a sufficient preservation requirement is
\[
\boxed{
|\Omega_H(\alpha)-1|\le\varepsilon
\qquad(\alpha\in\mathfrak M(Q,N)).
}
\]

Under this condition, the weighted major term differs from the unweighted major term by at most an \(\varepsilon\)-fraction of the corresponding absolute major-arc integral, plus the original major-arc approximation error.

The exact weighted main term must retain the factors \(\Omega_H(a/q)\). Replacing them by \(1\) without a quantitative preservation bound is invalid.

---

## 3. Derivative/uncertainty constraint for compact windows

Because \(\Omega_H\) is a trigonometric polynomial of degree at most \(H\), Bernstein's inequality gives
\[
\boxed{
\|\Omega_H'\|_\infty
\le 2\pi H\|\Omega_H\|_\infty.
}
\]

Hence if \(\Omega_H\) changes by an amount at least \(c>0\) across a frequency interval of width \(\Delta\), then
\[
H\ge \frac{c}{2\pi\Delta\|\Omega_H\|_\infty}.
\]

A compact output window therefore cannot create an arbitrarily sharp major/minor separator unless its support radius is correspondingly large. Large \(H\), in turn, enlarges the local averaging radius and changes the T3 reconstruction-tail budget.

This is the exact locality-versus-frequency-selectivity tradeoff for the OFI branch.

---

## 4. Denominator-stratified minor arcs

Partition the minor arcs into finitely many denominator regimes
\[
\mathfrak m(Q,N)=\bigcup_{r=1}^{R}\mathfrak m_r,
\]
where each \(\mathfrak m_r\) consists of frequencies whose best rational approximants have denominators in a specified dyadic range.

Define the weighted sector contribution
\[
\mathcal I_{r,j}^{\Omega}(E)
=
\int_{\mathfrak m_r}
\Omega_H(\alpha)
T_{\sigma,N}(\alpha)T_{\tau,N}(\alpha)e(-E\alpha)\,d\alpha.
\]

A pointwise P1 theorem follows from an explicit arc budget
\[
\boxed{
\sum_{r=1}^{R}
\left|\mathcal I_{r,j}^{\Omega}(E)\right|
\le
\vartheta\,c_0\mathfrak S_j(E)E
}
\]
with \(0<\vartheta<1\), after adding the major-arc, dual-tail, and prime-power ledgers.

This formulation forces every denominator regime to pay its own bill. There is no global phrase such as “the minor arcs are damped” standing in for the sum.

---

## 5. Three admissible kinds of OFI benefit

The order/window pair \((u,H)\) is useful only if it provides a theorem in at least one of these forms:

1. **Major-rational preservation:** \(\Omega_H(a/q)\) remains quantitatively close to \(1\) for all rational centers that carry material main-term mass.
2. **Regime-selective saving:** for at least one difficult stratum \(\mathfrak m_r\), the weighted estimate is smaller than the baseline estimate by a factor that exceeds the loss in all other regimes and ledgers.
3. **Averaged denominator saving:** \(\Omega_H\) interacts with a Type-I/II mean value so as to lower the summed denominator-stratified budget.

A small value of \(|\Omega_H|\) somewhere on the circle is not enough.

---

## 6. Baseline comparison

Take the triangular/cardinal baseline \(u_0=2\) with its associated local kernel. For another stable fractional order \(u\), define the total certified error budget
\[
\mathfrak E_u(E)
=
\sum_r|\mathcal I_{r,j}^{\Omega_u}(E)|
+\mathcal E^{\mathfrak M}_u(E)
+\mathcal E^{\mathrm{dual}}_u(E)
+\mathcal E^{\mathrm{pp}}(E).
\]

The order earns promotion only if one proves
\[
\mathfrak E_u(E)<\mathfrak E_{u_0}(E)
\]
uniformly on the target range while its weighted major term remains positive and of order \(E\).

---

## 7. Immediate consequence for the project

T10 rules out treating the OFI window as a magical minor-arc filter. It must solve a coupled design problem:

\[
\boxed{
\text{preserve rational major arcs}
\quad+\quad
\text{gain on denominator-stratified minor arcs}
\quad+\quad
\text{pay the local-extraction cost}.}
\]

The next concrete theorem is now a sector-aware bound for one selected difficult denominator regime, with \(\Omega_H\) retained explicitly throughout.