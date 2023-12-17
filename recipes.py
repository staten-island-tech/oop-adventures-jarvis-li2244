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
def create_list():
    item_name = names()
    print(f'''
══════════════════════════════════
1. {item_name[0]}                             
══════════════════════════════════
2. {item_name[1]}                             
══════════════════════════════════
3. {item_name[2]}                             
══════════════════════════════════
4. {item_name[3]}                             
══════════════════════════════════
5. {item_name[4]}                             
══════════════════════════════════
6. {item_name[5]}                             
══════════════════════════════════
7. {item_name[6]}                             
══════════════════════════════════
8. {item_name[7]}                             
══════════════════════════════════
9. {item_name[8]}                             
══════════════════════════════════
''')
print(len(recipes[0]))
create_list()
