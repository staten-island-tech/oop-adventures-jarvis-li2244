import json, random

with open('inventoryi.json') as ii:
    inventir = json.load(ii)
null = None


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
    print(loste)
    return loste
def inventory():
    page = page_scroll()
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
              <- 1 ->
''')
#quantity
def piie():
    pass
inventory()
