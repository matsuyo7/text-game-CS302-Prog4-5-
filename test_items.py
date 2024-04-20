'''
Molina Nhoung
CS302
3/11/24
Program 4/5
'''
import pytest
from items import weapon, potion, food

#WEAPON/ITEM TESTING
#test weapon's constructor
def test_weapon_creation_success():
    _weap = weapon('Sword', 20)
    assert _weap._name == 'Sword'
    assert _weap._attack == 20
    
#test weapon's constructor when name is an empty string
def test_weapon_creation_emptystring():
    with pytest.raises(ValueError, match='empty string'):
        _weap = weapon('', 20)

#test weapon's display
def test_weapon_display(capsys, _fixture_weap):
    _fixture_weap.display_item()
    #Capture printed output
    captured = capsys.readouterr()
    #Split them when encountering new line
    captured_lines = captured.out.strip().split('\n')
    assert captured_lines == ["Sword \tATK: 20"]

#test all item's constructor when their integer arg is not an integer
@pytest.mark.parametrize("item_type", ["Weapon", "Potion", "Food"])
def test_item_creation_not_int(item_type):
    with pytest.raises(ValueError, match='not an integer'):
        if item_type == "Weapon":
            _item = weapon('Sword', 'test')
        elif item_type == "Potion":
            _item = potion(item_type, 'test')
        elif item_type == "Food":
            _item = food('Bread', 'test')
        
#test for not the same type argument for comparisons
def test_weapon_notsame(_fixture_weap):
    #test different class type
    _test = potion('Potion', 13)
    assert _fixture_weap != _test
    
    #test not a class type
    assert _fixture_weap != 'test'
    _test = _fixture_weap != 4
    assert _test == 0
    assert _fixture_weap == 'Sword'
    
#test when class is the same
def test_weapon_eq(_fixture_weap):
    #when they have the same class and name
    _test = weapon('Sword', 15)
    assert _fixture_weap == _test
    
    #when they have the same class but not the same name
    _test = weapon('Axe', 15)
    assert _fixture_weap != _test
    
#test < overloaded operator
def test_weapon_lt(_fixture_weap):    
    #test < for different class type
    _test = potion('Potion', 15)
    assert _test < _fixture_weap
    
    #test < when passing in non-class type
    _weap = _fixture_weap < 'test'
    assert _weap == 1

    #test the < operator when to_compare name is less than self
    _test1 = weapon('Axe', 15)
    _weap1 = _test1 < _fixture_weap
    assert _weap1 == 1
    
    #test the < when to_compare is greater than self, returns 0
    _test2 = weapon('Weap', 15)
    _weap2 = _test2 < _fixture_weap
    assert _weap2 == 0
    
    #test < when same name, returns 0
    _test = weapon('Sword', 15)
    _weap = _fixture_weap < _test
    assert _weap == 0

#test > overloaded operator
def test_weapon_gt(_fixture_weap):    
    #test > for different class type
    _test = potion('Potion', 14)
    _result = _fixture_weap > _test
    assert _result == 1
    
    #test > when passing in non-class type
    _test = _fixture_weap > 'test'
    assert _test == 0

    #test the > operator that it returns 1 when to_compare name is greater than self
    _test = weapon('Weap', 15)
    _weap = _test > _fixture_weap
    assert _weap == 1
    
    #test the > when to_compare is less than self, returns 0
    _test = weapon('Axe', 15)
    _weap = _test > _fixture_weap
    assert _weap == 0
    
    #test > when same name, returns 0
    _test = weapon('Sword', 15)
    _weap = _fixture_weap > _test
    assert _weap == 0

#test cases for >= overloaded operator
def test_weapon_ge_notsame(_fixture_weap):    
    #test >= for different class type
    _food = food('Bread', 17)
    _test = _fixture_weap >= _food
    assert _test == 1
    
    #test >= when passing in non-class type
    _test1 = _fixture_weap >= 'test'
    assert _test1 == 0

    #test the >= operator that it returns 1 when to_compare name is greater than self
    _test2 = weapon('Weap', 15)
    _weap = _test2 >= _fixture_weap
    assert _weap == 1
    
    #test the >= when to_compare is less than self, returns 0
    _test3 = weapon('Axe', 15)
    _weap1 = _test3 >= _fixture_weap
    assert _weap1 == 0
    
    #test >= when same name, returns 1
    _test4 = weapon('Sword', 15)
    _weap2 = _fixture_weap >= _test4
    assert _weap2 == 1

#test <= overloaded operator
def test_weapon_le_notsame(_fixture_weap):    
    #test <= for different class type
    _pot = potion('Potion', 12)
    _test = _pot <= _fixture_weap
    assert _test == 1
    
    #test <= when passing in non-class type
    _test1 = _fixture_weap <= 'test'
    assert _test1 == 1

    #test the <= operator that it returns 1 when to_compare name is less than self
    _test2 = weapon('Axe', 15)
    _weap = _test2 <= _fixture_weap
    assert _weap == 1
    
    #test the <= when to_compare is greater than self, returns 0
    _test3 = weapon('Weap', 15)
    _weap1 = _test3 <= _fixture_weap
    assert _weap1 == 0
    
    #test <= when same name, returns 1
    _test4 = weapon('Sword', 15)
    _weap2 = _fixture_weap <= _test4
    assert _weap2 == 1
    
    
#POTION TESTING
#test potion's constructor
def test_potion_creation_success():
    _pot = potion('Potion', 15)
    assert _pot._name == 'Potion'
    assert _pot._use == 15
    
#test potion's display
def test_potion_display(capsys, _fixture_pot):
    _fixture_pot.display_item()
    #Capture printed output
    captured = capsys.readouterr()
    #Split them when encountering new line
    captured_lines = captured.out.strip().split('\n')
    assert captured_lines == ["Potion \tHeals: 15"]
            

#FOOD TESTING
#test food's constructor
def test_food_creation_success():
    _food = food('Potato', 15)
    assert _food._name == 'Potato'
    assert _food._use == 15
        
#test food's display
def test_food_display(capsys, _fixture_food):
    _fixture_food.display_item()
    #Capture printed output
    captured = capsys.readouterr()
    #Split them when encountering new line
    captured_lines = captured.out.strip().split('\n')
    assert captured_lines == ["Bread \tHeals: 15"]