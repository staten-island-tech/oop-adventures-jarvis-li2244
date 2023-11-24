
import json
import os


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
        
    def Info():
        x = (f'Health: {health}, Attack: {attack}, Dodge Rate: {dodge}, Defense: {defense}, Attack Speed: {atkspd}, Luck: {luck}, Mana: {mana}, Skill Tree: {skillTree}')
        print(x)        
        y = [health, attack, dodge, defense, atkspd, luck, mana]
        return y
    def returnS():
        y = [health, attack, dodge, defense, atkspd, luck, mana]
        return y



with open("character.json", "r") as f:
    jcharacter = json.load(f)
    
import choose
import character
character.ChangeC.setLocation("Oscar's Room")


    
new_file = "updated.json"
with open(new_file, "w") as f:

    json_string = json.dumps(jcharacter, indent=4)

    f.write(json_string)

os.remove("character.json")
os.rename(new_file, "character.json")
