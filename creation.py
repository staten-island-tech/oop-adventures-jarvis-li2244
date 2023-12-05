import json
import os
import math
import remove

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
        for i in range(len(jlocation)):
            if i == jcharacter[randvar]["location"]:
                print(jlocation[i])
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
    def __init__(self, id, name, role, level, story, location, sub_location):
        self.id = id
        self.name = name
        self.role = role
        self.level = level
        self.story = story
        self.location = location
        self.sub_location = sub_location
    def create():
        if len(jcharacter) >= 10:
            remove.Remove.remove()
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
            CreateC = CreationC(id, name, role, level, story, location, sub_location)
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