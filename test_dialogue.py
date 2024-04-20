'''
Molina Nhoung
CS302
3/18/24
Program 4/5
Tests the functions in dialogue.py file to make sure that the functions
work properly with the different cases and arguments being passed
in. The return values are also tested to see if the functions
return the right values
'''
import pytest
import dialogue
from BST import tree
from character import hero, ally, villain, monster
import numpy as np

#test the menu with user input, tests right values, empty intput, and non integer input
@pytest.mark.parametrize("user_input, expected_input", [("1", 1), ("2", 2)])
def test_menu_input(user_input, expected_input, monkeypatch):
    #monkeypatch pretends to be the user to input into the menu
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    #assert that the menu function returns the expected input
    assert dialogue.menu() == expected_input
    
#test the battle menu for user input
@pytest.mark.parametrize("user_input, expected_input", [("1", 1), ("2", 2), ("3", 3)])
def test_battle_menu_input(user_input, expected_input, monkeypatch):
    #monkeypatch pretends to be the user to input into the menu
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    #assert that the menu function returns the expected input
    assert dialogue.battle_menu() == expected_input
    
#test character attack
def test_someone_attacked(capsys, _fixture_hero, _fixture_monster):
    dialogue.someone_attacked(_fixture_hero, _fixture_monster)
    #catch the printed display
    captured = capsys.readouterr()
    captured_lines = captured.out.strip().split('\n')
    #check output
    assert captured_lines == ["Hero attacked! Dealt 10 damage"]
    
#test inventory display when inventory is empty
def test_display_inv_empty(capsys):
    empty = tree()
    dialogue.display_inventory(empty)
    #catch the printed display
    captured = capsys.readouterr()
    captured_lines = captured.out.strip().split('\n')
    #check output
    assert captured_lines == ["EMPTY INVENTORY"]
    
#test inventory display when there's an item
def test_display_inv(capsys, _fixture_bst, _fixture_sample):
    for data in _fixture_sample:
        _fixture_bst.insert(data)
    dialogue.display_inventory(_fixture_bst)
    #catch the printed display
    captured = capsys.readouterr()
    captured_lines = captured.out.strip().split('\n')
    #check output
    assert captured_lines == ['-Inventory-', 'Axe \tATK: 14 \tUse: 1', 'Bread \tHeals: 12 \tUse: 1', 'Potion \tHeals: 13 \tUse: 1']

#test using an item for a weapon
def test_use_item_weap(monkeypatch, _fixture_bst, _fixture_sample, _fixture_hero):
    #the item is in the inventory
    for data in _fixture_sample:
        _fixture_bst.insert(data)
    monkeypatch.setattr('builtins.input', lambda _: 'Sword')
    dialogue.use_item(_fixture_bst, _fixture_hero)
    #check that hero is holding a sword
    assert _fixture_hero._held_weap == 'Sword'
    assert _fixture_hero._attack == 10
    #check that the inventory now doesn't have a sword
    assert _fixture_bst.retrieve('Sword') == False

#test using an item for a potion
def test_use_item_pot(capsys, monkeypatch, _fixture_bst, _fixture_sample, _fixture_hero):
    #test using an item for a potion
    #the item is in the inventory
    for data in _fixture_sample:
        _fixture_bst.insert(data)
    monkeypatch.setattr('builtins.input', lambda _: 'Potion')
    dialogue.use_item(_fixture_bst, _fixture_hero)
    #catch the display and compare it
    captured = capsys.readouterr()
    captured_lines = captured.out.strip().split('\n')
    #check that hero's hp
    assert _fixture_hero._hp == 100
    #check that the inventory now doesn't have a sword
    assert _fixture_bst.retrieve('Potion') == False
    #compare the output
    assert captured_lines == ['You used a Potion', '', 'HP is full, item wasted!']
    
#test using an item but can't find an item
def test_use_item_nofind(capsys, monkeypatch, _fixture_bst, _fixture_sample, _fixture_hero):
    for data in _fixture_sample:
        _fixture_bst.insert(data)
    monkeypatch.setattr('builtins.input', lambda _: 'Pot')
    dialogue.use_item(_fixture_bst, _fixture_hero)
    captured = capsys.readouterr()
    captured_lines = captured.out.strip().split('\n')
    #check output
    assert captured_lines == ['Could not find']
    
#test for ally healing at max HP
def test_ally_heal(capsys, _fixture_ally, _fixture_hero):
    dialogue.ally_heal(_fixture_ally, _fixture_hero)
    #check that ally has 1 less heal
    assert _fixture_ally._heal == 9
    #check the output
    captured = capsys.readouterr()
    captured_lines = captured.out.strip().split('\n')
    #check output
    assert captured_lines == ['Ally used a healing spell on you!', '', 'Already at max HP, wasted a healing spell...']
    
#test for when ally has no more healing spells
def test_ally_heal_zero(capsys, _fixture_hero):
    dialogue.ally_heal(ally('Ally', 100, 0), _fixture_hero)
    #check the output
    captured = capsys.readouterr()
    captured_lines = captured.out.strip().split('\n')
    #check output
    assert captured_lines == ['...Ally has no more healing spells!']
    
#test fireball launching from an enemy
def test_fireball_empty(capsys, _fixture_hero):
    dialogue.launch_fireball(monster('Demon', 50, 0), _fixture_hero)
    captured = capsys.readouterr()
    captured_lines = captured.out.strip().split('\n')
    #check output
    assert captured_lines == ['Demon tried to cast a fireball, but they ran out of magic!']
    
#test display a scene
def test_scene_pick(capsys):
    arr = np.array([0])
    arr = dialogue.scene(arr)
    assert arr.size == 0
    captured = capsys.readouterr()
    captured_lines = captured.out.strip().split('\n')
    #check output
    assert captured_lines == ['You find yourself at the entrance of a forest, we have no choice but to go in',
                              'The forest seems calm, hope nothing bad happens here.']
    
    #pick another scene
    arr = np.arange(4)
    arr = dialogue.scene(arr)
    assert arr.size == 3
    
#test camping display when saying yes
def test_camping_yes(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Y')
    dialogue.camp()
    captured = capsys.readouterr()
    captured_lines = captured.out.strip().split('\n')
    #check output
    assert captured_lines == ['You and your Ally decided to camp for the night', '.', '.', '.',
                              'You and your Ally woke up feeling refreshed! You embark on your journey again']
    
#test camping display when saying no
def test_camping_no(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'N')
    dialogue.camp()
    captured = capsys.readouterr()
    captured_lines = captured.out.strip().split('\n')
    #check output
    assert captured_lines == ['You decided to keep moving']