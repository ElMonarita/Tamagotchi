import os
import time

def AnimateAscii(path, delay=0.2, repeat=1):
    """Displays an ASCII animation while browsing through each file in the folder."""
    frames = []
    for filename in sorted(os.listdir(path)):
        if filename.endswith(".txt"):
            with open(os.path.join(path, filename), "r", encoding="utf-8") as f:
                frames.append(f.read())
    for _ in range(repeat):
        for frame in frames:
            os.system("cls" if os.name == "nt" else "clear")
            print(frame)
            time.sleep(delay)

def ClearScreen():
    os.system("cls" if os.name == "nt" else "clear")
