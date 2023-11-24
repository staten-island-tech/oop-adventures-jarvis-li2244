import json
import random
import time
drop = True
var = 1
x=0
y=2
z=1
screen_trigger = True
with open('location.json','r') as e: 
    data = json.load(e)
def intro_screen():
    if screen_trigger == True: 
        print(f"Entering {data['location_1'][0]['locationname']}")
    time.sleep(5)
    print("ENEMIES!")

intro_screen()

def enemy_spawn():
    global x
    global y
    #list func to find spawn amounts of each thing
    list = []
    #find number of types of enemies
    eamount = data['location_1'][0]['types']
    print(data['location_1'][0]['enemies'][z][f'{y}'][0]['name'])
    #get spawn amounts of each type of enemy and append to a list
    #for i in range(eamount):
        #print(data['location_1'][0]['enemies'][1])
        #y+=1
        #x+=1


    

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




