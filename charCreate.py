from c1ass import Class

import json
import os

with open("character.json", "r") as f:
    character = json.load(f)

with open("stats.json", "r") as g:
    stats = json.load(g)

class Creation:
    def __init__(self, id, name, role, level, story, location):
        self.id = id
        self.name = name
        self.role = role
        self.level = level
        self.story = story
        self.location = location
    def create(self):
        id = Creator.cID()
        name = Creator.cName()
        role = Creator.cRole()
        level = 0
        story = "Tutorial"
        location = "Anthill Forest"
        Create = Creation(id, name, role, level, story, location)
        character.append(Create.__dict__)



class Creator:
    def cID():
        if len(character) == 0:
            id = 1
        else:
            sin = 0
            testid = 1
            while sin == 0:
                cos = 0
                for i in range(len(character)):
                    if character[i]["id"] == testid:
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
            for i in range(len(character)):
                if character[i]["name"].lower() == testname.lower():
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
                        Class.warrior()
                        Class.test()
                    elif searchRole == "archer":
                        Class.archer()
                        Class.test()
                    elif searchRole == "mage":
                        Class.mage()
                        Class.test()
                    elif searchRole == "assassin":
                        Class.assassin()
                        Class.test()
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
                Class.warrior()
                stats.append(Class.Info())
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

Creation.create()


new_file = "updated.json"
with open(new_file, "w") as f:

    json_string = json.dumps(character, indent=4)

    f.write(json_string)

os.remove("character.json")
os.rename(new_file, "character.json")


new_file2 = "updated.json"
with open(new_file2, "w") as g:

    json_string = json.dumps(stats, indent=4)

    g.write(json_string)

os.remove("stats.json")
os.rename(new_file2, "stats.json")