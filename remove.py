import json
import os

with open("character.json", "r") as f:
    jcharacter = json.load(f)

with open("stats.json", "r") as f:
    jstats = json.load(f)

with open("role.json", "r") as f:
    jrole = json.load(f)

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

Remove.remove()

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