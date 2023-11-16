#dodge 
import time
import random 


time.sleep()


health = 0
damage = 0
dodge = 0
defense = 0
atkspd = 0
luck = 0
mana = 0


class Dodge():
    if dodge != 0: 
        for i in range(dodge):
            x = random.randint(0, 100)
            if x == random.randint(0,100):
                print("DODGED")
    elif dodge == 0:
        print("no dodge")

#health
class Health():
    health =  100
    damage = 10
    damage_taken = True
    if damage_taken == True:
         x = health - damage 
         print(x)

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
        spell_cast = True
        spell_cost = 10
        if spell_cast == True:
            print("Spell Cast")
            print("-" +spell_cost+ "Mana")
            mana = mana - spell_cost
            print("current mana: " + mana + "")



