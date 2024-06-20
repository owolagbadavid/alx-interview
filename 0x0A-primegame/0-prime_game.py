#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """Prime Game"""
    if x < 1 or nums is None:
        return None
    n = max(nums)
    primes = [True for _ in range(max(n + 1, 2))]
    primes[0], primes[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    primes_count = [0 for _ in range(len(primes))]
    count = 0
    for i in range(len(primes)):
        if primes[i]:
            count += 1
        primes_count[i] = count
    player = 0
    for i in nums:
        player += primes_count[i] % 2 == 1
    if player * 2 == len(nums):
        return None
    if player * 2 == len(nums) - 1:
        return "Maria"
    return "Ben"
