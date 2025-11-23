def Feed(pet):
    """Reduces Hunger"""
    pet.stats["hunger"] = min(100, pet.stats["hunger"] + 20)
    pet.stats["cleanliness"] = max(0, pet.stats["cleanliness"] - 20)

def Sleep(pet):
    """It allows you to have a little more energy."""
    pet.stats["energy"] = min(100, pet.stats["energy"] + 30)
    pet.stats["hunger"] = max(0, pet.stats["hunger"] - 10)

def Play(pet):
    """Play with the pet but the pet decreases energy"""
    pet.stats["mood"] = min(100, pet.stats["mood"] + 25)
    pet.stats["energy"] = max(0, pet.stats["energy"] - 10)

def Wash(pet):
    """Clean Pet"""
    pet.stats["cleanliness"] = min(100, pet.stats["cleanliness"] + 40)
    pet.stats["mood"] = max(0, pet.stats["mood"] - 10)
