#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """Create a function def canUnlockAll(boxes): that returns True if all boxes
    can be opened, else return False
    """
    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    return len(keys) == len(boxes)
