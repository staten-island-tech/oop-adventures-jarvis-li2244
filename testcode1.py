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
            print(''' ''')
def equip_function():
    pass
@Modified_Functions.timing
def piie():
    item_name = Modified_Functions.proper_input('str')
    for i,(k, v) in enumerate(invent.items()):
        if item_name != v[0]['name']:
            continue
        print('item found')
        for i2,(k2,v2) in enumerate(item[0].items()):
            if item_name != k2:
                continue
            for i3, (v3,k3) in enumerate(equips.items()):
                if k3[0]['type'] != v2[0]['type']:
                    continue
                print('yay')
                equips[f'slot{i3+1}'][0]['name'] = item_name
                equips[f'slot{i3+1}'][0]['quantity'] = 1
                with open('inventorye.json', 'w+') as outl:
                    outl.write(json.dumps(equips, indent = 2))
                #parse stat modifier here or smth
            break
def un_piie():
    item_name = Modified_Functions.proper_input('str')
    for i,(k, v) in enumerate(equips.items()):
        if item_name != v[0]['name']:
            continue
        options = Modified_Functions.proper_input('str')
        if options == 'unequip':
            equips[f'slot{i+1}'][0]['name'] = 0
            equips[f'slot{i+1}'][0]['quantity'] = None
        elif options == 'destroy':
            equips[f'slot{i+1}'][0]['name'] = 0
            equips[f'slot{i+1}'][0]['quantity'] = None
        with open('inventorye.json', 'w+') as nuance:
            nuance.write(json.dumps(equips, indent=2))

piie()
