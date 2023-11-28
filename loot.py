import json
import random
import time
drop = True
var1 = 1
enemy_alive = True
y=1
z=0
screen_trigger = True
def player_exp_check():
    temp = 1 
    #create a json file with all level up levels(maybe use a formula to generalzie the amount of exp needed to leve up)
    #compare the total amount of exp and set the levels to the respective amount of level
def temp_exp_meter():
    #open json file here
    #use player json file to update
    temp = 1 
def skill_points():
    temp = 1
    #when level_up trigger add skill point to json file
    #when skill_point used remove skill point from json file

class Testvar():
    temp = 1



with open('enemies.json','r') as f:
    enemy = json.load(f)
with open('location.json','r') as e: 
    location = json.load(e)

def location_set():
    abc = int(input("Options: (1, 2, 3, 4, 5, 6, 7) "))
    return abc
var = location_set()


def intro_screen():
    if screen_trigger == True: 
        var = 1 
        print(f'Entering {location[f'location_{var}'][0]['locationname']}')
    time.sleep(5)
    print("ENEMIES!")
def reward_screen():
    if enemy_alive:
        
        lootcheck()


intro_screen()
def loot_list():
    llist = enemy
    return list


def enemy_spawn(): 
    #find number of types of enemies
    eamount = location[f'location_{var}'][0]['types']
    enemy_am = location[f'location_{var}'][0]['ratio']
    e_numstart = location [f'location_{var}'][0]['enemy_numstart']
    index_start = e_numstart - 1 
    #get spawn amounts of each type of enemy and append to a list
    global enemy_alive
    for i in range(eamount):
        create_newinstance()
        index_start += 1
        e_numstart += 1
def enemy_name():
    enemy_stat = location[f'location_{var}'][0]['enemies'][0]['name']
enemy_spawn()
def enemy_am():
    test1 = location['location_1'][0]['enemies'][0]['spawn_amount']
    print(test1)

def create_newinstance(): 
    lest = []
    lest.append()
    return lest


def enemy_spawnlocation():
    tat = create_newinstance()
enemy_am()

def location_reward():
    temp = 1
    
def lootcheck():
    if drop == True:
        drop_chancetemp = enemy['generic_enemy1'][0]['loot_table'][0]['generic_loot1']
        drop_chance = int(100/drop_chancetemp)
        if random.randint(1, drop_chance) == random.randint(1, drop_chance):
            with open('loot.json','r') as r:
                dete = json.load(r)
            print(f'DROPPED: {dete[f'generic_loot{var1}'][0]['name']} ({drop_chancetemp}% drop chance)')

def expdrop():
    exp_gain = enemy['generic_enemy1'][0]['loot_table'][0]['exp']
    