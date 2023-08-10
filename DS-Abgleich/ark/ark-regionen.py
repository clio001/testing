import json

with open("ark-regionen.json", "r") as json_file:
    data = json.load(json_file)

for subCollection in data[1]['subCollections'][0]['subCollections']:
    print(f"Systemstelle: {subCollection['name']}")
    print(f"Notationsbereich: {subCollection['notationRange']}")
    print(f"Titelanzahl: {subCollection['numberRecords']}" + '\n')



