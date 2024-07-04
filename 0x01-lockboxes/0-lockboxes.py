#!/usr/bin/python3
"""
Module for canUnlockAll method.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    :param boxes: list of lists, where each sublist contains keys to other boxes
    :return: True if all boxes can be opened, else False
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
