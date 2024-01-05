import json
import time
import random
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
with open('enemyinstance.json')as f:
    enemies1 = json.load(f)
with open('attacks.json') as i:
    attacks = json.load(i)
with open('player.json') as w:
    player = json.load(w)
with open('inventorye.json') as el:
    inventorye = json.load(el)
with open('character.json') as elf:
    character = json.load(elf)
with open('enemies.json') as flafel:
    ade = json.load(flafel)
with open('mapinstance.json', mode='r') as infile:
    mapperjapper = json.load(infile)
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
            Player.modify(new_level, 'level', 'set')
            Levels.exp_display()
        else:
            Levels.exp_display()
    def exp_display():
        pass
    def stats_boost():
        pass

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
def enemy_trigger():
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
                Player.new_screen()
                print(r'''
                             ____  _____    _    ____  
                            |  _ \| ____|  / \  |  _ \ 
                            | | | |  _|   / _ \ | | | |
                            | |_| | |___ / ___ \| |_| |
                            |____/|_____/_/   \_\____/
''')
                Player.modify(0, 'health', 'set')
                print("modified")
                return False
            else:
                print("modified")
                Player.modify(self.health, 'health', 'set')
                return True
    def heal_damage(self):
        pe = play()
        heal = 100
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
    def spell(self):
        mana = self.mana
        egg = input("")
        first_spell() if egg == 1 else(second_spell() if egg == 2 else(third_spell() if egg == 3 else (fourth_spell() if egg == 4 else(print("no spell_cast")))))
        ela = player[0]['selected_spells']
        print(ela)
        def first_spell():
            first = ela[0]
            attack =  1
        def second_spell():
            second = ela[1]
        def third_spell():
            third = ela[2]
        def fourth_spell():
            fourth = ela[3]
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
    def spell_equip():
        "ask player what spells/attacks they would like to equip, check json file if it exists, if not print spell does not exist or not unlocked yet, if it does exist we replace the current spell selection with the new spell"
        "make sure to ask which slot to equip spell into, like slot 1, etc. if no slot is returned print was not able to add spell into category"
    def weapon_equip():
        "same system as above basically except it's limited to 1 slot"
        "certain class weapons have certain spells ingrained/inscribed into them"
    def armor_equip():
        "IDK YET"
    def gui():
        egg = play()
        Player.new_screen()
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
        pe.atk() if egg == "1" else (pe.run()) if egg == "2" else (pe.equip()) if egg == "3" else ((pe.items)) if egg == "4" else (Player.gui())
        return True
    def atk(self):
        pe = play()
        player_class = "Warrior"
        pe.deal_damage() if player_class == "Warrior" else(pe.heal_damage() if player_class == "Archer" else pe.deal_damage if player_class == "Mage" else(pe.deal_damage if player_class == "Assassin" else(print("ERROR: PLEASE CONTACT A DEV "))))
    def run(self):
        em = play()
        egg = False
        if em.dodge != 0:
            roll = int(100/self.dodge)
            if random.randint(1, roll) == random.randint(1, roll):
                Player.new_screen()
                print(r""" 
            ╔═════════════════════════╗
            ║     ESCAPE SUCESSFUL    ║
            ╚═════════════════════════╝
                """)
        else:
            Player.new_screen()
            print(r""" 
        ╔═════════════════════════╗
        ║      ESCAPE FAILED      ║
        ╚═════════════════════════╝
            """)  
    def equip(self):
        em = play()    
    def items(self):
        em = play()
    def default_screen():
        pass
    def new_screen():
        print(r'''
''')
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
            print("file read")
            rel.seek(0)
        with open('enemyinstance.json','w+') as icecubes:
            icecubes.write(json.dumps(egg, indent=2))
            print("file changed")
    def doge(self):
        dod = self.dodge
        egg = True
        if dod != 0:
            egg = int(100/dod)
            if random.randint(1, egg) == random.randint(1, egg):
                egg = False
        return egg
    def take_damage_enemy(self, damage):
        print('enemy_took_damage')
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
    def display(): 
        #gonna create a new index for sprites 
        pass
    def drops(self):
        loot_table = enemies1[0]['loot_table'][0]
        listed_loot_table = list(loot_table.items())
        bigjar = 0
        for i in range(len(loot_table)):
            drop_rate = listed_loot_table[bigjar][1]
            drop_name = listed_loot_table[bigjar][0]
            bigjar+=1
            prob = 100/drop_rate
            type_drop = ""
            if prob <= 100:
                type_drop = "Super Rare Drop"
            elif prob <= 1000:
                type_drop = "Crazy Rare Drop"
            if random.randint(1, int(prob)) == random.randint(1, int(prob)):
                print(f'{type_drop}! {drop_name} dropped!({drop_rate}%)')
                #trigger the put into inventory function
                #determine quantity dropped and if stackable or not
            else: 
                print("haha no loot for u")
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
                Location.location()
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
            Mapmap.display()
        else:
            print("ENEMY")
            lm.action()
            Turn.tempvar()
with open('character.json', 'r+') as awesome:
    character = json.load(awesome)
class Location():
    def location():
        current_player_location = character[0]['location']
        current_player_sublocation = character[0]['sub_location']
        print(f'Location: {current_player_location}, {current_player_sublocation}')

#once enemy is dead exi

#take enemey and player, print heir stats and whtev, then for the enemey's name we gonna take their respective sprite and put it along with them aswell. we can check if enemy dead using >< and then we can print their dead sprite
#if item drops check which slot is empty and if it is empty drop the item into there. currently only funcntions as a list/ 
def fuckery():
    var = 1
    x = 0
    elgelg = []
    for i in range(6):
        egg = inventorye[f'slot{var}'][0]['name']
        var+=1
        elgelg.append(egg)
        if elgelg[x] == 0:
            print("EMPTY")
        x+=1
def verify_usage():
    egg = input("")
    if egg == "Y":
        return True
    else:
        return False
class Main_menu():
    print("")
    def base():
        egg = int(input(""))
        Main_menu.Start_Game() if egg == "1" else Main_menu.Options() if egg == "2" else Main_menu.Exit() if egg == "3" else Main_menu.Stats() if egg == "4" else Main_menu.base()
    def Start_Game():
        #tutorial here
        print("Skip Tutorial? Y/N")
        if verify_usage() == True:
            print("Skip")
        else: 
            pass
    def Options():
        pass
    def Exit():
        pass
    def Stats():
        pass
    enemy_trigger()
    #we assign differnt functions to each nmber so that if the player goes up 
class Crafting():
    def recipes():
        pass
    def craft():
        pass
class Area_Selection():
    pass

level = 0
egg = '\t' * level
class Items():
    def map():
        item_name = Mapmap.item_pickup()
        with open('inventoryi.json') as egg:
            actualinventory = json.load(egg)
        if item_name in actualinventory:
            print("Item +1")

class Mapmap():
    item =0
    def controls():
        dimensions = Mapmap.map_boundary()
        height = dimensions[1]
        length = dimensions[0]
        Map = Mapmap.item_map()
        while True:
            print(r'''
             ''')
            print(f'x: {x}, y :{y}')
            control = input("")
            if control == 'w':
                y -= 1
                Map[y+1][x] = f'[ ]'
            elif control == 's':
                y += 1
                Map[y-1][x] = f'[ ]'
            elif control == 'a':
                x -= 1
                Map[y][x+1] = f'[ ]'
            elif control == 'd':
                x += 1
                Map[y][x-1] = f'[ ]'    
            if y == height:
                y -=1
            elif x == length:
                x -=1
            elif x == -1:
                x +=1
            elif y == -1:
                y +=1
            current_position = y, x 
            return current_position
    def map_boundary():
        map_dimensions = location['location_1'][0]['map_dimensions']
        height = map_dimensions[1]
        length = map_dimensions[0]
        if location['location_1'][0]['type'] == 'enemy':
            Mapmap.enemy_map()
        elif location['location_1'][0]['type'] == 'item':
            Mapmap.item_map()
        return length, height
    def player_spawn():
        pass
    def item_map():
        location = Location.location()
        map_dimensions = Mapmap.map_boundary()
        height = map_dimensions[1]
        length = map_dimensions[0]
        item_map = [['[ ]' for i in range(height)] for i in range(length)] 
        itemspawnx = random.randint(0, length -1)
        itemspawny = random.randint(0, height -1)
        while True: 
            item_position = item_map[itemspawny][itemspawnx]
            item_position = "[I]"
            return item_map
    def enemy_map():
        map_dimensions = Mapmap.map_boundary()  
        height = map_dimensions[1] 
        length = map_dimensions[0] 
        enemy_spawnx = random.randint(0,length - 1)
        enemy_spawny = random.randint(0,height - 1)
        x = Mapmap.controls()[1]
        y = Mapmap.controls()[0]
        item = " "
        Map = [['[ ]' for i in range(length)] for i in range(height)] 
        player_spawn = Map[y][x]
        while True:
            Map[y][x] = "[X]"
            Map[enemy_spawny][enemy_spawnx] = "[O]"
            current_position = Map[y][x]
            enemy_position = Map[enemy_spawny][enemy_spawnx]
            if current_position == enemy_position:
                Turn.determine()
            for something in Map:
                print("".join(something))  
    def item_pickup():
        item_name = 'APPLE'
        print(f'Pickup Item: {item_name}')
        print(item_name)
        pick_up = input('Y/N')
        if pick_up == 'Y':
            print(f'{item_name} picked up')
        elif pick_up == 'N':
            print('Escape')
            return item_name
#lenghth = [0], height = [1]
#possible overlap where enemies can be on top of materials such as trees or ores


egg = atte()
egg.drops()