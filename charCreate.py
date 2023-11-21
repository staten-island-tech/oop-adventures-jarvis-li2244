from role import Class

import json
import os

with open("character.json", "r") as f:
    character = json.load(f)


class CreationC:
    def __init__(self, id, name, role, level, story, location):
        self.id = id
        self.name = name
        self.role = role
        self.level = level
        self.story = story
        self.location = location
    def create():
        id = Creator.cID()
        global ID
        ID = id
        name = Creator.cName()
        role = Creator.cRole()
        global ROLE
        ROLE = role
        level = 0
        story = "Tutorial"
        location = "Anthill Forest"
        CreateC = CreationC(id, name, role, level, story, location)
        character.append(CreateC.__dict__)

class CreationS:
    def __init__(self, id, health, attack, dodge, defense, atkspd, luck, mana):
        self.id = id
        self.health = health
        self.attack = attack
        self.dodge = dodge
        self.defense = defense
        self.atkspdd = atkspd
        self.luck = luck
        self.mana = mana
    def create():
        id = ID
        if ROLE == "Warrior":
            Class.warrior()
        elif ROLE == "Archer":
            Class.archer()
        elif ROLE == "Mage":
            Class.mage()
        elif ROLE == "Assassin":
            Class.assassin()
        y = Class.Info()
        health = y[0]
        attack = y[1]
        dodge = y[2]
        defense = y[3]
        atkspd = y[4]
        luck = y[5]
        mana = y[6]
        CreateS = CreationS(id, health, attack, dodge, defense, atkspd, luck, mana)
        character.append(CreateS.__dict__)

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
CreationS.create()


new_file = "updated.json"
with open(new_file, "w") as f:

    json_string = json.dumps(character, indent=4)

    f.write(json_string)

os.remove("character.json")
os.rename(new_file, "character.json")


