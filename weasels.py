import random
import sys
import string

INITIAL_TARGET_LENGTH = 7
MAX_CHILDREN = 1000
POSSIBLE_CHARS = string.whitespace + string.ascii_letters + string.punctuation


class WeaselGenerator:
    def __init__(self, initial=None):
        if initial is None:
            self._weasel = ''.join([random.choice(POSSIBLE_CHARS) for _ in range(INITIAL_TARGET_LENGTH)])
        else:
            self._weasel = initial
        self.choices = (self.add_character, self.delete_character, self.change_character)

    def get_weasel(self):
        return self._weasel

    def set_weasel(self, weasel):
        self._weasel = weasel

    def generate_new_mutations(self):
        idx = random.randint(0, len(self._weasel))
        return (random.choice(self.choices)(idx) for i in range(MAX_CHILDREN))

    def add_character(self, idx):
        new_char = random.choice(POSSIBLE_CHARS)
        return self._weasel[0:idx] + new_char + self._weasel[idx:len(self._weasel)]

    def delete_character(self, idx):
        return self._weasel[0:idx] + self._weasel[idx+1:len(self._weasel)]

    def change_character(self, idx):
        new_char = random.choice(POSSIBLE_CHARS)
        return self._weasel[0:idx] + new_char + self._weasel[idx+1:len(self._weasel)]


if __name__ == '__main__':
    from target import selector
    w = WeaselGenerator()
    generation = 0
    distance = sys.maxsize
    while True:
        generation += 1
        weasel, distance = selector([w.get_weasel()])
        print('Generation {}: {}    Distance: {}'.format(generation, weasel, distance))
        if distance == 0:
            break
        new_weasels = w.generate_new_mutations()
        selected_weasel, distance = selector(new_weasels)
        w.set_weasel(selected_weasel)
