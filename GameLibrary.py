gamesInLibrary = []

def gameLibrary():
    while True:
        print("1.Open Game library 2. Add Game")
        main_menu_select = input("Type number to choose")

        if main_menu_select == "1":
            print(gamesInLibrary)

        if main_menu_select == "2":
            addGame = input("Type game title you wish to add:")
            gamesInLibrary.append(addGame)
        continue
gameLibrary()