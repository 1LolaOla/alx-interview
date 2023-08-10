#!/usr/bin/python3
"""Minimum Operations"""

def minOperations(n):
    """a method that calculates the fewest number of operations needed to
    result n characters in a file"""

    # all outputs should be at least 2 char: (min, Copy All => Paste)
   if not isinstance(n, int):
        return 0

    op = 0
    i = 2
    while (i <= n):
        if not (n % i):
            n = int(n / i)
            op += i
            i = 1
        i += 1
    return op
