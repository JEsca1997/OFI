# Correction: Transitional Rational-Annulus Gate

**Status:** consequence of the reported in-house fourth-moment diagnostics, conditional on reproducing those computations with archived code and fixed-cutoff controls.  
**Effect:** a polylogarithmic major-arc cutoff cannot be followed immediately by a pure far-minor fourth-moment target with a power saving. The just-past-cutoff rational annuli must be treated as a separate transition regime.

---

## 1. The diagnostic consequence

The reported experiments indicate that, for a cutoff
\[
Q_0=(\log X)^A,
\]
the localized energy
\[
\int_{\mathfrak F(Q_0)}|S(\alpha)|^4d\alpha
\]
is consistent with scale
\[
\asymp \frac{X^3}{Q_0},
\]
and that most of this mass is carried by neighborhoods of rationals with
\[
Q_0<q\le4Q_0.
\]

If this behavior persists under fixed-\(Q_0\), resolution, and cutoff-profile controls, then the T33/T34 target
\[
\int_{\mathfrak F(Q_0)}|S_\sigma|^2|S_\tau|^2\ll X^{3-\eta}
\]
cannot hold for a fixed \(\eta>0\) merely by declaring all denominators \(q>Q_0\) to be far minor.

The obstruction is denominator-localized, not a failure at genuinely irrational frequencies.

---

## 2. Correct three-region partition

Replace the binary major/far split by
\[
1=\chi_{\mathfrak M_0}+\chi_{\mathfrak T}+\chi_{\mathfrak F_1},
\]
where:

\[
\mathfrak M_0
:=
\bigcup_{q\le Q_0}\bigcup_{(a,q)=1}
\left\{\alpha=\frac aq+\beta:\ |\beta|\le\frac{W}{qX}\right\},
\]

\[
\mathfrak T
:=
\bigcup_{Q_0<q\le Q_1}\bigcup_{(a,q)=1}
\left\{\alpha=\frac aq+\beta:\ |\beta|\le\frac{W}{qX}\right\},
\]

and
\[
\mathfrak F_1
:=\mathbb T\setminus(\mathfrak M_0\cup\mathfrak T)
\]
up to smooth collars.

Here \(Q_1\) is not cosmetic. It must be selected from a theorem that controls the rational-annulus contribution.

---

## 3. Annular energy to be estimated

For dyadic \(Q\) with \(Q_0<Q\le Q_1\), define
\[
\mathcal A(Q)
:=
\bigcup_{Q<q\le2Q}\bigcup_{(a,q)=1}
\left\{\frac aq+\beta:\ |\beta|\le\frac{W}{qX}\right\}.
\]

The corrected transition energy is
\[
\boxed{
\mathfrak E_{\sigma,\tau}(Q)
:=
\int_{\mathcal A(Q)}
|S_\sigma(\alpha)|^2|S_\tau(\alpha)|^2d\alpha.
}
\]

The observed collar concentration says that the first annuli
\[
Q\asymp Q_0,\ 2Q_0,\ 4Q_0
\]
are a primary term in the proof ledger, not an error that can be dismissed by a generic far-minor bound.

---

## 4. Rational parametrization of sector sums

Let
\[
L=[q,6].
\]
For \(\alpha=a/q+\beta\), the sector sum decomposes exactly as
\[
S_{\sigma,X}(\alpha)
=
\sum_{\substack{r\bmod L\\r\equiv\sigma\ (6)}}
 e(ar/q)
 \sum_{\substack{n\le X\\n\equiv r\ (L)}}
 \theta(n)e(\beta n).
\]

Thus every annular estimate is an averaged statement about primes in residue classes modulo \([q,6]\), with an additive twist \(e(\beta n)\).

This is where denominator information actually enters. A radial multiplier in \(\alpha\) generally cannot replace it.

---

## 5. The real transition theorem

A usable transition theorem must control the dyadic sum
\[
\boxed{
\sum_{Q_0<Q\le Q_1}^{\rm dyadic}
\mathfrak E_{\sigma,\tau}(Q)
\le
\rho_{\mathfrak T}X^3,
}
\]
with a quantitatively specified \(\rho_{\mathfrak T}\), or preferably a power-saving version after subtraction of an explicit rational model.

For a density-one theorem, it is not enough to use the raw fourth moment if it remains of order \(X^3/Q_0\). One needs either:

\[
\text{(T1) an explicit transition main model and a small residual,}
\]

or

\[
\text{(T2) a denominator-sensitive averaged estimate with a power saving,}
\]

or

\[
\text{(T3) a known zero-density / exceptional-set theorem used transparently as the engine.}
\]

No OFI mechanism currently proves any of (T1)--(T3).

---

## 6. Why a short output window does not solve this gate

Let
\[
\Omega(\alpha)=\sum_{|h|\le H}\omega_he(\alpha h).
\]

Such a multiplier is controlled primarily by the geometric location of \(\alpha\) on the circle. It is not intrinsically a function of the reduced denominator \(q\) in a representation \(\alpha=a/q+\beta\).

The reported experiment further indicates that a Fej\'er-style window can reduce raw energy while losing after the extraction cost. Therefore \(\Omega\) is not retained in the primary transition target unless it supplies a proved denominator-sensitive gain on \(Q_0<q\le Q_1\) that exceeds its exact extraction ledger.

---

## 7. Consequence for the corrected proof spine

The valid decomposition is now
\[
\text{small denominators }q\le Q_0
\quad+\quad
\text{transition denominators }Q_0<q\le Q_1
\quad+\quad
\text{genuinely far region }q>Q_1.
\]

The proof obligations are correspondingly:

\[
\mathfrak M_0:\ \text{standard major model and singular-series positivity},
\]

\[
\mathfrak T:\ \text{denominator-sensitive annular theorem},
\]

\[
\mathfrak F_1:\ \text{a truly far-minor bilinear estimate}.
\]

The former T33 claim that a support-separated model leaves one pure far-minor energy remains algebraically correct, but its designation of all \(q>Q_0\) as the region for a power-saving fourth moment is not viable under the reported data.

---

## 8. Immediate proof-facing experiments

Before asserting any theorem from this gate, archive and reproduce:

1. fixed-\(Q_0\) scaling of \(\mathfrak E(Q_0)\) across \(X\);
2. the sector energies \(|S_+|^2|S_-|^2\), \(|S_+|^4\), and \(|S_-|^4\);
3. annular masses \(\mathfrak E_{\sigma,\tau}(Q)\) for dyadic \(Q\);
4. the same experiment for actual Type-II components from a fixed Vaughan/Heath--Brown identity.

These experiments cannot prove the theorem. They decide whether a proposed theorem is numerically plausible and which denominator range must be attacked.

---

## 9. Outcome

The active proof problem is no longer an undifferentiated far-minor fourth moment. It is:
\[
\boxed{
\text{prove or import a denominator-sensitive transition-annulus estimate.}
}
\]

A claimed OFI advance must state exactly how it changes the contribution of rationals with
\[
Q_0<q\le Q_1,
\]
not merely how it smooths or suppresses frequencies distant from zero.