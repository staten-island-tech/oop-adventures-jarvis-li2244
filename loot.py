import json
import random
drop = True
var = 1
x=1
y=0
def enemy_spawn():
    global x
    global y
    #list func to find spawn amounts of each thing
    list = []
    with open('location.json','r') as e: 
        data = json.load(e)
    #find number of types of enemies
    eamount = data['location_1'][0]['enemies'][0]['types']
    #get spawn amounts of each type of enemy and append to a list
    while x != eamount+1:
        list.append(data['location_1'][0]['enemies'][y][f'generic_enemy{x}'][0]['spawn_amount'])
        x+=1
        y+=1
    #use indexing to take the numbers out of a list and pass it through another function later on
    print(list[0])
    


def lootcheck():
    if drop == True:
        with open('enemies.json','r') as f:
            data = json.load(f)
        drop_chancetemp = data['generic_enemy1'][0]['loot_table'][0]['generic_loot1']
        drop_chance = 100/drop_chancetemp
        if random.randint(1,drop_chance) == random.randint(1, drop_chance):
            with open('loot.json','r') as r:
                dete = json.load(r)
            print(dete[f'generic_loot{var}'][0]['name'])
enemy_spawn()



