import json
import os
import math
import choose
import creation
from creation import Id, Name

#json files being altered
with open("character.json", "r") as f:
    jcharacter = json.load(f)

with open("stats.json", "r") as f:
    jstats = json.load(f)

with open("inventorys.json", "r") as f:
    jinventorys = json.load(f)


#json files for info
with open("role.json", "r") as f:
    jrole = json.load(f)

with open("skilltree.json", "r") as f:
    jskilltree = json.load(f)

with open("skills.json", "r") as f:
    jskills = json.load(f)

with open("location.json", "r") as f:
    jlocation = json.load(f)



class ChangeC:
    def characterNum():
        for i in range(len(jcharacter)):
            if jcharacter[i]["id"] == Id:
                global characterNum
                characterNum = i  

    def setLevel():
        ChangeC.characterNum()
        for i in range(len(jstats)):
            if jstats[i]["id"] == Id:
                exp = jstats[i]["exp"]
        olevel = jcharacter[characterNum]["level"]
        dlevel = math.sqrt(exp)
        nlevel = math.floor(dlevel)
        id = Id
        name = Name
        role = jcharacter[characterNum]["role"]
        level = nlevel
        story = jcharacter[characterNum]["story"]
        location = jcharacter[characterNum]["location"]
        sub_location = jcharacter[characterNum]["sub_location"]
        jcharacter.pop(characterNum)
        CreateC = creation.CreationC(id, name, role, level, story, location, sub_location)
        jcharacter.insert(characterNum, CreateC.__dict__)
        updateJSONC()
        if olevel != nlevel:
            diff = nlevel - olevel 
            addskillpts = 0
            addstatpts = diff * 2
            for i in range(diff):
                olevel += 1
                if olevel % 5 == 0:
                    if olevel <= 50:
                        addskillpts += 1
                    elif olevel >= 55:
                        addskillpts += 2
            print(""), print(f'You LEVELED up {diff} time(s)! Level {nlevel}')
            ChangeIS.skill_pointsAdd(addskillpts)
            ChangeS.stat_pointsAdd(addstatpts)
            ChangeS.max_healthAdd(diff)
            ChangeS.healthAdd(diff)    
            ChangeS.attackAdd(diff)
            ChangeS.defenseAdd(diff)
            ChangeS.speedAdd(diff)
            ChangeS.manaAdd(diff)
            creation.Info.nstatsInfo()
            creation.Info.ncharacterInfo()
            creation.Info.ninventorysInfo()

    def setStory(nstory):
        ChangeC.characterNum()
        id = Id
        name = Name
        role = jcharacter[characterNum]["role"]
        level = jcharacter[characterNum]["level"]
        story = nstory
        location = jcharacter[characterNum]["location"]
        sub_location = jcharacter[characterNum]["sub_location"]
        jcharacter.pop(characterNum)
        CreateC = creation.CreationC(id, name, role, level, story, location, sub_location)
        jcharacter.insert(characterNum, CreateC.__dict__)
        print(""), print(nstory)
        updateJSONC()

    def setLocation(nlocation):
        ChangeC.characterNum()
        id = Id
        name = Name
        role = jcharacter[characterNum]["role"]
        level = jcharacter[characterNum]["level"]
        story = jcharacter[characterNum]["story"]
        location = nlocation
        sub_location = jcharacter[characterNum]["sub_location"]
        jcharacter.pop(characterNum)
        CreateC = creation.CreationC(id, name, role, level, story, location, sub_location)
        jcharacter.insert(characterNum, CreateC.__dict__)
        print(""), print(nlocation)
        updateJSONC()
    
    def setSub_Location(nsub_location):
        ChangeC.characterNum()
        id = Id
        name = Name
        role = jcharacter[characterNum]["role"]
        level = jcharacter[characterNum]["level"]
        story = jcharacter[characterNum]["story"]
        location = jcharacter[characterNum]["location"]
        sub_location = nsub_location
        jcharacter.pop(characterNum)
        CreateC = creation.CreationC(id, name, role, level, story, location, sub_location)
        jcharacter.insert(characterNum, CreateC.__dict__)
        print(""), print(nsub_location)
        updateJSONC()

class ChangeS:
    def statsNum():
        for i in range(len(jstats)):
            if jstats[i]["id"] == Id:
                global statsNum
                statsNum = i

    def expAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"] + addend
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You GAINED {addend} experience.')
    
    def stat_pointsAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"] + addend
        max_health = jstats[statsNum]["max_health"] 
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You GAINED {addend} stat point(s).')

    def stat_pointsSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"] - subtrahend
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You LOST {subtrahend} stat point(s).')

    def max_healthAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"] + addend
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You GAINED {addend} max health.')
    
    def max_healthSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"] - subtrahend
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You LOST {subtrahend} max health.')

    def healthAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"] + addend
        if health > max_health:
            health = max_health
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You GAINED {addend} health.')

    def healthSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"] - subtrahend
        if health < 0:
            health = 0
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You LOST {subtrahend} health.')

    def attackAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"] + addend
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You GAINED {addend} attack.')

    def attackSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"] - subtrahend
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You LOST {subtrahend} attack.')
    
    def dodgeAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"] + addend
        if dodge > 30:
            dodge = 30
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You GAINED {addend} dodge.')
    
    def dodgeSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"] - subtrahend
        if dodge < 0:
            dodge = 0
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You LOST {subtrahend} dodge.')

    def defenseAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"] 
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"] + addend
        if defense > 100:
            defense = 100
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You GAINED {addend} defense.')
    
    def defenseSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"] - subtrahend
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You LOST {subtrahend} defense.')

    def speedAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"] + addend
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You GAINED {addend} speed.')

    def speedSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"] - subtrahend
        if speed < 0:
            speed = 0
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You LOST {subtrahend} speed.')

    def luckAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"] 
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"] + addend
        if luck > 10:
            luck = 10
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You GAINED {addend} luck.')

    def luckSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"] - subtrahend
        if luck < 0:
            luck = 0
        mana = jstats[statsNum]["mana"]
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You LOST {subtrahend} luck.')

    def manaAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"] + addend
        if mana > 200:
            mana = 200
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You GAINED {addend} mana.')

    def manaSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"] - subtrahend
        if mana < 0:
            mana = 0
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You LOST {subtrahend} mana.')

    def critchanceAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]  
        critchance = jrole[statsNum]["critchance"] + addend
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You GAINED {addend} crit chance.')        

    def critchanceSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]  
        critchance = jrole[statsNum]["critchance"] - subtrahend
        critdmg = jrole[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You LOST {subtrahend} crit chance.')        

    def critdmgAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]  
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"] + addend
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You GAINED {addend} crit damage.')        
    
    def critdmgSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        stat_points = jstats[statsNum]["stat_points"]
        max_health = jstats[statsNum]["max_health"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]  
        critchance = jrole[statsNum]["critchance"]
        critdmg = jrole[statsNum]["critdmg"] - subtrahend
        jstats.pop(statsNum)
        CreateS = creation.CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        print(f'You LOST {subtrahend} crit damage.')        

class ChangeIS:
    def inventorysNum():
        for i in range(len(jinventorys)):
            if jinventorys[i]["id"] == Id:
                global inventorysNum
                inventorysNum = i  
    def skill_pointsAdd(addend):
        ChangeIS.inventorysNum()
        id = Id
        name = Name
        skill_points = jinventorys[inventorysNum]["skill_points"] + addend
        Level_1_Skills = jinventorys[inventorysNum]["Level_1_Skills"]
        Level_2_Skills = jinventorys[inventorysNum]["Level_2_Skills"]
        Level_3_Skills = jinventorys[inventorysNum]["Level_3_Skills"]
        Level_4_Skills = jinventorys[inventorysNum]["Level_4_Skills"]
        Level_5_Skills = jinventorys[inventorysNum]["Level_5_Skills"]
        jinventorys.pop(inventorysNum)
        CreateIS = creation.CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
        jinventorys.insert(inventorysNum, CreateIS.__dict__)
        updateJSONIS()
        print(f'You GAINED {addend} skill point(s).')        

    def skill_pointsSubtract(subtrahend):
        ChangeIS.inventorysNum()
        id = Id
        name = Name
        skill_points = jinventorys[inventorysNum]["skill_points"] - subtrahend
        Level_1_Skills = jinventorys[inventorysNum]["Level_1_Skills"]
        Level_2_Skills = jinventorys[inventorysNum]["Level_2_Skills"]
        Level_3_Skills = jinventorys[inventorysNum]["Level_3_Skills"]
        Level_4_Skills = jinventorys[inventorysNum]["Level_4_Skills"]
        Level_5_Skills = jinventorys[inventorysNum]["Level_5_Skills"]
        jinventorys.pop(inventorysNum)
        CreateIS = creation.CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
        jinventorys.insert(inventorysNum, CreateIS.__dict__)
        updateJSONIS()
        print(f'You LOST {subtrahend} skill point(s).')

    def InsertLevel_1_Skills(skill):
        ChangeIS.inventorysNum()
        id = Id
        name = Name
        skill_points = jinventorys[inventorysNum]["skill_points"]
        Level_1_Skills = jinventorys[inventorysNum]["Level_1_Skills"]
        Level_1_Skills.append(skill)
        Level_2_Skills = jinventorys[inventorysNum]["Level_2_Skills"]
        Level_3_Skills = jinventorys[inventorysNum]["Level_3_Skills"]
        Level_4_Skills = jinventorys[inventorysNum]["Level_4_Skills"]
        Level_5_Skills = jinventorys[inventorysNum]["Level_5_Skills"]
        jinventorys.pop(inventorysNum)
        CreateIS = creation.CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
        jinventorys.insert(inventorysNum, CreateIS.__dict__)
        updateJSONIS()
        print(f'You LEARNED "{skill}".')
        
    def InsertLevel_2_Skills(skill):
        ChangeIS.inventorysNum()
        id = Id
        name = Name
        skill_points = jinventorys[inventorysNum]["skill_points"]
        Level_1_Skills = jinventorys[inventorysNum]["Level_1_Skills"]
        Level_2_Skills = jinventorys[inventorysNum]["Level_2_Skills"]
        Level_2_Skills.append(skill)
        Level_3_Skills = jinventorys[inventorysNum]["Level_3_Skills"]
        Level_4_Skills = jinventorys[inventorysNum]["Level_4_Skills"]
        Level_5_Skills = jinventorys[inventorysNum]["Level_5_Skills"]
        jinventorys.pop(inventorysNum)
        CreateIS = creation.CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
        jinventorys.insert(inventorysNum, CreateIS.__dict__)
        updateJSONIS()
        print(f'You LEARNED "{skill}".')
        
    def InsertLevel_3_Skills(skill):
        ChangeIS.inventorysNum()
        id = Id
        name = Name
        skill_points = jinventorys[inventorysNum]["skill_points"]
        Level_1_Skills = jinventorys[inventorysNum]["Level_1_Skills"]
        Level_2_Skills = jinventorys[inventorysNum]["Level_2_Skills"]
        Level_3_Skills = jinventorys[inventorysNum]["Level_3_Skills"]
        Level_3_Skills.append(skill)
        Level_4_Skills = jinventorys[inventorysNum]["Level_4_Skills"]
        Level_5_Skills = jinventorys[inventorysNum]["Level_5_Skills"]
        jinventorys.pop(inventorysNum)
        CreateIS = creation.CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
        jinventorys.insert(inventorysNum, CreateIS.__dict__)
        updateJSONIS()
        print(f'You LEARNED "{skill}".')
        
    def InsertLevel_4_Skills(skill):
        ChangeIS.inventorysNum()
        id = Id
        name = Name
        skill_points = jinventorys[inventorysNum]["skill_points"]
        Level_1_Skills = jinventorys[inventorysNum]["Level_1_Skills"]
        Level_2_Skills = jinventorys[inventorysNum]["Level_2_Skills"]
        Level_3_Skills = jinventorys[inventorysNum]["Level_3_Skills"]
        Level_4_Skills = jinventorys[inventorysNum]["Level_4_Skills"]
        Level_4_Skills.append(skill)
        Level_5_Skills = jinventorys[inventorysNum]["Level_5_Skills"]
        jinventorys.pop(inventorysNum)
        CreateIS = creation.CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
        jinventorys.insert(inventorysNum, CreateIS.__dict__)
        updateJSONIS()
        print(f'You LEARNED "{skill}".')
        
    def InsertLevel_5_Skills(skill):
        ChangeIS.inventorysNum()
        id = Id
        name = Name
        skill_points = jinventorys[inventorysNum]["skill_points"]
        Level_1_Skills = jinventorys[inventorysNum]["Level_1_Skills"]
        Level_2_Skills = jinventorys[inventorysNum]["Level_2_Skills"]
        Level_3_Skills = jinventorys[inventorysNum]["Level_3_Skills"]
        Level_4_Skills = jinventorys[inventorysNum]["Level_4_Skills"]
        Level_5_Skills = jinventorys[inventorysNum]["Level_5_Skills"]
        Level_5_Skills.append(skill)
        jinventorys.pop(inventorysNum)
        CreateIS = creation.CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
        jinventorys.insert(inventorysNum, CreateIS.__dict__)
        updateJSONIS()
        print(f'You LEARNED "{skill}".')
        


def updateJSONC():
    new_file = "updated.json"
    with open(new_file, "w") as f:

        json_string = json.dumps(jcharacter, indent=4)

        f.write(json_string)

    os.remove("character.json")
    os.rename(new_file, "character.json")

def updateJSONS():
    new_file = "updated.json"
    with open(new_file, "w") as f:

        json_string = json.dumps(jstats, indent=4)

        f.write(json_string)

    os.remove("stats.json")
    os.rename(new_file, "stats.json")

def updateJSONIS():
    new_file = "updated.json"
    with open(new_file, "w") as f:

        json_string = json.dumps(jinventorys, indent=4)

        f.write(json_string)

    os.remove("inventorys.json")
    os.rename(new_file, "inventorys.json")

choose.ChooseC.choose()
ChangeC.setStory("stratyd")