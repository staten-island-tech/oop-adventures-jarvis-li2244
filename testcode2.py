import json 
with open('mapinstance.json') as dropp:
    locatien = json.load(dropp)
with open('enemies.json') as infile:
    enemy = json.load(infile)
def enemy_spawn():
    for i, (v, k) in enumerate(locatien['enemies'][0].items()):
        print(i, v, k)
enemy_spawn()