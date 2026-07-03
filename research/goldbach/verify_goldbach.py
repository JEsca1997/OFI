#!/usr/bin/env python3
"""Finite verifier for the Goldbach research track.

Checks every even E in [4, limit] and reports one explicit prime pair.
This is a finite computation only; it is not evidence of a global proof.

Usage:
    python3 verify_goldbach.py --limit 2000000
"""

from __future__ import annotations

import argparse
from math import isqrt
from typing import Optional


def sieve(limit: int) -> bytearray:
    """Return a bytearray whose nth entry is 1 iff n is prime."""
    if limit < 2:
        return bytearray(limit + 1)

    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if is_prime[p]:
            start = p * p
            is_prime[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return is_prime


def goldbach_pair(even_target: int, primes: list[int], is_prime: bytearray) -> Optional[tuple[int, int]]:
    """Return one unordered Goldbach pair, or None if no pair is found."""
    if even_target < 4 or even_target % 2:
        raise ValueError("Target must be an even integer at least 4.")
    for p in primes:
        if p > even_target // 2:
            break
        q = even_target - p
        if is_prime[q]:
            return p, q
    return None


def sector(p: int, q: int) -> str:
    """Classify a non-exceptional pair by its mod-6 Goldbach branch."""
    if p == 3 or q == 3:
        return "exceptional-3"
    residues = tuple(sorted((p % 6, q % 6)))
    return {
        (1, 1): "C2 (+,+)",
        (1, 5): "C0 (+,-)",
        (5, 5): "C4 (-,-)",
    }.get(residues, f"unexpected residues {residues}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify Goldbach through a finite cutoff.")
    parser.add_argument("--limit", type=int, default=2_000_000, help="Inclusive even cutoff; default: 2,000,000")
    parser.add_argument("--examples", type=int, default=12, help="Number of sample decompositions to print")
    args = parser.parse_args()

    if args.limit < 4:
        raise SystemExit("--limit must be at least 4")
    limit = args.limit if args.limit % 2 == 0 else args.limit - 1

    is_prime = sieve(limit)
    primes = [n for n in range(2, limit + 1) if is_prime[n]]
    failures: list[int] = []
    samples: list[tuple[int, int, int, str]] = []

    for even_target in range(4, limit + 1, 2):
        pair = goldbach_pair(even_target, primes, is_prime)
        if pair is None:
            failures.append(even_target)
            continue
        if len(samples) < args.examples:
            p, q = pair
            samples.append((even_target, p, q, sector(p, q)))

    print(f"checked every even integer from 4 through {limit:,}")
    print(f"primes sieved: {len(primes):,}")
    print(f"failures: {len(failures)}")
    if failures:
        print("first failures:", failures[:20])
        raise SystemExit(1)

    print("sample witnesses:")
    for even_target, p, q, branch in samples:
        print(f"  {even_target} = {p} + {q}    [{branch}]")


if __name__ == "__main__":
    main()
