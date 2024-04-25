#!/usr/bin/python3
"""
Minimum operations
"""


def minOperations(n):
    """Create a function def minOperations(n): that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    for i in range(2, n):
        if n % i == 0:
            return minOperations(n // i) + i
    return n
