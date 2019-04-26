#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


import random



class Character:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0:
            return True





class Hero(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        if random.random() < 0.2:
            self.power = self.power * 2
        else:
            enemy.health -= self.power
        print("You do {} damage to your enemy".format(self.power))
        if enemy.health <= 0:
            print("You have vanquished your foe!")

    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))

class Goblin(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, enemy):
        enemy.health -= self.power
        print("You took {} damage from the enemy.".format(self.power))
        if enemy.health <= 0:
            print("You are dead. RIP")

    def print_status(self):
        print("The enemy has {} health and {} power.".format(self.health, self.power))



class Medic(Character):
    def __init__(self, health, power):
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        enemy.health -= self.power
        print("You took {} damage from the enemy.".format(self.power))
        if enemy.health <= 0:
            print("You are dead. RIP.")

    def print_status(self):
        print("The enemy has {} health and {} power.".format(self.health, self.power))



def main():
    hero = Hero(20, 5)
    goblin = Goblin(16, 2)
    medic = Medic(16, 2)


    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("4. fight medic")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Coward! Run home to your mother!")
            break
        elif raw_input == "4":
            medic.print_status()
            hero.attack(medic)
        else:
            print("Invalid input {}".format(raw_input))
        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)


main()
