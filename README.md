# Tamagotchi
Creation of a game based on the Tamagotchi concept to learn more about Python. To do this, the game must include certain actions such as eating, sleeping, playing, etc. The game must also have a system to save the game in JSON.

## 📌 Project Content

    Tamagotchi/
    │
    ├── main.py
    ├── test.py
    ├── src/
    │   ├── tamagotchi.py
    │   ├── events.py
    │   ├── game.py
    │   ├── saveManager.py
    │   ├── utils.py
    │   └── deathCheck.py
    │
    ├── data/
    │   └── ascii/
    │       ├── appear/
    │       ├── cleaning/
    │       ├── disappear/
    │       ├── dying/
    │       ├── enjoying/
    │       ├── feeding/
    │       ├── playing/
    │       └── sleeping/
    │
    └── README.md

## 🐾 Game description

Your Tamagotchi has **4 essential gauges**: Hunger, Energy,
Mood, Cleanliness.

## 🕹️ Events

-   Feed
-   Sleep
-   Play
-   Wash
-   Save & Quit

## ⚠️ Game Over

The slime dies if :
- Hunger = 100
- Energy = 0
- Mood = 0
- Cleanliness = 0

## 💾 Save and Load

The game uses a JSON file: `save.json`.

## 🚀 Play the game

### Method 1

    python main.py

## 👥 Authors

Project completed by:
- Rémy Bordes alias
<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="18"> ElMonarita and boremy-ynov