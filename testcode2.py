from methods import Modified_Functions as module
import random
import json
null = None
with open('skills.json') as infile:
    skills = json.load(infile)
with open('character.json') as infile:
    character = json.load(infile)
with open('attacks.json') as infile:
    attacks = json.load(infile)
with open('shopinstance.json') as infile:
    shopinstance = json.load(infile)
with open('shop.json') as infile:
    shop  = json.load(infile)
with open('player.json') as infile:
    player = json.load(infile)
def create_shop_instance():
    items = []
    for i in range(5):
        random_item = shop[f'PLACEHOLDER{random.randint(0, int(len(shopinstance)-1))}']
        while True:
            if random_item in items:
                random_item = shop[f'PLACEHOLDER{random.randint(0, int(len(shopinstance)-1))}']
            else:
                break
        items.append(random_item)
    with open('shopinstance.json', 'w+') as infile:
        infile.write(json.dumps(items, indent=2))
        infile.seek(0)
def display_purchase():
    with open('shopinstance.json') as infile:
        shopinstance1 = json.load(infile)
    print(r'''
                SHOP 
        ''', end='')
    for i in range(len(shopinstance1)):
        item_name = shopinstance1[i][0]['name']
        print(f'''
    ══════════════════════════════════
    {i}. {item_name}''', end='')
    print(f'''
    ══════════════════════════════════
            ''')
    item = module.proper_input('str')
    if item == 'exit':
        print('exit')
    for i, v in enumerate(shopinstance1):
        print(i)
        print(len(shopinstance))
        if v[i]['name'] == item:
            print('item found')
        else:
            continue
        verify = module.proper_input('str').lower()
        if verify != 'y':
            continue
        if v[i]['stock'] == 0:
            print('item out of stock')
            display_purchase()
        amount = module.proper_input('int')
        while True:
            if amount > v[i]['stock']:
                print('not enough')
                amount  = module.proper_input('int')
            else:break
        if player[0]['coins'] < v[i]['price'] * amount:
            print('Not Enough Coins')
            display_purchase()
        else:
            coins = player[0]['coins'] - v[i]['price'] * amount
            stock = v[i]['stock'] - amount
            print(coins,stock)
            module.file_modification('shopinstance.json',[0, i, 'stock'], stock)
            module.file_modification('player.json',[0,'coins'], coins)
            display_purchase()
create_shop_instance()
display_purchase()