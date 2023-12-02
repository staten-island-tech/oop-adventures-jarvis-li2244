import json

with open('inventory.json', 'r') as f:
    inventory = json.load(f)
with open('loot.json', 'r') as egg:
    loot =json.load(egg)
var = 1,2,3,4,5,6,7,8,9



def hotbar():
    trigger = input("")
    return trigger
def tempe():
    trigger = hotbar()
    return inventory['inventory'][0][f'slot{trigger}']

def item_used():
    temp = tempe() #name of item
    print(f'selected item : {temp}')
    use = input("")
    if use == "y" :
        item_usage()
def item_usage():
    temp = tempe()
    print('item used')
    blah = loot[temp][0]['']
def laewkwg_update_stats():
item_used()