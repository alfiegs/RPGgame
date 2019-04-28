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
    
    def coin_purse(self):
        print('''
                                ****************************
                                *        COIN PURSE        *
                                     You have {} coins.    
                                ****************************
        '''.format(self.coins))

    def store_menu(self):
        print('''
                                    Welcome to WalMart!

                            We are short on supplies right now,
                            but here is a list of what we do have:
                            ||===============================||
                            || 1. Potion: 10 coins   - Adds 20 Health||
                            || 2. Power Up: 10 coins - Adds 10 power   ||

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

    
    def fight_menu(self, enemy):
        enemy.description()
        enemy.print_status()
        if enemy.health > 0:
            fight_input = input('''
    
    1. Attack {}!
    2. Flee.
        '''.format(enemy.name))
            if fight_input == "1":
                hero.attack(enemy)
                if enemy.name == "A bear":
                    bear.bear_move(hero)
                if enemy.name == "The Man With The Golden Gun":
                    gg.gg_move(hero)
                hero.fight_menu(enemy)
            elif fight_input == "2":
                main()
            elif enemy.health <= 0:
                print("{} is dead!".format(enemy.name))
                main()
        elif enemy.health < 0:
            print("He dead.")
            main()


    def attack(self, enemy):
        #Attacker attacks
        if enemy.health > 0:
            enemy.health -= self.power
        #Enemy attacks back
            self.health -= enemy.power
        #Print result of both attacks
            print("     ||You did {} damage to {} and took {} damage.".format(self.power, enemy.name, enemy.power))
            print("     Your health: {}".format(self.health))
            print("     {}\'s health: {}".format(enemy.name, enemy.health))
        #Take enemy coins once they are dead
        if enemy.health <= 0:
            enemy.health = 0 #Display 0 rather than negative number
            self.coins += enemy.coins #Add enemy coins to attacker coins
            if enemy.coins > 0:
                print("     >>You stole {} of your enemy's coins!".format(enemy.coins))
                print("     >>You now have {} coins".format(self.coins))
            else:
                print("     >>He has no more money, you've taken it all.")
            enemy.coins = 0 #Reduce enemy coins to 0
            enemy.alive = False
            main()


    def print_status(self):
            print("{} has {} health and {} coins.".format(self.name, self.health, self.coins))


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

    def description(self):
        print('''
The goblin is an evil creature straight from hell. He steals the souls of innocent victims 
and takes them back to Satan. He will not be missed. He's weak, but he'll take your soul 
if you don't watch out.
        ''')






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

    def description(self):
        print('''
The medic is a man of science and wisdom. 
He spends his time healing others and can also heal himself. 
His health status can randomly go up by 10 points during a fight. 
He is paid handsomely for his valuable services, so he has many coins in his purse. 
        ''') 

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
    
    def description(self):
        print('''
The Man With The Golden Gun has a 20 percent chance of killing you immediately.
He has a lot of coins, but is it worth the risk?
        ''')

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

    def description(self):
        print('''
The bear only wants to love you.
If you attack him he will give you health.
But he will also scream in agony.
Do you really want to hurt this loving creature?
        ''')




hero = Hero("Hero", 100, 5, 0)
goblin = Goblin("Goblin", 50, 2, 5)
medic = Medic("Medic", 50, 2, 10)
zombie = Character("Zombo", 2, 1, 15)
gg = GoldenGun("The Man With The Golden Gun", 10, 0, 20)
bear = Bear("A bear", 20, 0, 100)

def enemies_list():
    enemies_input = input('''
        *******************************************
                YOUR ENEMIES LIE BEFORE YOU!
        *******************************************
        What's your move Hero? Are you as brave as they say??

        1. Fight the goblin
        2. Fight the medic
        3. Fight the zombie
        4. Fight The Man With The Golden Gun
        5. Fight a bear
        ...
        8. Do nothing (scared??)
        9. Flee (coward!)
    ''')
    if enemies_input == "1":
        hero.fight_menu(goblin)
    elif enemies_input == "2":
        hero.fight_menu(medic)
    elif enemies_input == "3":
        hero.fight_menu(zombie)
    elif enemies_input == "4":
        hero.fight_menu(gg)
    elif enemies_input == "5":
        hero.fight_menu(bear)
    elif enemies_input == "8":
        pass
    elif enemies_input == "9":
        main()
        


def enemy_status():
    print("")
    print("ENEMY HEALTH STATUS")
    goblin.print_status()
    medic.print_status()
    zombie.print_status()
    gg.print_status()
    bear.print_status()
    enemy_status_input = input('''
1. Back to the Main Menu
    ''')
    if enemy_status_input == "1":
        main()



def main():
    while hero.alive():
        if hero.coins >= 30:
            print('''
                            ********************************
                            * You have collected 30 coins! *
                            *         YOU WIN!             *
                            ********************************
            ''')
            break
        main_input = input('''
********************************************
*             WELCOME HERO!                *
* Kill your enemies and steal their coins! *
*      Collect 30 coins and you win!       *
********************************************

1. See the health and status of your victims.
2. Choose a victim to fight.
3. View your coin purse.
4. Enter the store.
5. Run away like a coward.
        ''')
        if main_input == "1":
            enemy_status()
        elif main_input == "2":
            enemies_list()
        elif main_input == "3":
            hero.coin_purse()
        elif main_input == "4":
            hero.store_menu()
        elif main_input == "5":
            print("You have fled town like a coward! Go home to your mother")
            break








    # while hero.alive():
    #     print('''
    #     *******************************************
    #             YOUR ENEMIES LIE BEFORE YOU!
    #     *******************************************
    #     Study your enemy. Choose your battles wisely!
    #     ''')
    #     hero.print_status()
    #     goblin.print_status()
    #     medic.print_status()
    #     zombie.print_status()
    #     gg.print_status()
    #     bear.print_status()
    #     print('''
        
    #     *******************************************

    #     What's your move Hero? Are you as brave as they say??

    #     1. Fight the goblin
    #     2. Fight the medic
    #     3. Fight the zombie
    #     4. Fight The Man With The Golden Gun
    #     5. Fight a bear
    #     6. Enter the store
    #     ...
    #     8. Do nothing (scared??)
    #     9. Flee (coward!)
        

        
        
    #     ''')

    #     # GAME PLAY STARTS HERE
    #     user_choice = input()
    #     if user_choice == "1":
    #         # Hero attacks goblin
    #         hero.attack(goblin)
    #         # if goblin.health > 0:
    #         #     if random.random() < 0.2:
    #         #         hero.hero_attack(goblin)
    #         #     else:
    #         #         hero.attack(goblin)
    #         # if goblin.health <= 0:
    #         #     hero.coins = hero.coins + 5
    #         #     goblin.coins = 0
    #         #     print("Enemy is dead.")
    #         #     goblin.alive = False
    #         # if goblin.alive == False:
    #         #     hero.coins = hero.coins - 5
    #         #     print("You have already taken a life! How much more blood do you want?")

    #     elif user_choice == "2":
    #         # Hero attacks medic
    #         hero.attack(medic)
    #         # if medic.health > 0:
    #         #     hero.attack(medic)
    #         #     medic.medic_move()
    #         # if medic.health <= 0:
    #         #     hero.coins = hero.coins + 10
    #         #     medic.coins = 0
    #         #     medic.alive = False
    #         # if medic.alive == False:
    #         #     print("You have already taken a life! How much more blood do you want?")
    #         #     hero.coins = hero.coins - 10
    #     elif user_choice == "3":
    #         # Hero attacks zombie
    #         # zombie doesn't die
    #         zombie.health = zombie.health - hero.power
    #         hero.health = hero.health - zombie.power
    #         if zombie.health < 0:
    #             print("Fool! Zombies don't die! You shall never take his coins!")
    #     elif user_choice == "4":
    #         # Hero attacks the Man With The Golden Gun
    #         # GG has 20% chance of killing Hero immediately
    #         if gg.health > 0:
    #             hero.attack(gg)
    #             gg.gg_move(hero)
    #         if gg.health <= 0:
    #             hero.coins = hero.coins + 20
    #             gg.coins = 0
    #             gg.alive = False
    #         if gg.alive == False:
    #             print("You have already taken a life! How much more blood do you want?")
    #             hero.coins = hero.coins - 20
    #     elif user_choice == "5":
    #         # Hero attacks a bear
    #         # Bear gives Hero 10 health every time Hero attacks and screams when attacked
    #         if bear.health > 0:
    #             hero.attack(bear)
    #             bear.bear_move(hero)
    #         if bear.health <= 0:
    #             hero.coins = hero.coins + 100
    #             bear.coins = 0
    #             bear.alive = False
    #         if bear.alive == False:
    #             print("You killed him already! Stop beating a dead bear!")
    #             hero.coins = hero.coins - 100
    #     elif user_choice == "6":
    #         # Enter the Store
    #         hero.store_menu(hero)
    #     elif user_choice == "8":
    #         # Hero does nothing
    #         pass
    #     elif user_choice == "9":
    #         # Hero flees (like a coward!)
    #         print("Coward! Run home to your mother!")
    #         break
    #     else:
    #         print("Invalid input {}".format(user_choice))



main()
