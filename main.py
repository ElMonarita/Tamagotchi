from src.game import StartGame, GameLoop

if __name__ == '__main__':
    """
    t = Tamagotchi("BOB")
    b = Tamagotchi("Patrick")
    print(t)
    Feed(t)
    print(t)
    Sleep(t)
    print(t)
    Play(t)
    print(t)
    Wash(t)
    print(t)

    if Is_dead(t):
        print("Game Over !")
    else :
        print("Your pet is alive")

    print(SaveExists())
    SaveGame(b)
    print(SaveExists())
    data = LoadGame()
    pet=Tamagotchi.fromSave(data)
    print(pet)
    """

    pet = StartGame()
    GameLoop(pet)