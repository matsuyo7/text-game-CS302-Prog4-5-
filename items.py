'''
Molina Nhoung
CS302
3/18/24
Program 4/5
Holds the item hierarchy, where the item is the base class that holds the name of the item,
and three derived classes (weapon, potion, food) to deal with the different item features.
The names of the items are randomly picked from the enum class to make the game more
entertaining. Some items have randomly generated numbers to associate with their features.
such as random attack stat or healing stat. The ==, !=, <, <=, >, >= were overloaded.
'''
from enum import Enum, auto

#enum class for weapon name
class weapon_name(Enum):
    Sword = auto()
    Axe = auto()
    Staff = auto()
    Club = auto()
    Spear = auto()
    Dagger = auto()
    Bow = auto()
    Pole = auto()
    Stick = auto()
    Pebble = auto()
    Knife = auto()
    Scythe = auto()
    Leaf = auto()

#enum class for food name    
class food_name(Enum):
    Rice = auto()
    Bread = auto()
    Soup = auto()
    Steak = auto()
    Wing = auto()
    Pork = auto()
    Potato = auto()
    Pasta = auto()
    Bean = auto()
    Berry = auto()
    Fish = auto()
    Carrot = auto()
    Pear = auto()

#base class
class item:
    #constructor with arguments
    def __init__(self, name):
        if len(name) < 1:
            raise ValueError('empty string')
        self._name = name
        
    #destructor
    def __del__(self):
        self._name = None
    
    #display the name of the item
    def display_item(self):
        print(f'{self._name}', end=' ')
        
    #just display the name
    def display_name(self):
        return self._name
        
    #overload == operator to compare the names and checks if it's the same class type
    def __eq__(self, to_compare):
        #check if the same class type
        if isinstance(to_compare, item):
            if self._name == to_compare._name:
                return 1
            return 0
        elif isinstance(to_compare, str):
            if self._name == to_compare:
                return 1
            return 0
        else:
            return 0
    
    #overload != operator to compare the names and checks if it's the same class type
    def __ne__(self, to_compare):
        #check if the same class type
        if isinstance(to_compare, item):
            if self._name != to_compare._name:
                return 1
            return 0
        elif isinstance(to_compare, str):
            if self._name != to_compare:
                return 1
            return 0
        else:
            return False
    
    #overloaded < operator, compares if incoming name is less than current name
    def __lt__(self, to_compare):
        if isinstance(to_compare, item):
            if self._name < to_compare._name:
                return 1
            return 0
        elif isinstance(to_compare, str):
            if self._name < to_compare:
                return 1
            return 0
        else:
            return 0
    
    #overloaded > operator, compares if incoming name is greater than current name
    def __gt__(self, to_compare):
        if isinstance(to_compare, item):
            if self._name > to_compare._name:
                return 1
            return 0
        if isinstance(to_compare, str):
            if self._name > to_compare:
                return 1
            return 0
        else:
            return 0
    
    #overloaded >= operator, compares if incoming name is greater than or equal to current name
    def __ge__(self, to_compare):
        if isinstance(to_compare, item):
            if self._name >= to_compare._name:
                return 1
            return 0
        if isinstance(to_compare, str):
            if self._name >= to_compare:
                return 1
            return 0
        else:
            return 0
        
    #overloaded <= operator, compares if incoming name is greater than or equal to current name
    def __le__(self, to_compare):
        if isinstance(to_compare, item):
            if self._name <= to_compare._name:
                return 1
            return 0
        if isinstance(to_compare, str):
            if self._name <= to_compare:
                return 1
            return 0
        else:
            return 0
 
    
#derived class derived from item    
class weapon(item):
    #constructor with arguments
    def __init__(self, name, atk):
        super().__init__(name)
        if not isinstance(atk, int):
            raise ValueError('not an integer')
        self._attack = atk
        
    #destructor
    def __del__(self):
        super().__del__()
        self._attack = None
    
    #displays the name of the weapon, not uses
    def display_item(self):
        super().display_item()
        print(f'\tATK: {self._attack}', end=' ')
    
    
#derived class derived from item        
class potion(item):
    #constructor with arguments
    def __init__(self, name, use):
        super().__init__(name)
        if not isinstance(use, int):
            raise ValueError('not an integer')
        self._use = use
        
    #destructor
    def __del__(self):
        super().__del__()
        self._use = None
        
    #displays the name of the potion and its use (how much it can heal)
    def display_item(self):
        super().display_item()
        print(f'\tHeals: {self._use}', end=' ')


#derived class derived from item         
class food(item):
    #constructor with arguments
    def __init__(self, name, use):
        super().__init__(name)
        if not isinstance(use, int):
            raise ValueError('not an integer')
        self._use = use
        
    #destructor
    def __del__(self):
        super().__del__()
        self._use = None
         
    #displays the name of the food and its use (how much it heals)
    def display_item(self):
        super().display_item()
        print(f'\tHeals: {self._use}', end=' ')    
        