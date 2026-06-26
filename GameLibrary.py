import json
gamesInLibrary = []



def gameLibrary():
    while True:
        print("1.Open Game library 2. Add Game 3. Remove Game 4. Quit 5. Save")
        main_menu_select = input("Type number to choose")

        if main_menu_select == "1":
            for item in gamesInLibrary:
                print(item, sep= "\n")

        if main_menu_select == "2":
            while True:
                game = input("Type game title:")
                platform = input("Type which platform:")
                gamesInLibrary.append({"Game": game, "Platform": platform})
                #games = json.dumps(gamesInLibrary, indent=4)
                #with open("games.json", "w") as f:
                #    f.write(games)
                break

        if main_menu_select == "3":
            removeGame = input("Type game title you wish to remove:")
            for game in gamesInLibrary:
                if game["Game"].lower() == removeGame:
                    gamesInLibrary.remove(game)

        if main_menu_select == "4":
            print("GoodBye!")
            break

        if main_menu_select == "5":
            games = json.dumps(gamesInLibrary, indent=4)
            with open("games.json", "w") as f:
                f.write(games)
                print("Library Saved")


gameLibrary()