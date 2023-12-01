import json
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
        damage = enemies['generic_enemy1'][0]['damage']
        dodge = enemies['generic_enemy1'][0]['dodge']
        defense = enemies['generic_enemy1'][0]['defense']
        atkspd = enemies['generic_enemy1'][0]['atkspd']
        mana = enemies['generic_enemy1'][0]['mana']
        critchance = enemies['generic_enemy1'][0]['critchance']
        critdmg = enemies['generic_enemy1'][0]['critdmg']
        w = (health, damage, dodge, defense, atkspd, mana, critchance, critdmg)
        w.register()
    def health_display(self):
        max = self.health
        current = 80
        print(f'ENEMY HEALTH: {current}/{max}')
        yes_health = int(current/5) * "█"
        no_health = int((max - current)/5) * "▒"
        print(f'\033[1;{x};40m{yes_health}{no_health}\n')
Enemy.health_display(self)