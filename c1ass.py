#from charCreate.py import CharCreator 

class_select = input("CLASS: ")
class Class():

    def archer():
        global health
        health = 100
        global damage
        damage = 10
        global dodge
        dodge = 0
        global defense
        defense = 10
        global atkspd
        atkspd = 1.00
        global luck
        luck = 1
        global mana
        mana = 1
    def mage():
        global health
        health = 100
        global damage
        damage = 10
        global dodge
        dodge = 3
        global defense
        defense = 1
        global atkspd
        atkspd = 1
        global luck
        luck = 1 
        global mana
        mana = 1
    def warrior():
        global health
        health = 1
        global damage
        damage = 100
        global dodge
        dodge = 3
        global defense
        defense = 1
        global atkspd
        atkspd = 1
        global luck
        luck = 1 
        global mana
        mana = 1 
    def assassin():
        global health
        health = 1
        global damage
        damage = 100
        global dodge
        dodge = 3
        global defense
        defense = 1
        global atkspd
        atkspd = 1
        global luck
        luck = 1 
        global mana
        mana = 1
    def opt():
        if class_select == "archer":
            Class.archer()
        if class_select == "assassin":
            Class.assassin()
        if class_select == "warrior":
            Class.warrior()
        if class_select == "mage":
            Class.mage()
    def test():
        print(health, damage, dodge, defense, atkspd, luck, mana)




