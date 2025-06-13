from json_loader import JsonImporter

ji = JsonImporter()

npc = ji.get_npc('mini_turret')

print(npc.name, npc.actions)