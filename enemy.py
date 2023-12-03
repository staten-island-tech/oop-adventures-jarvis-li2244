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
#simulating player class here : this isn't going to be permanant once branches get merged, just testing 
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
    def crit(self):
        critical = False
        roll = 100/self.critchance
        if random.randint(1, roll) == random.randint(1, roll):
            critical = True
        return critical
    def deal_damage(self):
        crit = Player.crit()
        var = 0
        if crit == True:
            critical_hit = self.dmg * self.critdmg
            var = critical_hit
            print("critical hit!")
        elif crit == False:
            var = self.attack
        return var
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
    def damage_take(self, damage):
        self.current_health = self.health - damage
        print(self.current_health)
    def health_heal(self, heal):
        self.current_health = self.health + heal
        print(self.current_health)
def play():
    id = 1
    name = 2
    exp = 3
    stat_point = 4
    max_health = 5
    health = 6
    attack = 7
    dodge = 8
    defense = 9
    speed = 10
    luck = 11
    mana = 12
    critchance = 100
    critdmg = 14
    pe = Player(id, name, exp, stat_point, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
    return pe
def atte():
    elf = play()
    egg = elf.deal_damage()
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
    temp.damage_take(egg)

#somehow call var into damage positional argument
#prob a shit ton of bugs here so might wanna check this later on
atte()

"""  def health_display(self):
        max = self.healthd
        current = current_health(self)
        teegreg = max/100
        max1 =int(max/teegreg)
        current1 = int(current/teegreg)
        print(f'{color_default}ENEMY HEALTH: {current}/{max}')
        yes_health = int(current1/5) * "█"
        no_health = int((max1 - current1)/5) * "▒"
        #print(f'{color_default}╔════════════════════╗' )
        print(f'\033[1;91;40m{yes_health}{no_health}{color_default}')
        #print(f'{color_default}╚════════════════════╝' )"""


    #take enemey and player, print their stats and whtev, then for the enemey's name we gonna take their respective sprite and put it along with them aswell. we can check if enemy dead using >< and then we can print their dead sprite

