"""Tiny stats helpers."""


def mean(xs):
    if not xs:
        raise ValueError("mean() of empty sequence")
    return sum(xs) / len(xs)


def median(xs):
    """Return the median of a non-empty sequence."""
    if not xs:
        raise ValueError("median() of empty sequence")
    xs = sorted(xs)
    n = len(xs)
    mid = n // 2
    if n % 2:
        return xs[mid]
    return (xs[mid - 1] + xs[mid]) / 2
