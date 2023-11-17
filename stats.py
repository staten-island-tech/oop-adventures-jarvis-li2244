#dodge 
import time
import random 





health = 0
damage = 0
dodge = 0
defense = 0
atkspd = 0
luck = 0
mana = 100


class Dodge():
    if dodge != 0: 
        for i in range(dodge):
            x = random.randint(0, 100)
            if x == random.randint(0,100):
                print("DODGED")
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
        place_mana = 100
        spell_cast = True
        spell_cost = 10
        if spell_cast == True:
            print("Spell Cast")
            print(f'"-" {spell_cost} "Mana"')
            mana1 = mana - spell_cost
            mana = mana1
            print(f'"current mana: " {mana1} ""')
            while mana != place_mana:
                time.sleep(1.0)
                print("+1 Mana")
                mana += 1 
                if place_mana == mana:
                    print("MANA FULL")

                    
                

MANA.spellcasting()

