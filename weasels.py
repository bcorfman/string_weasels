import random
import string
from itertools import chain

MAX_CHILDREN = 1000
MUTATION_RATE = 0.05
POSSIBLE_CHARS = " " + string.ascii_letters + string.punctuation


class WeaselGenerator:
    def __init__(
        self,
        initial=None,
        initial_length=None,
        max_children=MAX_CHILDREN,
        mutation_rate=MUTATION_RATE,
        substitution_only=True,
    ):
        if initial is None:
            if initial_length is None:
                from target import TARGET
                initial_length = len(TARGET)
            self._weasel = ''.join(random.choice(POSSIBLE_CHARS) for _ in range(initial_length))
        else:
            self._weasel = initial
        self.max_children = max_children
        self.mutation_rate = mutation_rate
        self.substitution_only = substitution_only
        self.choices = (self.add_character, self.delete_character, self.change_character)

    @property
    def weasel(self):
        return self._weasel

    @weasel.setter
    def weasel(self, value):
        self._weasel = value

    def generate_new_mutations(self):
        parent = self._weasel
        return (self._mutate_child(parent) for _ in range(self.max_children))

    def _mutate_child(self, parent):
        child = parent
        mutation_count = sum(1 for _ in range(len(parent)) if random.random() < self.mutation_rate)
        for _ in range(mutation_count):
            child = self._mutate_once(child)
        return child

    def _mutate_once(self, source):
        if not source:
            return self.add_character(0, source)
        operation = self.change_character if self.substitution_only else random.choice(self.choices)
        if operation.__name__ == "add_character":
            idx = random.randint(0, len(source))
        else:
            idx = random.randint(0, len(source) - 1)
        return operation(idx, source)

    def add_character(self, idx, source=None):
        source = self._weasel if source is None else source
        return f'{source[:idx]}{random.choice(POSSIBLE_CHARS)}{source[idx:]}'

    def delete_character(self, idx, source=None):
        source = self._weasel if source is None else source
        return f'{source[:idx]}{source[idx + 1:]}'

    def change_character(self, idx, source=None):
        source = self._weasel if source is None else source
        return f'{source[:idx]}{random.choice(POSSIBLE_CHARS)}{source[idx + 1:]}'


if __name__ == '__main__':
    from target import selector, TARGET_WIDTH

    wg = WeaselGenerator()
    generation = 0
    while True:
        generation += 1
        weasel, distance = selector([wg.weasel])
        print(f'Gen {generation:3}: {weasel:{TARGET_WIDTH}}  Distance: {distance}')
        if distance == 0:
            break
        new_weasels = chain((wg.weasel,), wg.generate_new_mutations())
        selected_weasel, _ = selector(new_weasels)
        wg.weasel = selected_weasel
