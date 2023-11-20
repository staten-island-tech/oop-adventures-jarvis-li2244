#from charCreate.py import CharCreator 


class Class():

    def archer():
        global exp
        exp = 0
        global health
        health = 100
        global attack
        attack = 10
        global dodge
        dodge = 0
        global defense
        defense = 10
        global atkspd
        atkspd = 1
        global luck
        luck = 1
        global mana
        mana = 1
        global skillTree
        skillTree = "Placeholder"
    def mage():
        global exp
        exp = 0
        global health
        health = 100
        global attack
        attack = 10
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
        global skillTree
        skillTree = "Placeholder"
    def warrior():
        global exp
        exp = 0
        global health
        health = 1
        global attack
        attack = 100
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
        global skillTree
        skillTree = "Placeholder"
    def assassin():
        global exp
        exp = 0
        global health
        health = 1
        global attack
        attack = 100
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
        global skillTree
        skillTree = "Placeholder"
    def opt():
        class_select = input("CLASS: ")
        if class_select == "archer":
            Class.archer()
        if class_select == "assassin":
            Class.assassin()
        if class_select == "warrior":
            Class.warrior()
        if class_select == "mage":
            Class.mage()
    def Info():
        x = (f'Health: {health}, Attack: {attack}, Dodge Rate: {dodge}, Defense: {defense}, Attack Speed: {atkspd}, Luck: {luck}, Mana: {mana}, Skill Tree: {skillTree}')
        print(x)
        return exp, health, attack, dodge, defense, atkspd, luck, mana




