TARGET = "Methinks it is like a weasel."
PADDING = 2
TARGET_WIDTH = len(TARGET) + PADDING


def mismatch_score(candidate):
    return abs(len(candidate) - len(TARGET)) + sum(left != right for left, right in zip(candidate, TARGET))


def selector(mutations):
    best_value = len(TARGET) + 1
    selection = None
    for mutation in mutations:
        score = mismatch_score(mutation)
        if score < best_value:
            best_value = score
            selection = mutation
    return selection, best_value
