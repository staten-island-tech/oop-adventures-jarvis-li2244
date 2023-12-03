import json
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


class Enemy():
    def __init__(self, health, damage, dodge, defense, atkspd, mana, critchance, critdmg):
        self.health = health
        self.damage = damage
        self.dodge = dodge
        self.defense = defense
        self.atkspd = atkspd
        self.mana = mana
        self.critchance = critchance
        self.critdmg = critdmg
    def register():
        health = enemies['generic_enemy1'][0]['health']
        current_health = health
        damage = enemies['generic_enemy1'][0]['damage']
        dodge = enemies['generic_enemy1'][0]['dodge']
        defense = enemies['generic_enemy1'][0]['defense']
        atkspd = enemies['generic_enemy1'][0]['atkspd']
        mana = enemies['generic_enemy1'][0]['mana']
        critchance = enemies['generic_enemy1'][0]['critchance']
        critdmg = enemies['generic_enemy1'][0]['critdmg']
        w = (health, damage, dodge, defense, atkspd, mana, critchance, critdmg)
        w.register()

    def health_display(max, current):
        x = 91
        health_dis = 0
        teegreg = max/100
        max1 =int(max/teegreg)
        current1 = int(current/teegreg)
        print(f'{color_default}ENEMY HEALTH: {current}/{max}')
        yes_health = int(current1/5) * "█"
        no_health = int((max1 - current1)/5) * "▒"

        #print(f'{color_default}╔════════════════════╗' )
        print(f'\033[1;{x};40m{yes_health}{no_health}{color_default}')
        #print(f'{color_default}╚════════════════════╝' )

health = 1003984798473598
chealth = 339873498747771
Enemy.health_display(health, chealth )