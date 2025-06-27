from json_importer import JsonImporter

class Player:
    instance = None
    initialized = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Player, cls).__new__(cls)
        return cls.instance

    def __init__(self, player_class_index, name=""):
        if Player.initialized:
            return
        Player.initialized = True

        classes = JsonImporter.loadJSON('player')
        data_object = classes[player_class_index]
        self.name = name
        self.class_name = data_object.get("name")
        self.actions = data_object.get("actions", [])
        self.atacks = data_object.get("atacks", [])
        self.base_hp = int(data_object.get("base_hp"))
        self.current_hp = int(data_object.get("current_hp", self.base_hp))
        self.base_dodge = int(data_object.get("base_dodge"))
        self.base_defense = int(data_object.get("base_defense"))
        self.elements = data_object.get("elements")
        self.status = []