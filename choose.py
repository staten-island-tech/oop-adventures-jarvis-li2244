import json
import os
import math
import creation

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


class ChooseC:
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
            creation.Info.characterInfo()
            creation.Info.statsInfo()    
        else:
            print("There are no existing characters.")

    
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