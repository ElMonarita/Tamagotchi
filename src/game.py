from src.tamagotchi import Tamagotchi
from src.events import Feed, Sleep, Play, Wash
from src.deathCheck import IsDead
from src.saveManager import SaveGame, SaveExists, LoadGame
from src.utils import ClearScreen, AnimateAscii

def StartGame():
    print("====================Tamagotchi====================")
    print("1. New Game")
    print("2. Continue")

    choice = input("> ")

    if choice == "2" and SaveExists():
        data = LoadGame()
        pet = Tamagotchi.fromSave(data)
        print("Save game loading")
        return pet

    name = input("Name of your Tamagotchi : ")
    return Tamagotchi(name)

def GameLoop(pet):
    ClearScreen()
    AnimateAscii("data/ascii/appear")
    while True:
        print(pet)
        print("=== Events ===")
        print("1. Feed")
        print("2. Sleep")
        print("3. Play")
        print("4. Wash")
        print("5. Save and Quit")
        choice = input("> ")
        match choice:
            case "1":
                ClearScreen()
                AnimateAscii("data/ascii/feeding")
                Feed(pet)
            case "2":
                ClearScreen()
                AnimateAscii("data/ascii/sleeping")
                Sleep(pet)
            case "3":
                ClearScreen()
                AnimateAscii("data/ascii/playing")
                Play(pet)
            case "4":
                ClearScreen()
                AnimateAscii("data/ascii/cleaning")
                Wash(pet)
            case "5":
                ClearScreen()
                AnimateAscii("data/ascii/disappear")
                SaveGame(pet)
                print("Backup complete. See you soon!")
                break
            case _: 
                print("Invalid choice.")
                continue
        if IsDead(pet):
            ClearScreen()
            AnimateAscii("data/ascii/dying")
            print("Game Over !")
            break