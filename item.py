import json, random, copy, time, sys
from methods import Modified_Functions
module = Modified_Functions
with open('inventoryi.json') as ii:
    inventir = json.load(ii)
with open('item.json') as falafel:
    item = json.load(falafel)
with open('inventorye.json') as illager:
    inverter = json.load(illager)
with open('recipes.json') as f:
    recipes = json.load(f)
with open('character.json') as infile:
    character = json.load(infile)
null = None

currentdict = recipes[0]['item_1'][0]['items_needed']
class Inventory():
    def update_json(item_name, item_stats, module, amount_used):
        new_value = list(item_stats.items())
        egg = 0
        if item[0][f'{item_name}'][0]['stackable'] == False:
            print('unstackable')
        elif inventir[0][f'{item_name}'][0]['stackable'] == True:
            item_stats = item_stats * amount_used 
            print('stacking')
        for i in range(len(item_stats)):
            stat_name = new_value[egg][0]
            stat_item = new_value[egg][1]
            Inventory.modify(stat_item, f'{stat_name}', f'{module}')
            egg += 1
            #this da format: item[0][f'{name}'][0]['stats'][0] for item stats
        #figure out how iterate through the list
    def inventory_update(item_name, slot_num, mode, item_amount):
        with open('inventoryi.json')  as finale:
            inventi = json.load(finale)
            if mode == 'add':
                inventi[f'{slot_num}'][0]['quantity'] += item_amount
                print(inventi[f'{slot_num}'][0]['quantity'])
            elif mode == 'subtract':
                inventi[f'{slot_num}'][0]['quantity'] -= item_amount
                print(inventi[f'{slot_num}'][0]['quantity'])
                if inventi[f'{slot_num}'][0]['quantity'] <= 0:
                    inventi[f'{slot_num}'][0]['quantity'] = 0
                    inventi[f'{slot_num}'][0]['name'] = None
            else:
                print('else')
                inventi[f'{slot_num}'][0]['name'] = item_name
                inventi[f'{slot_num}'][0]['quantity'] = item_amount
        with open('inventoryi.json', 'w+') as fermi:
            fermi.write(json.dumps(inventi, indent=2)) 
            fermi.seek(0)
    def psi(item_name, quantity, mode):
        with open('inventoryi.json') as finsi:
            inventiro = json.load(finsi)
        for i, (k, v) in enumerate(inventiro.items()):
            if item_name == v[0]['name']:
                egg = True
                break 
            else:
                egg = False
        for i2, (k2, v2) in enumerate(inventiro.items()):
            if egg == False:
                if v2[0]['name'] == null:
                    Inventory.inventory_update(item_name, k2, 'placeholdernone', quantity)
                    break
            elif egg == True:
                if mode == 'subtract':
                    Inventory.inventory_update(item_name, k, 'subtract' , quantity)
                elif mode == 'add':
                    Inventory.inventory_update(item_name, k, 'add', quantity)
                break
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
        asf = []
        null = None
        with open('inventoryi.json')  as test:
            inventoryi = json.load(test)
        for i, (k, v) in enumerate(inventoryi.items()):
            if v[0]['name'] != null:
                asf.append(v[0]['name'])
        if len(asf) < 36:
            for i in range(36-len(asf)):
                asf.append("")
        print(asf)
        return asf
    def inventory_display():
        indel = Inventory.page_scroll()
        print('ENTER PAGE TO SCROLL TO: ')
        pagenum = module.proper_input('int') * 9 - 9
        print(r'''
                INVENTORY 
    ''', end='')
        for i in range(9):
            print(f'''
    ══════════════════════════════════
    {i+1}. {indel[pagenum]}''', end='')
            pagenum+=1
        print(f'''
    ══════════════════════════════════
    ''')
        inventory_actions = module.proper_input('str')
        if inventory_actions == 'exit':
            pass
            #put open_menu() here
        elif inventory_actions == 'item_select':
            print('ENTER ITEM NAME')
            item_name = module.proper_input('str')
            if item_name in indel:
                action = module.proper_input('str')
                if action == 'equip':
                    Inventory.equip(item_name)
                elif action == 'use':
                    Inventory.actual_item_usage(item_name)
            else:
                print('PLEASE ENTER AN ACTUAL ITEM')
                Inventory.inventory_display()
    def verify_usage():
        egg = input("")
        if egg == "Y":
            return True
        else:
            return False
    def item_usage():
        with open('inventoryi.json')  as test:
            inventoryi = json.load(test)
        Inventory.inventory_display()
        print('To open inventory again enter open')
        while True:
            if module.proper_input('str') == 'open':
                Inventory.inventory_display()
            else:
                break 
        item =  module.proper_input('str')
        for i, (k,v) in enumerate(inventoryi.items()):
            if v['name'] != item:
                continue
            else:
                Inventory.actual_item_usage()
                break
        Inventory.item_usage()
    def actual_item_usage(item_name):
        for i,(k, v) in enumerate(item[0].item()):
            if item_name == v['name']:
                if v['type'] == 'consumable':
                    Inventory.modify(v['stats'][0]['health'], 'health', 'add')
                elif v['type'] == 'boots' or v['type'] == 'chestplate' or v['type'] ==  'leggings' or v['type'] == 'helmet' or v['type'] == 'weapon':
                    Inventory.equip(item_name)
        #menu here
    def equip(item_name):
        for i,(k, v) in enumerate(item[0].items()):
            if item_name == k: 
                if Inventory.check_slot(v[0]['type']) == False:
                    print('Slot currently has item equipped')
                    break
                else:
                    for index, (key,value) in enumerate(v[0]['stats'][0].items()):
                        print(key, value)
                        Inventory.modify(value, key, 'add')
                        with open('inventoryi.json') as infile:
                            inventoryi=  json.load(infile)
                    break
    def check_slot(slot):
        with open('inventorye.json') as infile:
            inventorye  = json.load(infile)
        for i,(k, v) in enumerate(inventorye.items()):
            if v[0]['type'] == slot:
                if v[0]['name'] == null:
                    return True
                else:
                    return False
    def unequip():
        item_name = module.proper_input('str')
        mode = module.proper_input('str')
        while mode != 'destroy' or mode != 'unequip':
            mode = module.proper_input('str')
        for i,(k, v) in enumerate(item[0].item()):
            if item_name == v['name']: 
                for index, (key,value) in enumerate(v[0]['stats'][0].items()):
                    Inventory.modify[value, key, 'subtract']
                Inventory.un_piie(item_name, mode)
                break
    def un_piie(item_name, mode):
        for i,(k, v) in enumerate(inverter.items()):
            if item_name == v[0]['name']:
                continue
            if mode == 'unequip':
                inverter[f'slot{i+1}'][0]['name'] = 0
                inverter[f'slot{i+1}'][0]['quantity'] = None
                Inventory.psi(item_name, 1 ,'')
            elif mode == 'destroy':
                inverter[f'slot{i+1}'][0]['name'] = 0
                inverter[f'slot{i+1}'][0]['quantity'] = None
            with open('inventorye.json', 'w+') as nuance:
                nuance.write(json.dumps(inverter, indent=2))
    def piie():
        item_name = module.proper_input('str')
        for i,(k, v) in enumerate(inventir.items()):
            if item_name != v[0]['name']:
                continue
            print('item found')
            for i2,(k2,v2) in enumerate(item[0].items()):
                if item_name != k2:
                    continue
                for i3, (v3,k3) in enumerate(inverter.items()):
                    if k3[0]['type'] != v2[0]['type']:
                        continue
                    print('yay')
                    inverter[f'slot{i3+1}'][0]['name'] = item_name
                    inverter[f'slot{i3+1}'][0]['quantity'] = 1
                    with open('inventorye.json', 'w+') as outl:
                        outl.write(json.dumps(inverter, indent = 2))
                    #parse stat modifier here or smth
                break
class Crafting:
    def names():
        cyclone = 1
        item_name = []
        for i in range(len(recipes[0])):
            name = recipes[0][f'item_{cyclone}'][0]['name']
            item_name.append(name)
            cyclone += 1
        return item_name
    def page_scroll():
        print('ENTER PAGE NUMBER')
        numpad = module.proper_input('int')
        loste = []
        fur = [1,2,3,4]
        if numpad not in fur:
            Crafting.page_scroll()
        else:
            max_range = int(numpad) * 9 + 1
            lowest_range = max_range - 9
            for i in range(9):
                loste.append(lowest_range)
                lowest_range += 1
        print(loste)
        return loste
    def create_list( ):
        recipe_page = Crafting.page_scroll()
        item_name = Crafting.names()
        print(f'''
        ══════════════════════════════════
        1. {recipes[0][f'item_{recipe_page[0]}'][0]['name']}                             
        ══════════════════════════════════
        2. {recipes[0][f'item_{recipe_page[1]}'][0]['name']}                             
        ══════════════════════════════════
        3. {recipes[0][f'item_{recipe_page[2]}'][0]['name']} 
        ══════════════════════════════════
        4. {recipes[0][f'item_{recipe_page[3]}'][0]['name']} 
        ══════════════════════════════════
        5. {recipes[0][f'item_{recipe_page[4]}'][0]['name']}                         
        ══════════════════════════════════
        6. {recipes[0][f'item_{recipe_page[5]}'][0]['name']}                              
        ══════════════════════════════════
        7. {recipes[0][f'item_{recipe_page[6]}'][0]['name']} 
        ══════════════════════════════════
        8. {recipes[0][f'item_{recipe_page[7]}'][0]['name']} 
        ══════════════════════════════════
        9. {recipes[0][f'item_{recipe_page[8]}'][0]['name']} 
        ══════════════════════════════════
                1 2 3 4 5 6 7 8...
        ''')
        print('type continue to continue browsing and select to select a recipe')
        egg = module.proper_input('str')
        if egg == 'continue':
            Crafting.create_list()
        elif egg == 'select':
            pass
        elif egg == 'exit':
            pass
    def recipe_select( ):
        print('ENTER ITEM YOU WOULD LIKE TO CRAFT')
        selection = module.proper_input('str').lower()
        if selection == "exit":
            print("EXITING")
            #PUT THIS INTO THE MAP
        for i, (k,v) in enumerate(recipes[0].items()):
            if v[0]['name'] == selection:
                print(f'''
Item: {v[0]['name']} 
Level Requirement: {v[0]['level_req']}
Items Needed: {v[0]['items_needed']}''')
                if v[0]['level_req'] > character[0]['level']:
                    print('Not High Enough Level')
                    Crafting.create_list()
                else:
                    return v[0]
    def craft_item( ):
        barf = Crafting.recipe_select()
        print('ENTER AMOUNT YOU WOPULD LIKE TO CRAFT')
        face = module.proper_input('int')
        print('VERIFY YOU WOULD LIKE TO CRAFT THIS: ')
        if Crafting.confirmation() == True:
            egg = []
            with open('inventoryi.json') as facter:
                inventoryi = json.load(facter)
            print('ITEM AMOUNT:')
            for i, (k, v) in enumerate(barf['items_needed'].items()):
                print(f'{k}:{v*face}')
                for i, (name, value) in enumerate(inventoryi.items()):
                    if value[0]['name'] == k:
                        if value[0]['quantity'] * face >= v:
                            egg.append(True)
                        else:
                            egg.append(False)
            if False in egg or len(egg) == 0:
                print('''You don't have enough materials to craft this item''')
            else:
                for i2, (k2, v2) in enumerate(barf['items_needed'].items()):
                    Inventory.psi(k2, v2 * face, 'subtract')
                print("Crafting Item...")
                fri = 1
                for ul in range(10):
                    print(f'''



    Crafting Progress:
    {'○ '*fri}




    

    
    
    
    

    ''')
                    time.sleep(0.1)
                    fri+=1
                Inventory.psi(barf['name'], face, 'add')

        else:
            exit()
    def confirmation():
        cherg = input() 
        if cherg == 'Y':
            return True
        else:
            return False
Inventory.equip('crystal pants')