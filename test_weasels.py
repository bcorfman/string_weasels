import pytest
from weasels import WeaselGenerator
from target import selector, TARGET


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


def test_target_exact_match(weasel_generator):
    close_match = "Mythinks it is like a weasel."
    best_match = TARGET[:]
    assert selector([close_match, best_match]) == (TARGET, 0)


def test_target_close_match(weasel_generator):
    bad_match = "David Bowie was here."
    close_match = "Mythinks it is like a weasel."
    assert selector([bad_match, close_match]) == (close_match, 1)


