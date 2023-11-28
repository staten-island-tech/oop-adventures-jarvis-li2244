import json

with open('inventory.json', 'r') as f:
    inventory = json.load(f)
var = 1,2,3,4,5,6,7,8,9

def hotbar():
    trigger = input("")
    return trigger
def item_used():
    trigger = hotbar()
    temp = inventory['inventory'][0][f'slot{trigger}']
    print(f'selected item : {temp}')
def item_usagecheck():
    print('')


item_used()