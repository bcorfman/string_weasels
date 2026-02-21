import pytest

from target import TARGET, selector
from weasels import WeaselGenerator


@pytest.fixture(scope='module')
def weasel_generator():
    return WeaselGenerator('Brandon')


def test_add_character_at_start(weasel_generator):
    assert weasel_generator.add_character(0)[1:] == 'Brandon'


def test_add_character_at_end(weasel_generator):
    assert weasel_generator.add_character(7)[:7] == 'Brandon'


def test_delete_character_at_start(weasel_generator):
    assert weasel_generator.delete_character(0) == 'randon'


def test_delete_character_at_end(weasel_generator):
    assert weasel_generator.delete_character(6) == 'Brando'


def test_change_character_at_start(weasel_generator):
    new_weasel = weasel_generator.change_character(0)
    assert new_weasel[1:] == 'randon'


def test_change_character_at_middle(weasel_generator):
    new_weasel = weasel_generator.change_character(2)
    assert new_weasel[0:2] == 'Br' and new_weasel[3:] == 'ndon'


def test_change_character_at_end(weasel_generator):
    new_weasel = weasel_generator.change_character(6)
    assert new_weasel[0:6] == 'Brando'


def test_target_exact_match():
    close_match = "Mythinks it is like a weasel."
    best_match = TARGET[:]
    assert selector([close_match, best_match]) == (TARGET, 0)


def test_target_close_match():
    bad_match = "David Bowie was here."
    close_match = "Mythinks it is like a weasel."
    assert selector([bad_match, close_match]) == (close_match, 1)


def test_initial_length_matches_target_by_default():
    generated = WeaselGenerator()
    assert len(generated.weasel) == len(TARGET)


def test_generate_new_mutations_uses_random_index_per_child(monkeypatch):
    generator = WeaselGenerator("abcd", max_children=2, max_mutations_per_child=1)

    randint_values = iter([1, 0, 1, 2])

    def fake_randint(_min, _max):
        return next(randint_values)

    def fake_choice(options):
        if isinstance(options, tuple):
            return generator.change_character
        return "X"

    monkeypatch.setattr("weasels.random.randint", fake_randint)
    monkeypatch.setattr("weasels.random.choice", fake_choice)

    assert list(generator.generate_new_mutations()) == ["Xbcd", "abXd"]
