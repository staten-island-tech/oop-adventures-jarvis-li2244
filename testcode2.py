"""import json 
with open('mapinstance.json') as dropp:
    locatien = json.load(dropp)
with open('enemies.json') as infile:
    enemy = json.load(infile)
def enemy_spawn():
    for i, (v, k) in enumerate(locatien['enemies'][0].items()):
        print(i, v, k)
enemy_spawn()

"""

import json, random
with open('mapinstance.json', mode='r') as infile:
    mapperjapper = json.load(infile)
def spawnenemy():
    for index, stuff in enumerate(mapperjapper['enemies']):
        spawn = stuff[f'{index}'][0]['spawn_rate']
        if random.randint(1, spawn) == random.randint(1, spawn):
            print('enemy_spawned')
spawnenemy()

    