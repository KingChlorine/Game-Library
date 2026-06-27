import json
import os

#sets directory to path containing this file
directory = os.path.dirname(os.path.abspath(__file__))
#Adds json file to path
jsonPath = os.path.join(directory, "games.json")

if os.path.exists(jsonPath):
    with open(jsonPath, "r") as f:
        gamesInLibrary = json.load(f)
else:
    gamesInLibrary = []

def viewLibrary():
    for item in gamesInLibrary:
        print(item, sep= "\n")

def addGame():
    while True:
        game = input("Type game title:")
        platform = input("Type which platform:")
        gamesInLibrary.append({"Game": game, "Platform": platform})
        break

def removeGame():
    removeGame = input("Type game title you wish to remove:")
    for game in gamesInLibrary:
        if game["Game"].lower() == removeGame:
            gamesInLibrary.remove(game)

def saveToJson():
    games = json.dumps(gamesInLibrary, indent=4)
    with open("games.json", "w") as f:
        f.write(games)
        print("Library updated successfully!")


def gameLibrary():
    while True:
        print("1.Open Game library 2. Add Game 3. Remove Game 4. Quit")
        main_menu_select = input("Type number to choose")

        if main_menu_select == "1":
            viewLibrary()

        if main_menu_select == "2":
            addGame()
            saveToJson()

        if main_menu_select == "3":
              removeGame()
              saveToJson()

        if main_menu_select == "4":
            print("GoodBye!")
            break


gameLibrary()


