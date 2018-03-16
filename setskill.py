# Function to define each skill and must be executed in order Attack, Defense, Special
points = 30
attackPoints = 0
defensePoints = 0
specialPoints = 0


def printskills():
    print("\nAttack:", attackPoints, "\nDefense:", defensePoints, "\nSpecial:", specialPoints)


# Allows user to allocate points to attack skill.
def attack():
    global points, attackPoints, defensePoints, specialPoints
    printskills()
    print("\nYou are now choosing attack points. You have " + str(points) + " skill points left to allocate.")
    num = input("Enter how many skill points you would like to allocate: ").strip()

    # Checks if user input is an int and if not recalls the method
    try:
        val = int(num)
        # Checks if enough skill points are available
        if val > points:
            print("\nNot enough skill points.")
            attack()
        elif val < 0:
            print("\nYou cannot allocate a negative number of points.")
            attack()
        else:
            attackPoints += val
            points -= val
    except ValueError:
        attack()


# Allows user to allocate points to defense skill.
def defense():
    global points, attackPoints, defensePoints, specialPoints
    printskills()
    print("\nYou are now choosing defense points. You have " + str(points) + " skill points left to allocate.")
    num = input("Enter how many skill points you would like to allocate: ").strip()

    try:
        val = int(num)

        if val > points:
            print("\nNot enough skill points.")
            defense()
        elif val < 0:
            print("\nYou cannot allocate a negative number of points.")
            defense()
        else:
            defensePoints += val
            points -= val
    except ValueError:
        defense()


# Allows user to allocate points to special skill.
def special():
    global points, attackPoints, defensePoints, specialPoints
    printskills()
    print("\nYou are now choosing special points. You have " + str(points) + " skill points left to allocate.")
    num = input("Enter how many skill points you would like to allocate: ").strip()

    try:
        val = int(num)

        if val > points:
            print("\nNot enough skill points.")
            special()
        elif val < 0:
            print("\nYou cannot allocate a negative number of points.")
            special()
        else:
            specialPoints += val
            points -= val

    except ValueError:
        special()


