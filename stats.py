#dodge 
import time
import random 


role = 1
class Enemy:
    def __init__(self, health, damage, dodge, defense, atkspd, mana, ctch, crit, luck ):
        self.health = health
        self.damage = damage 
        self.dodge = dodge
        self.defense = defense
        self.takspd = atkspd
        self.mana = mana
        self.ctch = ctch
        self.crit = crit
        self.luck = luck
    def statselect():
        if role == "Warrior":
            hp = 100
            dmg = 100
            edodge = 0
            edefense = 10
            eatkspd = 100
            emana = 0
            ectch = 1
            ecrit = 100
            luck = 0
            x = Enemy(hp, dmg, edodge, edefense, eatkspd, emana, ectch, ecrit, luck)
            x.register()
    

health = 0
damage = 1
dodge = 100
defense = 0
atkspd = 0
luck = 0
mana = 100
mana2 = 100
ctch= 100
crit = 10




class Dodge():
    def doge():
        if dodge != 0: 
            for i in range(dodge):
                x = random.randint(0, 100)
                if x == random.randint(0,100):
                    print("DODGED")
                    break
        elif dodge == 0:
            print("no dodge")


class Take_Damage():
    def dmg():
        edmg = 100 
        damage_taken = True
        if damage_taken == True:
            x = defense * 0.03 
            y = edmg * x
            print(health - x)

class MANA():
    def spellcasting(): 
        place_mana = mana2
        spell_cast = True
        spell_cost = 10
        if spell_cast == True:
            print("Spell Cast")
            print(f'- {spell_cost}')
            global mana
            mana1 = mana - spell_cost
            mana = mana1
            print(f'current mana: {mana1}')
            while mana != place_mana:
                time.sleep(1.0)
                print("+1 Mana")
                mana += 1 
                print(mana)

class CC():
    def trigger():
        if ctch != 0:
            CC.chance()
        else:
            print("no crit chance ")
    def chance():
        for i in range(ctch):
            x = random.randint(1,100)
            if x == random.randint(1, 100):
                    CC.crit_trigger()
                    break
    def crit_trigger():
        cd = crit * damage
        print(cd)
        print("CRIT!")

class Enemy_Stats():
    class Atk():
        def meelee():
            if 
        def ranged():
        def magic():
        



