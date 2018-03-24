# Creates mine puzzle
import paths
import parts
import maze
import os

clear = lambda: os.system("cls")


# Simple word scramble puzzle solution is HELP
def puzzle():
    clear()
    solution = "help"
    # Intro into the mine
    maze.rprint("You decided to go down into the mine, it looks like there are 4 shafts which one would you like to go "
                "down?")
    val = input("> 1\n> 2\n> 3\n> 4\n")
    clear()
    if val == "1":
        maze.rprint("There is writing on the wall. It looks like an \"E\".")
        maze.enter("Press enter to go back to the mine HUB.")
    elif val == "2":
        maze.rprint("There is writing on the wall. It looks like an \"H\".")
        maze.enter("Press enter to go back to the mine HUB.")
    elif val == "3":
        maze.rprint("There is writing on the wall. It looks like an \"P\".")
        maze.enter("Press enter to go back to the mine HUB.")
    elif val == "4":
        maze.rprint("There is writing on the wall. It looks like an \"L\".")
        maze.enter("Press enter to go back to the mine HUB.")
    else:
        maze.rprint("It doesn't look like I can go that way.")
        maze.enter()
        puzzle()

    clear()

    maze.rprint("The writing on the walls may have something to do with a puzzle."
                " Maybe if you figure out what word they spell something might happen.")
    maze.enter()
    # Player has to go to every shaft and then guess the scrambled word
    while val.lower() != solution:
        clear()
        maze.rprint("Which way would you like to go or try and enter the solution.")
        val = input("> 1\n> 2\n> 3\n> 4\n")
        clear()
        if val == "1":
            maze.rprint("It looks like there is writing on the wall. It looks like an \"E\".")
            maze.enter("Press enter to go back to the mine HUB.")
        elif val == "2":
            maze.rprint("It looks like there is writing on the wall. It looks like an \"H\".")
            maze.enter("Press enter to go back to the mine HUB.")
        elif val == "3":
            maze.rprint("It looks like there is writing on the wall. It looks like an \"P\".")
            maze.enter("Press enter to go back to the mine HUB.")
        elif val == "4":
            maze.rprint("It looks like there is writing on the wall. It looks like an \"L\".")
            maze.enter("Press enter to go back to the mine HUB.")
        elif val.lower() == solution:
            maze.rprint("It looks like a new door opened in the mine HUB. You decide to go see what's there.\n")
            maze.load()
            maze.rprint("You found the Quantum Transmitter!")
            maze.enter()
            parts.quantumTransmitter = True
        else:
            maze.rprint("That doesn't seem to be the correct solution...")
            maze.enter()

    paths.menu()
