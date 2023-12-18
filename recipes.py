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
        max_range = int(numpad) * 9
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
1. {item_name[recipe_page[0]]}                             
══════════════════════════════════
2. {item_name[recipe_page[1]]}                             
══════════════════════════════════
3. {item_name[recipe_page[2]]}
══════════════════════════════════
4. {item_name[recipe_page[3]]}                             
══════════════════════════════════
5. {item_name[recipe_page[4]]}                             
══════════════════════════════════
6. {item_name[recipe_page[5]]}                             
══════════════════════════════════
7. {item_name[recipe_page[6]]}                             
══════════════════════════════════
8. {item_name[recipe_page[7]]}                             
══════════════════════════════════
9. {item_name[recipe_page[8]]}                             
══════════════════════════════════
        1 2 3 4 5 6 7 8...
''')
create_list()