import json
import sys
import time
from item import Inventory
from methods import Modified_Functions as mod
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
        numpad = mod.proper_input('int')
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
        egg = mod.proper_input('str')
        if egg == 'continue':
            Crafting.create_list()
        elif egg == 'select':
            pass
        elif egg == 'exit':
            pass
    def recipe_select( ):
        print('ENTER ITEM YOU WOULD LIKE TO CRAFT')
        selection = mod.proper_input('str').lower()
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
        face = mod.proper_input('int')
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
                        print("here")
                        if value[0]['quantity'] * face >= v:
                            egg.append(True)
                        else:
                            egg.append(False)
            if False in egg or len(egg) == 0:
                print('''You don't have enough materials to craft this item''')
            else:
                print(egg)
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
                print("ITEM CRAFTED!")
                Inventory.psi(barf['name'], face, 'add')
                print("ITEM ATTEMPTED CRAFT")
        else:
            exit()
    def confirmation():
        cherg = input() 
        if cherg == 'Y':
            return True
        else:
            return False
