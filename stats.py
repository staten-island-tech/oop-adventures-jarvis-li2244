import json
import os


from character import Id, Name, Role


with open("character.json", "r") as f:
    jcharacter = json.load(f)

with open("stats.json", "r") as f:
    jstats = json.load(f)

with open("role.json", "r") as f:
    jrole = json.load(f)

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
        id = Id
        name = Name
        for i in range(len(jcharacter)):
            if jcharacter[i]["id"] == id:
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

CreationS.create()
def function():
    from character import RemoveC
    RemoveC.remove()
    from character import removeNum
function()

new_file = "updated.json"
with open(new_file, "w") as f:

    json_string = json.dumps(jstats, indent=4)

    f.write(json_string)

os.remove("stats.json")
os.rename(new_file, "stats.json")