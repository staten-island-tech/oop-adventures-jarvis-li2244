import time
import sys
import json
with open('inventorye.json')  as eq:
    equips  = json.load(eq)
with open('inventoryi.json') as inv:
    invent = json.load(inv)
with open('item.json') as us:
    item = json.load(us)
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
def timing(func):
    def tim():
        start_time = time.time()
        func()
        time_run = time.time() - start_time
        print(f'{time_run} seconds to run')
    return tim
@timing
def dialogue():
    with open('dialogue.json') as dialogu:
        dialogue = json.load(dialogu)
    for i, (v, k) in enumerate(dialogue.items()):
        for i in range(len(k)):
            delay_print(k[i])
            input()
            print(''' ''')
def equip_function():
    pass
def proper_input(type):
    while True:
        try:
            if type == 'int':   
                anput = int(input())
            elif type == 'str':
                anput = str(input())
            return anput
        except:
            print("Enter a valid input please")
@timing
def piie():
    item_name = proper_input('str')
    for i,(k, v) in enumerate(invent.items()):
        if item_name == v[0]['name']:
            print('item found')
            for i2,(k2,v2) in enumerate(item[0].items()):
                if item_name == k2:
                    type = v2[0]['type']
                    for i3, (v3,k3) in enumerate(equips.items()):
                        if k3[0]['type'] == v2[0]['type']:
                            print('yay')
                            equips[f'slot{i3+1}'][0]['name'] = item_name
                            with open('inventorye.json', 'w+') as outl:
                                outl.write(json.dumps(equips, indent = 2))
            break
        else:
            print('item not in inventory, please enter a valid item')
piie()
