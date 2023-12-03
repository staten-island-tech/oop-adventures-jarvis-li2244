import json
import random
color_red = "\033[91m"
color_purple = "\33[95m"
color_blue1 = "\33[34m"
color_blue2 = "\33[36m"
color_blue3 = "\33[96m"
color_green1 = "\033[92m"
color_green2 = "\033[32m"
color_brown = "\33[33m"
color_yellow = "\33[93m"
color_grey = "\33[37m"
color_default = "\033[0m"

with open('enemies.json','r') as f:
    enemies = json.load(f)
with open('attacks.json') as i:
    attacks = json.load(i)
with open('player.json') as w:
    player = json.load(w)
#simulating player class here : this isn't going to be permanant once branches get merged, just testing 
def play():
    id = 1
    name = "pe"
    exp = 3
    stat_point = 1221342423
    max_health = 100000
    health = 90000
    attack = 7
    dodge = 8
    defense = 9
    speed = 10
    luck = 11
    mana = 12
    critchance = 100
    critdmg = 1.00
    pe = Player(id, name, exp, stat_point, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
    return pe
def atte():
    max_health = enemies['generic_enemy1'][0]['max_health']
    health = enemies['generic_enemy1'][0]['health']
    damage = enemies['generic_enemy1'][0]['damage']
    dodge = enemies['generic_enemy1'][0]['dodge']
    defense = enemies['generic_enemy1'][0]['defense']
    atkspd = enemies['generic_enemy1'][0]['atkspd']
    mana = enemies['generic_enemy1'][0]['mana']
    critchance = enemies['generic_enemy1'][0]['critchance']
    critdmg = enemies['generic_enemy1'][0]['critdmg']
    temp = Enemy(max_health, health, damage, dodge, defense, atkspd, mana, critchance, critdmg)
    return temp
class Player():
    def __init__(self, id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg):
        self.id = id
        self.name = name
        self.exp = exp
        self.stat_points = stat_points
        self.max_health = max_health
        self.health =  health
        self.attack = attack
        self.dodge = dodge
        self.defense = defense
        self.speed = speed 
        self.luck = luck
        self.mana = mana
        self.critchance = critchance
        self.critdmg = critdmg
    def critical_hit(self):
        crit = False
        roll = int(100/self.critchance)
        if random.randint(1, roll) == random.randint(1, roll):
            crit = True
        return crit
    def deal_damage(self):
        pe = play()
        crit = Player.critical_hit(pe)
        var = 0
        if crit == True:
            critical_hit = self.attack * self.critdmg
            var = critical_hit
            print("critical hit!")
        elif crit == False:
            var = self.attack
        print(var)
        return var
    def take_damage(self, damage):
        self.current_health = self.health - damage
        return self.current_health
    def heal_damage(self, heal):
        self.current_health = self.health + heal
        print(self.current_health)
        return self.current_health
    def health_display(self):
        pe = play()
        #we can prob check if the amount of characters in the healthbar is equal to 20 or whtev and if not we just add another value to the end of it
        max = self.max_health
        current = self.health
        teegreg = max/100
        max1 = max/teegreg
        current1 = current/teegreg
        print(f'{color_default}PLAYER HEALTH: {current}/{max}')
        yes_health = int(current1/5) * "█"
        no_health = int((max1 - current1)/5) * "▒"
        print(f'{color_default}╔════════════════════╗' )
        print(f'║\033[1;91;40m{yes_health}{no_health}{color_default}║')
        print(f'{color_default}╚════════════════════╝' )
    def spell(self):
        mana = self.mana
        egg = input("")
        first_spell() if egg == 1 else(second_spell() if egg == 2 else(third_spell() if egg == 3 else (fourth_spell() if egg == 4 else(print("no spell_cast")))))
        ela = player[0]['selected_spells']
        print(ela)
        def first_spell():
            egg = 1
            print("")
        def second_spell():
            egg = 1
        def third_spell():
            egg = 1
        def fourth_spell():
            egg = 1
    def spell_equip():
        "ask player what spells/attacks they would like to equip, check json file if it exists, if not print spell does not exist or not unlocked yet, if it does exist we replace the current spell selection with the new spell"
        "make sure to ask which slot to equip spell into, like slot 1, etc. if no slot is returned print was not able to add spell into category"
    def weapon_equip():
        "same system as above basically except it's limited to 1 slot"
        "certain class weapons have certain spells ingrained/inscribed into them"
class Enemy():
    def __init__(self, max_health, health, damage, dodge, defense, atkspd, mana, critchance, critdmg):
        self.max_health = max_health
        self.health = health
        self.damage = damage
        self.dodge = dodge
        self.defense = defense
        self.atkspd = atkspd
        self.mana = mana
        self.critchance = critchance
        self.critdmg = critdmg
    def deal_damage(self):
        crit = False
    def damage_take(self, damage):
        self.current_health = self.health - damage
        print(self.current_health)
    def health_heal(self, heal):
        self.current_health = self.health + heal
        print(self.current_health)
    def health_display(self):
        max = self.max_health
        current = self.health
        teegreg = max/100
        max1 =int(max/teegreg)
        current1 = int(current/teegreg)
        print(f'{color_default}PLAYER HEALTH: {current}/{max}')
        yes_health = int(current1/5) * "█"
        no_health = int((max1 - current1)/5) * "▒"
        print(f'{color_default}╔════════════════════╗' )
        print(f'║\033[1;91;40m{yes_health}{no_health}{color_default}║')
        print(f'{color_default}╚════════════════════╝' )

#somehow call var into damage positional argument
#prob a shit ton of bugs here so might wanna check this later on



ela = player[0]['selected_spells']
print(ela[0])

    #take enemey and player, print their stats and whtev, then for the enemey's name we gonna take their respective sprite and put it along with them aswell. we can check if enemy dead using >< and then we can print their dead sprite

