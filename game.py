from json_loader import JsonImporter

ji = JsonImporter()

npc = ji.get_npc('fungi_folk')

print(npc.name, npc.actions)