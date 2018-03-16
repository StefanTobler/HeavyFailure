import time

###########
# CREDITS #
###########
names = ["# CREDITS #", "Story Board Director - Bentley Long", "Sound Developer - Matthew Merck",
         "Lead Developer - Stefan Tobler"]


def credits():
    for i in range(30):
        print()
    for i in names:
        x = 0
        for letters in i:
            x += 1
            if letters == "-":
                break
        if "-" in i:
            for num in range(60-x):
                print(" ", end="")
        else:
            for num in range(59-(len(i)//2)):
                print(" ", end="")
        print(i)
        for z in range(8):
            time.sleep(.25)
            print()
    for i in range(22):
        time.sleep(.25)
        print()

