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
    



class Enemy():
    def __init__(self, health, damage, dodge, defense, mana, atkspd, critchance, critdmg):
        self.health = health
        self.damage = damage
        self.dodge = dodge
        self.defense = defense
        self.mana = mana
        self.atkspd = atkspd
        self.critchance = critchance
        self.critdmg = critdmg
    def enemy_stat_register():
        health = enemy[f'generic_enemy{var}'][0]['health']
        damage = enemy[f'generic_enemy{var}'][0]['damage']
        dodge = enemy[f'generic_enemy{var}'][0]['dodge']
        defense = enemy[f'generic_enemy{var}'][0]['defense']
        mana = enemy[f'generic_enemy{var}'][0]['mana']
        atkspd = enemy[f'generic_enemy{var}'][0]['atkspd']
        critchance = enemy[f'generic_enemy{var}'][0]['critchance']
        critdmg = enemy[f'generic_enemy{var}'][0]['critdmg']
        w = (health, damage, dodge, defense, mana, atkspd, critchance, critdmg)
        w.register(Enemy)
    def testprinter(self):
        print(self.health)
    def enemy_losehealth():
        el =1
    def enemy_heal():
        el =1
    def enemy_fight():
        enemy = True
        while enemy == True:
            print("ATTACK")
            print("ENEMY HEALTH: {")
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
        create_newinstance()
def create_newinstance():
    testl = []
    for i in range():
        testl.append()
    return testl
        

def spawn_randomizer():
    use_list = create_newinstance()
            






def lootcheck():
    if drop == True:
        drop_chancetemp = enemy['generic_enemy1'][0]['loot_table'][0]['generic_loot1']
        drop_chance = int(100/drop_chancetemp)
        if random.randint(1, drop_chance) == random.randint(1, drop_chance):
            with open('loot.json','r') as r:
                dete = json.load(r)
            test1 = dete[f'generic_loot{var1}'][0]['name']
            print(f'DROPPED: {test1} ({drop_chancetemp}% drop chance)')
