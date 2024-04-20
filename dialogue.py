'''
Molina Nhoung
CS302
3/18/24
Program 4/5
The game's features are held in this file, with dialogue, battling, looting, using items,
taking damage, displaying to the user, etc. This file helps manage the game so that main
would not be left disorganized. Ech scenario has a chance to happen, and a random item
is picked to match which scene should be displayed to the user. The percent an action
takes place is dependent on the random item picked, for example, a random item between
0-99 is picked and if the item is less than 75, then it has a 75% chance to be used.
'''
import random
import time
from BST import tree
from items import weapon, potion, food, weapon_name, food_name
from character import hero, ally, villain, monster, enemy_name
import numpy as np

#introduce the game to the user by telling the story
def intro():
    print("\n                       -JOURNEY TO DEFEAT THE DEMON KING-"
          "\nYou, the Hero, have been tasked by the king of your kingdom to save the missing Prince"
          "\nwas kidnapped by the Demon King! You must go to the Demon King's castle, defeat enemies"
          "\non your way to the Demon King, and defeat the Demon King to save the prince! The King has"
          "\ngifted you a Sword to start your journey off. To help you, an Ally has joined your team,"
          "\nhowever, they only have the power to heal and cannot engage in combat. Be off, brave Hero!", end= '\n')
    
#the main menu to start the game or end the game
def menu():
    option = input("\n\t1. Start your adventure"
                   "\n\t2. Leave"
                   "\nChoice: ")
    #check if the user enters the right option
    try:
        option = int(option)
        if option == 1 or option == 2:
            return option
        else:
            print('Try again.')
            return menu()
    #exception is thrown when user doesn't enter an int
    except ValueError:
        print('Try again.')
        return menu()

#start an event
def event(bst, user, friend, picked_scene):
    name1 = random.choice(list(enemy_name))
    name2 = random.choice(list(enemy_name))
    ran1 = random.randint(30, 60)
    ran2 = random.randint(30, 60)
    mon = monster(name1.name, ran1, 5)
    mon2 = monster(name2.name, ran2, 5)
    pause()
    print('\n. . . . . . . . . . . . . . . . . . . . . .', end= '\n\n')
    pause()
    #randomly picks a scene to encounter first time
    new_picked = scene(picked_scene)
    pause()
    scene_action(bst, user, friend, mon, mon2)
    camp()
    return new_picked

#final battle with the Demon King
def final_battle(bst, user, friend, vill):
    pause()
    print('\n. . . . . . . . . . . . . . . . . . .', end= '\n\n')
    pause()
    print("...You have finally made it to the Demon King's castle")
    pause()
    print("\nYou enter the gates to the castle into the throne room...")
    pause()
    print("\nThere sits the Demon King on his throne while you spot the Prince in a cage")
    pause()
    print("\nYou challenge the Demon King into a battle!", end='\n\n')
    pause()
    while user._hp > 0 and vill._hp > 0:
        display_battle(user, friend, vill)
        option = battle_menu()
        pause()
        #attack the demon king
        if option == 1:
            percent = random.randint(0, 99)
            #85% chance to attack
            if percent < 85:
                someone_attacked(user, vill)
            else:
                print('\nYou tried to attack, but missed!', end='\n')
            pause()
            #65% chance for the opponent to attack
            percent = random.randint(0, 99)
            if percent < 65:
                someone_attacked(vill, user)
            #10% chance to launch a fireball
            elif percent >= 65 and percent < 75:
                launch_fireball(vill, user)
            else:
                print('\nDemon King tried to attack, but missed!', end='\n')
            pause()
        #open the inventory to use an item
        elif option == 2:
            check = display_inventory(bst)
            if check:
                use_item(bst, user)
            pause()
        #try to use an ally heal
        else:
            ally_heal(friend, user)
            pause()

#battle menu
def battle_menu():
    option = input("\n1. Attack"
                   "\n2. Open inventory"
                   "\n3. Use ally heal"
                   "\nChoice: ")
    try:
        option = int(option)
        if option == 1 or option == 2 or option == 3:
            return option
        else:
            print('Try again.')
            return battle_menu()
    except ValueError:
        print('Try again.')
        return battle_menu()

#attack the opponent, any character can take and deal damage when sent in
def someone_attacked(user, opp):
    attack = user.attack()
    print(f'\n{user._name} attacked! Dealt {attack} damage', end='\n')
    opp.take_damage(attack)
    if isinstance(opp, hero) or isinstance(opp, villain):
        opp.check_health(opp._hp)
        
#display the inventory
def display_inventory(bst):
    check = bst.count_tree()
    if check == 0:
        print('\nEMPTY INVENTORY', end='\n\n')
    else:
        print('\n          -Inventory-')
        bst.display()
    return check

#pick an item to use    
def use_item(bst, a_char):
    option = input('Name of the item to use: ')
    #check if the user entered anything
    if not option:
        print("Didn't enter anything, try again.")
        use_item(bst, a_char)
    #check if the user entered numbers instead of word
    elif any(char.isdigit() for char in option):
        print("Enter the name of the item, not numbers")
        use_item(bst, a_char)
    else:
        #retrieve and remove the item from the list
        retrieved = bst.retrieve(option)
        if retrieved:
            bst.remove(option)
            #only the hero can change their weapon
            if isinstance(retrieved, weapon) and isinstance(a_char, hero):
                a_char.use_weap(retrieved._name, retrieved._attack)
                print(f'\nYou changed your weapon to a {a_char._held_weap}')
            #else it's a healing item
            else:
                did_heal = a_char.use_item(a_char._hp, retrieved._use)
                print(f'\nYou used a {retrieved._name}')
                if did_heal == 0:
                    print('\nHP is full, item wasted!')
                else:
                    a_char.update_hp(did_heal)
        else:
            print('Could not find')
    
#use an ally heal
def ally_heal(an_ally, a_hero):
    heal = an_ally.use_heal()
    if heal == 0:
        print('\n...Ally has no more healing spells!')
        return
    print('\nAlly used a healing spell on you!')
    hp = a_hero.heal_chara(heal)
    if hp == 0:
        print('\nAlready at max HP, wasted a healing spell...')
    else:
        print(f'You gained {heal} HP.', end='\n')
        
#enemy launches a fireball attack
def launch_fireball(enem, a_hero):
    launch = enem.fireball()
    #if there is mre magic left
    if launch == 0:
        print(f'\n{enem._name} tried to cast a fireball, but they ran out of magic!')
    #deal damage to the hero when there's magic
    else:
        print(f"\n{enem._name} launched a fireball! Dealt {launch} damage to the hero")
        a_hero.take_damage(launch)
        #check if gameover
        a_hero.check_health(a_hero._hp)
        
#display the current stats
def display_battle(a_hero, an_ally, an_enem):
    print('\n. . . . . . . . . . . .', end='\n')
    a_hero.display_stat()
    print()
    print(f'Name: {an_ally._name}')
    print(f'Heals: {an_ally._heal}', end='\n\n')
    an_enem.display_stat()
    
#randomize scenes
def scene(picked_scene):
    pick = random.choice(picked_scene)
    if pick == 0:
        print("You find yourself at the entrance of a forest, we have no choice but to go in")
        pause()
        print("The forest seems calm, hope nothing bad happens here.", end= '\n')
        pause()
    elif pick == 1:
        print('You found a town, maybe you can find something')
        pause()
        print("You walk by and see that the town is empty", end='\n')
    elif pick == 2:
        print('You entered a village, maybe you can find something')
        pause()
        print("You walk by and see that the town is empty", end='\n')
    elif pick == 3:
        print('You entered a tunnel, hopefully it is safe enough')
        pause()
        print('The tunnel is dark, your Ally decides to light up a torch', end='\n')
    elif pick == 4:
        print('You entered a cave, hopefully it is safe enough')
        pause()
        print('The tunnel is dark, your Ally decides to light up a torch', end='\n')
    #picked_scene = np.delete(picked_scene, pick, None)
    new_picked = picked_scene[picked_scene != pick]
    return new_picked
        
#chances to encounter at the scene
def scene_action(bst, user, friend, opp, opp2):
    encounters = 0
    #have a chance to grab loot
    encounters += encounter_loot(bst)
    encounters += encounter_loot(bst)
    encounters += encounter_loot(bst)
    encounters += encounter_loot(bst)
    chance = random.randint(0, 99)
    #75% chance to encounter a monster
    if chance > 25:
        encounter_demon(bst, user, friend, opp)
        encounters += 1
        pause()
    #another chance to grab loot
    encounters += encounter_loot(bst)
    encounters += encounter_loot(bst)
    encounters += encounter_loot(bst)
    encounters += encounter_loot(bst)
    chance = random.randint(0, 99)
    #45% chance to encounter a monster
    if chance < 45:
        encounter_demon(bst, user, friend, opp2)
    #last chance to grab loot
    encounters += encounter_loot(bst)
    encounters += encounter_loot(bst)
    encounters += encounter_loot(bst)
    encounters += encounter_loot(bst)
    #the chance that nothing happend
    if encounters <= 0:
        print('What a peaceful day! You did not find any loot or encounter monsters.')
        pause()
        
#ask the user if they want to stay and camp there for the night
def camp():
    option = input("\nIt's getting dark, do you want to camp here for the night?"
                   "\nY/N: ")
    if option.upper() == 'Y':
        print('\nYou and your Ally decided to camp for the night')
        pause()
        print('.')
        pause()
        print('.')
        pause()
        print('.')
        pause()
        print('You and your Ally woke up feeling refreshed! You embark on your journey again')
    elif option.upper() == 'N':
        print('\nYou decided to keep moving')
    else:
        print("\nInvalid input, enter 'Y' or 'N'")
        camp()
    return option

#pick up an item
def find_loot(bst):
    #generate loot
    gen = random.randint(1, 3)
    #if 1 generate a weapon
    if gen == 1:
        random_weap = random.choice(list(weapon_name))
        random_num = random.randint(10, 40)
        item = weapon(random_weap.name, random_num)
    #if 2 generate a potion
    elif gen == 2:
        item = potion('Potion', 10)
    #if 3 generate a food
    else:
        random_food = random.choice(list(food_name))
        random_num2 = random.randint(10, 20)
        item = food(random_food.name, random_num2)
    print(f'\nYou found a {item.display_name()}!', end=' ')
    if bst.count_tree() >= 10:
        print("...Can't add, Inventory full!")
    else:
        print('Added to your inventory')
        bst.insert(item)
            
#monster encounter
def encounter_demon(bst, user, friend, opp):
        print(f'\nA {opp._name} has appeared! Get read to battle!', end='\n')
        pause()
        while opp._hp > 0:
            display_battle(user, friend, opp)
            option = battle_menu()
            pause()
            #attack the enemy
            if option == 1:
                percent = random.randint(0, 99)
                #85% chance to attack
                if percent < 85:
                    someone_attacked(user, opp)
                else:
                    print('\nYou tried to attack, but missed!', end='\n')
                pause()
                #check if monster was defeated
                defeat = opp.defeat(opp._hp)
                if defeat == 1:
                    #65% chance for the opponent to attack
                    percent = random.randint(0, 99)
                    if percent < 65:
                        someone_attacked(opp, user)
                    #10% chance to launch a fireball
                    elif percent >= 65 and percent < 75:
                        launch_fireball(opp, user)
                    else:
                        print(f'\n{opp._name} tried to attack, but missed!', end='\n')
                else:
                    print(f'\n{opp._name} has been defeated! Onwards on your journey')
                pause()
            #open the inventory to use an item
            elif option == 2:
                check = display_inventory(bst)
                if check:
                    use_item(bst, user)
                pause()
            #try to use an ally heal
            else:
                ally_heal(friend, user)
                pause()
                
#encounter loot
def encounter_loot(bst):
    chance = random.randint(0, 99)
    #15% chance to encounter loot once
    if chance < 15:
        find_loot(bst)
        pause()
        return 1
    return 0
        
#have a 1.5 second buffer between events/statements
def pause():
    time.sleep(1)