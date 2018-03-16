# Game settings
import pygame
import os


clear = lambda: os.system("cls")
volumeLevel = 10
speed = .05
pygame.mixer.init()
pygame.mixer.music.load("audio\\Andrew Applepie - 4 - 06 Mystery.mp3")
pygame.mixer.music.set_volume(1.0)


# Starts music
def music():
    pygame.mixer.music.play(-1)


# Prints title
def title():
    print(" _   _                         ______    _ _                ")
    print("| | | |                        |  ___|  (_) |               ")
    print("| |_| | ___  __ ___   ___   _  | |_ __ _ _| |_   _ _ __ ___ ")
    print("|  _  |/ _ \/ _` \ \ / / | | | |  _/ _` | | | | | | '__/ _ \\")
    print("| | | |  __/ (_| |\ V /| |_| | | || (_| | | | |_| | | |  __/")
    print("\_| |_/\___|\__,_| \_/  \__, | \_| \__,_|_|_|\__,_|_|  \___|")
    print("                         __/ |                              ")
    print("                        |___/                               ")


# Settings Menu
def settings():
    global volumeLevel, speed
    clear()
    title()
    print("Settings\n"
          "========")
    print("1. Volume"
          "\n2. Text speed"
          "\n3. Exit")
    set = input("What would you like to change? ")
    try:
        int(set)
    except ValueError:
        settings()

    if set == "1":
        volume()
    elif set == "2":
        textSpeed()
    elif set == "3":
        return
    else:
        settings()


# Changes music volume
def volume():
    global volumeLevel
    clear()
    title()
    print("Volume ["+ str(volumeLevel) + "/10]")
    set = input("Enter a volume level. ")
    if set == "":
        settings()
    elif float(set) < 0:
        volume()
    try:
        float(set)
    except ValueError:
        volume()
    volumeLevel = set
    pygame.mixer.music.set_volume(float(set) * .1)
    settings()


# Changes text speed
def textSpeed():
    global speed
    clear()
    title()
    print("Text Speed\n"
          "=========="
          "\n0. Instant"
          "\n1. Fast"
          "\n2. Normal"
          "\n3. Slow")
    set = input("Enter a text speed. ")
    try:
        int(set)
    except ValueError:
        textSpeed()
    if set == "1":
        speed = .025
    elif set == "2":
        speed = .05
    elif set == "3":
        speed = .1
    elif set == "0":
        speed = 0
    else:
        textSpeed()
    settings()


def updateSpeed():
    return speed

