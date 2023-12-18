import json

with open('recipes.json') as f:
    recipes = json.load(f)
currentdict = recipes[0]['item_1'][0]['items_needed']
luo = list(currentdict.items())
print(luo[0])
def names():
    cyclone = 1
    item_name = []
    for i in range(len(recipes[0])):
        name = recipes[0][f'item_{cyclone}'][0]['name']
        item_name.append(name)
        cyclone += 1
    return item_name
def page_scroll():
    numpad = input()
    loste = []
    fur = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if numpad not in fur:
        page_scroll()
    else:
        max_range = int(numpad) * 9 + 1
        lowest_range = max_range - 9
        for i in range(9):
            loste.append(lowest_range)
            lowest_range += 1
    print(loste)
    return loste
def create_list():
    recipe_page = page_scroll()
    item_name = names()
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
create_list()

def requirements():
    pass