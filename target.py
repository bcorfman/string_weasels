import sys

from Levenshtein import distance

TARGET = 'Methinks it is like a weasel.'


def selector(mutations):
    best_value = sys.maxsize
    selection = None
    for mutation in mutations:
        dist = distance(mutation, TARGET)
        if dist < best_value:
            best_value = dist
            selection = mutation
    return selection, best_value
