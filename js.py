import json
import os
import math

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