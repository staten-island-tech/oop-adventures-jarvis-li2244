import json
import os

with open("character.json", "r") as f:
    jcharacter = json.load(f)

with open("stats.json", "r") as f:
    jstats = json.load(f)

with open("role.json", "r") as f:
    jrole = json.load(f)

class Info:
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
        else:
            print("There are no existing characters.")
        updateJSONC()
        updateJSONS()

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
            Remove.remove()
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
            updateJSONC()
        else:
            Id = -1

class CreationS:
    def __init__(self, id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana):
        self.id = id
        self.name = name
        self.exp = exp
        self.maxhealth = maxhealth
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
            maxhealth = jrole[roleNum]["maxhealth"]
            health = jrole[roleNum]["health"]
            attack = jrole[roleNum]["attack"]
            dodge = jrole[roleNum]["dodge"]
            defense = jrole[roleNum]["defense"]
            speed = jrole[roleNum]["speed"]
            luck = jrole[roleNum]["luck"]
            mana = jrole[roleNum]["mana"]
            CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
            jstats.append(CreateS.__dict__)
            updateJSONS()
    
class Choose:
    def choose():
        if len(jcharacter) != 0:
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
        dlevel = exp/100 
        nlevel = int(dlevel)
        id = Id
        name = Name
        role = jcharacter[characterNum]["role"]
        level = nlevel
        story = jcharacter[characterNum]["story"]
        location = jcharacter[characterNum]["location"]
        jcharacter.pop(characterNum)
        CreateC = CreationC(id, name, role, level, story, location)
        jcharacter.insert(characterNum, CreateC.__dict__)
        updateJSONC()
        Info.ncharacterInfo()

    def setLocation(nlocation):
        ChangeC.characterNum()
        id = Id
        name = Name
        role = jcharacter[characterNum]["role"]
        level = jcharacter[characterNum]["level"]
        story = jcharacter[characterNum]["story"]
        location = nlocation
        jcharacter.pop(characterNum)
        CreateC = CreationC(id, name, role, level, story, location)
        jcharacter.insert(characterNum, CreateC.__dict__)
        updateJSONC()
        Info.ncharacterInfo()

    def setStory(nstory):
        ChangeC.characterNum()
        id = Id
        name = Name
        role = jcharacter[characterNum]["role"]
        level = jcharacter[characterNum]["level"]
        story = nstory
        location = jcharacter[characterNum]["location"]
        jcharacter.pop(characterNum)
        CreateC = CreationC(id, name, role, level, story, location)
        jcharacter.insert(characterNum, CreateC.__dict__)
        updateJSONC()
        Info.ncharacterInfo()

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
        maxhealth = jstats[statsNum]["maxhealth"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()

    def maxhealthAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"] + addend
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()
    
    def maxhealthSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"] - subtrahend
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()

    def healthAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"]
        health = jstats[statsNum]["health"] + addend
        if health > maxhealth:
            health = maxhealth
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()

    def healthSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"]
        health = jstats[statsNum]["health"] - subtrahend
        if health < 0:
            health = 0
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()

    def attackAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"] + addend
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()

    def attackSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"] - subtrahend
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()
    
    def dodgeAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"] + addend
        if dodge > 30:
            dodge = 30
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()
    
    def dodgeSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"] - subtrahend
        if dodge < 0:
            dodge = 0
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()

    def defenseAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"] 
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"] + addend
        if defense > 100:
            defense = 100
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()
    
    def defenseSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"] - subtrahend
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()

    def speedAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"] + addend
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()

    def speedSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"] - subtrahend
        if speed < 0:
            speed = 0
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()

    def luckAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"] 
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"] + addend
        if luck > 10:
            luck = 10
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()

    def luckSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"] - subtrahend
        if luck < 0:
            luck = 0
        mana = jstats[statsNum]["mana"]
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()

    def manaAdd(addend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"] + addend
        if mana > 200:
            mana = 200
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()

    def manaSubtract(subtrahend):
        ChangeS.statsNum()
        id = Id
        name = Name
        exp = jstats[statsNum]["exp"]
        maxhealth = jstats[statsNum]["maxhealth"]
        health = jstats[statsNum]["health"]
        attack = jstats[statsNum]["attack"]
        dodge = jstats[statsNum]["dodge"]
        defense = jstats[statsNum]["defense"]
        speed = jstats[statsNum]["speed"]
        luck = jstats[statsNum]["luck"]
        mana = jstats[statsNum]["mana"] - subtrahend
        if mana < 0:
            mana = 0
        jstats.pop(statsNum)
        CreateS = CreationS(id, name, exp, maxhealth, health, attack, dodge, defense, speed, luck, mana)
        jstats.insert(statsNum, CreateS.__dict__)
        updateJSONS()
        Info.nstatsInfo()





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

