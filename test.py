from src.tamagotchi import Tamagotchi
from src.events import Feed, Sleep, Play, Wash
from src.deathCheck import IsDead
from src.saveManager import SaveGame, LoadGame, SaveExists

def TestCreation():
    print("=== TEST : Create ===")
    pet = Tamagotchi("Testy")
    print(pet)
    return pet

def TestEvents(pet):
    print("\n=== TEST : Events ===")
    print("-> Feed")
    Feed(pet)
    print(pet)
    print("-> Sleep")
    Sleep(pet)
    print(pet)
    print("-> Play")
    Play(pet)
    print(pet)
    print("-> Wash")
    Wash(pet)
    print(pet)

def TestDeath():
    print("\n=== TEST : Dead ===")
    pet = Tamagotchi("Morty")
    pet.stats["hunger"] = 0
    IsDead(pet)

def TestSave(pet):
    print("\n=== TEST : Save ===")
    SaveGame(pet)
    print("Save exist ?", SaveExists())
    print("\n=== TEST : Loading ===")
    data = LoadGame()
    print(data)

def RunAllTests():
    print("====== PLAY Test ======")
    pet = TestCreation()
    TestEvents(pet)
    TestDeath()
    TestSave(pet)
    print("\n====== TESTS Finish ======")

if __name__ == "__main__":
    RunAllTests()