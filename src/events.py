def Feed(pet):
    """Reduces Hunger"""
    pet.hunger = max(0, pet.hunger - 20)


def Sleep(pet):
    """It allows you to have a little more energy."""
    pet.energy = min(100, pet.energy + 30)


def Play(pet):
    """Play with the pet but the pet decreases energy"""
    pet.mood = min(100, pet.mood + 25)
    pet.energy = max(0, pet.energy - 10)


def Wash(pet):
    """Clean Pet"""
    pet.cleanliness = min(100, pet.cleanliness + 40)
