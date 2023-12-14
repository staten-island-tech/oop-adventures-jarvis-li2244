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
        # do exp display here
#list of known bugs currently(repport bugs here) : health_bar display gets fucked over when the value gets rounded down weird(not resolved yet)
#healing overflow(resolved) 
#once enemy reaches a certain point it ends up trying to focus everything on healing itself and ends up not attacking, 
with open('locationenemy.json') as fifa:
    location = json.load(fifa)
with open('enemyinstance.json','r+')as f:
    enemies1 = json.load(f)
with open('attacks.json') as i:
    attacks = json.load(i)
with open('player.json') as w:
    player = json.load(w)
with open('inventorye.json') as el:
    inventorye = json.load(el)
with open('character.json') as elf:
    character = json.load(elf)
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
    max_health = enemies['generic_enemy1'][0]['max_health']
    health = enemies['generic_enemy1'][0]['health']
    damage = enemies['generic_enemy1'][0]['damage']
    dodge = enemies['generic_enemy1'][0]['dodge']
    defense = enemies['generic_enemy1'][0]['defense']
    mana = enemies['generic_enemy1'][0]['mana']
    critchance = enemies['generic_enemy1'][0]['critchance']
    critdmg = enemies['generic_enemy1'][0]['critdmg']
    speed = enemies['generic_enemy1'][0]['speed']
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
        damage_dealt_player = 0
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
                return False
            else:
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
    def modify(change, var, mode):
        with open('player.json', 'r+') as r:
            unique_variable = json.load(r)
        if mode == 'set':
            unique_variable[0][f'{var}'] = change
        elif mode == 'add':
            unique_variable[0][f'{var}'] += change
        elif mode == 'subtract':
            unique_variable[0][f'{var}'] -= change
        with open('player.json','w') as i:
            i.write(json.dumps(unique_variable))
            i.seek(0)
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
        player_class = character[0]['role']
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
        healthjson = eggd['generic_enemy1'][0]['health']
        pe = atte()
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
                print(f'health damage{self.health}')
        if healthjson <= 0 or self.health <= 0:
            Enemy.health_modify(0)
        else:
            Enemy.health_modify(self.health)
        return self.health
    def health_heal(self):
        en = atte()
        heal = 10
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
        healthjson = ide['generic_enemy1'][0]['health']
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
    def health_modify(health_change):
        with open('enemyinstance.json', 'r+') as r:
            egg = json.load(r)
            egg['generic_enemy1'][0]['health'] = health_change
        with open('enemyinstance.json','w') as i:
            i.write(json.dumps(egg))
            i.seek(0)
    def action(self):
        egg = atte()
        print("ATTACK")
        if self.health < self.max_health/2:
            roll = int(100/self.dodge)
            if random.randint(1, roll) == random.randint(1, roll):
                egg.health_heal()
        else: 
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
        pass
class Turn():
    def determine():
        psp = player[0]['speed']
        esp = enemies1['generic_enemy1'][0]['speed']
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
            eaf2 = enemies1['generic_enemy1'][0]['health']
            if eaf2 <= 0:
                    exp_drop = enemies1['generic_enemy1'][0]['exp']
                    print("ENEMY DEAD")
                    print(f'EXP DROPPED : {exp_drop}')
                    new_exp = player[0]['exp'] + exp_drop
                    Player.modify(new_exp, 'exp', 'set')
                    Levels.current_exp()
            else:
                    print("ENEMY")
                    Enemy.enemy_show()
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
START = input("")
if START != "0":
    Turn.determine()
#take enemey and player, print heir stats and whtev, then for the enemey's name we gonna take their respective sprite and put it along with them aswell. we can check if enemy dead using >< and then we can print their dead sprite
#if item drops check which slot is empty and if it is empty drop the item into there. currently only funcntions as a list/ 
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
print(elgelg)
class Main_menu():
    print("")
    def base():
        egg = int(input(""))
        Main_menu.Start_Game() if egg == "1" else Main_menu.Options() if egg == "2" else Main_menu.Exit() if egg == "3" else Main_menu.Stats() if egg == "4" else Main_menu.base()
    def Start_Game():
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
class Spawn():
    def enemy_name():
        enemy_list = []
        test = len(location['location_1'][0]['enemies'])
        numbers = 0
        for i in range(test):
            enemy_name = location['location_1'][0]['enemies'][numbers][f'{numbers}'][0]['name']
            numbers += 1
            enemy_list.append(enemy_name)
        return enemy_list
    def spawn():
        names = Spawn.enemy_name()
        print(names[0])
class Area_Selection():
    pass
Spawn.spawn()

level = 0
egg = '\t' * level
class Map():
    map_dimensions = location['location_1'][0]['map_dimensions']
    length = map_dimensions[0]
    height = map_dimensions[1]
    liste = []
    area = length * height
    for i in range(area):
        liste.append([])
    print(liste)
    
    tiles = len(liste) - 1
    #grid size
    randomizer = random.randint(1, tiles) 
    liste[randomizer] = 1
            #x = 0    x = 1     x = 2     x = 3     x = 4 
    for i in range(length):
        for i in range(length):
            print(liste[length - 1])
        length +=1
    print(f'''
            {liste[0]}{liste[1]}{liste[2]}{liste[3]}{liste[4]}
            {liste[5]}{liste[6]}{liste[7]}{liste[8]}{liste[9]}
            {liste[10]}{liste[11]}{liste[12]}{liste[13]}{liste[14]}
            {liste[15]}{liste[16]}{liste[17]}{liste[18]}{liste[19]}
            {liste[20]}{liste[21]}{liste[22]}{liste[23]}{liste[24]}

            ''')
    space = 1
    player_occupied =  1
    enemy_occupied = 2
    if player_occupied != space:
        space = "YAY " 
#lenghth = [0], height = [1]
#possible overlap where enemies can be on top of materials such as trees or ores
