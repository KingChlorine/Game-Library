gamesInLibrary = []

def gameLibrary():
    while True:
        print("1.Open Game library 2. Add Game 3. Remove Game 4. Quit")
        main_menu_select = input("Type number to choose")

        if main_menu_select == "1":
            print(gamesInLibrary)

        if main_menu_select == "2":
            addGame = input("Type game title you wish to add:")
            gamesInLibrary.append(addGame)

        if main_menu_select == "3":
            removeGame = input("Type game title you wish to remove:").lower
            gamesInLibrary.remove(removeGame)

        if main_menu_select == "4":
            break

gameLibrary()