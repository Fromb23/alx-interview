#!/usr/bin/python3

def canUnlockAll(boxes):
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
