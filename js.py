import json
import os

with open("character.json", "r") as f:
    jcharacter = json.load(f)

with open("stats.json", "r") as f:
    jstats = json.load(f)

with open("role.json", "r") as f:
    jrole = json.load(f)

    
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