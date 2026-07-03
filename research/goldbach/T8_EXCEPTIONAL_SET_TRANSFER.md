# T8: OFI-Weighted Exceptional-Set Transfer

**Status:** exact conditional transfer theorem.  
**Purpose:** separate the attainable "almost all even targets" milestone from the much stronger pointwise binary-Goldbach theorem.

---

## 1. Why an exceptional-set stage is the right next milestone

A weighted fourth-moment or mean-square estimate naturally controls an **average over targets**. It does not automatically control every individual even integer.

The honest intermediate target is therefore:

\[
\#\{E\in[X,2X]\cap2\mathbb Z: E\text{ has no Goldbach representation}\}
=o(X).
\]

This is meaningful progress only when the estimate is stated for the exact sector channels and when the prime-power removal is included.

---

## 2. Exact local output sequence

Let \(R_j(E)\) denote the Mangoldt-weighted Goldbach correlation in the sector required by \(E\bmod6\). Let \(\omega=(\omega_h)\) be the discrete output kernel induced by a compact OFI local dual approximation. Define
\[
A_{u,\psi,j}(E)
:=(\omega*R_j)(E)
=\sum_h\omega_hR_j(E-h).
\]

Equivalently, on the circle,
\[
A_{u,\psi,j}(E)
=
\int_0^1
\Omega_{u,\psi}(\alpha)
T_{\sigma,N}(\alpha)T_{\tau,N}(\alpha)e(-E\alpha)\,d\alpha.
\]

The sequence \(A_{u,\psi,j}\) is the local OFI-extracted output. It is not automatically identical to \(R_j\) at finite window radius; the difference remains in the reconstruction ledger.

---

## 3. Mean-square hypothesis

Fix a dyadic target block
\[
\mathcal E_X:=\{E\in[X,2X]\cap2\mathbb Z:E\text{ is in sector }j\}.
\]

Suppose there is a model main term \(M_{u,\psi,j}(E)\) satisfying
\[
M_{u,\psi,j}(E)\ge c_0X
\qquad(E\in\mathcal E_X)
\]
for some \(c_0>0\), and a weighted mean-square estimate
\[
\boxed{
\sum_{E\in\mathcal E_X}
\left|A_{u,\psi,j}(E)-M_{u,\psi,j}(E)\right|^2
\le C X^{3-\eta}
}
\]
for some \(\eta>0\).

The exponent is chosen so that the average squared error is \(O(X^{2-\eta})\), strictly smaller than the square of the order-\(X\) main term.

---

## 4. Exceptional-set lemma

Define the bad local-output set
\[
\mathcal B_X^{\mathrm{loc}}
:=
\left\{E\in\mathcal E_X:
A_{u,\psi,j}(E)\le\frac{c_0}{2}X
\right\}.
\]

For each \(E\in\mathcal B_X^{\mathrm{loc}}\),
\[
|A_{u,\psi,j}(E)-M_{u,\psi,j}(E)|
\ge\frac{c_0}{2}X.
\]

Therefore
\[
\boxed{
\#\mathcal B_X^{\mathrm{loc}}
\le\frac{4C}{c_0^2}X^{1-\eta}.
}
\]

This is just Chebyshev/Markov applied to the exact mean-square hypothesis. It is a rigorous transfer from a weighted spectral estimate to an almost-all statement about the OFI local output.

---

## 5. Descending from local output to the actual Mangoldt coefficient

Let \(\Delta_{u,\psi,j}(E)\) be the exact local reconstruction discrepancy:
\[
R_j(E)=A_{u,\psi,j}(E)+\Delta_{u,\psi,j}(E).
\]

A sufficient uniform local-tail condition is
\[
\boxed{
|\Delta_{u,\psi,j}(E)|\le\frac{c_0}{4}X
\qquad(E\in\mathcal E_X).
}
\]

Then all targets outside \(\mathcal B_X^{\mathrm{loc}}\) satisfy
\[
R_j(E)\ge\frac{c_0}{4}X.
\]

This is where T3 is used: its compact dual-window tail has to be genuinely small relative to the major term, not merely convergent as the window grows.

---

## 6. Prime-power stripping and actual primes

Let \(G_j(E)\) be the prime-only sector correlation and write
\[
R_j(E)-G_j(E)=\Pi_j(E).
\]

Suppose the prime-power bound obeys, uniformly on \(\mathcal E_X\),
\[
|\Pi_j(E)|\le\frac{c_0}{8}X.
\]

The elementary target \(O(\sqrt X\log^3X)\) is more than sufficient for large \(X\), once its sectorwise constants and exceptional small values are proved.

For every target outside \(\mathcal B_X^{\mathrm{loc}}\),
\[
G_j(E)
\ge
R_j(E)-|\Pi_j(E)|
\ge\frac{c_0}{8}X>0.
\]

Thus:

### Conditional almost-all Goldbach theorem

Under the mean-square hypothesis, the local-tail hypothesis, and the prime-power bound,
\[
\boxed{
\#\{E\in\mathcal E_X:G_j(E)=0\}
\le\frac{4C}{c_0^2}X^{1-\eta}.
}
\]

This yields density-one Goldbach representations in every admissible sector.

---

## 7. What this does not prove

An exceptional-set theorem does **not** prove every even integer is Goldbach. A sparse infinite exceptional set remains possible.

To upgrade from
\[
O(X^{1-\eta})
\]
exceptions to none, the program needs a separate pointwise mechanism, such as:

1. a uniform minor-arc estimate strong enough for every target;
2. a descent/induction that rules out a least exceptional target;
3. a local-density theorem that forces a representation in every short additive neighborhood and an exact unwindowing argument;
4. independent finite verification below a threshold plus a uniform theorem above it.

Neither compactness nor smoothing supplies that upgrade by itself.

---

## 8. OFI-specific contribution test

For a baseline triangle order \(u_0=2\), a fractional order \(u\) makes genuine progress at the exceptional-set level only if it improves the proven exponent or constant after all ledgers are charged:
\[
\eta_u>\eta_{u_0}
\quad\text{or}\quad
C_u<C_{u_0}
\]
while preserving the local-tail requirement.

That creates a falsifiable experimental and theorem-selection rule. The fractional order is not valuable because it is novel; it is valuable only if it strengthens the mean-square correlation theorem or makes its local descent cheaper.

---

## 9. Current theorem ladder

\[
\text{T1--T3: lossless local OFI representation and descent}\]
\[
\text{T4--T7: corrected spectral/minor-arc barriers}\]
\[
\text{T8: conditional density-one transfer}\]
\[
\text{T9: pointwise elimination of the exceptional set (open)}.
\]

T8 is the first realistic arithmetic milestone after the representation architecture. T9 remains the binary-Goldbach boss fight.