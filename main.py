'''
Molina Nhoung
CS302
3/18/24
Program 4/5
This game will have the user battle against monsters and pick up items along the way.
Each item picked will be stored in an inventory, where the user can use items when
they encounter a monster. Once an item is used, it is removed from the inventory
and used once. However, when a weapon is used the user will be able to use it until the
next weapon is picked up and used from the inventory. Each weapon is randomized.
The user has a chance to encounter the monsters, or successfully avoid them for the day.
Three scenes will be randomly picked from five scenes, and each scene will end with
the user being asked to sleep for the night or continue to move forward. The end of the
journey, the user will be forced to fight the villain as the last battle, and this
battle will only finish if the user dies or the villain dies.
'''
from character import hero, ally, villain, WinGameException, GameOverException
from BST import tree
import dialogue
import numpy as np

def main():
    #Variables
    bst = tree()
    user = hero('Hero', 100, 'Sword', 10)
    friend = ally('Ally', 100, 10)
    vill = villain('Demon King', 100, 15)
    picked_scene = np.arange(5)
    
    dialogue.intro()
    option = dialogue.menu()
    if option == 1:
        try:
            #scene 1
            picked_scene = dialogue.event(bst, user, friend, picked_scene)
            #scene 2
            picked_scene = dialogue.event(bst, user, friend, picked_scene)
            #scene 3
            picked_scene = dialogue.event(bst, user, friend, picked_scene)
            #final battle with the boss
            dialogue.final_battle(bst, user, friend, vill)
        except GameOverException as e:
            print(e.message)
            return
        except WinGameException as e:
            print(e.message)
            return
    return
if __name__ == "__main__":
    main()