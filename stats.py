#dodge 
import random 
class Dodge():
    dodge = 100
    if dodge != 0: 
        for i in range(dodge):
            x = random.randint(0, 100)
            if x == 39:
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

class Defense():
    defense = 100
    health = 100
    damage_taken = True
    damage = 10
    if damage_taken == True:
        x = defense * 0.03 
        y = damage * x
        print(health - x)

class Wisdom():
    mana = 100
    spell_cast = True
    spell_cost = 10
    if spell_cast == True:
        print("Spell Cast")
        print("-" +spell_cost+ "Mana")
        mana = mana - spell_cost
        print("current mana: " + mana + "")
