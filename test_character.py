'''
Molina Nhoung
CS302
3/18/24
Program 4/5
Tests the functions in character.py file to make sure that the functions
work properly with the different cases and arguments being passed
in. The return values are also tested to see if the functions
return the right values
'''
import pytest
from character import hero, ally, villain, monster, GameOverException, WinGameException

#HERO/CHARACTERS TESTING
#test the hero's constructor
def test_hero_creation_success():
    _hero = hero("Hero", 100, "Sword", 10)
    assert _hero._name == "Hero"
    assert _hero._hp == 100
    assert _hero._held_weap == "Sword"
    assert _hero._attack == 10

#test constructor when empty string comes for name
def test_hero_creation_emptystring_name():
    with pytest.raises(ValueError, match = "empty string"):
        _hero = hero("", 100, "Sword", 10)

#test constructor when empty string comes for weapon
def test_hero_creation_emptystring_weapon():
    with pytest.raises(ValueError, match = "empty string"):
        _hero = hero("Hero", 100, "", 10)

#test constructor when hp is not an integer
def test_hero_creation_no_int_hp():
    with pytest.raises(ValueError, match = "not an integer"):
        _hero = hero("Name", "test", "Sword", 10)

#test constructor when attack is not an integer
def test_hero_creation_not_int_atk():
    with pytest.raises(ValueError, match = "not an integer"):
        _hero = hero("Name", 100, "Sword", 'test')

#test hero's display
def test_hero_display_success(capsys, _fixture_hero):
    _fixture_hero.display_stat()
    #Catch the printed display
    captured = capsys.readouterr()
    #Split them for every \n
    captured_lines = captured.out.strip().split('\n')
    assert captured_lines == ["Name: Hero \tHP: 100", "Weapon: Sword \tATK: 10"]
    
#test the hero's check health function by checking if it raises an exception if an int is not passed
def test_hero_check_health(_fixture_hero):
    with pytest.raises(ValueError, match = "not an integer"):
        _fixture_hero.check_health("test")
        
#test hero's check health when hero's hp is 0 or below
def test_hero_check(_fixture_hero):
    #test hero's check health when hero's health is 0
    with pytest.raises(GameOverException, match='The hero has died. GAME OVER'):
        _fixture_hero.check_health(0)
    
    #test hero's check health when hero's health is negative
    with pytest.raises(GameOverException, match='The hero has died. GAME OVER'):
        _fixture_hero.check_health(-10)

#test the if the hero can use an item
def test_hero_use_item(_fixture_hero):
    with pytest.raises(ValueError, match = "not an integer"):
        _fixture_hero.use_item("not an integer", 5)
        
def test_hero_use_item_fullhp(_fixture_hero):
    #test the use item if the health is already full, should exit out of the function and return 0
    _hero = _fixture_hero.use_item(110, 10)
    #_hero will return 0 when hp is at max
    assert _hero == 0
    
    #test the use item and if hp is not maxed, but is maxed now after heal, it should return max hp 100
    _hero = _fixture_hero.use_item(90, 10)
    #_hero will return 0 when hp is at max
    assert _hero == 100
    
#test that a hero can take damage/check when damage is not an integer
def test_hero_take_damage(_fixture_hero):
    with pytest.raises(ValueError, match = "not an integer"):
        _fixture_hero.take_damage("test")
        
    #test take_damage return value, returns the new hp
    _hero = _fixture_hero.take_damage(10)
    assert _hero == 90
    
#test that the hero can heal/check if heal is not an integer
def test_hero_heal(_fixture_hero):
    with pytest.raises(ValueError, match= "not an integer"):
        _fixture_hero.heal_chara("test")

#test heal function
def test_hero_heal_hpmax(_fixture_hero):
    #test when hp is at max
    _hero = _fixture_hero.heal_chara(10)
    #_hero will return 0 when hp is at max
    assert _hero == 0
    
    #test heal_chara when hp is greater than 100, returns 0
    _hero = hero("Hero", 200, 'Sword', 10)
    _test = _hero.heal_chara(10)
    assert _test == 0
    
    #test when hp is not max, and used potion to get it to max, it returns max hp (100)
    _test = hero("Hero", 90, "Sword", 10)
    _hero = _test.heal_chara(10)
    #_hero will return 100 at max
    assert _hero == 100
        
#test update hp function
def test_hero_update_hp(_fixture_hero):
    #test her's update_hp, check that health is an integer
    with pytest.raises(ValueError, match= "not an integer"):
        _fixture_hero.update_hp("test")
        
    #test that the hero's hp has been updated, returns the new hp
    _hero = _fixture_hero.update_hp(50)
    assert _hero == 50
        

        
#ALLY TESTING
#test ally's constructor
def test_ally_creation_success():
    _ally = ally("Ally", 100, 10)
    assert _ally._name == "Ally"
    assert _ally._hp == 100
    assert _ally._heal == 10

#test ally's constructor when heal is not an integer
def test_ally_creation_heal_not_integer():
    with pytest.raises(ValueError, match = "not an integer"):
        _ally = ally("Ally", 100, "test")
        
#test that ally displays name, hp, and heals
def test_ally_display_success(capsys, _fixture_ally):
    _fixture_ally.display_stat()
    #Catch the printed display
    captured = capsys.readouterr()
    #Split them for every \n
    captured_lines = captured.out.strip().split('\n')
    assert captured_lines == ["Name: Ally \tHP: 100", "Heals available: 10"]
    
#test ally's heal if the ally has no more heals (0), should return 0
def test_ally_no_heals():
    _ally = ally("Ally", 100, 0)
    _test = _ally.use_heal()
    assert _test == 0

    #test ally's heal if it's in the negatives, returns 0
    _ally = ally("Ally", 100, -10)
    _test = _ally.use_heal()
    assert _test == 0
    
#test ally's defeat if health is not an integer
def test_ally_defeat_not_integer(_fixture_ally):
    with pytest.raises(ValueError, match= "not an integer"):
        _fixture_ally.defeat("test")
        
#test ally's defeat at 0 or negative or positive
def test_ally_defeat_zero(_fixture_ally):
    #test ally's defeat when health is 0, will return 0
    _ally = _fixture_ally.defeat(0)
    assert _ally == 0
    
    #test ally's defeat if health is negative, will return 0
    _ally = _fixture_ally.defeat(-10)
    assert _ally == 0
    
    #test ally's defeat when the ally's health is non-negative
    _ally = _fixture_ally.defeat(10)
    assert _ally == 1
    
    
#VILLAIN TESTING
#test villain's constructor
def test_villain_creation_success():
    _vill = villain("Demon King", 100, 10)
    assert _vill._name == "Demon King"
    assert _vill._hp == 100
    assert _vill._magic == 10
    
#test villain's constructor when magic is not an integer
def test_villain_creation_not_int_magic():
    with pytest.raises(ValueError, match= "not an integer"):
        _vill = villain("Demon King", 100, "test")
        
#test villain's display
def test_villain_display_stats(capsys, _fixture_villain):
    _fixture_villain.display_stat()
    #Catched pritned display
    captured = capsys.readouterr()
    #Split them for every \n
    captured_lines = captured.out.strip().split('\n')
    assert captured_lines == ["Name: Demon King \tHP: 100", "Magic spells left: 10"]
    
#test villain's fireball to check if magic is 0, returns 0
def test_villain_fire_zero():
    _vill = villain("Demon King", 100, 0)
    _test = _vill.fireball()
    assert _test == 0
    
    #test villain's fireball to check if magic is negative, returns 0
    _vill = villain("Demon King", 100, -10)
    _test = _vill.fireball()
    assert _test == 0


#MONSTER TESTING
#test monster's constructor
def test_monster_creation_success():
    _mon = monster("Demon Soldier", 100, 10)
    assert _mon._name == "Demon Soldier"
    assert _mon._hp == 100
    assert _mon._magic == 10
    
#test monster constructor magic is it's not an integer
def test_monster_creaton_not_int():
    with pytest.raises(ValueError, match='not an integer'):
        _mon = monster('Demon Soldier', 100, 'test')
        
#test monster display_stat that it outputs correctly
def test_monster_display_stat(capsys, _fixture_monster):
    _fixture_monster.display_stat()
    #Catched printed display
    captured = capsys.readouterr()
    #Split them for every \n
    captured_lines = captured.out.strip().split('\n')
    assert captured_lines == ["Name: Demon Soldier \tHP: 100", "Magic spells left: 5"]
    
#test monster's fireball to check if magic is 0, returns 0
def test_monster_fire_zero():
    _mon = monster("Demon Soldier", 100, 0)
    _test = _mon.fireball()
    assert _test == 0
    
    #test monster's fireball to check if magic is negative, returns 0
    _mon = monster("Demon Soldier", 100, -10)
    _test = _mon.fireball()
    assert _test == 0
    
#test monster's defeat when health is a non integer
def test_monster_defeat_not_int(_fixture_monster):
    with pytest.raises(ValueError, match='not an integer'):
        _mon = _fixture_monster.defeat('test')

#test monster's defeat when health is 0, returns 0
def test_monster_defeat_zero(_fixture_monster):
    _mon = _fixture_monster.defeat(0)
    assert _mon == 0        
    
    #test monster's defeat when health is negative, returns 0
    _mon = _fixture_monster.defeat(-10)
    assert _mon == 0