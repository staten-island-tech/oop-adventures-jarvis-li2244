#dodge 
import time
import random 


class stats_enemy ():
    atk = 1
class stats_player():
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

class Enemy_Stats_health():
    class Atk():
        def meelee():
            if attack == 'meelee'
        def ranged():
        def magic():
        

Enemy_Stats_health.Atk()

