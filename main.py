import setskill
import random
import pygame
import time
import encounter
import os
import maze
import settings
import credit
import paths



pygame.mixer.init()
settings.music()
easterEggNameSound = pygame.mixer.Sound("audio\\meow.wav")

clear = lambda: os.system("cls")

speed = settings.speed


def load():
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(.5)
    print("\n")


def rprint(statement, stop="\n"):
    for i in statement:
        print(i, end="", flush=True)
        time.sleep(speed)
    print(stop, end="")


def enter(phrase="Press enter to continue."):
    user = input(phrase)


running = False
start = True


# Start menu
while start:
    clear()
    settings.title()
    speed = settings.updateSpeed()
    print("**For the best experience play in original window size.**")
    print("\n> Start Game"
          "\n> Settings"
          "\n> Quit")
    val = input("\nPlease enter what you would like to do.\n")
    if val.lower() == "start game" or val.lower() == "start":
        running = True
        start = False
    elif val.lower() == "settings":
        settings.settings()
    elif val.lower() == "quit":
        start = False
        break


# Game Runs
while running:
    clear()
    settings.title()
    time.sleep(1)

    uname = input("Please enter a name: ")
    playerHealth = 50
    playerSpecialPoints = 5
    score = 0
    easterEggNameList = ["Kip", "Gameboy", "Envy", "Admin", "Evernbro"]

    if uname in easterEggNameList:
        print("Congratulations you discovered an easter egg!")
        easterEggNameSound.play()
        setskill.points = 50

    rprint("\nWelcome", stop=" ")
    rprint(uname, stop=" ")
    rprint("to Heavy! Please continue to select your skills.")

    enter()
    clear()

    # Defines each skill
    setskill.attack()
    clear()
    setskill.defense()
    clear()
    setskill.special()
    clear()

    # Checks to see if all skill points have been spent
    while setskill.points > 0:
        if setskill.points != 0:
            setskill.printskills()
            skill = input("\nAll your points have not been allocated enter which skill you"
                          " would like to add more too? ")
            skill = skill.lower()
            if skill == "attack":
                setskill.attack()
                clear()
            elif skill == "defense":
                setskill.defense()
                clear()
            elif skill == "special":
                setskill.special()
                clear()
            else:
                print('\nPlease enter either attack, defense, or special.')

    setskill.printskills()
    print("\n")
    enter()
    print("\n")
    # ##################################
    # # For testing purposes
    # setskill.specialPoints = 10
    # setskill.attackPoints = 10
    # setskill.defensePoints = 10
    # ##################################
    load()
    clear()

    rprint("You just woke up from a long slumber on Heavy, a solo space shuttle mission that was bound for Alpha "
           "3-Delta Zone, approximately 15au from Earth.")
    enter()
    rprint("\nThe shuttle didn't make it to A3D, it looks like that it crashed on Symr, a planet inhabited by hostile "
           "creatures.")
    enter()
    rprint("\nYou have to repair the Heavy, so you decide to wander looking for scattered parts.")
    enter()

    load()

    clear()

    paths.menu()
    running = False

clear()
credit.credits()
enter("Press enter to quit.")
