# OFI × Goldbach: Triangular-Spline Arithmetic Experiment Design

**Status:** research design and falsification protocol.  
**Purpose:** integrate the existing OFI operator architecture into the Goldbach program without treating OFI geometry as a substitute for prime arithmetic.

---

## 0. Design decision

The OFI repository supplies four reusable structural ingredients:

1. **Riesz operator:** \(I^\alpha\) with Fourier multiplier \(|\xi|^{-\alpha}\).
2. **Semigroup:** \(I^\alpha I^\beta=I^{\alpha+\beta}\).
3. **Defect functional:** compare an observable before and after an OFI lift.
4. **Euler--Maclaurin/Bernoulli regularization:** the repository treats a \(1/12\)-type correction and the vacuum pair \((-1,1/12)\) as central structural data.

For Goldbach, those ingredients must sit **above an explicit prime sequence**, not below it:

\[
\boxed{
\text{prime coefficients}
\to
\text{half-step triangular lattice}
\to
\text{boxcar/B-spline synthesis}
\to
\text{discrete Riesz/OFI lift}
\to
\text{coefficient extraction}
\to
\text{analytic lower-bound test}.
}
\]

The prime support is always supplied by \(\theta\) or \(\Lambda\). OFI is tested as a structured regularizer and estimator of the resulting additive correlations.

---

## 1. Arithmetic source layer

For a cutoff \(N\), define
\[
\theta^{(N)}(n)=\begin{cases}\log n,&n\le N\text{ prime},\\0,&\text{otherwise},\end{cases}
\qquad
\Lambda^{(N)}(n)=\begin{cases}\log p,&n=p^k\le N,\\0,&\text{otherwise}.\end{cases}
\]

Separate the mod-\(6\) branches
\[
\theta^{(N)}_\pm(n)=\theta^{(N)}(n)\mathbf 1_{n\equiv\pm1\pmod6},
\]
with the prime \(3\) recorded as an isolated exceptional component.

The primary proof observable remains
\[
\mathfrak G_{\sigma,\tau}(E)
=(\theta_\sigma*\theta_\tau)(E),
\qquad (\sigma,\tau)\in\{(+,-),(+,+),(-,-)\}.
\]

Nothing in the spline, OFI, or vacuum layers is allowed to replace this definition.

---

## 2. Centered triangular lattice

Use the centered coordinate
\[
x_n=n+\frac12,
\qquad
T_n=\frac{n(n+1)}2=\frac12x_n^2-\frac18.
\]

This is the appropriate discrete--continuous coordinate for the experiment because
\[
T_{n+1}-T_n=n+1,
\qquad
\frac{d}{dx}\left(\frac{x^2}{2}-\frac18\right)=x.
\]

The half shift avoids choosing a preferred integer endpoint and makes the product of two lifted atoms land at
\[
x_a+x_b=(a+b)+1.
\]
That is exactly the additive coordinate required by Goldbach.

---

## 3. Boxcar and B-spline synthesis layer

Define the centered boxcar
\[
B_0(x)=\mathbf 1_{[-1/2,1/2]}(x),
\]
and the centered cardinal B-splines
\[
B_m=B_0^{*(m+1)}\qquad(m\ge0).
\]

For each branch, synthesize the continuous field
\[
\Phi^{(N)}_{m,\sigma}(x)
=
\sum_{n\le N}\theta^{(N)}_\sigma(n)B_m(x-x_n).
\]

The B-spline derivative recurrence gives an exact discrete-difference interface:
\[
\frac{d}{dx}B_m(x)
=
B_{m-1}\!\left(x+\frac12\right)-B_{m-1}\!\left(x-\frac12\right).
\]
Thus differentiation of the spline field implements a centered first-difference operator on the coefficient sequence. This is the concrete location for the repository’s \(D\)-arm.

### Coefficient-extraction rule

A raw continuous correlation is **not** automatically the Goldbach coefficient. Instead use the identity
\[
\Phi_{m,\sigma}^{(N)}*\Phi_{m,\tau}^{(N)}
=
\sum_{r\le2N}
\mathfrak G_{\sigma,\tau}^{(N)}(r)
B_{2m+1}(x-(r+1)).
\]

Let \(\widetilde B_{2m+1}\) be a biorthogonal dual to the integer shifts of \(B_{2m+1}\) on the generated shift-invariant space. Define
\[
\mathcal C_{m,\sigma,\tau}^{(N)}(E)
=
\left\langle
\Phi_{m,\sigma}^{(N)}*\Phi_{m,\tau}^{(N)},
\widetilde B_{2m+1}(\cdot-(E+1))
\right\rangle.
\]
Then
\[
\boxed{\mathcal C_{m,\sigma,\tau}^{(N)}(E)=\mathfrak G_{\sigma,\tau}^{(N)}(E).}
\]

This dual-extraction condition is mandatory. It prevents spline smoothing from being mistaken for an exact proof coefficient.

---

## 4. Discrete OFI / Riesz lift

The repository’s continuous Riesz operator has multiplier \(|\xi|^{-\alpha}\). The arithmetic-compatible experiment uses its positive-frequency discrete analogue:
\[
\mathcal I_\beta\!\left(\sum_{n\ge1}a_ne(nx)\right)
=
\sum_{n\ge1}n^{-\beta}a_ne(nx),
\qquad \beta\in\mathbb R,
\]
first at finite cutoff. It has the exact OFI semigroup law
\[
\mathcal I_\beta\mathcal I_\gamma=\mathcal I_{\beta+\gamma}.
\]

For branch data, define
\[
S_{\sigma,N}(x)=\sum_{n\le N}\theta_\sigma^{(N)}(n)e(nx),
\qquad
S^{(\beta)}_{\sigma,N}=\mathcal I_\beta S_{\sigma,N}.
\]
The weighted Goldbach coefficient is
\[
\mathfrak G^{(\beta)}_{\sigma,\tau}(E)
=
\sum_{a+b=E}a^{-\beta}b^{-\beta}
\theta_\sigma(a)\theta_\tau(b).
\]

Because all weights are strictly positive for finite \(a,b\),
\[
\boxed{
\mathfrak G^{(\beta)}_{\sigma,\tau}(E)>0
\Longleftrightarrow
\mathfrak G_{\sigma,\tau}(E)>0.
}
\]

This is the exact validity property that allows an OFI lift to participate in Goldbach research: it preserves existence of representations, but does not invent them.

---

## 5. Defect functional redesigned for arithmetic

The physical-Lagrangian defect in the OFI repository is not directly an arithmetic object. Replace it, for this experiment, with a **coefficient defect**:
\[
\mathscr D_{m,\beta}^{\sigma,\tau}(E)
:=
\mathfrak G_{\sigma,\tau}(E)
-
E^{2\beta}\mathfrak G^{(\beta)}_{\sigma,\tau}(E).
\]

The scaling \(E^{2\beta}\) is chosen because each contributing pair satisfies \(a+b=E\); it places the weighted and unweighted coefficients on comparable polynomial scale.

This defect is measurable, falsifiable, and can be studied numerically. The experiment asks whether it admits a bound of the form
\[
|\mathscr D_{m,\beta}^{\sigma,\tau}(E)|
\le C_{m,\beta}E^{1-\delta}
\]
or an explicitly better sector-sensitive analogue. No such bound is assumed.

---

## 6. Euler--Maclaurin and the \(1/12\) issue

The repository identifies \(B_2/2=1/12\) with a central OFI correction. In the present experiment it must be used as a **calibrated summation correction**, not as a direct lower bound on a Goldbach coefficient.

For the centered grid, the Euler--Maclaurin expansion uses Bernoulli polynomials:
\[
\sum_{n=0}^{M-1}f\!\left(n+\frac12\right)
=
\int_0^M f(x)\,dx
+
\sum_{k\ge1}\frac{B_k(1/2)}{k!}
\left(f^{(k-1)}(M)-f^{(k-1)}(0)\right).
\]
In particular,
\[
B_2(1/2)=-\frac1{12},
\qquad
\frac{B_2(1/2)}{2!}=-\frac1{24}.
\]

Therefore the sign and normalization differ from the unshifted \(B_2/2=+1/12\) convention. The experiment must report both conventions explicitly and may not transfer a \(+1/12\) correction into the midpoint lattice without derivation.

### Vacuum-arm role

The pair \((-1,1/12)\) may be tested as a **parameterized renormalization family**:
\[
\beta\in[-1,1/12],
\]
but only values for which the finite-cutoff transforms, coefficient extraction, and error controls are well-defined are admissible. Negative \(\beta\) magnifies high modes and is a stress-test arm, not a positivity argument.

---

## 7. \(V_4\) and mod-\(3\) character layer

Keep the \(V_4\) system as a sorting symmetry. For actual analytic computation, use
\[
A=\theta-\theta_3,
\qquad
B=\chi_3\theta,
\]
so that
\[
\theta_+=\frac{A+B}{2},
\qquad
\theta_-=\frac{A-B}{2}.
\]
The three sectors are exactly
\[
\mathfrak G_0=\frac14(A*A-B*B),
\]
\[
\mathfrak G_2=\frac14(A*A+2A*B+B*B),
\]
\[
\mathfrak G_4=\frac14(A*A-2A*B+B*B).
\]

The experiment must track ordinary and \(\chi_3\)-twisted channels separately. A result obtained only after recombining them is insufficient for the mixed sector, where cancellation is the main risk.

---

## 8. Spectral readout and prime-power stripping

The prime-only experiment is evaluated through the analytic proxy
\[
-\frac{\zeta'}{\zeta}(s)=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},
\qquad
-\frac{L'}{L}(s,\chi_3)=\sum_{n\ge1}\frac{\chi_3(n)\Lambda(n)}{n^s}.
\]

For the OFI-lifted sums this becomes a shift of the Dirichlet parameter:
\[
\sum_{n\ge1}\frac{\Lambda(n)n^{-\beta}}{n^s}
=-\frac{\zeta'}{\zeta}(s+\beta),
\]
with the corresponding \(L\)-function identity in the twisted channel.

Any \(\Lambda\)-weighted lower bound must beat a prime-power correction before it is called a strong-Goldbach result. A deliberately safe target is
\[
R_\Lambda(E)-G(E)=O\!\left(\sqrt E\log^3E\right).
\]

---

## 9. Experiment matrix

| Axis | Values | Purpose |
|---|---|---|
| cutoff | \(N=10^4,10^5,10^6,\dots\) | test stability across scale |
| spline degree | \(m=0,1,2,3,4\) | inspect local-support and extraction conditioning |
| OFI order | \(\beta=0,1/24,1/12,1/8,1/6,\dots\) | test semigroup and weighting sensitivity |
| stress arm | \(\beta<0\), finite cutoff only | detect UV amplification and numerical instability |
| sector | \(0,2,4\bmod6\) | prevent aggregate data from hiding mixed-sector failure |
| observable | \(\theta,\Lambda,\chi_3\Lambda\) | separate true prime support from spectral proxy |

### Required controls

1. **Identity control:** \(\beta=0\), \(m=0\), dual extraction must reproduce direct convolution exactly.
2. **Semigroup control:** applying \(\mathcal I_{\beta_1}\) then \(\mathcal I_{\beta_2}\) equals \(\mathcal I_{\beta_1+\beta_2}\) numerically to stated tolerance.
3. **Spline reconstruction control:** synthesize then dual-extract a known sparse test sequence exactly up to floating-point/rational arithmetic tolerance.
4. **Composite decoy control:** replace \(\theta\) by the full \(6n\pm1\) mask. The method must visibly distinguish this decoy from the true prime signal; otherwise it has not solved the prime-indicator problem.
5. **Character control:** independently compute \(\theta_\pm\) and \((A\pm B)/2\), and require coefficientwise equality.
6. **Prime-power control:** independently compute \(R_\Lambda-G\) and compare with the declared remainder bound.

---

## 10. Falsification gates

The OFI experiment fails as a Goldbach route at any gate below:

- a dual spline extractor does not recover direct Goldbach coefficients;
- positive OFI lifting changes the zero/nonzero support of a sector coefficient;
- the apparent gain disappears against the full \(6n\pm1\) composite decoy;
- the gain occurs only after summing sectors, while the mixed \(0\bmod6\) sector remains uncontrolled;
- a proposed \(1/12\) term changes sign or size under the centered-grid convention and is still used unchanged; or
- no quantitative error bound follows from the observed regularization.

Numerical success without a uniform bound is evidence for a useful estimator only, not a proof.

---

## 11. The actual theorem ladder

The experiment is successful only if it advances through this ladder:

1. **Exact representation theorem:** dual spline extraction returns \(\mathfrak G_j(E)\) coefficientwise.
2. **OFI invariance theorem:** for every admissible \(\beta\), the lifted coefficient has the same positivity support.
3. **Arithmetic defect theorem:** prove a nontrivial deterministic bound on \(\mathscr D_{m,\beta}^j(E)\).
4. **Spectral estimate theorem:** derive a sectorwise lower bound for the \(\zeta/L\)-readout after OFI lifting.
5. **Prime-power theorem:** prove that the lower bound exceeds the \(O(\sqrt E\log^3E)\) stripping allowance.
6. **Finite verification:** check all remaining even \(E<E_0\) by two independent implementations.

Only Steps 1--2 are definitions/identities. Step 4 is the current global bottleneck.

---

## 12. Immediate implementation plan

Create a small reproducible module with:

```text
research/goldbach/ofi_experiment/
  sieve.py                 # theta, Lambda, chi_3
  sectors.py               # direct convolutions and character identities
  splines.py               # B_0...B_4 and dual coefficient extraction
  discrete_riesz.py        # I_beta and semigroup tests
  euler_maclaurin.py       # centered-grid correction ledger
  run_matrix.py            # full parameter sweep and JSON/CSV outputs
  tests/                   # six controls in Section 9
```

Use exact integer indices and high-precision/rational values wherever possible. Floating point is acceptable only for spline quadrature after direct-coefficient controls have passed.

---

## 13. Honest conclusion

This design uses the repo’s actual OFI core—Riesz multiplier, semigroup, defect language, and Bernoulli regularization—while assigning each item a falsifiable arithmetic job.

It does **not** assert that the existing OFI papers already contain the prime-correlation estimate needed for Goldbach. The experiment is designed to discover whether the triangular/B-spline/OFI lift yields a new uniform bound. Until that happens, the work is a rigorous research program, not a completed proof.
