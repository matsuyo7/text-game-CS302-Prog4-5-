'''
Molina Nhoung
CS302
3/18/24
Program 4/5
Holds the character hierarchy where the base class character holds the name and hp of the character
while the four derived classes (hero, ally, villain, monster) hold their own unique features and
functions. The monster has an enum class to randomly pick a name from it to make the monster
encounters more interesting. The two exception classes deal with ending the game, when the
villain dies, the win exception is raised to end the game, while the game over exception is raised
when the hero dies. Each send a message to the user which action had happened.
'''
import random
from enum import Enum, auto

#exception for when the villain dies, then we win the game
class WinGameException(Exception):
    def __init__(self, message="\nHORRAY! The Demon King has been defeated! The Prince was saved and has now returned to the kingdom safely!"):
        self.message = message
        super().__init__(self.message)


#exception for when the hero dies, then game over and the game ends
class GameOverException(Exception):
    def __init__(self, message="\nThe hero has died. GAME OVER"):
        self.message = message
        super().__init__(self.message)


#randomly generate the name of the enemy
class enemy_name(Enum):
    Demon = auto()
    Lizard = auto()
    Guard = auto()
    Witch = auto()
    Wizard = auto()
    Bear = auto()
    Crow = auto()
    Dwarf = auto()
    Minion = auto()


#Base class character, data members are name and hp
class characters:
    #Initialization list (constructor with arguments)
    def __init__(self, name, hp):
        #check if incoming name is empty
        if len(name) < 1:
            raise ValueError("empty string")
        #check if incoming hp is an int
        if not isinstance(hp, int):
            raise ValueError("not an integer")
        self._name = name
        self._hp = hp
    
    #Destructor    
    def __del__(self):
        self._name = None
        self._hp = None
        
    #Display the name and hp of a character
    def display_stat(self):
        print(f"Name: {self._name}", end=' ')
        print(f"\tHP: {self._hp}")
    
    #Once a character is attacked, the character will lose hp
    def take_damage(self, damage):
        #Check if damage is an int, if it's not raise an exception
        if not isinstance(damage, int):
            raise ValueError("not an integer")
        #Take damage out of hp
        self._hp -= damage
        return self._hp
        
    #Only the characters that can heal will be healed
    def heal_chara(self, to_heal):
        #check if to_heal is an integer, throw an exception if not
        if not isinstance(to_heal, int):
            raise ValueError("not an integer")
        #check if already at full health
        if self._hp >= 100:
            return 0
        self._hp += to_heal
        #hp can only be at max 100, when over max, set it back to max
        if self._hp > 100:
            self._hp = 100
        return self._hp
    
    #update health after a heal
    def update_hp(self, health):
        if not isinstance(health, int):
            raise ValueError("not an integer")
        #update new hp
        self._hp = health
        return self._hp
        
    
#Derived class hero that will be able to use the weapons and attack
class hero(characters):
    #Initialization list, calls the base class
    def __init__(self, name, hp, weap, attack):
        #pass to the base class
        super().__init__(name, hp)
        #check if the string is empty
        if len(weap) < 1:
            raise ValueError("empty string")
        if not isinstance(attack, int):
            raise ValueError('not an integer')
        self._held_weap = weap
        self._attack = attack
    
    #Destructor, calls the base class    
    def __del__(self):
        super().__del__()
        self._held_weap = None
        self._attack = None
    
    #Display the stats, call the base class display, display the hero's weapon and armor    
    def display_stat(self):
        super().display_stat()
        print(f"Weapon: {self._held_weap}", end=' ')
        print('\tATK:', self._attack)
    
    #Attack a character and the attacked character loses hp.
    def attack(self):
        return self._attack
    
    #Check the hero's hp, if it is 0 or negative, then end the game
    def check_health(self, health):
        #check if health is an integer
        if not isinstance(health, int):
            raise ValueError("not an integer")
        #if health is 0, return 0 to end the game
        if health <= 0:
            raise GameOverException()
        #return 1 to continue the game
        return 1
    
    #Use items, can only eat food
    def use_item(self, health, pot):
        #check if health and potion are an integer
        if not isinstance(health, int) or not isinstance(pot, int):
            raise ValueError("not an integer")
        if health >= 100:
            return 0
        health += pot
        if health > 100:
            health = 100
        return health
    
    #use item, if it's a weapon change weapons
    def use_weap(self, weap, atk):
        if not isinstance(weap, str):
            raise ValueError('not a string')
        if not isinstance(atk, int):
            raise ValueError('not an int')
        self._held_weap = weap
        self._attack = atk
        return True

        
#Derived class ally (medic), who can use healing items (food/potions) and heals the hero, a passive ally who cannot attack be attacked
class ally(characters):
    #Initialization list, calls base cVlass
    def __init__(self, name, hp, heal):
        super().__init__(name, hp)
        if not isinstance(heal, int):
            raise ValueError("not an integer")
        self._heal = heal
    
    #Destructor, calls base class    
    def __del__(self):
        super().__del__()
        self._heal = 0
    
    #Displays the ally's stats with the number of heals available
    def display_stat(self):
        super().display_stat()
        print("Heals available:", self._heal)
    
    #Use the potions and food
    def use_item(self, pot):
        #check if health and potion are an integer
        if not isinstance(health, int) or not isinstance(pot, int):
            raise ValueError("not an integer")
        if health >= 100:
            return 0
        health += pot
        if health > 100:
            health = 100
        return health
    
    #Use a heal
    def use_heal(self):
        if self._heal <= 0:
            return 0
        heal = random.randint(15, 25)
        self._heal -= 1
        return heal
    
    #Check if ally dies, there can only be one ally on the field, but can encounter more than one ally if one is defeated
    def defeat(self, health):
        if not isinstance(health, int):
            raise ValueError("not an integer")
        #check if health is at 0 or below, return 0 to indicate death
        if health <= 0:
            return 0
        #return 1 to indicate they are alive
        return 1


#Derived class villain who can attack the hero and deal damage, can do a partywide attack
class villain(characters):
    #Initialization list
    def __init__(self, name, hp, magic):
        super().__init__(name, hp)
        if not isinstance(magic, int):
            raise ValueError("not an integer")
        self._magic = magic
    
    #Destructor
    def __del__(self):
        super().__del__()
        self._magic = None
        
    #Display the stats
    def display_stat(self):
        super().display_stat()
        print("Magic spells left:", self._magic)

    #Attack a character and the attacked character loses hp.
    def attack(self):
        hit = random.randint(10, 25)
        return hit
    
    #Check the villain's hp, if it is 0 or negative, then end the game
    def check_health(self, health):
        #check if health is an integer
        if not isinstance(health, int):
            raise ValueError("not an integer")
        #if health is 0, return 0 to end the game
        if health <= 0:
            raise WinGameException()
        #return 1 to continue the game
        return 1
    
    #If the chance to fire magic is successful, fire a fireball and deal damage
    def fireball(self):
        if self._magic <= 0:
            return 0
        self._magic -= 1
        hit = random.randint(20, 30)
        return hit


#Derived class of monsters, the minions of the villain, can do a partywide attack on the hero and ally
class monster(characters):
    #Initialization list, call the base class    
    def __init__(self, name, hp, magic):
        super().__init__(name, hp)
        if not isinstance(magic, int):
            raise ValueError('not an integer')
        self._magic = magic
    
    #Destructor
    def __del__(self):
        super().__del__()
        self._magic = None
        
    #Display the monster's stats, plus the amount of magic left to use    
    def display_stat(self):
        super().display_stat()
        print("Magic spells left:", self._magic)
    
    #Attack a character and the attacked character loses hp.
    def attack(self):
        hit = random.randint(10, 15)
        return hit
    
    #If the chance to fire magic is successful, fire a fireball and deal damage
    def fireball(self):
        if self._magic <= 0:
            return 0
        self._magic -= 1
        hit = random.randint(15, 20)
        return hit
        
    #when hp is below 0, monster is defeated, since there can be multiple monsters, but does not end game like hero or villain
    def defeat(self, health):
        if not isinstance(health, int):
            raise ValueError("not an integer")
        #return 0 to indicate that the monster is dead
        if health <= 0:
            return 0
        #return 1 to indicate the monster is still alive
        return 1