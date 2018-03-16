import maze
import paths


titaniumPlates = 5
heavyCore = True
toolBox = True
quantumTransmitter = True


# Prints the status of the parts
def status():
    maze.rprint("Parts Status\n============\nTitanium Plates:", " ")
    maze.rprint(str(titaniumPlates))
    maze.rprint("HEAVY Core:", " ")
    if heavyCore:
        maze.rprint("Found")
    else:
        maze.rprint("Missing")
    maze.rprint("Quantum Transmitter:", " ")
    if quantumTransmitter:
        maze.rprint("Found")
    else:
        maze.rprint("Missing")
    maze.rprint("Tool Box:", " ")
    if toolBox:
        maze.rprint("Found")
    else:
        maze.rprint("Missing")
    maze.enter("\nPress enter to exit.")


# Checks to see if player has all the parts available to end the game.
def repair():
    if heavyCore and toolBox and quantumTransmitter and titaniumPlates >= 5:
        maze.rprint("Heavy has been repaired are you ready for take off?\nYes\nNo")
        val = input()
        if val.lower() == "yes":
            return False
        elif val.lower() == "no":
            paths.menu()
        else:
            repair()
    else:
        maze.rprint("Sorry you do not have all the parts required to fix Heavy, keep exploring.")
        maze.enter()
        return True

