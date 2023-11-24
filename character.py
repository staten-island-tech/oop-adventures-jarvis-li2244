import json
import os
import create
from choose import *

with open("character.json", "r") as f:
    jcharacter = json.load(f)

with open("stats.json", "r") as f:
    jstats = json.load(f)

with open("role.json", "r") as f:
    jrole = json.load(f)

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
        CreateC = create.CreationC(id, name, role, level, story, location)
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
        CreateC = create.CreationC(id, name, role, level, story, location)
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
        CreateC = create.CreationC(id, name, role, level, story, location)
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
        CreateC = create.CreationC(id, name, role, level, story, location)
        jcharacter.insert(characterNum, CreateC.__dict__)
        print("New Character Info:")
        print(jcharacter[characterNum])

ChooseC.choose()    
ChangeC.setLocation("OOOOscar Room")


new_file = "updated.json"
with open(new_file, "w") as f:

    json_string = json.dumps(jcharacter, indent=4)

    f.write(json_string)

os.remove("character.json")
os.rename(new_file, "character.json")