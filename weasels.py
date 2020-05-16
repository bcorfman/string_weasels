import random
import string

INITIAL_TARGET_LENGTH = 7
MAX_CHILDREN = 1000
POSSIBLE_CHARS = " " + string.ascii_letters + string.punctuation


class WeaselGenerator:
    def __init__(self, initial=None):
        if initial is None:
            self._weasel = ''.join([random.choice(POSSIBLE_CHARS) for _ in range(INITIAL_TARGET_LENGTH)])
        else:
            self._weasel = initial
        self.choices = (self.add_character, self.delete_character, self.change_character)

    @property
    def weasel(self):
        return self._weasel

    @weasel.setter
    def weasel(self, value):
        self._weasel = value

    def generate_new_mutations(self):
        idx = random.randint(0, len(self._weasel))
        return (random.choice(self.choices)(idx) for _ in range(MAX_CHILDREN))

    def add_character(self, idx):
        return f'{self._weasel[0:idx]}{random.choice(POSSIBLE_CHARS)}{self._weasel[idx:len(self._weasel)]}'

    def delete_character(self, idx):
        return f'{self._weasel[0:idx]}{self._weasel[idx + 1:len(self._weasel)]}'

    def change_character(self, idx):
        return f'{self._weasel[0:idx]}{random.choice(POSSIBLE_CHARS)}{self._weasel[idx + 1:len(self._weasel)]}'


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
        new_weasels = wg.generate_new_mutations()
        selected_weasel, _ = selector(new_weasels)
        wg.weasel = selected_weasel
