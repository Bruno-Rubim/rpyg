def requestNumberChoice(min, max):
    option = input('\n> ')
    try:
        option = int(option)
    except ValueError:
        print("""\nDo not mess around, this is not a game.""")
        return requestNumberChoice(min, max)

    if option <= max and option >= min:
        return option

    else:
        print("""\nThat's not an option, maybe you should rethink your decisions.""")
        return requestNumberChoice(min, max)
