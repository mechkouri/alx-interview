#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes)
    keys = {0}
    opened_boxes = set()
    queue = [0]

    while queue:
        box = queue.pop(0)
        if box not in opened_boxes:
            opened_boxes.add(box)
            for key in boxes[box]:
                if key not in keys:
                    keys.add(key)
                if key < n and key not in opened_boxes:
                    queue.append(key)

    return len(opened_boxes) == n

