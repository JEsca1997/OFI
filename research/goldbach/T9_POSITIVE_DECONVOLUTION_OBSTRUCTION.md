# T9: Positive Deconvolution Obstruction and Pointwise Bridge

**Status:** elementary obstruction theorem plus a precise list of admissible pointwise routes.  
**Purpose:** prevent a false upgrade from an OFI-windowed almost-all theorem to pointwise Goldbach positivity.

---

## 1. The tempting but invalid shortcut

Let \(g=(g_E)_{E\in\mathbb Z}\) be a nonnegative Goldbach-correlation sequence and let \(\omega\) be a nonnegative local output window. Suppose one proves
\[
A=\omega*g
\]
is strictly positive at every target. It is tempting to claim that positivity of \(A\) forces positivity of every \(g_E\) after exact deconvolution.

That implication is false for a nontrivial local average: a zero coefficient can be masked by positive nearby coefficients.

The obstruction below shows why no positivity-preserving exact inverse exists for such a window.

---

## 2. Positive deconvolution obstruction

### Lemma

Let \(\omega,v:\mathbb Z\to[0,\infty)\) be nonzero sequences for which the convolution is defined and
\[
\omega*v=\delta_0.
\]
Then there exist \(a\in\mathbb Z\) and \(c>0\) such that
\[
\omega=c\,\delta_a,
\qquad
v=c^{-1}\,\delta_{-a}.
\]

### Proof

Choose \(a\in\operatorname{supp}\omega\) and \(b\in\operatorname{supp}v\). Since all summands are nonnegative and \((\omega*v)(n)=0\) for \(n\ne0\), one must have
\[
a+b=0.
\]

If \(a'\in\operatorname{supp}\omega\), then also \(a'+b=0\), hence \(a'=a\). Thus \(\operatorname{supp}\omega=\{a\}\). The identical argument gives \(\operatorname{supp}v=\{-a\}\). The coefficient condition at zero gives the stated reciprocal constants. \(\square\)

### Consequence

\[
\boxed{
\text{No nontrivial nonnegative local average on }\mathbb Z
\text{ has a nonnegative exact convolution inverse.}
}
\]

Thus a positive OFI output window cannot be both genuinely local/smoothing and positivity-preserving under exact inversion.

---

## 3. What this means for the OFI construction

The B-spline / dual-extractor scheme is still valid because exact extraction uses a generally **signed** dual, or a local approximation with a charged tail. But that also means:

\[
A_{u,\psi}(E)>0
\not\Rightarrow
 g_E>0
\]
without an independent quantitative error comparison.

The exact T3 certificate remains the correct statement:
\[
g_E
\ge
\mathcal C_{u,R,E}[\widehat H_u]
-
\eta_u(N)\|\widetilde\gamma_{u,R}\|_2
-
\|H_u\|_2\varepsilon_u(R).
\]

It can certify one coefficient only when the local functional exceeds every signed reconstruction and approximation error.

---

## 4. Why minimal-counterexample induction does not close T9 by itself

Assume for contradiction that \(E_0\) is the least even target with \(g_{E_0}=0\). Information that all smaller even targets have positive coefficients does not algebraically force
\[
g_{E_0}>0.
\]

Goldbach coefficients are additive correlations of prime indicators, not values of a recurrence with a positivity-propagation law. A valid descent would require a new theorem of the form
\[
g_E=0
\Longrightarrow
\text{a concrete contradiction involving coefficients at smaller targets},
\]
or a monotone invariant that cannot occur at a first zero.

Neither B-spline smoothing, compactness, nor countable-cover arguments supplies such a recurrence automatically.

---

## 5. Three legitimate pointwise bridges

### Bridge P1 — Direct pointwise minor-arc theorem

Prove, for every admissible even \(E\ge E_0\),
\[
\left|
\int_{\mathfrak m}
\Omega_{u,\psi}(\alpha)
T_{\sigma,N}(\alpha)T_{\tau,N}(\alpha)e(-E\alpha)
\,d\alpha
\right|
\le cE
\]
with a constant strictly below the major-arc lower constant after all ledgers are charged.

This is the conventional direct route.

### Bridge P2 — Local deficit propagation

Prove a quantitative theorem saying that a zero at \(E\) creates a whole block of sizeable deficits in the OFI local output:
\[
g_E=0
\Longrightarrow
\sum_{|h|\le H(E)}
|A_{u,\psi}(E+h)-M(E+h)|^2
\ge cE^2H(E).
\]

Combined with T8, this could rule out even one zero if the global mean-square budget is smaller than the forced local deficit.

This is a serious new local-correlation theorem, not a consequence of averaging.

### Bridge P3 — Exact finite verification plus uniform theorem

Prove a uniform theorem for all \(E\ge E_0\) by P1 or P2, then check every even target below \(E_0\) by an independent exact computation.

This is the cleanest final assembly route once a true asymptotic pointwise theorem exists.

---

## 6. Possible role of topology after the obstruction

Topology can still organize a proof of P1 or P2:

- compact local dual windows give finite-support test objects;
- finite covers of minor-arc regimes organize different estimates;
- \(T_1\) separation keeps coefficient atoms distinct;
- countable compactness/limit-point compactness can support subsequence extraction in a compactified parameter space.

But topology cannot convert positivity of a nontrivial local average into positivity of its center coefficient. The positive-deconvolution lemma is the exact reason.

---

## 7. Exact T9 target

The pointwise boss fight can now be stated without ambiguity:

\[
\boxed{
\text{Either prove a uniform post-extraction minor-arc bound (P1),
or prove zero-forces-block-deficit propagation (P2).}
}
\]

Everything else in the OFI construction—B-splines, fractional order, Bernoulli corrections, compact local windows, sector decomposition, and weighted moments—has to feed one of those two statements.

Until P1 or P2 is established, the program supports exact representations and conditional/almost-all results, but not a proof of every even integer.