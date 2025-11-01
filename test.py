from __future__ import annotations
import argparse
import sys

#!/usr/bin/env python3
"""
/home/kingfruit/repos/test/test.py

Small dummy Python script with a few utility functions and a simple CLI.
"""



def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def factorial(n: int) -> int:
    """Return n! for n >= 0. Raises ValueError for negative n."""
    if n < 0:
        raise ValueError("n must be non-negative")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n: int) -> int:
    """Return the n-th Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Dummy utilities: add, factorial, fibonacci")
    p.add_argument("--add", nargs=2, type=float, metavar=("A", "B"), help="Add two numbers")
    p.add_argument("--fact", type=int, metavar="N", help="Compute factorial of N")
    p.add_argument("--fib", type=int, metavar="N", help="Compute N-th Fibonacci number (0-indexed)")
    p.add_argument("--version", action="store_true", help="Show version and exit")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)

    if args.version:
        print("test.py version 0.1")
        return 0

    if args.add:
        a, b = args.add
        print(f"add({a}, {b}) = {add(a, b)}")
        return 0

    if args.fact is not None:
        try:
            print(f"factorial({args.fact}) = {factorial(args.fact)}")
        except ValueError as e:
            print("Error:", e, file=sys.stderr)
            return 2
        return 0

    if args.fib is not None:
        try:
            print(f"fibonacci({args.fib}) = {fibonacci(args.fib)}")
        except ValueError as e:
            print("Error:", e, file=sys.stderr)
            return 2
        return 0

    # If no args provided, show brief usage and run a tiny demo
    print("No arguments given. Demo output:")
    print(" add(1, 2) =", add(1, 2))
    print(" factorial(5) =", factorial(5))
    print(" fibonacci(7) =", fibonacci(7))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())