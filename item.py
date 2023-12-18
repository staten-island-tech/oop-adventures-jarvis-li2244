import json, random

with open('inventoryi.json') as ii:
    inventi = json.load(ii)
null = None
def fucked():
    var = 1
    x = 0
    elgelg = []
    for i in range(len(inventi)):
        egg = inventi[f'slot{var}'][0]['name']
        var+=1
        elgelg.append(egg)
        if elgelg[x] == null:
            print(f'{x}'"EMPTY")
        x+=1
    print(elgelg)
    return elgelg

def put_item_in_inventory(item_name):
    egg = fucked()
    vary = 0
    null = None
    while vary != len(inventi):
        if inventi[f'slot{vary+1}'][0]['name'] == null:
            print('woah u suck at writign code')
            with open('inventoryi.json') as iii:
                inventii = json.load(iii)
                inventii[f'slot{vary+1}'][0]['name'] = item_name
            with open('inventoryi.json','w+') as i:
                i.write(json.dumps(inventii, indent = 2))
                i.seek(0)
            print(vary)
        else:
            vary += 1
            print('else')
put_item_in_inventory('cat')


def tfih():
    pass
def tfhi():
    pass
