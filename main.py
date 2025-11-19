from src.tamagotchi import Tamagotchi
from src.events import *

if __name__ == '__main__':
    t = Tamagotchi("BOB")
    print(t)

    Feed(t)
    print(t)
    Sleep(t)
    print(t)
    Play(t)
    print(t)
    Wash(t)
    print(t)

