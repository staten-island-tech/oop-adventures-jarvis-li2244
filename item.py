import json, random

with open('inventoryi.json') as ii:
    inventir = json.load(ii)

with open('item.json') as falafel:
    item = json.load(falafel)

null = None


def stim_opt():
    pass
def update_json(item_stats, module):
    new_value = list(item_stats.items())
    egg = 0
    for i in range(len(item_stats)):
        stat_name = new_value[egg][0]
        stat_item = new_value[egg][1]
        modify(stat_item, stat_name, f'{module}')
        egg +=1
        #this da format: item[0][f'{name}'][0]['stats'][0] for item stats
    #figure out how iterate through the list
def put_slotin_inventory(item_name, quantity):
    vary = 0
    null = None
    while vary != len(inventir):
        with open('inventoryi.json') as finale:
            inventi = json.load(finale)
        if inventi[f'slot{vary+1}'][0]['name'] == null:
            print('woah u suck at writign code')
            with open('inventoryi.json') as iii:
                inventii = json.load(iii)
                inventii[f'slot{vary+1}'][0]['name'] = item_name
                inventii[f'slot{vary+1}'][0]['quantity'] = quantity
            with open('inventoryi.json','w+') as i:
                i.write(json.dumps(inventii, indent = 2))
                i.seek(0)
            print(vary)
            break
        else:
            vary += 1
            print('else')

def modify(change, var, mode):
    with open('player.json', 'r+') as r:
        unique_variable = json.load(r)
    if mode == 'set':
        unique_variable[0][f'{var}'] = change
    elif mode == 'add':
        unique_variable[0][f'{var}'] += change
    elif mode == 'subtract':
        unique_variable[0][f'{var}'] -= change
    elif mode == 'append':
        unique_variable[0][f'{var}'].append(change)
    with open('player.json','w+') as i:
        i.write(json.dumps(unique_variable, indent = 2))
        i.seek(0)
def page_scroll():
    numpad = input()
    loste = []
    fur = ['1', '2', '3']
    if numpad not in fur:
        page_scroll()
    else:
        max_range = int(numpad) * 10 + 1
        lowest_range = max_range - 10
        for i in range(10):
            loste.append(lowest_range)
            lowest_range += 1
    return loste
def inventory():
    page = page_scroll()
    pravda = ['<',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print(f'''
             INVENTORY 
══════════════════════════════════
{page[0]}.  {inventir[f'slot{page[0]}'][0]['name']}    {pravda[0]}                         
══════════════════════════════════
{page[1]}.  {inventir[f'slot{page[1]}'][0]['name']}    {pravda[1]}                        
══════════════════════════════════
{page[2]}.  {inventir[f'slot{page[2]}'][0]['name']}    {pravda[2]}
══════════════════════════════════
{page[3]}.  {inventir[f'slot{page[3]}'][0]['name']}    {pravda[3]}
══════════════════════════════════
{page[4]}.  {inventir[f'slot{page[4]}'][0]['name']}    {pravda[4]}                     
══════════════════════════════════
{page[5]}.  {inventir[f'slot{page[5]}'][0]['name']}    {pravda[5]}                          
══════════════════════════════════
{page[6]}.  {inventir[f'slot{page[6]}'][0]['name']}    {pravda[6]}
══════════════════════════════════
{page[7]}.  {inventir[f'slot{page[7]}'][0]['name']}    {pravda[7]}
══════════════════════════════════
{page[8]}.  {inventir[f'slot{page[8]}'][0]['name']}    {pravda[8]} 
══════════════════════════════════
{page[9]}.  {inventir[f'slot{page[9]}'][0]['name']}    {pravda[9]} 
══════════════════════════════════
              <- - ->
''')
    potatojam = input()
    print(inventir[f'slot{potatojam}'][0]['name'])
def verify_usage():
    egg = input("")
    if egg == "Y":
        return True
    else:
        return False
def item_usage():
    #idk
    inventory()
    print("Scroll up and Down Using")
    eralt = input("")
    name = inventir[f'slot{eralt}'][0]['name']
    item_stats = item[0][f'{name}'][0]['stats'][0]
    if name == null:
        print("Nothing to see here")
    elif name != null:
        print(item_stats)
        if item[0][f'{name}'][0]['type'] == "consumable":
            print("Use item?")
            if verify_usage() == True:
                update_json(name, item_stats, 'add')
        elif item[0][f'{name}'][0]['type'] == "weapon_sword":
            print("Equip Item?")
            if verify_usage() == True:
                update_json(name, item_stats, 'add')
def item_unusage():
    lemfa = input("")
    if lemfa not in inventir: 
        print("ni")
    elif lemfa in inventir:
        #put the check function here later, too lazy to write 
        print("Unequip?")
        equp = input()
        if equp == True:
            print("Unequiped")
            update_json("false", "stat_items ", 'subtract')
def fish():
    pass
def piie():
    pass

item_usage()