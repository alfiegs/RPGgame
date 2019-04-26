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
        print(">> {} has {} health left. He has {} coins on him.".format(self.name, self.health, self.coins))



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
    goblin = Goblin("Goblin", 100, 2, 5)
    medic = Medic("Medic", 100, 2, 10)
    zombie = Character("Zombo", 2, 1, 15)
    gg = GoldenGun("The Man With The Golden Gun", 100, 0, 20)
    bear = Bear("bear", 20, 0, 100)


    while hero.alive():
        print(" ")
        print(" ")
        print("*******************************************")
        print("~~~~~YOUR ENEMIES LIE BEFORE YOU! IF YOU COLLECT 30 COINS, YOU WIN!")
        print("*******************************************")
        print("")
        print("Study your enemy. Choose your battles wisely!")
        print("")
        hero.print_status()
        goblin.print_status()
        medic.print_status()
        zombie.print_status()
        gg.print_status()
        bear.print_status()
        print("*******************************************")

        print("")
        print("What's your move Hero? Are you as brave as they say??")
        print("")
        print("1. Fight the goblin")
        print("2. Fight the medic")
        print("3. Fight the zombie")
        print("4. Fight The Man With The Golden Gun")
        print("5. Fight a bear")
        print("...")
        print("8. Do nothing (scared??)")
        print("9. Flee (coward!)")
        print(
            '''

            '''
        )
        print("> ", end=' ')
        print(" ")
        print("NEW MESSAGE>>")
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            if random.random() < 0.2:
                hero.hero_attack(goblin)
            else:
                hero.attack(goblin)
            if goblin.health < 0:
                print("Enemy is dead.")
            # Hero does nothing

        elif raw_input == "2":
            # Hero attacks medic
            if medic.health > 0:
                hero.attack(medic)
                medic.medic_move()
            if medic.health <= 0:
                hero.coins = hero.coins + 10
                bear.alive = False
            if bear.alive == False:
                print("You have already taken a life! How much more blood do you want?")
                hero.coins = hero.coins - 10
        elif raw_input == "3":
            # Hero attacks zombie
            hero.attack(zombie)
            hero.health = hero.health - zombie.power
        elif raw_input == "4":
            # Hero attacks the Man With The Golden Gun
            hero.attack(gg)
            gg.gg_move(hero)
        elif raw_input == "5":
            # Hero attacks a bear
            if bear.health > 0:
                hero.attack(bear)
                bear.bear_move(hero)
            if bear.health <= 0:
                hero.coins = hero.coins + 100
                bear.alive = False
            if bear.alive == False:
                print("You killed him already! Stop beating a dead bear!")
                hero.coins = hero.coins - 100
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
