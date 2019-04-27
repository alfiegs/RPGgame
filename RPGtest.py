#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


import random



class Character:
    def __init__(self, name, health, power, coins):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

    def alive(self):
        if self.health > 0:
            return True

    def attack(self, enemy):
        enemy.health -= self.power
        if enemy.health > 0:
            self.health -= enemy.power
            print("You did {} damage to the enemy and took {} damage.".format(self.power, enemy.power))
        if enemy.health <= 0:
            self.coins += enemy.coins
            print("You stole {} of your enemy's coins!".format(enemy.coins))



    def print_status(self):
        print("         >> {} has {} health left. He has {} coins on him.".format(self.name, self.health, self.coins))

    


class Hero(Character):
    def __init__(self, name, health, power, coins):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

    def hero_attack(self, enemy):
        enemy.health -= self.power * 2
        if enemy.health > 0:
            self.health -= enemy.power

    def store_menu(self, hero):
        print('''
                                      Welcome to WalMart!

                                We are short on supplies right now,
                                but here is a list of what we do have:
                                ||===============================||
                                || 1. Potion - Adds 100 Health   ||
                                || 2. Power Up - Adds 10 power   ||

        ''')
        store_choice = input()
        if store_choice == "1":
            if hero.coins >= 10:
                hero.health = hero.health + 100
                hero.coins = hero.coins - 10
                print("You bought a potion! Thanks for shopping at WalMart!")
            if hero.coins < 10:
                print("Sorry, you doing have the cash for this.")
        if store_choice == "2":
            hero.power = hero.power + 10
            print("You bought a power up! Thanks for shopping at WalMart!")




class Goblin(Character):
    def __init__(self, name, health, power, coins):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins






class Medic(Character):
    def __init__(self, name, health, power, coins):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

    def medic_move(self):
        if random.random() < 0.2:
            self.health = self.health + 2
            print('Oh no! Medic gained 2 health! He now has {}'.format(self.health))

class GoldenGun(Character):
    def __init__(self, name, health, power, coins):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
    
    def gg_move(self, hero):
        if random.random() < 0.2:
            hero.health = 0
            print("Oh no, you got shot with the Golden Bullet! You are now dead!")

class Bear(Character):
    def __init__(self, name, health, power, coins):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins

    def bear_move(self, hero):
        num = random.randint(0, 5)
        print(
        '''
        AAAAAAAHHHHHHHHHHHHHHAAAAAAHHHHHHHHH!!!
        If you let me hug you I can heal you!
        ''')
        if num == 0:
            print("I don't want to die!")
        if num == 1:
            print("Your sword is hurting me! Don't stab me!")
        if num == 2:
            print("There's so much blood!")
        if num == 3:
            print("Why are you trying to kill me?")
        if num == 4:
            print("OH GOD IM IN SO MUCH PAIN")
        if num == 5:
            print("Don't hurt me! I only want to love you!")
        hero.health = hero.health + 10




def main():
    hero = Hero("Hero", 100, 5, 0)
    goblin = Goblin("Goblin", 1, 2, 5)
    medic = Medic("Medic", 1, 2, 10)
    zombie = Character("Zombo", 2, 1, 15)
    gg = GoldenGun("The Man With The Golden Gun", 10, 0, 20)
    bear = Bear("bear", 20, 0, 100)


    while hero.alive() and hero.coins >= 0:
        print('''
        *******************************************


    
        *******************************************
                YOUR ENEMIES LIE BEFORE YOU!"
        *******************************************
        
        Study your enemy. Choose your battles wisely!
        

        ''')
        hero.print_status()
        goblin.print_status()
        medic.print_status()
        zombie.print_status()
        gg.print_status()
        bear.print_status()
        print('''
        
        *******************************************

        What's your move Hero? Are you as brave as they say??

        1. Fight the goblin"
        2. Fight the medic"
        3. Fight the zombie"
        4. Fight The Man With The Golden Gun"
        5. Fight a bear"
        6. Enter the store"
        ...
        8. Do nothing (scared??)"
        9. Flee (coward!)"
        

        
        
        ''')

        #GAME PLAY STARTS HERE
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            if goblin.health > 0:
                if random.random() < 0.2:
                    hero.hero_attack(goblin)
                else:
                    hero.attack(goblin)
            if goblin.health <= 0:
                hero.coins = hero.coins + 5
                goblin.coins = 0
                print("Enemy is dead.")
                goblin.alive = False
            if goblin.alive == False:
                hero.coins = hero.coins - 5
                print("You have already taken a life! How much more blood do you want?")
            # Hero does nothing

        elif raw_input == "2":
            # Hero attacks medic
            if medic.health > 0:
                hero.attack(medic)
                medic.medic_move()
            if medic.health <= 0:
                hero.coins = hero.coins + 10
                medic.coins = 0
                medic.alive = False
            if medic.alive == False:
                print("You have already taken a life! How much more blood do you want?")
                hero.coins = hero.coins - 10
        elif raw_input == "3":
            # Hero attacks zombie
            # zombie doesn't die
            if zombie.health > 0:
                hero.attack(zombie)
                hero.health = hero.health - zombie.power
            if zombie.health < 0:
                print("Fool! Zombies don't die! You shall never take his coins!")
        elif raw_input == "4":
            # Hero attacks the Man With The Golden Gun
            # GG has 20% chance of killing Hero immediately
            if gg.health > 0:
                hero.attack(gg)
                gg.gg_move(hero)
            if gg.health <= 0:
                hero.coins = hero.coins + 20
                gg.coins = 0
                gg.alive = False
            if gg.alive == False:
                print("You have already taken a life! How much more blood do you want?")
                hero.coins = hero.coins - 20
        elif raw_input == "5":
            # Hero attacks a bear
            # Bear gives Hero 10 health every time Hero attacks and screams when attacked
            if bear.health > 0:
                hero.attack(bear)
                bear.bear_move(hero)
            if bear.health <= 0:
                hero.coins = hero.coins + 100
                bear.coins = 0
                bear.alive = False
            if bear.alive == False:
                print("You killed him already! Stop beating a dead bear!")
                hero.coins = hero.coins - 100
        elif raw_input == "6":
            # Enter the Store
            hero.store_menu(hero)
        elif raw_input == "8":
            # Hero does nothing
            pass
        elif raw_input == "9":
            # Hero flees (like a coward!)
            print("Coward! Run home to your mother!")
            break
        else:
            print("Invalid input {}".format(raw_input))



main()
