# Tamagotchi
Creation of a game based on the Tamagotchi concept to learn more about Python. To do this, the game must include certain actions such as eating, sleeping, playing, etc. The game must also have a system to save the game in JSON.

## 📌 Contenu du projet

    project/
    │
    ├── main.py
    ├── game.py
    ├── src/
    │   ├── tamagotchi.py
    │   ├── actions.py
    │   ├── save_manager.py
    │   ├── utils.py
    │   └── check.py
    │
    ├── data/
    │   └── ascii/
    │       ├── eat/
    │       ├── sleep/
    │       ├── play/
    │       ├── wash/
    │       ├── death/
    │       └── others…
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

Le slime meurt si : - Faim = 100
- Énergie = 0
- Humeur = 0
- Propreté = 0

## 💾 Save and Load

The game uses a JSON file: `save.json`.

## 🚀 Play the game

### Method 1

    python main.py

## 👥 Auteurs

Project completed by:
- Rémy Bordes alias
<img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="18"> ElMonarita and boremy-ynov