#from charCreate.py import CharCreator 


class Class():

    def archer():
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
        skillTree = "Sniper"
    def mage():
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
        skillTree = "Berserker"
    def warrior():
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
        skillTree = "Berserker"
    def assassin():
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
        skillTree = "Berserk"
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
    def test():
        print(f'Health: {health}, Attack: {attack}, Dodge Rate: {dodge}, Defense: {defense}, Attack Speed: {atkspd}, Luck: {luck}, Mana: {mana}, Skill Tree: {skillTree}')




