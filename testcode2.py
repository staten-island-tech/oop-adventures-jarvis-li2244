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
with open('enemies.json', 'r+') as fr:
    ade = json.load(fr)
with open('mapinstance.json', mode='r') as infile:
    mapperjapper = json.load(infile)
with open('player.json') as infile:
    plop = json.load(infile)
class Spawn():
    def blit_enemy():
        for i, (k, v) in enumerate(ade.items()):
            if v['names'] == Spawn.spawnenemy():
                with open('maperjap.json')  as outfile:
                    outfile.write(json.dumps(v, indent=2))
                    outfile.seek(0)
    def spawnenemy():
        for index, stuff in enumerate(mapperjapper['enemies']):
            spawn = stuff[f'{index}'][0]['spawn_rate']
            if random.randint(1, int(spawn/10)) == random.randint(1, int(spawn/10)):
                return stuff[f'{index}'][0]['name']
def stat_usage():
    if plop[0]['stat_points'] == 0:
        print('no stat points')
        #add return statment back to the main menu here
    else:
        ask = input("Boost which stat: ")
        if ask in plop:
            print(ask)
def enter_integer():
    askdd = input()
    try:
        askdd = int(askdd)
        return askdd
    except:
        print('try again')
        return enter_integer()
        
