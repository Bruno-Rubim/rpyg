import time

class UI():
    def request_number_choice(min, max):
        option = input('\n> ')
        try:
            option = int(option)
        except ValueError:
            print("""\nDo not mess around, this is not a game.""")
            return UI.request_number_choice(min, max)

        if option <= max and option >= min:
            return option

        else:
            print("""\nThat's not an option, maybe you should rethink your decisions.""")
            return UI.request_number_choice(min, max)

    def print_text(string: str):
        texts = string.split('\n')
        for index in texts:
            print(index)
            length = len(index)
            time.sleep(length/300)

    def promt_user(text: str, number = False, min = 0, max = 0):
        if text:
            print(text)
        if number:
            return UI.request_number_choice(min, max)
        return input("> ")
        ...