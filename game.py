import sys
sys.dont_write_bytecode = True
from json_importer import JsonImporter

def selectPlayerClass():
    print("""\nSelect your presence:""")
    for index, player_class in enumerate(JsonImporter.player_classes):
        print(f"{index + 1} - {player_class['name']}")

    option = input('\n> ')
    try:
        option = int(option)
    except ValueError:
        print("""\nDo not mess around, this is not a game.""")
        return selectPlayerClass()

    option -= 1
    if option < len(JsonImporter.player_classes) and option >= 0:
        return option

    else:
        print("""\nThat's not an option, maybe you should rethink your decisions.""")
        return selectPlayerClass()