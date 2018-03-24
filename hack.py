# Hacking Maintenance closet to get tool box

import paths
import parts
import maze
import random
import os
import time

clear = lambda: os.system("cls")


# Simple algebra problem, I wish I could make it more interactive
def hacking():
    # Creates 2 numbers num2 can be anywhere between 1 and 5 times larger than num1
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 5) * num1
    sum = num1 + num2
    multiple = num2 // num1
    maze.rprint("It seems that the door got stuck when Heavy crashed. "
                "You’re going to have to hack it to get through.\n")
    maze.enter("Press enter to initiate hacking.")
    clear()
    for i in range(5):
        time.sleep(.25)
        maze.rprint("Hacking initiating. . .")
        clear()
    attempts = 3

# Actual hacking
    while attempts > 0:
        clear()
        print("Attempts:", attempts, "\n")
        maze.rprint("The sum of two numbers is ", "")
        maze.rprint(str(sum), " ")
        maze.rprint("and the second number is", " ")
        maze.rprint(str(multiple), " ")
        maze.rprint("times larger than the first number")
        maze.rprint("\nWhat is the value of the first number?")
        val1 = input()
        maze.rprint("\nWhat is the value of the second number?")
        val2 = input()
        if val1 == str(num1) and val2 == str(num2):
            maze.rprint("Success!")
            maze.enter()
            attempts = -1
        else:
            if attempts != 1:
                maze.rprint("Error try again.")
                maze.enter()
            attempts -= 1
        # Checks if hacking failed
        if attempts == 0:
            maze.rprint("Hacking failed. To try again enter \"again\" or \"exit\" to leave.")
            val = input().lower()
    try:
        if val == "again":
            hacking()
    except UnboundLocalError:
        pass
    if attempts == -1:
        clear()
        maze.rprint("You got the door open and found the tool box!")
        parts.toolBox = True
        maze.enter()

    paths.menu()
