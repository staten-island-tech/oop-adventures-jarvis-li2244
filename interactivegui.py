import json
import time
import random
from item import Inventory
from recipes import *
from map import *
from methods import Modified_Functions
mod = Modified_Functions
re = "\033[91m█"
pu = "\33[95m█" 
bl = "\33[34m█"
b2 = "\33[36m█"
b3 = "\33[96m█"
gr = "\033[92m█"
g2 = "\033[32m█"
br = "\33[33m█"
ye = "\33[93m█"
g1 = "\33[37m█"
wh = "\033[0m█"
color_default = "\033[0m"
color_red = "\033[91m"
with open('locationenemy.json') as fifa:
    location = json.load(fifa)
with open('dialogue.json') as dialogu:
    dialogue = json.load(dialogu)
with open('enemyinstance.json')as f:
    enemies1 = json.load(f)
with open('player.json') as w:
    player = json.load(w)
with open('inventorye.json') as el:
    inventorye = json.load(el)
with open('character.json') as elf:
    character = json.load(elf)
with open('enemies.json') as flafel:
    enemies = json.load(flafel)
with open('classStats.json') as cs1:
    cs = json.load(cs1)
with open('mapinstance.json', mode='r') as infile:
    mapperjapper = json.load(infile)
class Start():
    def intro_screen():
        print(r"""
    _    ____   ____ ___ ___    ____  ____   ____ 
   / \  / ___| / ___|_ _|_ _|  |  _ \|  _ \ / ___|
  / _ \ \___ \| |    | | | |   | |_) | |_) | |  _ 
 / ___ \ ___) | |___ | | | |   |  _ <|  __/| |_| |
/_/   \_\____/ \____|___|___|  |_| \_\_|    \____|
                            
                By: Jarvis and Johnny
                         _
                        ( )
                        \|/
                         |
                        / \      
                Press Enter to Begin
""")
        time.sleep(0.5)
        input()
        Start.class_select()
    def modify(file, content, mode):
        with open(f'{file}.json')  as openfile:
            filed = json.load(openfile)
        if mode == '':
            filed = content
        elif mode != '':
            filed[0][mode] = content
        with open(f'{file}.json', 'w+')  as closedfile:
            closedfile.write(json.dumps(filed, indent=2))
    def class_select():
        print(r'''
                        CLASS SELECT 
        ╔═════════╗╔═════════╗╔═════════╗╔═════════╗
        ║     o   ║║   | \   ║║     /   ║║         ║
        ║    /    ║║  >|-->  ║║   _/_   ║║  -]═──  ║ 
        ║   /     ║║   | /   ║║   /     ║║         ║  
        ╚═════════╝╚═════════╝╚═════════╝╚═════════╝
            MAGE      ARCHER    WARRIOR    ASSASSIN
        ''')
        class_selected = mod.proper_input('str').lower() 
        if class_selected == 'mage' or class_selected == 'archer' or class_selected == 'warrior' or class_selected == 'assassin':
            print(f'{class_selected} Selected')
            Start.blit_class_stats(class_selected)
            Start.clear_equips()
            Start.clear_inventory()
        else:
            print('Class Entered Does Not Exist')
            print('Try Again')
            Start.class_select()
    def blit_class_stats(class_name):
        for i,(v,k) in enumerate(cs.items()):
            if class_name == k[0]['class_name']:
                Start.modify('player', k[0]['stats'], '')
                name = input("ENTER YOUR NAME : ")
                Start.modify('player', name, 'name' )
                Start.location_set(class_name)
                break
    def location_set(name):
        character[0]['role'] = name
        character[0]['name'] = player[0]['name']
        character[0]['location'] = 'Anthill Forest'
        character[0]['sub_location'] = 'The Myrminki Village'
        character[0]['level'] = 0 
        character[0]['story'] = 'Chapter 1'
        character[0]['questname'] = null
        character[0]['skills'] = [null,null,null,null]
        character[0]['attacks'] = [null,null,null,null]
        with open('character.json', 'w+')  as infile:
            infile.write(json.dumps(character, indent=2))
    def clear_equips():
        with open('inventorye.json') as infile:
            equips = json.load(infile)
        for i, (k,v) in enumerate(equips.items()):
            equips[k][0]['name'] = None
            equips[k][0]['quantity'] = 0
            with open('inventorye.json', 'w+') as outfile:
                outfile.write(json.dumps(equips, indent=2))
    def clear_inventory():
        with open('inventoryi.json') as infile:
            inventory = json.load(infile)
        for i,(k, v) in enumerate(inventory.items()):
            inventory[k][0]['name'] = None
            inventory[k][0]['quantity'] = 0
            with open('inventoryi.json' ,'w+') as outfile:
                outfile.write(json.dumps(inventory, indent=2))
    def intro():
        if input() == 'skip':
            print('skipping cutscne')
            pass
            Maper.map()
        else:
            #dialogue here
            pass
            Maper.map()
    def dialogue():
        if character[0]['sub_location'] == 'The Myrminki Village':
            Start.actual_dialogue('Tutorial: Act I')
        elif character[0]['sub_location'] == 'The Myrminki Assembly':
            Start.actual_dialogue('Tutorial: Act II')
        elif character[0]['sub_location'] == 'Treehouse':
            Start.acutal_dialogue('Tutorial: Act III')
        elif character[0]['sublocaiton'] == '''Blacksmith's Cabin''':
            opt = 'Act III Item 1'
        elif character[0]['sublocation'] == '''Chemist's Lab''':
            Start.actual_dialogue()
    def actual_dialogue(scene_name):
        for i, k in enumerate(dialogue[scene_name]):
            for ee in range(len(k)):
                mod.delay_print(k[i])
                if input() == 'skip':
                    return
                print(''' ''')

class Menu():
    def open_menu():
        mod.line_split_print(r''' MENU 
╔════════════════╗
║    Inventory   ║
╚════════════════╝
╔════════════════╗
║    Equipment   ║
╚════════════════╝
╔════════════════╗
║      Stat      ║
╚════════════════╝
╔════════════════╗
║    Exit Menu   ║
╚════════════════╝
╔════════════════╗
║      Quit      ║
╚════════════════╝
    ''')
        mod.indent_cutscene()
        idea = mod.proper_input('str').lower()
        if idea == 'help':
            print('inv to enter inventory, equip to enter equipment, stat to enter stat, quit to quit and exit to exit')
        elif idea == 'stat':
            print('Opening Stats')
            for i,(k,v) in enumerate(player[0].items()):
                print(k,':',v)
        elif idea == 'equip' or idea == 'equipment':
            print('Opening Equips')
            for i, (k, v) in enumerate(inventorye.items()):
                print(v[0]['type'],":",v[0]['name'])
        elif idea == 'inv':
            print('Opening Inventory')
            Inventory.inventory_display()
        elif idea == 'exit':
            print('Exiting menu')
            print('going back to map')
            return
        elif idea == 'quit':
            sys.exit()
            print("CLOSE")
        elif idea == 'craft':
            Crafting.create_list()
            Crafting.recipe_select()
        Menu.open_menu()
class Levels():
    def calculate():
        level = player[0]['level']
        next_level = level + 1
        exp_req = (next_level/0.1)**2
        print(exp_req)
        return exp_req
    def current_exp():
        exp_req = Levels.calculate()
        level = player[0]['level']
        exp = player[0]['exp']
        if exp >= exp_req:
            egg = exp - exp_req
            new_level = level + 1
            print('LEVEL UP!')
            Player.modify(egg, 'exp', 'set')
            Player.modify(new_level, 'level', 'add')
            Levels.exp_display()
        else:
            Levels.exp_display()
    def exp_display():
        with open('player.json', 'r+') as i:
            plays = json.load(i)
        regular_health = plays[0]['exp']
        #we can prob check if the amount of characters in the healthbar is equal to 20 or whtev and if not we just add another value to the end of it
        teegreg = Levels.calculate()/100
        max1 = (int(Levels.calculate()/teegreg)/5)
        current1 = int((regular_health/teegreg)/5)
        print(f'{color_default}PLAYER HEALTH: {regular_health}/{Levels.calculate()}')
        yes_health = current1 * "█"
        no_health = (max1 - current1)
        egg = current1 + no_health
        if egg != 20:
            no_health += 1
        no_health1 =int(no_health)* "▒"
        print(f'{color_default}╔════════════════════╗' )
        print(f'║\033[1;91;40m{yes_health}{no_health1}{color_default}║')
        print(f'{color_default}╚════════════════════╝' )
    def stats_boost():
        pass
class Spawn():
    def blit_enemy():
        for i, (k, v) in enumerate(enemies.items()):
            if v['names'] == Spawn.spawnenemy():
                with open('maperjap.json', 'w+')  as outfile:
                    outfile.write(json.dumps(v, indent=2))
                    outfile.seek(0)
    def spawnenemy():
        for index, stuff in enumerate(mapperjapper['enemies']):
            spawn = stuff[f'{index}'][0]['spawn_rate']
            if random.randint(1, int(spawn/10)) == random.randint(1, int(spawn/10)):
                return stuff[f'{index}'][0]['name']
# do exp display here
#list of known bugs currently(repport bugs here) : health_bar display gets fucked over when the value gets rounded down weird(not resolved yet)
#healing overflow(resolved) 
#once enemy reaches a certain point it ends up trying to focus everything on healing itself and ends up not attacking, 

def play():
    with open('player.json', 'r+') as f:
        plays = json.load(f)
    id = plays[0]['id']
    name = plays[0]['name']
    exp = plays[0]['exp']
    stat_point = plays[0]['stat_points']
    max_health = plays[0]['max_health']
    health = plays[0]['health']
    attack = plays[0]['attack']
    dodge = plays[0]['dodge']
    defense = plays[0]['defense']
    luck = plays[0]['luck']
    mana = plays[0]['mana']
    critchance = plays[0]['critchance']
    critdmg = plays[0]['critdmg']
    speed = plays[0]['speed']
    pe = Player(id, name, exp, stat_point, max_health, health, attack, dodge, defense, luck, mana, critchance, critdmg, speed)
    return pe
def enemy_spawn():
    with open('mapinstance.json') as infile:
        mapinstance = json.load(infile)
        enemy_amount = len(mapinstance['enemies']) 
        if enemy_amount == 1:
            enemy_name = mapinstance['enemies'][0]['0'][0]['name']
        elif enemy_amount > 1:
            enemy_spawn = random.randint(0, enemy_amount)
            enemy_name = mapinstance['enemies'][0][f'{enemy_spawn}'][0]['name']
        for i, (k,v) in enumerate(enemies.items()):
            if enemy_name == v[0]['name']:
                break
        with open('enemyinstance.json', 'w+') as infile:
            infile.write(json.dumps(enemies[k], indent=2))
def atte():
    with open('enemyinstance.json', 'r+') as e:
        enemies = json.load(e)
    max_health = enemies[0]['max_health']
    health = enemies[0]['health']
    damage = enemies[0]['damage']
    dodge = enemies[0]['dodge']
    defense = enemies[0]['defense']
    mana = enemies[0]['mana']
    critchance = enemies[0]['critchance']
    critdmg = enemies[0]['critdmg']
    speed = enemies[0]['speed']
    temp = Enemy(max_health, health, damage, dodge, defense, mana, critchance, critdmg, speed)
    return temp
def story():
    with open('character.json') as infile:
        character =  json.load(infile) 
    if character['sublocation']:
        pass
#create an instance of the enemy using a loop. loop does not move on til enemy is dead or the player has moved into a certain location. 
class Player():
    def __init__(self, id, name, exp, stat_points, max_health, health, attack, dodge, defense, luck, mana, critchance, critdmg, speed):
        self.id = id
        self.name = name
        self.exp = exp
        self.stat_points = stat_points
        self.max_health = max_health
        self.health =  health
        self.attack = attack
        self.dodge = dodge
        self.defense = defense
        self.luck = luck#
        self.mana = mana
        self.critchance = critchance#
        self.critdmg = critdmg#
        self.speed = speed
    def modify(change, var, mode):
        with open('player.json', 'r+') as r:
            unique_variable = json.load(r)
        if mode == 'set':
            unique_variable[0][f'{var}'] = change
        elif mode == 'add':
            unique_variable[0][f'{var}'] += change
        elif mode == 'subtract':
            unique_variable[0][f'{var}'] -= change
        elif mode == 'append':
            unique_variable[0][f'{var}'].append(change)
        with open('player.json','w+') as i:
            i.write(json.dumps(unique_variable, indent = 2))
            i.seek(0)
    def start_game():
        Player.gui()
    def critical_hit(self):
        crit = False
        roll = int(100/self.critchance)
        if random.randint(1, roll) == random.randint(1, roll):
            crit = True
        return crit
    def deal_damage(self):
        pe = play()
        crit = pe.critical_hit()
        damage_dealt_player = self.attack
        if crit == True:
            critdmg = self.critdmg/100 + 1
            critical_hit = self.attack * critdmg
            damage_dealt_player = critical_hit
            print(f'{color_red}critical hit!{color_default}')
        elif crit == False:
            damage_dealt_player = self.attack
        print(damage_dealt_player)
        egg = atte()
        egg.take_damage_enemy(damage_dealt_player)
        return damage_dealt_player
    def take_damage(self, damage):
        egg = atte()
        pe = play()
        dod = pe.doge()
        df = self.defense
        if dod == False:
            print("DODGED")
        else:
            if df == 0:
                self.health = self.health - damage
            elif df != 0:
                multiplier = self.defense * 0.01
                dmg = damage - damage * multiplier
                self.health = self.health - dmg
            if self.health <= 0:
                print(r'''
                             ____  _____    _    ____  
                            |  _ \| ____|  / \  |  _ \ 
                            | | | |  _|   / _ \ | | | |
                            | |_| | |___ / ___ \| |_| |
                            |____/|_____/_/   \_\____/
''')
                Player.modify(0, 'health', 'set')
                return False
            else:
                Player.modify(self.health, 'health', 'set')
                return True
    def heal_damage(self, amount):
        pe = play()
        heal = amount
        self.health = self.health + heal
        if self.health > self.max_health:
            egg = self.health - self.health
            self.health  = self.health - egg
        self.health = self.health
        Player.modify(self.health, 'health', 'set')
        return self.health
    def health_display(self):
        with open('player.json', 'r+') as i:
            plays = json.load(i)
        regular_health = plays[0]['health']
        #we can prob check if the amount of characters in the healthbar is equal to 20 or whtev and if not we just add another value to the end of it
        teegreg = self.max_health/100
        max1 = int((self.max_health/teegreg)/5)
        current1 = int((regular_health/teegreg)/5)
        print(f'{color_default}PLAYER HEALTH: {regular_health}/{self.max_health}')
        yes_health = current1 * "█"
        no_health = (max1 - current1)
        egg = current1 + no_health
        if egg != 20:
            no_health += 1
        no_health1 = (no_health)* "▒"
        print(f'{color_default}╔════════════════════╗' )
        print(f'║\033[1;91;40m{yes_health}{no_health1}{color_default}║')
        print(f'{color_default}╚════════════════════╝' )
    def doge(self):
        dod = self.dodge
        egg = True
        if dod != 0:
            egg = int(100/dod)
            if random.randint(1, egg) == random.randint(1, egg):
                egg = False
        else:
            return egg
        return egg
    def show_equips():
        with open('inventorye.json') as infile:
            envy = json.load(infile)
        for i, (v,k) in enumerate(envy.items()):
            pass
    def gui():
        egg = play()
        print(r"""
╔═════════╗ ╔═════════╗ ╔═════════╗ ╔═════════╗
║         ║ ║         ║ ║         ║ ║         ║
║   ATK   ║ ║   RUN   ║ ║  EQUIP  ║ ║  ITEMS  ║
║         ║ ║         ║ ║         ║ ║         ║  
╚═════════╝ ╚═════════╝ ╚═════════╝ ╚═════════╝
                """)
        egg.health_display()
        egg = input("")
        pe = play()
        pe.deal_damage() if egg == "1" else (pe.run()) if egg == "2" else (Player.show_equips()) if egg == "3" else ((Inventory.inventory_display())) if egg == "4" else (Player.gui())
        return True
    def run(self):
        em = play()
        egg = False
        if em.dodge != 0:
            roll = int(100/self.dodge)
            if random.randint(1, roll) == random.randint(1, roll):
                print(r""" 
            ╔═════════════════════════╗
            ║     ESCAPE SUCESSFUL    ║
            ╚═════════════════════════╝
                """)
            Enemy.health_modify(0)
        else:
            print(r""" 
        ╔═════════════════════════╗
        ║      ESCAPE FAILED      ║
        ╚═════════════════════════╝
            """)  
class Enemy():
    def __init__(self, max_health, health, damage, dodge, defense, mana, critchance, critdmg, speed):
        self.max_health = max_health
        self.health = health
        self.damage = damage
        self.dodge = dodge
        self.defense = defense
        self.mana = mana
        self.critchance = critchance
        self.critdmg = critdmg
        self.speed = speed
    def health_modify(health_change):
        with open('enemyinstance.json', 'r+') as rel:
            egg = json.load(rel)
            egg[0]['health'] = health_change
            rel.seek(0)
        with open('enemyinstance.json','w+') as icecubes:
            icecubes.write(json.dumps(egg, indent=2))
    def doge(self):
        dod = self.dodge
        egg = True
        if dod != 0:
            egg = int(100/dod)
            if random.randint(1, egg) == random.randint(1, egg):
                egg = False
        return egg
    def take_damage_enemy(self, damage):
        with open('enemyinstance.json', 'r') as id:
            eggd = json.load(id)
        healthjson = eggd[0]['health']
        pe = atte()
        dod = pe.doge()
        df = self.defense
        if dod == False:
            print("DODGED")
        else:
            if df == 0:
                self.health = self.health - damage
                print("No Defense")
            elif df != 0:
                multiplier = self.defense * 0.01
                dmg = damage - damage * multiplier
                self.health -= dmg
                print(f'health damage{self.health}')
        if healthjson <= 0 or self.health <= 0:
            Enemy.health_modify(0)
            print('0 hp')
        else:
            print('woah, your still alive')
            Enemy.health_modify(self.health)
        print(self.health)
        return self.health
    def health_heal(self):
        en = atte()
        heal = 10000
        self.health += heal
        print(f'health_heal{self.health}')
        if self.health > self.max_health:
            eggg = self.health - self.max_health
            self.health -= eggg
        print(f'heal:{self.health}')
        Enemy.health_modify(self.health)
        en.health_display()
        return self.health
    def health_display(self):
        with open('enemyinstance.json', 'r') as id:
            ide = json.load(id)
        healthjson = ide[0]['health']
        teegreg = self.max_health/100
        max1 = int((self.max_health/teegreg)/5)
        current1 = int((healthjson/teegreg)/5)
        print(f'{color_default}ENEMY HEALTH: {healthjson}/{self.max_health}')
        yes_health = current1 * "█"
        no_health = (max1 - current1)
        egg = current1 + no_health
        if egg != 20:
            no_health += 1
        no_health1 = (no_health)* "▒"
        print(f'{color_default}╔════════════════════╗' )
        print(f'║\033[1;91;34m{yes_health}{no_health1}{color_default}║')
        print(f'{color_default}╚════════════════════╝' )
    def enemy_show():
        egg = atte()
        print(r"""
    GHOST ATTACK!!!
          ___
        \/   \/
        |\o o/|  
        |  0  |
        \     |
         \    /
          \  / 
           \|
           """)
        egg.health_display()
    def action(self):
        egg = atte()
        print("ATTACK")
        if self.health < self.max_health/2:
            roll = int(100/self.dodge)
            if random.randint(1, roll) == random.randint(1, roll):
                egg.health_heal()
                print("heal")
        else: 
            print("dealdamagew")
            egg.deal_damage()
        return True
    def critical_hit(self): 
        crit = False
        roll = int(100/self.critchance)
        if random.randint(1, roll) == random.randint(1, roll):
            crit = True
        return crit
    def deal_damage(self):
        egg = atte()
        player = play()
        crit = egg.critical_hit()
        var = 0
        if crit == True:
            elaf = self.critdmg/100 + 1
            critical_hit = int(self.damage * elaf)
            var = critical_hit
            print("enemy critical hit!")
        elif crit == False:
            var = self.damage
        player.take_damage(var)
        print(var)  
        return var
class Turn():
    def determine():
        psp = player[0]['speed']
        esp = enemies1[0]['speed']
        if esp < psp:
            Turn.tempvar()
        elif esp > psp:
            Turn.tempvar2()
    def tempvar():
        with open('player.json','r+') as ief:
            iea = json.load(ief)
        eaf = iea[0]['health']
        if eaf <= 0:
                print("PLAYER DEAD")
                print(r'''
╔═════════════════════════════════════╗ 
║    RETURNING TO LAST CHECKPOINT     ║
╚═════════════════════════════════════╝
''')
                pass
                Maper.map()
                #add soemthing that loops the player back out to their last location, so 2 variables : 1 for current location and 1 for last saved location. no saves during battles or any interactions. 
        else:
                print("PLAYER")
                Player.start_game()
                print("""
                """)
                Turn.tempvar2()
    def tempvar2():
        lm = atte()
        with open('enemyinstance.json','r+') as eg:
                enemies1 = json.load(eg)
        eaf2 = enemies1[0]['health']
        if eaf2 <= 0:
            exp_drop = enemies1[0]['exp']
            print("ENEMY DEAD")
            print(f'EXP DROPPED : {exp_drop}')
            new_exp = player[0]['exp'] + exp_drop
            Player.modify(new_exp, 'exp', 'set')
            Levels.current_exp()
            Drops.drop_item()
            
        else:
            print("ENEMY")
            Enemy.enemy_show()
            lm.action()
            Turn.tempvar()
class Drops():
    def drop_item():
        with open('enemyinstance.json') as infile:
            denim = json.load(infile)
        for i, (v, k) in enumerate(enemies.items()):
            if k[0]['name'] != denim[0]['name']:
                continue
            for index,(value,key) in enumerate(k[0]['loot_table'][0].items()):
                if random.randint(1,int(100/key)) ==  random.randint(1, int(100/key)):
                    print(f'{value} dropped! {key}% drop rate')
                    Inventory.psi(value,random.randint(1, 100),'add', 'inventoryi.json')
def verify_usage():
    egg = input("")
    if egg == "Y":
        return True
    else:
        return False
level = 0
egg = '\t' * level
#lenghth = [0], height = [1]
#possible overlap where enemies can be on top of materials such as trees or ores
Start.intro_screen()