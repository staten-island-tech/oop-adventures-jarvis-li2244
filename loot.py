import json
import random
drop = True
var = 1
def lootcheck():
    if drop == True:
        with open('enemies.json','r') as f:
            data = json.load(f)
        drop_chancetemp = data['generic_enemy1'][0]['loot_table'][0]['generic_loot1']
        drop_chance = 100/drop_chancetemp
        if random.randint(1,drop_chance) == random.randint(1, drop_chance):
            print("FUNCT")
            with open('loot.json','r') as r:
                dete = json.load(r)
            print(dete[f'generic_loot{var}'][0]['name'])
lootcheck()
