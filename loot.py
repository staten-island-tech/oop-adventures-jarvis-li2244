import json
import random
import time
drop = True
var1 = 1
enemy_alive = True
y=1
z=0
screen_trigger = True






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
        test = location[f'location_{var}'][0]['locationname']
        print(f'Entering {test}')
    time.sleep(5)
    print("ENEMIES!")




intro_screen()
def loot_list():
    llist = enemy




def enemy_spawn():
    #find number of types of enemies
    eamount = location[f'location_{var}'][0]['types']
    enemy_am = location[f'location_{var}'][0]['ratio']
    e_numstart = location [f'location_{var}'][0]['enemy_numstart']
    index_start = e_numstart - 1
    #get spawn amounts of each type of enemy and append to a list
    global enemy_alive
    for i in range(eamount):
        for w in range(enemy_am):
            print(location['location_1'][0]['enemies'][index_start][f'{e_numstart}'][0]['name'])
            while enemy_alive == True:
                if input("EGGS?: ") != "":
                    enemy_alive = False
                print("FIGHT")


        index_start += 1
        e_numstart += 1
enemy_spawn()
def player_attack():
    moves = 0
    if moves != "":
        attack = True
    return attack


def enemy_battle():
    #use enemy_spawn here
    def attack():
        if player_attack() == True:
            print("ENEMY TURN : ")



def lootcheck():
    if drop == True:
        drop_chancetemp = enemy['generic_enemy1'][0]['loot_table'][0]['generic_loot1']
        drop_chance = int(100/drop_chancetemp)
        if random.randint(1, drop_chance) == random.randint(1, drop_chance):
            with open('loot.json','r') as r:
                dete = json.load(r)
            test1 = dete[f'generic_loot{var1}'][0]['name']
            print(f'DROPPED: {test1} ({drop_chancetemp}% drop chance)')
