import random, json, sys, time
from methods import Modified_Functions as module
with open('locationenemy.json') as dropp:
    locationenemy= json.load(dropp)
with open('shopinstance.json') as draf:
    shopinstance = json.load(draf)
with open('mapinstance.json') as mapi:
    mapinstance = json.load(mapi)
with open('dontmesswiththis.json')  as inf:
    dmwt = json.load(inf)
with open('character.json') as inf2:
    character = json.load(inf2)
with open('shop.json') as infile:
    shop = json.load(infile)
with open('player.json') as infile:
    player = json.load(infile)
class Location_Creation():
    def fulcrum():
        with open('character.json') as inf3:
            chare = json.load(inf3)
        name = chare[0]['sub_location']
        for i, (k, v) in enumerate(locationenemy.items()):
            if name == v[0]['locationname']:
                print('yay')
                with open('mapinstance.json', 'w+') as fel:
                    fel.write(json.dumps(v[0], indent = 2))
                    fel.seek(0)
    def change(mode):
        if mode  == 'story':
            for i,(v,k) in enumerate(dmwt.items()):
                if k[0]['locationname'] ==  character[0]['location']:
                    indexing = k[0]['sublocations'].index(character[0]['sub_location'])
                    if indexing == len(k[0]['sublocations']) -1:
                        print('locationname changing')
                        modifiant = 'location'
                        algae = dmwt[f'location{i+2}'][0]['locationname']
                    else:
                        modifiant = 'sub_location'
                        algae = k[0]['sublocations'][indexing+1] 
                    with open('character.json')  as inf: 
                        charac = json.load(inf)
                        charac[0][modifiant] = algae
                        if modifiant == 'location':
                            charac[0]['sub_location'] = dmwt[f'location{i+2}'][0]['sublocations'][0]
                    with open('character.json', 'w+')  as false:
                        false.write(json.dumps(charac,indent=2))
                        false.seek(0)
    def update_location_instance(key, value):
        with open('mapinstance.json', 'r+') as efl:
            mri = json.load(efl)
            mri[key] = value
            print('dumped')
            efl.seek(0)
            efl.truncate()
            efl.write(json.dumps(mri, indent=2))
    def remove_enemy_pos(item_removal):
        with open('mapinstance.json', 'r+') as frit:
            friot = json.load(frit)
            try:
                friot['enemy_positions'].remove(item_removal)
            except ValueError:
                print("POSITION COULD NOT BE REMOVED")
        with open('mapinstance.json', 'w+') as felon:
            felon.write(json.dumps(friot, indent=2))
            felon.seek(0)
class MAPPING():
    def load_map_instance():
        with open('mapinstance.json') as infile:
            refreshmap = json.load(infile)
        return refreshmap
    def check_map_instance():
        mapset = MAPPING.load_map_instance()
        height, length = mapset['map_dimensions'][0], mapset['map_dimensions'][0]
        return height, length
    def spawn_position():
        mapset = MAPPING.load_map_instance()
        map_positions = []
        for i in range(mapset['map_amount']):
            coords = [random.randint(0, MAPPING.check_map_instance()[0] - 1), random.randint(0, MAPPING.check_map_instance()[1])]
            while True:
                if coords in map_positions:
                    coords = [random.randint(0, MAPPING.check_map_instance()[0] - 1), random.randint(0, MAPPING.check_map_instance()[1])]
                else:
                    break
            map_positions.append(coords)
        print(map_positions)
        Location_Creation.update_location_instance('enemy_positions', map_positions)
        return map_positions
    def actual_map():
        with open('mapinstance.json') as instance:
                mapset = json.load(instance)
        Location_Creation.fulcrum()
        spawns = MAPPING.spawn_position()
        height, length = MAPPING.check_map_instance()[0], MAPPING.check_map_instance()[1]
        item =' '
        items = 'E'
        if mapset['type'] == 'Item':
            items = 'I'
        elif mapset['type'] ==  'Enemy':
            items = 'E'
        elif mapset['type'] == 'Boss':
            items = 'B'
        time.sleep(1)
        Map = [['[ ]' for i in range(height)] for i in range(length)]
        print(mapset['enemy_positions'][0][1])
        for i, v in enumerate(mapset['enemy_positions']):
            Map[v[1]][v[0]] = f'[{items}]'
        x = mapset['spawn_position'][1]
        y = mapset['spawn_position'][0]
        while True:
            print(f'y: {y}, x :{x}') 
            current_position = [y, x]
            control = input("")
            if control == 'w':
                y -= 1
                Map[y+1][x] = f'[{item}]'
            elif control == 's':
                y += 1
                Map[y-1][x] = f'[{item}]'
            elif control == 'a':
                x -= 1
                Map[y][x+1] = f'[{item}]'
            elif control == 'd':
                x += 1
                Map[y][x-1] = f'[{item}]'
            elif control == 'menu':
                print('options')  
            if y == height:
                y -=1
            elif x == length:
                x -=1
            elif x == -1:
                x +=1
            elif y == -1:
                y +=1
            Map[y][x] = '[X]'
            if len(spawns) == 0:
                Map[mapset['exit_position'][0]][mapset['exit_position'][1]] = '[Q]'
                if current_position == [mapset['exit_position'][0],mapset['exit_position'][1]]:
                    print('MOVING ONTO NEXT LOCATION')
                    Location_Creation.fulcrum()
                    Location_Creation.change('story')
                    MAPPING.actual_map()
            if mapset['type'] == 'Enemy':
                if current_position in mapset['enemy_positions']:
                    print('ENEMY KILED')
                    print(current_position, spawns)
                    Location_Creation.remove_enemy_pos(current_position)
            elif mapset['type'] == 'Items':
                if current_position in mapset['enemy_positions']:
                    print('Item Picked Up')
                    Location_Creation.remove_enemy_pos(current_position)
                    #trigger item pickup or smth
            elif mapset['type'] == 'Shop':
                Map[mapset['shop_position'][0]][mapset['shop_position'][1]] = '[S]'
                if current_position == mapset['shop_position']:
                    print('ENTERING SHOP')
                    Shop.create_shop_instace()
                    Shop.display_purcahse()
            for something in Map:
                print("".join(something))
class Shop():
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
        {i+1}. {item_name}''', end='')
        print(f'''
        ══════════════════════════════════
                ''')
        item = module.proper_input('str')
        if item == 'exit':
            print('exit')
        for index, v in enumerate(shopinstance1):
            if v[0]['name'] == item:
                print('')
            else:
                continue
            verify = module.proper_input('str').lower()
            if verify != 'y':
                continue
            print(f'Item Price:{v[0]['price']}')
            if v[0]['stock'] == 0:
                print('item out of stock')
                Shop.display_purchase()
            amount = module.proper_input('int')
            print(f'Current_Price:{amount*v[0]['price']}')
            print(f'Amount in Stock:{v[0]['stock']}')
            while True:
                if amount > v[0]['stock']:
                    print('Not enoguh item in Stock')
                    amount  = module.proper_input('int')
                else:break
            if player[0]['coins'] < v[0]['price'] * amount:
                print('Not Enough Coins')
                Shop.display_purchase()
            else:
                coins = player[0]['coins'] - v[0]['price'] * amount
                stock = v[0]['stock'] - amount
                print(coins,stock)
                module.file_modification('shopinstance.json',[index,0,'stock'], stock)
                module.file_modification('player.json',[0,'coins'], coins)
                Shop.display_purchase()
MAPPING.actual_map()