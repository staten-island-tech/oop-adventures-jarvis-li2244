import time
import sys
import json
from methods import Modified_Functions
with open('inventorye.json')  as eq:
    equips  = json.load(eq)
with open('inventoryi.json') as inv:
    invent = json.load(inv)
with open('item.json') as us:
    item = json.load(us)
def dialogue():
    with open('dialogue.json') as dialogu:
        dialogue = json.load(dialogu)
    for i, (v, k) in enumerate(dialogue.items()):
        for i in range(len(k)):
            Modified_Functions.delay_print(k[i])
            input()
            print('''''')
    