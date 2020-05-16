import sys

from Levenshtein import distance

TARGET = "Methinks it looks like a weasel."
PADDING = 2
TARGET_WIDTH = len(TARGET) + PADDING


def selector(mutations):
    best_value = sys.maxsize
    selection = None
    for mutation in mutations:
        dist = distance(mutation, TARGET)
        if dist < best_value:
            best_value = dist
            selection = mutation
    return selection, best_value
