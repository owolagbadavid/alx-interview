#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """ Making Change """
    if total <= 0:
        return 0
    coins.sort()
    coins.reverse()
    n = len(coins)
    i = 0
    num_coins = 0
    while i < n and total > 0:
        num_coins += total // coins[i]
        total = total % coins[i]
        i += 1
    if total != 0:
        return -1
    return num_coins
