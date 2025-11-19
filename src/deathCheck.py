def IsDead(pet):
    dead_messages = {
        "hunger": "died of starvation...",
        "energy": "collapsed from exhaustion...",
        "mood": "fell into a depression...",
        "cleanliness": "fell ill because of the filth..."
    }

    for stat, value in pet.stats.items():
        if value <= 0:
            print(f"{pet.name} {dead_messages[stat]}")
            return True

    return False
