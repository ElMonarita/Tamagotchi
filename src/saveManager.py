import json
import os

SAVE_PATH = "data/save.json"

def SaveGame(pet):
    """Saves the Tamagotchi to a JSON file."""
    data = {
        "name": pet.name,
        "stats": pet.stats
    }
    os.makedirs("data", exist_ok=True)
    with open(SAVE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print("Game saved!")

def LoadGame():
    """Loads the backup if it exists. Returns None if no backup exists."""
    if not os.path.exists(SAVE_PATH):
        print("There is no game save.")
        return None
    with open(SAVE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def SaveExists():
    """Returns True if a backup exists."""
    return os.path.exists(SAVE_PATH)
