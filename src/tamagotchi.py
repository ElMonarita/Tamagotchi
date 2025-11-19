class Tamagotchi:
    def __init__(self, name: str):
        self.name = name
        self.stats = {
            "hunger": 50,
            "energy": 50,
            "mood": 50,
            "cleanliness": 50
        }

    @classmethod
    def fromSave(cls, data):
        """Crée un Tamagotchi à partir d'un dictionnaire chargé du JSON."""
        pet = cls(data["name"])
        pet.stats = data["stats"]
        return pet
    
    def __str__(self):
        """Show Stat of your pet"""
        return (
            f"\n----- {self.name} -----\n"
            f"Hunger       : {self.stats["hunger"]}% \n"
            f"Energy       : {self.stats["energy"]}% \n"
            f"Mood         : {self.stats["mood"]}% \n"
            f"Cleanliness  : {self.stats["cleanliness"]}% \n"
        )
