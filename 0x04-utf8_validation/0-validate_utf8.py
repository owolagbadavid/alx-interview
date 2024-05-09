#!/usr/bin/python3
"""
0-validate_utf8.py
"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    n_bytes = 0
    for num in data:
        mask1 = 1 << 7
        if n_bytes == 0:
            mask = 1 << 7
            while mask & num:
                n_bytes += 1
                mask = mask >> 1
            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask1 << 1)):
                return False
        n_bytes -= 1
    return n_bytes == 0
