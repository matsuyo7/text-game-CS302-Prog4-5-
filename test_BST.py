'''
Molina Nhoung
CS302
3/18/24
Program 4/5
Tests the functions in BST.py file to make sure that the functions
work properly with the different cases and arguments being passed
in. The return values are also tested to see if the functions
return the right values
'''
import pytest
from BST import TNode, tree
from items import weapon, potion, food

#test insert into the BST
def test_bst_insert(_fixture_bst):
    #insert 3 different items so that there is a root, left and right
    _fixture_bst.insert(food('Bread', 12))
    _fixture_bst.insert(weapon('Axe', 14))
    _fixture_bst.insert(potion('Potion', 13))
    
    #check that there's a root, left, and right
    assert _fixture_bst._root._data[0]._name == 'Bread'
    assert _fixture_bst._root.get_left()._data[0]._name == 'Axe'
    assert _fixture_bst._root.get_right()._data[0]._name == 'Potion'
    
#test that the tree can display
def test_bst_display(capsys, _fixture_bst, _fixture_sample):
    #insert into the bst
    for data in _fixture_sample:
        _fixture_bst.insert(data)
    #display the list then catch all displays
    _fixture_bst.display()
    captured = capsys.readouterr()
    expected = "Axe \tATK: 14 \tUse: 1\nBread \tHeals: 12 \tUse: 1\nPotion \tHeals: 13 \tUse: 1"
    #check that it displays alphabetical order
    assert captured.out.strip() == expected.strip()
    
#test retrieve success and failure
def test_bst_retrieve_success(_fixture_bst, _fixture_sample):
    #insert into the bst
    for data in _fixture_sample:
        _fixture_bst.insert(data)
    #test the retrieve after sending in the name of the item
    #find the item and catch it
    _found = _fixture_bst.retrieve('Bread')
    assert _found._name == 'Bread'

    #test the retrieve when sending in the name of the item and can't find it
    _found = _fixture_bst.retrieve('Potato')
    assert _found == False
    
#test retrieve for non string type and empty string
def test_bst_arg_fail(_fixture_bst, _fixture_sample):
    #insert into the bst
    for data in _fixture_sample:
        _fixture_bst.insert(data)
    with pytest.raises(ValueError, match='not a string'):
        _found = _fixture_bst.retrieve(0)
    with pytest.raises(ValueError, match='empty string'):
        _find = _fixture_bst.retrieve('')
    
#test retrieve an item and remove it from the tree, ios is immediate right, two children
def test_bst_remove_ios_right(_fixture_bst, _fixture_sample):
    #insert into the bst
    for data in _fixture_sample:
        _fixture_bst.insert(data)
    #call retrieve and remove, returns the removed item
    _fixture_bst.remove('Bread')
    #check that root is not ios
    assert _fixture_bst._root._data[0]._name == 'Potion'
    #check that ios is now null
    assert _fixture_bst._root.get_right() == None
    
#test retrieve an item and remove it from the tree, no left child
def test_bst_retrieve_remove_noleft(_fixture_bst):
    #insert into the bst
    _fixture_bst.insert(food('Bread', 12))
    _fixture_bst.insert(potion('Potion', 14))
    #call retrieve and remove, returns the removed item
    _fixture_bst.remove('Bread')
    #check that right child is now root
    assert _fixture_bst._root._data[0]._name == 'Potion'
    
#test retrieve and remove it from the tree, no right child
def test_bst_retrieve_remove_noright(_fixture_bst):
    #insert into the bst
    _fixture_bst.insert(food('Bread', 12))
    _fixture_bst.insert(weapon('Axe', 17))
    #call retrieve and remove, returns the removed item
    _fixture_bst.remove('Bread')
    #assert _test._name == 'Bread'
    #check that root is now the left child
    assert _fixture_bst._root._data[0]._name == 'Axe'
    
#test retrieve and remove a duplicate data from a node
def test_bst_remove_dup(_fixture_bst, _fixture_sample):
    #insert into the bst
    for data in _fixture_sample:
        _fixture_bst.insert(data)
    #insert a duplicate
    _fixture_bst.insert(food('Bread', 15))
    _fixture_bst.remove('Bread')
    #check that the root still has the same data
    assert _fixture_bst._root._data[0]._name == 'Bread'

#test retrieve and remove if the tree is empty
def test_bst_retrieve_remove_empty(_fixture_bst):
    _test = _fixture_bst.remove('Bread')
    assert _test == False
    
#test the retrieve when sending in the name of the item and can't find it
def test_bst_retrieve_fail(_fixture_bst, _fixture_sample):
    #insert into the bst
    for data in _fixture_sample:
        _fixture_bst.insert(data)
    #find the item and catch it
    _found = _fixture_bst.remove('Potato')
    assert _found == True
    
#test retrieve for non string type and empty string
def test_bst_retrieve_arg_fail(_fixture_bst, _fixture_sample):
    #insert into the bst
    for data in _fixture_sample:
        _fixture_bst.insert(data)
    with pytest.raises(ValueError, match='not a string'):
        _found = _fixture_bst.remove(0)
    with pytest.raises(ValueError, match='empty string'):
        _find = _fixture_bst.remove('')