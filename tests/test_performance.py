import random
from itertools import chain

import pytest

from target import TARGET, selector
from weasels import POSSIBLE_CHARS, WeaselGenerator

SEEDS = range(30)
MAX_GENERATIONS = 500
BASELINE_AVERAGE_GENERATIONS = 42.53333333333333


def generations_to_target(seed):
    random.seed(seed)
    initial = ''.join(random.choice(POSSIBLE_CHARS) for _ in range(len(TARGET)))
    generator = WeaselGenerator(initial)
    for generation in range(1, MAX_GENERATIONS + 1):
        _, score = selector([generator.weasel])
        if score == 0:
            return generation
        selected, _ = selector(chain((generator.weasel,), generator.generate_new_mutations()))
        generator.weasel = selected
    return MAX_GENERATIONS + 1


@pytest.mark.performance
def test_average_generations_does_not_regress():
    runs = [generations_to_target(seed) for seed in SEEDS]
    average = sum(runs) / len(runs)
    assert average <= BASELINE_AVERAGE_GENERATIONS
