import random
import time
import json

with open('enemies.json','r') as f:
    data = json.load(f)

ehealth = data['generic_enemy1'][0]['health']
edamage = data['generic_enemy1'][0]['damage']
edodge = data['generic_enemy1'][0]['dodge']
edefense = data['generic_enemy1'][0]['defense']
eatkspd = data['generic_enemy1'][0]['atkspd']
emana = data['generic_enemy1'][0]['mana']
ectch= data['generic_enemy1'][0]['critchance']
ecrit = data['generic_enemy1'][0]['critdmg']
temphealth = ehealth
pot = 10
take_dmg = True
atk = 100




class Damage():
    def reg():
        egg = 1
    def defense():
        dmgtk = atk * edefense * 0.01
        tempvar = atk - dmgtk
        hp = ehealth - tempvar
        print(hp)
class Dodge():
    def dodge():
        for i in range(edodge):
                x = random.randint(0, 100)
                if x == random.randint(0,100):
                    print("DODGED")
                    break
class Mana():
    place_mana = emana
    spell_cast = True
    spell_cost = 10

    if spell_cast == True and emana != 0:
        print("Spell Cast")
        print(f'- {spell_cost}')
        mana1 = emana - spell_cost
        emana = mana1
        print(f'current mana: {mana1}')
        while emana != place_mana:
            time.sleep(1.0)
            print("+1 Mana")
            emana += 1 
            print(emana)
    elif emana == 0:
        print("no mana")
    

class action():
    def test():
        if take_dmg == True and edefense != 0:
            Damage.defense()
            




