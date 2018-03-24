# Creates paths for player to find parts on

import maze
import parts
import mine
import encounter
import hack
import os
import time


clear = lambda: os.system("cls")
running = True


# When game is complete reward message
def winning():
    clear()
    maze.rprint("You have made it off Symr and are headed to AD3!")
    maze.enter()
    print()
    maze.rprint("The expected travel time is three light years. Cryogenics should be activating soon.")
    maze.enter()
    clear()
    for i in range(3):
        maze.rprint("Freezing...")
        time.sleep(.25)
        clear()
    maze.enter("Press enter to roll credits.")


# Main game menu
# I should create a list instead of checking the input so that when they find the item the player cannot
# go do the challenge again. Make a list containing all the menu items and delete them when the player
# completes the zone.
def menu():
    global running
    clear()
    while running:
        maze.rprint("Where would you like to go to search for parts for Heavy?")
        # Checks if each part has not been found, if it has it removes it from the menu.
        if not parts.heavyCore:
            maze.rprint("> Runes")
        if not parts.quantumTransmitter:
            maze.rprint("> Mine")
        if parts.titaniumPlates < 5:
            maze.rprint("> Cave")
        if parts.heavyCore and not parts.toolBox:
            maze.rprint("> Maintenance Closet")
        maze.rprint("> Repair\n> Status")

        val = input().lower()

        # Runs the rune maze
        if val == "runes" or val == "rune":
            clear()
            maze.rune()
            maze.rprint("You made it out good job! It looks like you also found the HEAVY Core. You are one step "
                        "closer to getting off this awful planet.")
            maze.enter()
            menu()

        # Runs the mine puzzle
        elif val == "mines" or val == "mine":
            clear()
            mine.puzzle()

        # Runs the cave battles
        elif val == "cave":
            clear()
            maze.rprint("You decided to wander into a suspicious looking cave.\n")
            maze.load()
            maze.rprint("It looks like it's full of hostile Symrites!")
            for i in range(5):
                encounter.throw()
                if encounter.status():
                    pass
                else:
                    break
            if encounter.status():
                clear()
                maze.rprint("You defeated all the Symrites and made it out of the cave!")
                maze.enter()
                menu()
            running = encounter.status()

        # Runs the hacking puzzle
        elif val == "closet" or val == "maintenance" or val == "maintenance closet":
            clear()
            hack.hacking()

        # Attempts to repair the ship
        elif val == "repair":
            clear()
            running = parts.repair()

        # Checks the status of the parts
        elif val == "status":
            clear()
            parts.status()
            menu()

        else:
            menu()
    if encounter.status():
        winning()
