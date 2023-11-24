import json
import os
import remove

with open("character.json", "r") as f:
    jcharacter = json.load(f)

with open("stats.json", "r") as f:
    jstats = json.load(f)

with open("role.json", "r") as f:
    jrole = json.load(f)

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
                while b == 0:
                    searchRole = input("Info for Warrior, Archer, Mage, or Assassin?: ").lower()
                    if searchRole == "warrior":
                        for i in range(len(jrole)):
                            if jrole[i]["role"].lower() == searchRole:
                                print(jrole[i])
                    elif searchRole == "archer":
                        for i in range(len(jrole)):
                            if jrole[i]["role"].lower() == searchRole:
                                print(jrole[i])
                    elif searchRole == "mage":
                        for i in range(len(jrole)):
                            if jrole[i]["role"].lower() == searchRole:
                                print(jrole[i])
                    elif searchRole == "assassin":
                        for i in range(len(jrole)):
                            if jrole[i]["role"].lower() == searchRole:
                                print(jrole[i])
                    else:
                        print("That is not a valid input.")
                    c = 0
                    while c == 0:
                        print("")
                        Choice = input("Ready to choose? Y/N: ").lower()
                        if Choice == "y":
                            c = 1
                            b = 1
                            a = 1
                        elif Choice == "n":
                            c = 1
                        else:
                            print("That is not a valid input.")
            elif searchYN == "n":
                a = 1
            else:
                print("That is not a valid input.")        
        d = 0
        while d == 0:
            role = input("Warrior, Archer, Mage, or Assassin?: ").lower()
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
    def __init__(self, id, name, role, level, story, location):
        self.id = id
        self.name = name
        self.role = role
        self.level = level
        self.story = story
        self.location = location
    def create():
        if len(jcharacter) >= 10:
            remove.Remove
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
            story = "Tutorial"
            location = "Anthill Forest"
            CreateC = CreationC(id, name, role, level, story, location)
            jcharacter.append(CreateC.__dict__)
        else:
            Id = -1

class CreationS:
    def __init__(self, id, name, exp, health, attack, dodge, defense, speed, luck, mana):
        self.id = id
        self.name = name
        self.exp = exp
        self.health = health
        self.attack = attack
        self.dodge = dodge
        self.defense = defense
        self.speed = speed
        self.luck = luck
        self.mana = mana
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
            health = jrole[roleNum]["health"]
            attack = jrole[roleNum]["attack"]
            dodge = jrole[roleNum]["dodge"]
            defense = jrole[roleNum]["defense"]
            speed = jrole[roleNum]["speed"]
            luck = jrole[roleNum]["luck"]
            mana = jrole[roleNum]["mana"]
            CreateS = CreationS(id, name, exp, health, attack, dodge, defense, speed, luck, mana)
            jstats.append(CreateS.__dict__)


new_file = "updated.json"
with open(new_file, "w") as f:

    json_string = json.dumps(jcharacter, indent=4)

    f.write(json_string)

os.remove("character.json")
os.rename(new_file, "character.json")

new_file = "updated.json"
with open(new_file, "w") as f:

    json_string = json.dumps(jstats, indent=4)

    f.write(json_string)

os.remove("stats.json")
os.rename(new_file, "stats.json")