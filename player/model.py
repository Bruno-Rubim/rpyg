from json_importer import JsonImporter

class Player:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Player, cls).__new__(cls)
        return cls.instance

    def __init__(self, player_class_index, name=""):
        list = JsonImporter.loadJSON('player')
        data_object = list[player_class_index]
        self.name = name
        self.class_name = data_object.get("name")
        self.actions = data_object.get("actions")
        self.attacks = data_object.get("attacks", [])
        self.base_hp = data_object.get("base_hp")
        self.base_dodge = data_object.get("base_dodge")
        self.base_defense = data_object.get("base_defense")
        self.elements = data_object.get("elements")
        self.status = []