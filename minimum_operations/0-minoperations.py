#!/usr/bin/python3
"""Find the minimum Copy All and Paste operations for n characters."""


def minOperations(n):
    """Return the sum of prime factors, or zero for invalid targets."""
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n
    return operations
