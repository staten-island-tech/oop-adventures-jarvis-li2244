import json
import os

with open("data.json", "r") as f:
    data = json.load(f)

class CharCreation:
    def __init__(self, id, name, role, story, location):
        self.id = id
        self.name = name
        self.role = role
        self.story = story
        self.location = location
    def create():
        id = Creator.cID()
        name = Creator.cName()
        role = Creator.cRole()
        story = "Tutorial"
        location = "Anthill Forest"
        Create = CharCreation(id, name, role, story, location)
        data.append(Create.__dict__)

class Creator:
    def cID():
        if len(data) == 0:
            id = 1
        else:
            sin = 0
            testid = 1
            while sin == 0:
                cos = 0
                for i in range(len(data)):
                    if data[i]["id"] == testid:
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
            for i in range(len(data)):
                if data[i]["name"].lower() == testname.lower():
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
                        print("Role Stats")
                        # print form a list of info of roles
                    elif searchRole == "archer":
                        print("Role Stats")
                    elif searchRole == "mage":
                        print("Role Stats")
                    elif searchRole == "assassin":
                        print("Role Stats")
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
        role = input("Warrior, Archer, Mage, or Assassin?: ")
        return role


CharCreation.create()


new_file = "updated.json"
with open(new_file, "w") as f:

    json_string = json.dumps(data, indent=4)

    f.write(json_string)

os.remove("data.json")
os.rename(new_file, "data.json")
