import json
import os
import math

#json files being altered
with open("character.json", "r") as f:
    jcharacter = json.load(f)

with open("stats.json", "r") as f:
    jstats = json.load(f)

with open("inventorys.json", "r") as f:
    jinventorys = json.load(f)

with open("inventoryq.json", "r") as f:
    jinventoryq = json.load(f)


#json files for info
with open("role.json", "r") as f:
    jrole = json.load(f)

with open("skilltree.json", "r") as f:
    jskilltree = json.load(f)

with open("skills.json", "r") as f:
    jskills = json.load(f)

with open("location.json", "r") as f:
    jlocation = json.load(f)

with open("story.json", "r") as f:
    jstory = json.load(f)

class Info:
    def roleInfo():
        print(""), print("Role Info")
        for i in jrole:
            print(i), print("")
    def skilltreeInfo():
        print(""), print("Skill Tree Info")
        for i in jskilltree:
            print(i), print("")
    def skilltreeInfo_specific(skilltree):
        h = 0
        for i in range(len(jskilltree)):
            if jskilltree[i]["skilltree"] == skilltree:
                print(""), print("Skill Tree Info")
                print(jskilltree[i]), print("")
                h = 1
        if h == 0:
            print("That Skill Tree does not exist.")
    def skillsInfo():
        print(""), print("Skills Info")
        for i in jskills:
            print(i), print("")
    def skillsInfo_specific(skill):
        h = 0
        for i in range(len(jskills)):
            if jskills[i]["name"].lower() == skill.lower():
                print(""), print("Skill Info")
                print(jskills[i]), print("")
                h = 1
        if h == 0:
            print("That skill does not exist.")    
    def locationInfo():
        print(""), print("Location Info")       
        for i in jlocation:
            print(i), print("")
    def nlocationInfo():
        for i in range(len(jcharacter)):
            if jcharacter[i]["id"] == Id:
                randvar = i
        for j in range(len(jlocation)):
            if jlocation[j]["location"] == jcharacter[randvar]["location"]:
                print(""), print(jlocation[j]["location"])
                print(jlocation[j])
    def characterInfo():
        for i in range(len(jcharacter)):
            if jcharacter[i]["id"] == Id:
                print(""), print("Character Info")
                print(jcharacter[i])
    def ncharacterInfo():
        for i in range(len(jcharacter)):
            if jcharacter[i]["id"] == Id:
                print(""), print("New Character Info")
                print(jcharacter[i])
    def statsInfo():
        for i in range(len(jstats)):
            if jstats[i]["id"] == Id:
                print(""), print("Stats Info")
                print(jstats[i])
    def nstatsInfo():
        for i in range(len(jstats)):
            if jstats[i]["id"] == Id:
                print(""), print("New Stats Info")
                print(jstats[i])
    def inventorysInfo():
        for i in range(len(jinventorys)):
            if jinventorys[i]["id"] == Id:
                print(""), print("Skill Inventory Info")
                print(jinventorys[i])
    def ninventorysInfo():
        for i in range(len(jinventorys)):
            if jinventorys[i]["id"] == Id:
                print(""), print("New Skill Inventory Info")
                print(jinventorys[i])

class Remove:
    def remove():
        if len(jcharacter) != 0:
            for i in jcharacter:
                print(i), print("")
            print("Character List is Full")
            outer = 0
            while outer == 0:
                removeBy = input("Remove by Id or Name? ('quit' to end): ").lower()
                if removeBy == "id":
                    inner1 = 0
                    while inner1 == 0:
                        IntList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                        inner1a = 0
                        removeId = input("Remove a Id: ")
                        for i in removeId:
                            if i in IntList:
                                inner1a += 1
                        if inner1a == len(removeId):
                            for i in range(len(jcharacter)):
                                if jcharacter[i]["id"] == int(removeId):
                                    inner1 = 1
                                    listNum = i
                                    break
                            if inner1 == 0:
                                print("That Id does not exist.")
                        else:
                            print("That is not a valid input.")
                    outer = 1
                elif removeBy == "name":
                    inner2 = 0
                    while inner2 == 0:
                        chooseName = input("Choose a Name: ")
                        for i in range(len(jcharacter)):
                            if jcharacter[i]["name"] == chooseName:
                                inner2 = 1
                                listNum = i
                                break
                        else:
                            print("That Name does not exist.")
                    outer = 1
                elif removeBy == "quit":
                    return "quit"
                else:
                    print("That is not a valid input.")
            removeNum = jcharacter[listNum]["id"]
            jcharacter.pop(listNum)
            for i in range(len(jstats)):
                if jstats[i]["id"] == removeNum:
                    listNum = i
                    break
            jstats.pop(listNum)
            for i in range(len(jinventorys)):
                if jinventorys[i]["id"] == removeNum:
                    listNum = i
                    break
            jinventorys.pop(listNum)
        else:
            print("There are no existing characters.")
        updateJSONC()
        updateJSONS()
        updateJSONIS()

class Creator:
    def cID():
        if len(jcharacter) == 0:
            id = 1
        else:
            sin = 0
            testid = 1
            while sin == 0:
                cos = 0
                for i in range(len(jcharacter)):
                    if jcharacter[i]["id"] == testid:
                        cos += 1
                for i in range(len(jstats)):
                    if jstats[i]["id"] == testid:
                        cos += 1
                if cos == 0:
                    sin = 1
                else:
                    testid += 1
            id = testid
        return id
    def cName():
        alpha = 0
        while alpha == 0:
            beta = 0
            testname = input("Character Name: ")
            for i in range(len(jcharacter)):
                if jcharacter[i]["name"].lower() == testname.lower():
                    beta += 1
            if testname == "quit":
                beta += 1
            if beta == 0:
                alpha = 1
            else:
                print("That name has already been taken.")
        name = testname
        return name
    def cRole():
        a = 0
        while a == 0:
            b = 0
            searchYN = input("Do you want role info? Y/N: ").lower()
            if searchYN == "y":
                Info.roleInfo()
                a = 1
            elif searchYN == "n":
                a = 1
            else:
                print("That is not a valid input.")        
        d = 0
        while d == 0:
            role = input("Role: Warrior, Archer, Mage, or Assassin?: ").lower()
            if role == "warrior":
                role = "Warrior"
                d = 1
            elif role == "archer":
                role = "Archer"
                d = 1
            elif role == "mage":
                role = "Mage"
                d = 1
            elif role == "assassin":
                role = "Assassin"
                d = 1
            else:
                print("That is not a valid input.")        
        return role
    
class CreationC:
    def __init__(self, id, name, role, level, story, location, sub_location, active_quest):
        self.id = id
        self.name = name
        self.role = role
        self.level = level
        self.story = story
        self.location = location
        self.sub_location = sub_location
        self.active_quest = active_quest
    def create():
        if len(jcharacter) >= 10:
            Remove.remove()
            updateJSONC()
        if len(jcharacter) < 10:
            print(""), print("Create New Character")        
            id = Creator.cID()
            global Id
            Id = id
            name = Creator.cName()
            global Name
            Name = name
            role = Creator.cRole()
            level = 0
            story = "Tutorial: A Hopeful Start to a Hazardous Journey"
            location = "Anthill Forest"
            sub_location = "Dense Forest"
            active_quest = "Main Story: Tutorial"
            CreateC = CreationC(id, name, role, level, story, location, sub_location, active_quest)
            jcharacter.append(CreateC.__dict__)
            updateJSONC()
        else:
            Id = -1

class CreationS:
    def __init__(self, id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg):
        self.id = id
        self.name = name
        self.stat_points = stat_points
        self.exp = exp
        self.max_health = max_health
        self.health = health
        self.attack = attack
        self.dodge = dodge
        self.defense = defense
        self.speed = speed
        self.luck = luck
        self.mana = mana
        self.critchance = critchance
        self.critdmg = critdmg

    def create():
        if Id != -1:
            id = Id
            name = Name
            for i in range(len(jcharacter)):
                if jcharacter[i]["id"] == Id:
                    Role = jcharacter[i]["role"]
            if Role == "Warrior":
                for i in range(len(jrole)):
                    if jrole[i]["role"] == Role:
                        roleNum = i
            elif Role == "Archer":
                for i in range(len(jrole)):
                    if jrole[i]["role"] == Role:
                        roleNum = i
            elif Role == "Mage":
                for i in range(len(jrole)):
                    if jrole[i]["role"] == Role:
                        roleNum = i
            elif Role == "Assassin":
                for i in range(len(jrole)):
                    if jrole[i]["role"] == Role:
                        roleNum = i
            exp = 0
            stat_points = 0
            max_health = jrole[roleNum]["max_health"]
            health = jrole[roleNum]["health"]
            attack = jrole[roleNum]["attack"]
            dodge = jrole[roleNum]["dodge"]
            defense = jrole[roleNum]["defense"]
            speed = jrole[roleNum]["speed"]
            luck = jrole[roleNum]["luck"]
            mana = jrole[roleNum]["mana"]
            critchance = 5
            critdmg = 25
            CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
            jstats.append(CreateS.__dict__)
            updateJSONS()
    
class CreationIS:
    def __init__(self, id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills):
        self.id = id
        self.name = name
        self.skill_points = skill_points
        self.Level_1_Skills = Level_1_Skills
        self.Level_2_Skills = Level_2_Skills
        self.Level_3_Skills = Level_3_Skills
        self.Level_4_Skills = Level_4_Skills
        self.Level_5_Skills = Level_5_Skills
    def create():
        id = Id
        name = Name
        skill_points = 0
        Level_1_Skills = []
        Level_2_Skills = []
        Level_3_Skills = []
        Level_4_Skills = []
        Level_5_Skills = []
        CreateIS = CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
        jinventorys.append(CreateIS.__dict__)
        updateJSONIS()

class CreationIQ:
    def __init__(self, id, name, main_quest, fight_quest, collect_quest, puzzle_quest):
        print("placeholder")

class ChooseG:
    def choose():
        if len(jcharacter) != 0:
            print(""), print("All Character Info")
            for i in jcharacter:
                print(i), print("")
            outer = 0
            while outer == 0:
                chooseBy = input("Choose by Id or Name?: ").lower()
                if chooseBy == "id":
                    inner1 = 0
                    while inner1 == 0:
                        IntList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                        inner1a = 0
                        chooseId = input("Choose a Id: ")
                        for i in chooseId:
                            if i in IntList:
                                inner1a += 1
                        if inner1a == len(chooseId):
                            for i in range(len(jcharacter)):
                                if jcharacter[i]["id"] == int(chooseId):
                                    inner1 = 1
                                    listNum = i
                                    break
                            if inner1 == 0:
                                print("That Id does not exist.")
                        else:
                            print("That is not a valid input.")
                    innerId = jcharacter[listNum]["id"]
                    innerName = jcharacter[listNum]["name"]
                    outer = 1
                elif chooseBy == "name":
                    inner2 = 0
                    while inner2 == 0:
                        chooseName = input("Choose a Name: ")
                        for i in range(len(jcharacter)):
                            if jcharacter[i]["name"] == chooseName:
                                inner2 = 1
                                listNum = i
                                break
                        else:
                            print("That Name does not exist.")
                    innerId = jcharacter[listNum]["id"]
                    innerName = jcharacter[listNum]["name"]
                    outer = 1
                else:
                    print("That is not a valid input.")
            global Id
            Id = innerId
            global Name
            Name = innerName
            Info.characterInfo()
            Info.statsInfo()    
        else:
            print("There are no existing characters.")

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
        dlevel = math.sqrt(exp)/10
        nlevel = math.floor(dlevel)
        id = Id
        name = Name
        role = jcharacter[characterNum]["role"]
        level = nlevel
        story = jcharacter[characterNum]["story"]
        location = jcharacter[characterNum]["location"]
        sub_location = jcharacter[characterNum]["sub_location"]
        active_quest = jcharacter[characterNum]["active_quest"]
        jcharacter.pop(characterNum)
        CreateC = CreationC(id, name, role, level, story, location, sub_location, active_quest)
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
            Info.nstatsInfo()
            Info.ncharacterInfo()
            Info.ninventorysInfo()

    def setStory(nstory):
        ChangeC.characterNum()
        id = Id
        name = Name
        role = jcharacter[characterNum]["role"]
        level = jcharacter[characterNum]["level"]
        story = nstory
        location = jcharacter[characterNum]["location"]
        sub_location = jcharacter[characterNum]["sub_location"]
        active_quest = jcharacter[characterNum]["active_quest"]
        jcharacter.pop(characterNum)
        CreateC = CreationC(id, name, role, level, story, location, sub_location, active_quest)
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
        active_quest = jcharacter[characterNum]["active_quest"]
        jcharacter.pop(characterNum)
        CreateC = CreationC(id, name, role, level, story, location, sub_location, active_quest)
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
        active_quest = jcharacter[characterNum]["active_quest"]
        jcharacter.pop(characterNum)
        CreateC = CreationC(id, name, role, level, story, location, sub_location, active_quest)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"] + addend
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"] - subtrahend
        critdmg = jstats[statsNum]["critdmg"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"] + addend
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        critchance = jstats[statsNum]["critchance"]
        critdmg = jstats[statsNum]["critdmg"] - subtrahend
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, stat_points, max_health, health, attack, dodge, defense, speed, luck, mana, critchance, critdmg)
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
        CreateIS = CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
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
        CreateIS = CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
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
        CreateIS = CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
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
        CreateIS = CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
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
        CreateIS = CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
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
        CreateIS = CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
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
        CreateIS = CreationIS(id, name, skill_points, Level_1_Skills, Level_2_Skills, Level_3_Skills, Level_4_Skills, Level_5_Skills)
        jinventorys.insert(inventorysNum, CreateIS.__dict__)
        updateJSONIS()
        print(f'You LEARNED "{skill}".')
        
class ActionC:
    def locationSwitch():
        ChangeC.characterNum()
        Info.locationInfo()
        outer = 0
        while outer == 0:
            inner = 0
            locationGo = input("Where do you want to go? ('quit' to end): ").lower()
            if locationGo == "quit":
                break
            for i in range(len(jlocation)):
                if jlocation[i]["location"].lower() == locationGo:
                    locationNum = i
                    for j in range(len(jstory)):
                        if jstory[j]["story"] == jlocation[i]["story"]:
                            story = jstory[j]["numEquivalent"]
                    for j in range(len(jstory)):
                        if jstory[j]["story"] == jcharacter[characterNum]["story"]:
                            storyY = jstory[j]["numEquivalent"]
                    if storyY < story:
                        print("Unable to travel: Story not advanced enough.")
                        inner = 1
                    else:
                        ChangeC.setLocation(jlocation[locationNum]["location"])
                        ChangeC.setSub_Location(jlocation[locationNum]["center sub_location"])
                        updateJSONC()
                        Info.nlocationInfo()
                        Info.ncharacterInfo()
                        outer = 1
                        inner = 1
            if inner == 0:
                print("That location does not exist.")

    def sub_locationSwitch():
        ChangeC.characterNum()
        Info.nlocationInfo()
        for i in range(len(jlocation)):
            if jlocation[i]["location"] == jcharacter[characterNum]["location"]:
                locationNum = i
        sub_locations = []
        list_stuff = []
        for i in jlocation[locationNum]:
            list_stuff.append(i)
        for i in range(4):
            for j in jlocation[locationNum][list_stuff[-(i + 1)]]:
                sub_locations.append(j.lower())
        outer = 0
        while outer == 0:
            print(""), print("Sub Locations")
            print(sub_locations)
            sub_locationGo = input("Where do you want to go? ('quit' to end): ").lower()
            if sub_locationGo == "quit":
                break
            else:
                if sub_locationGo in sub_locations:
                    ChangeC.setSub_Location(sub_locationGo.title())
                    updateJSONC()
                    Info.ncharacterInfo()
                    outer = 1
                else:
                    print("That sub_location does not exist.")

class ActionS:
    def stat_pointsSpend(stat_points):
        ChangeS.statsNum()
        Info.statsInfo()
        if stat_points > jstats[statsNum]["stat_points"]:
            print(""), print("You do not have that many stat points.")
            print(f'Stat Points: {jstats[statsNum]["stat_points"]}')
        else:
            outer = 0
            while outer == 0:
                statUpgraded = input("Use stat points on Max_Health, Attack, Defense, Speed, or Mana: ").lower()
                if statUpgraded == "max_health" or "maxhealth" or "max health":
                    ChangeS.stat_pointsSubtract(stat_points)
                    ChangeS.max_healthAdd(stat_points)
                    ChangeS.healthAdd(stat_points)
                    outer = 1
                elif statUpgraded == "attack":
                    ChangeS.stat_pointsSubtract(stat_points)
                    ChangeS.attackAdd(stat_points)
                    outer = 1
                elif statUpgraded == "defense":
                    ChangeS.stat_pointsSubtract(stat_points)
                    ChangeS.defenseAdd(stat_points)
                    outer = 1
                elif statUpgraded == "speed":
                    ChangeS.stat_pointsSubtract(stat_points)
                    ChangeS.speedAdd(stat_points)
                    outer = 1
                elif statUpgraded == "mana":
                    ChangeS.stat_pointsSubtract(stat_points)
                    ChangeS.manaAdd(stat_points)
                    outer = 1
                else:
                    print("That is not a valid input.")
            updateJSONS()
            Info.nstatsInfo()

class ActionIS:
    def skill_pointsSpend():
        ChangeC.characterNum()
        ChangeIS.inventorysNum()
        role = jcharacter[characterNum]["role"]
        for i in range(len(jrole)):
            if jrole[i]["role"] == role:
                skilltree = jrole[i]["skilltree"]
        for i in range(len(jskilltree)):
            if jskilltree[i]["skilltree"] == skilltree:
                skilltreeY = jskilltree[i]
                print(""), print("Skill Tree Info")
                print(skilltreeY)
        Info.inventorysInfo()
        print("")
        print(f'Skill Points: {jinventorys[inventorysNum]["skill_points"]}')        
        skill_points = jinventorys[inventorysNum]["skill_points"]
        outer = "n"
        while outer == "n":
            inner = 0
            skillBuy = input("What skill would you like to purchase? ('quit' to end): ").lower()
            if skillBuy == "quit":
                break
            for i in skilltreeY:
                for j in skilltreeY[i]:
                    if len(j) > 1:
                        if skillBuy.lower() == j.lower():
                            inner += 1
                            for k in range(len(jskills)):
                                if jskills[k]["name"].lower() == skillBuy:
                                    skillY = jskills[k]
            if inner == 0:
                print("That skill does not exist.")
            else:
                Info.skillsInfo_specific(skillBuy)
                outin = 0
                while outin == 0:
                    confirm = input("Are you sure you want to purchase this skill? Y/N: ").lower()
                    if confirm == "y":
                        outer = "y"
                        outin = 1
                    elif confirm == "n":
                        outer ="n"
                        outin = 1
                    else:
                        print("That is not a valid input.")
        if skillBuy != "quit":
            if skillY["cost"] > skill_points:
                print(""), print("You do not have enough skill points.")
                print(f'Skill Points: {jinventorys[inventorysNum]["skill_points"]}')
            else:
                inner2 = 0
                for i in jinventorys[inventorysNum]:
                    if i == "id":
                        donothing = 0
                    elif i == "skill_points":
                        donothing = 0
                    else:
                        for j in jinventorys[inventorysNum][i]:
                            if skillBuy == j.lower():
                                print("You already own that skill.")
                                inner2 += 1
            if inner2 == 0:
                ChangeIS.skill_pointsSubtract(skillY["cost"])
                if skillY["level"] == "Level_1_Skills":
                    ChangeIS.InsertLevel_1_Skills(skillY["name"])
                elif skillY["level"] == "Level_2_Skills":
                    ChangeIS.InsertLevel_2_Skills(skillY["name"])
                elif skillY["level"] == "Level_3_Skills":
                    ChangeIS.InsertLevel_3_Skills(skillY["name"])
                elif skillY["level"] == "Level_4_Skills":
                    ChangeIS.InsertLevel_4_Skills(skillY["name"])
                elif skillY["level"] == "Level_5_Skills":
                    ChangeIS.InsertLevel_5_Skills(skillY["name"])
                else:
                    print("Unknown Error")
                updateJSONIS()
                Info.ninventorysInfo()



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

ChooseG.choose()
ActionC.sub_locationSwitch()