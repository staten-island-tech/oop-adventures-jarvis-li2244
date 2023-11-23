import json
import random
drop = True
var = 1
def enemy_spawn():
    with open('location.json','r') as e: 
        data = json.load(e)
    enemy_list = data['location_1'][0]['enemies']
    print(enemy_list)



def lootcheck():
    if drop == True:
        with open('enemies.json','r') as f:
            data = json.load(f)
        drop_chancetemp = data['generic_enemy1'][0]['loot_table'][0]['generic_loot1']
        print((data['generic_enemy1'][0]["loot_table"][0,3]))
        drop_chance = 100/drop_chancetemp
        if random.randint(1,drop_chance) == random.randint(1, drop_chance):
            with open('loot.json','r') as r:
                dete = json.load(r)
            print(dete[f'generic_loot{var}'][0]['name'])
lootcheck()


