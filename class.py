#from charCreate.py import CharCreator 

class_select = input("CLASS: ")


class Class():

    def archer():
        print("health = 100")
        damage = 100
        dodge = 3
        defense = 1
        atkspd = 1
        luck = 1 
        wisdom = 1
    def mage():
        health = 100 
        damage = 100
        dodge = 0
        defense = 1
        atkspd = 1
        luck = 1 
        wisdom = 1 
    def warrior():
        health = 100 
        damage = 100
        dodge = 0
        defense = 1
        atkspd = 1
        luck = 1 
        wisdom = 1        
    def assassin():
        health = 100 
        damage = 100
        dodge = 0
        defense = 1
        atkspd = 1
        luck = 1 
        wisdom = 1
    
    def opt():
        if class_select == "archer":
            Class.archer
        if class_select == "assassin":
            Class.assassin()
        if class_select == "warrior":
            Class.warrior()
        if class_select == "mage":
            Class.mage()
    


Class.opt()
