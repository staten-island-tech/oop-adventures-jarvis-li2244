import json
with open('mapinstance.json')  as f:
    mapin = json.load(f)

print(mapin['spawn_position'][0])
