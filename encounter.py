import random
import setskill
import pygame
import time
import os
import parts


clear = lambda: os.system("cls")
pygame.mixer.init()
hit = pygame.mixer.Sound("audio\\hit.wav")
miss = pygame.mixer.Sound("audio\\miss.wav")
health = 50
sp = 5


def enter():
    enter = input("Press enter to continue.")


def updateHealth():
    return health


def updateSP():
    return sp


def status():
    if health < 0:
        return False
    return True


# Combat Phase
def battle(enemy, hp, attack, defense, missChance, dodgeChance):
    global health, sp
    val = ""
    enter()
    first = random.randint(0, 1)
    damage = round(setskill.attackPoints - defense, 2)
    special = round(setskill.specialPoints * 2 - defense, 2)
    # Checks to make sure that the player is not dealing negative damage and if is sets damage = 1
    if damage < 0:
        damage = 1
    if special < 0:
        special = 1
    time.sleep(1)
    # Coin flip for who attacks first
    if first == 1:
        print("\nYou get to attack first!")
    else:
        health -= attack
        round(health, 2)
        print("\nThe", enemy, "got the drop on you and dealt", attack , "damage. Your health is now", health, end=".\n")
        hit.play()

    # Battle Phase begins
    while hp > 0 and health > 0:
        print("\n\nThe", enemy,"has", hp,"health left!")
        val = input("It's your turn to attack, what do you want to do?\nAttack\nSpecial [" + str(sp) + "/5]\nRun\n")
        # Regular attack
        if val.lower() == "attack":
            if random.uniform(0, 1) > dodgeChance:
                hp -= damage
                round(hp, 2)
                print("\nYou dealt", damage, "damage to the", enemy, end=".\n")
            else:
                print("\nYour attack missed!")
                miss.play()
        # Special attack
        elif val.lower() == "special" and sp > 0:
            if random.uniform(0, 1) > dodgeChance * 1.5:
                hp -= special
                round(hp, 2)
                print("\nYou dealt", special,"damage to the", enemy, "with your special!")
                sp -= 1
            else:
                print("\nYour special attack missed!")
                miss.play()
                sp -= 1
        elif val.lower() == "special" and sp == 0:
            print("\nNot enough special points!")

        # Run
        elif val.lower() == "run":
            if random.randint(1, 4) != 1:
                print("\nYou got away safely!")
                hp = 0
            else:
                print("\nYou didn't get away!")
        else:
            print("Not a valid move.")
        # Enemy turn to attack
        if hp > 0 and(val.lower() == "attack" or val.lower() == "run" or (val.lower() == "special" and sp == 0)):
            if random.uniform(0,1) > missChance:
                # Determines whether enemy attack hits for a critical
                if random.uniform(0,1) > .15:
                    health -= attack
                    round(health, 2)
                    if health > 0:
                        print("The", enemy, "hit you for", attack, "damage. Your health is now", health, end=".\n")
                    else:
                        print("The", enemy, "hit you for", attack, "damage. Your health is now 0.")
                    hit.play()
                else:
                    health -= attack * 1.5
                    round(health, 2)
                    if health > 0:
                        print("The", enemy, "got a critical hit, and did", round(attack * 1.5, 2), "damage. Your"
                              " health is now", health, end=".\n")
                    else:
                        print("The", enemy, "got a critical hit, and did", round(attack * 1.5, 2), "damage. Your"
                              " health is now 0.")
                    hit.play()
            else:
                print("The", enemy, "missed!")
                miss.play()

        # End Combat

    # Reward
    if val.lower() != "run" and health > 0:
        x = random.randint(1, 6)
        print("You have defeated", enemy, end=".\n")
        if x == 1:
            print('You have gained one attack point!')
            setskill.attackPoints += 1
        elif x == 2:
            print("You have gained one defense point!")
            setskill.defensePoints += 1
        elif x == 3:
            print("You have gained one special point!")
            setskill.specialPoints += 1
        elif x == 4:
            print("You have received full health!")
            health = 50
        elif x == 5:
            print("Your special points have been recovered!")
            sp = 5
        elif x == 6:
            print("The enemy dropped a titanium plate!")
            parts.titaniumPlates += 1
    elif health < 0:
        print("You have been defeated.")
        enter()


# Throws a random enemy to battle
def throw():
    x = [grunt, scout, tank, scorcher]
    random.choice(x)()


# Defining characteristics of a grunt
def grunt():
    hp = random.randint(15, 30)
    print("\nOh no you ran into a Symrite grunt! It has", hp, "health!")
    attack = round(.5 * setskill.attackPoints - setskill.defensePoints * .2 * random.uniform(0, 1), 2)
    # Checks to make sure enemy does't deal negative damage and if does sets attack to 1
    if attack < 0:
        attack = 1
    defense = round(.2 * setskill.defensePoints, 2)
    missChance = .15
    dodgeChance = .25
    battle("Symrite grunt", hp, attack, defense, missChance, dodgeChance)


# Defining characteristics of a scout
def scout():
    hp = random.randint(10, 15)
    print("\nOh no you have run into a Symrite scout! It has", hp, "health!")
    attack = round(.35 * setskill.attackPoints - setskill.defensePoints * .2 * random.uniform(0, 1), 2)
    if attack < 0:
        attack = 1
    defense = round(.1 * setskill.defensePoints, 2)
    missChance = .15
    dodgeChance = .45
    battle("Symrite scout", hp, attack, defense, missChance, dodgeChance)


# Defining characteristics of a tank
def tank():
    hp = random.randint(25, 50)
    print("\nOh no you have run into a Symrite tank! It has", hp, "health!")
    attack = round(.85 * setskill.attackPoints - setskill.defensePoints * .2 * random.uniform(0, 1), 2)
    if attack < 0:
        attack = 1
    defense = round(.4 * setskill.defensePoints, 2)
    missChance = .4
    dodgeChance = .05
    battle("Symrite tank", hp, attack, defense, missChance, dodgeChance)


# Defining characteristics of a scorcher
def scorcher():
    hp = random.randint(20, 35)
    print("\nOh no you have run into a Symrite scorcher! It has", hp, "health!")
    attack = round(.85 * setskill.attackPoints - setskill.defensePoints * .2 * random.uniform(0, 1), 2)
    if attack < 0:
        attack = 1
    defense = round(.0 * setskill.defensePoints, 2)
    missChance = .25
    dodgeChance = .25
    battle("Symrite scorcher", hp, attack, defense, missChance, dodgeChance)