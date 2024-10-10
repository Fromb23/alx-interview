#!/usr/bin/python3
"""
    lockboxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    boxes (list of lists): A list where each element
    is a list of keys contained in that box.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    unlocked = set()
    to_check = [0]

    while to_check:
        current_box = to_check.pop()
        if current_box not in unlocked:
            unlocked.add(current_box)
            for key in boxes[current_box]:
                if key not in unlocked:
                    to_check.append(key)

    return len(unlocked) == len(boxes)
