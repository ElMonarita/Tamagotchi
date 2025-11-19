class Tamagotchi:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.mood = 50
        self.cleanliness = 50

    def __str__(self):
        """Show Stat of your pet"""
        return (
            f"\n----- {self.name} -----\n"
            f"Hunger       : {self.hunger}% \n"
            f"Energy       : {self.energy}% \n"
            f"Mood         : {self.mood}% \n"
            f"Cleanliness  : {self.cleanliness}% \n"
        )
