import json, random, copy, time, sys

with open('inventoryi.json') as ii:
    inventir = json.load(ii)
with open('item.json') as falafel:
    item = json.load(falafel)
with open('inventorye.json') as illager:
    inverter = json.load(illager)
with open('recipes.json') as f:
    recipes = json.load(f)
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
                print("checked3")
                inventi[f'{slot_num}'][0]['quantity'] += item_amount
                print(inventi[f'{slot_num}'][0]['quantity'])
            elif mode == 'subtract':
                print("checked2")
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
        print("craft attempted")
        print(item_name)
        with open('inventoryi.json') as finsi:
            inventiro = json.load(finsi)
        for i, (k, v) in enumerate(inventiro.items()):
            if item_name == v[0]['name']:
                egg = True
                print("ITEM FOUND")
                break 
            else:
                print("ITEM NOT FOUND")
                egg = False
        for i2, (k2, v2) in enumerate(inventiro.items()):
            if egg == False:
                if v2[0]['name'] == null:
                    Inventory.inventory_update(item_name, k2, 'placeholdernone', quantity)
                    break
            elif egg == True:
                print("TRUE")
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
        print(len(asf))
        return asf
    def inventory_display():
        whilee = input("EXIT?: ")
        if whilee != 'exit':
            if input() == 'exit':
                whilee == 'exit'
            indel = Inventory.page_scroll()
            pagenum = int(input()) * 9 - 9
            print(r'''
                    INVENTORY 
        ''', end='')
            for i in range(9):
                print(f'''
        ══════════════════════════════════
        {pagenum+1}. {indel[pagenum]}''', end='')
                pagenum += 1
            print(f'''
        ══════════════════════════════════
                    <- - ->
        ''')
        else:
            exit()
    def verify_usage():
        egg = input("")
        if egg == "Y":
            return True
        else:
            return False
    def item_usage(): 
        #idk
        Inventory.inventory()
        print("Scroll up and Down Using A or D")
        eralt = input("")
        name = inventir[f'slot{eralt}'][0]['name']
        item_stats = item[0][f'{name}'][0]['stats'][0]
        if name == null:
            print("Nothing to see here")
        elif name != null:
            print(item_stats)
            if item[0][f'{name}'][0]['type'] == "consumable":
                print("Use item?")
                if Inventory.verify_usage() == True:
                    print("How many?")
                    egg = input("")
                    Inventory.update_json(name, item_stats, 'add', f'{egg}')
            elif item[0][f'{name}'][0]['type'] == "equippable":
                print("Equip Item?")
                if Inventory.verify_usage() == True:
                    Inventory.piie()
                    Inventory.update_json(name, item_stats, 'add', 1)

    def item_unusage():
        lemfa = input("")
        if lemfa not in inventir: 
            print("ni")
        elif lemfa in inventir:
            #put the check function here later, too lazy to write 
            print("Unequip?")
            equp = input("Y/N")
            if equp == "Y":
                print("Unequiped")
                Inventory.update_json("false", "stat_items ", 'subtract')
    def piie(item_name):
        vary = 0
        if inventir[f'slot{vary+1}'][0]['name'] in inverter:
            print("already equipped")
            print("scram")
            #cause placeholder function back to menu or smth
            pass
        while vary != len(inverter):
            if inventir[f'slot{vary+1}'][0]['name'] == null:
                with open('inventorye.json') as i4:
                    venti = json.load(i4)
                    venti[f'slot{vary+1}'][0]['name'] = item_name
                with open('inventorye.json','w+') as i2:
                    i2.write(json.dumps(venti, indent = 2))
                    i2.seek(0)
                break
            else:
                vary += 1
        print("damn ur inventory is full, no equips for you")
class Crafting:
    def names(self):
        cyclone = 1
        item_name = []
        for i in range(len(recipes[0])):
            name = recipes[0][f'item_{cyclone}'][0]['name']
            item_name.append(name)
            cyclone += 1
        return item_name
    def page_scroll(self):
        numpad = input()
        loste = []
        fur = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
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
    def create_list(self):
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
        egg = input("")
        if egg == 'page_scroll':
            Crafting.page_scroll()
        elif egg == 'exit':
            sys.exit()
    def recipe_select(self):
        selection = input()
        if selection == "Exit":
            print("EXIT")
        else:
            print("woah you're actually competent??!?!?!")
            position = recipes[0][f'item_{int(selection)}'][0]
            print(position['items_needed'])
            return position
    def craft_item(self):
        barf = Crafting.recipe_select()
        face = input("Amount?: ")
        if Crafting.confirmation() == True:
            egg = []
            with open('inventoryi.json') as facter:
                inventoryi = json.load(facter)
            for i, (k, v) in enumerate(barf['items_needed'].items()):
                for i, (name, value) in enumerate(inventoryi.items()):
                    if value[0]['name'] == k:
                        print("here")
                        if value[0]['quantity'] >= v:
                            egg.append(True)
                        else:
                            egg.append(False)
            if False in egg or len(egg) == 0:
                print(egg)
                print('''You don't have enough materials to craft this item''')
            else:
                print(egg)
                for i2, (k2, v2) in enumerate(barf['items_needed'].items()):
                    Inventory.psi(k2, v2, 'subtract')
                print("Crafting Item...")
                fri = 1
                for ul in range(10):
                    print(f'''




    Crafting Progress:
    {'○ '*fri}




    

    
    
    
    

    ''')
                    time.sleep(0.1)
                    fri+=1
                print("ITEM CRAFTED!")
                Inventory.psi(barf['name'], 1, 'add')
                print("ITEM ATTEMPTED CRAFT")
        else:
            exit()
    def confirmation():
        cherg = input() 
        if cherg == 'Y':
            return True
        else:
            return False

