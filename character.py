import json
import os

with open("character.json", "r") as f:
    jcharacter = json.load(f)

with open("stats.json", "r") as f:
    jstats = json.load(f)

with open("role.json", "r") as f:
    jrole = json.load(f)

class CreationC:
    def __init__(self, id, name, role, level, story, location):
        self.id = id
        self.name = name
        self.role = role
        self.level = level
        self.story = story
        self.location = location
    def create():
        while len(jcharacter) >= 10:
            RemoveC.remove()        
        id = Creator.cID()
        global Id
        Id = id
        name = Creator.cName()
        global Name
        Name = name
        role = Creator.cRole()
        global Role
        Role = role
        level = 0
        story = "Tutorial"
        location = "Anthill Forest"
        CreateC = CreationC(id, name, role, level, story, location)
        jcharacter.append(CreateC.__dict__)

class RemoveC:
    def remove():
        if len(jcharacter) != 0:
            for i in jcharacter:
                print(i), print("")
            outer = 0
            while outer == 0:
                removeBy = input("Remove by Id or Name?: ").lower()
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
                    jcharacter.pop(listNum)
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
                    global removeNum
                    removeNum = listNum
                    jcharacter.pop(listNum)
                    outer = 1
                else:
                    print("That is not a valid input.")
        else:
            print("There are no existing characters.")

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

CreationC.create()

class ChooseC:
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
            print(""), print("Character Info:")
            print(jcharacter[listNum])
        else:
            print("There are no existing characters.")

class ChangeC:
    def characterNum():
        for i in range(len(jcharacter)):
            if jcharacter[i]["id"] == Id:
                global characterNum
                characterNum = i  

    def change():
        ChangeC.characterNum()
        for i in range(len(jcharacter)):
            if jcharacter[i]["id"] == Id:
                characterNum = i
        id = Id
        name = Name
        role = jcharacter[characterNum]["role"]
        level = jcharacter[characterNum]["level"]
        story = jcharacter[characterNum]["story"]
        location = jcharacter[characterNum]["location"]
        jcharacter.pop(characterNum)
        CreateC = CreationC(id, name, role, level, story, location)
        jcharacter.insert(characterNum, CreateC.__dict__)

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
        print("New Character Info:")
        print(jcharacter[characterNum])

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
        print("New Character Info:")
        print(jcharacter[characterNum])

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
        print("New Character Info:")
        print(jcharacter[characterNum])

#ChooseC.choose()    
#ChangeC.setStory("Chapter 3: The Spark of a Rebellion")


new_file = "updated.json"
with open(new_file, "w") as f:

    json_string = json.dumps(jcharacter, indent=4)

    f.write(json_string)

os.remove("character.json")
os.rename(new_file, "character.json")