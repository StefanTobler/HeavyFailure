import time
import os
import settings
import parts
import paths


clear = lambda: os.system("cls")
playerLocation = []


def enter(x="Press enter to continue."):
    if x == "Press enter to continue.":
        enter = input("Press enter to continue.")
    else:
        enter = input(x)


# Rolling print
def rprint(x, stop="\n"):
    speed = settings.updateSpeed()
    for i in x:
        print(i, end="", flush=True)
        time.sleep(speed)
    print(stop, end="")


def load():
    for x in range(3):
        print(".", end="", flush=True)
        time.sleep(.5)
    print("\n")


# Creates a maze mechanism
def rune():
    solution = ["left", "left", "right", "left", "right"]
    rprint("You have stumbled on a strange looking ruin and you decide to explore it.\n")
    load()
    rprint("Oh no you have gotten lost in the ruins and can't find your way!\n")
    load()
    rprint("You're going to have to find your way through the maze to get back out!")
    enter()
    clear()
    out = False
    while not out:
        step = 0
        crossCheck = 0
        # Checks direction player wants to go against the solution
        for i in solution:
            # Checks to see playerLocation in the list
            try:
                if playerLocation[crossCheck] == i:
                    crossCheck += 1
                    step += 1
                    continue
            except IndexError:
                pass
            direction = input("Which direction would you like to go? Left or right? ")
            # Checks to see if direction is correct and adds it to the player location list
            if direction.lower().strip() == i:
                clear()
                step += 1
                playerLocation.append(i)
                if step != len(solution):
                    print("\nLooks like your on the right track.")
                    print("\n")
                break
            else:
                clear()
                print("\nThat doesn't seem right...")
                print("\n")
                break
        if step == len(solution):
            clear()
            out = True
            parts.heavyCore = True

        else:
            step = 0

