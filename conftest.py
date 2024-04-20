'''
Molina Nhoung
CS302
3/18/24
Program 4/5
Holds all fixtures for each class to help with testing functions.
The fixtures are premade classes so that each test function does
not need the extra lines to construct a class, instead a premade
fixture is passed into the test functions to test functionality.
'''
import pytest
from character import hero, ally, villain, monster
from items import weapon, potion, food
from BST import tree

#create a fixture for the hero
@pytest.fixture
def _fixture_hero():
    _fixture_hero = hero("Hero", 100, "Sword", 10)
    return _fixture_hero

#create a fixture for the ally
@pytest.fixture
def _fixture_ally():
    _fixture_ally = ally("Ally", 100, 10)
    return _fixture_ally

#create a fixture for the villain
@pytest.fixture
def _fixture_villain():
    _fixture_villain = villain("Demon King", 100, 10)
    return _fixture_villain

#create a fixture for the monster
@pytest.fixture
def _fixture_monster():
    _fixture_monster = monster("Demon Soldier", 100, 5)
    return _fixture_monster

#create a fixture for a weapon
@pytest.fixture
def _fixture_weap():
    _fixture_weap = weapon("Sword", 20)
    return _fixture_weap

#create a fixture for potion
@pytest.fixture
def _fixture_pot():
    _fixture_pot = potion("Potion", 15)
    return _fixture_pot

#create a fixture for a food
@pytest.fixture
def _fixture_food():
    _fixture_food = food("Bread", 15)
    return _fixture_food

#fixture for a BST
@pytest.fixture
def _fixture_bst():
    _fixture_bst = tree()
    return _fixture_bst

#fixture for sample data
@pytest.fixture
def _fixture_sample():
    _fixture_sample = [food('Bread', 12), weapon('Axe', 14), potion('Potion', 13)]
    return _fixture_sample