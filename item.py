import json, random

with open('inventoryi.json') as ii:
    inventir = json.load(ii)
with open('item.json') as falafel:
    item = json.load(falafel)
with open('inventorye.json') as illager:
    inverter = json.load(illager)
null = None
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
                inventi[f'slot{slot_num}'][0]['quantity'] += item_amount
                print(inventi[f'slot{slot_num}'][0]['quantity'])
            elif mode == 'subtract':
                inventi[f'slot{slot_num}'][0]['quantity'] -= item_amount
                print(inventi[f'slot{slot_num}'][0]['quantity'])
                if inventi[f'slot{slot_num}'][0]['quantity'] <= 0:
                    inventi[f'slot{slot_num}'][0]['quantity'] = 0
                    inventi[f'slot{slot_num}'][0]['name'] = None
            else:
                inventi[f'slot{slot_num}'][0]['name'] == 'item_name'
                inventi[f'slot{slot_num}'][0]['quantity'] == item
        with open('inventoryi.json', 'w+') as fermi:
            fermi.write(json.dumps(inventi, indent=2)) 
            fermi.seek(0)
    def psi(item_name, quantity, mode):
        with open('inventoryi.json') as finsi:
            inventiro = json.load(finsi)
        for i, (k, v) in enumerate(inventiro.items()):
            if item_name in inventiro:
                print("item found")
            else:
                print("nay")
            if v[0]['name'] == null:
                Inventory.inventory_update(item_name, i+1, 'placeholdernone', quantity )
                break
            elif v[0]['name'] == item_name:
                Inventory.inventory_update(item_name, i+1, mode, quantity)
    def check():
        with open('inventoryi.json') as factorial:
            invi = json.load(factorial)
        for i1,(k1, v1) in enumerate(invi.items()):
            print(k1, v1, 'enum1')
            if v1[0]['name'] == null:
                for i2, (k2, v2) in enumerate(invi.items()):
                    print(k2, v2, 'enum2')
                    if v2[0]['name'] != null:
                        invi[f'{k1}'][0]['name'] = invi[f'{k2}'][0]['name']
                        invi[f'{k1}'][0]['quantity'] = invi[f'{k2}'][0]['quantity']
                        invi[f'{k2}'][0]['quantity'] = 0
                        invi[f'{k2}'][0]['name'] = null
                    if v2[0]['name'] != null:
                        break
        with open('inventoryi.json', 'w+')  as fascism:
            fascism.write(json.dumps(invi, indent=2))
            fascism.seek(0)
    def put_slotin_inventory(item_name, quantity):
        vary = 0
        while vary != len(inventir):
            with open('inventoryi.json') as finale:
                inventi = json.load(finale)
            if inventi[f'slot{vary+1}'][0]['name'] == item_name:
                with open('inventoryi.json') as frag:
                    invventii = json.load(frag)
                    inventii[f'slot{vary+1}'][0]['quantity'] += 1
            elif inventi[f'slot{vary+1}'][0]['name'] == null:
                print('woah u suck at writign code')
                with open('inventoryi.json') as iii:
                    inventii = json.load(iii)
                    inventii[f'slot{vary+1}'][0]['name'] = item_name
                    inventii[f'slot{vary+1}'][0]['quantity'] = quantity
            else:
                vary += 1
                print('else')
            with open('inventoryi.json','w+') as i:
                i.write(json.dumps(inventii, indent = 2))
                i.seek(0)
        
        else:
            print("damn ur inventory full bro")
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
            Inventory.page_scroll()
        else:
            max_range = int(numpad) * 10 + 1
            lowest_range = max_range - 10
            for i in range(10):
                loste.append(lowest_range)
                lowest_range += 1
        return loste
    def inventory():
        page = Inventory.page_scroll()
        print(f'''
                INVENTORY 
    ══════════════════════════════════
    {page[0]}.  {inventir[f'slot{page[0]}'][0]['name']}                                
    ══════════════════════════════════
    {page[1]}.  {inventir[f'slot{page[1]}'][0]['name']}                         
    ══════════════════════════════════
    {page[2]}.  {inventir[f'slot{page[2]}'][0]['name']}  
    ══════════════════════════════════
    {page[3]}.  {inventir[f'slot{page[3]}'][0]['name']}    
    ══════════════════════════════════
    {page[4]}.  {inventir[f'slot{page[4]}'][0]['name']}                        
    ══════════════════════════════════
    {page[5]}.  {inventir[f'slot{page[5]}'][0]['name']}                            
    ══════════════════════════════════
    {page[6]}.  {inventir[f'slot{page[6]}'][0]['name']}   
    ══════════════════════════════════
    {page[7]}.  {inventir[f'slot{page[7]}'][0]['name']}   
    ══════════════════════════════════
    {page[8]}.  {inventir[f'slot{page[8]}'][0]['name']}   
    ══════════════════════════════════
    {page[9]}.  {inventir[f'slot{page[9]}'][0]['name']}    
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
    def fish():
        pass
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
Inventory.check()