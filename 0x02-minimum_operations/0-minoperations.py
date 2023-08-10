#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(n: int) -> int:
    """a method that calculates the fewest number of operations needed to
    result n characters in a file"""

    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if n <= 1:
        return 0
    # start loop from 2 to n
    for i in range(2, n + 1):
        # if n has factors in range
        if n % i == 0:
            # recursively check for prime num & add factor
            return minOperations(int(n / i)) + i
    # if n is prime
    return n
