import json
import os

class CharCreation:
    def __init__(self, id, name, role):
        self.id = id
        self.name = name
        self.role = role


with open("data.json", "r") as f:
    data = json.load(f)

def create():
    id = int(input("ID: "))
    name = input("Character Name: ")
    role = input("Chracter Role: ")
    Create = CharCreation(id, name, role)
    data.append(Create.__dict__)
create()


new_file = "updated.json"
with open(new_file, "w") as f:

    json_string = json.dumps(data, indent=4)

    f.write(json_string)

os.remove("data.json")
os.rename(new_file, "data.json")
