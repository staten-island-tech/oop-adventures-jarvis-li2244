import time
import sys
import json
from methods import Modified_Functions as mod
with open('inventorye.json')  as eq:
    equips  = json.load(eq)
with open('inventoryi.json') as inv:
    invent = json.load(inv)
with open('item.json') as us:
    item = json.load(us)
with open('character.json') as infile:
    character = json.load(infile)

