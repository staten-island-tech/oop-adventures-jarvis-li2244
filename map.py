import random, json, sys
from interactivegui import Menu, Turn
from methods import Modified_Functions
module = Modified_Functions
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
with open('enemies.json') as infile:
    enemies = json.load(infile)
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
        with open('character.json') as infile:
            character = json.load(infile)
        for i, v in enumerate(dmwt['location1'][0]['sublocations']):
            if v[i] == character[0]['sub_location']:
                next_locate = v[i+1]
                character[0]['sub_location'] = next_locate
                with open('character.json', 'w+') as infile:
                    infile.write(json.dumps(character, indent=2))
                break
    def update_location_instance(key, value):
        with open('mapinstance.json') as efl:
            mri = json.load(efl)
            mri[f'{key}'] = value
        with open('mapinstance.json', 'w+') as fe:
            fe.write(json.dumps(mri, indent = 2 ))
            fe.seek(0)
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
##COMPLETE OPTIONS FIRST
def enemy_spawn():
    with open('mapinstance.json') as infile:
        mapinstance = json.load(infile)
        enemy_amount = len(mapinstance['enemies']) 
        if enemy_amount == 1:
            enemy_name = mapinstance['enemies'][0]['0'][0]['name']
        elif enemy_amount > 1:
            enemy_spawn = random.randint(0, enemy_amount-1)
            enemy_name = mapinstance['enemies'][0][f'{enemy_spawn}'][0]['name']
        for i, (k,v) in enumerate(enemies.items()):
            if enemy_name == v[0]['name']:
                break
        with open('enemyinstance.json', 'w+') as infile:
            infile.write(json.dumps(enemies[k], indent=2))
#just json file opening here
with open('shop.json')  as fre:
    ihop = json.load(fre)
with open('mapinstance.json') as aei:
    mapinstance = json.load(aei)
with open('character.json') as efe:
    char = json.load(efe)
#updating whatever key pair needed

#placeholder for battle system, once finished with this file
class Lakes():
    def kill_enemy():
        print("ENEMY KILLED")
#map function 
class Maper():
    def spawn_positions():
        map_dimensions = Maper.boundaries()
        height = map_dimensions[1]#probably reduce this somehow
        length = map_dimensions[0] 
        randy = random.randint(0, height - 1)
        randx = random.randint(0, length - 1)
        return randy, randx
    def boundaries():
        with open('mapinstance.json') as mapird:
            mapinstances =json.load(mapird)
        map_dimensions = mapinstances['map_dimensions']
        height = map_dimensions[1]
        length = map_dimensions[0]
        return height, length
    def open():
        with open('mapinstance.json') as infile:
            pit=json.load(infile)
        return pit
    def map():
        Location_Creation.fulcrum()
        mapir = Maper.open()
        map_dimensions = Maper.boundaries()
        height, length= map_dimensions[1], map_dimensions[0]
        spawn_amount  =  mapir['map_amount']
        eg = 0
        Map = [['[ ]' for i in range(length)] for i in range(height)] 
        if mapir['type'] == 'Enemy' or mapir['type'] == 'Items':
            variablename = [[Maper.spawn_positions()[1], Maper.spawn_positions()[0]] for i in range(spawn_amount)]
            Location_Creation.update_location_instance('enemy_positions', variablename)
            for i in range(spawn_amount):
                y_cords = variablename[i][0]
                x_cords = variablename[i][1]
                print(x_cords, y_cords)
                Map[y_cords][x_cords] = '[O]'
                eg+=1
        elif mapir['type'] == 'Shop':
            coords = mapir['shop_position']
            Map[coords[0]][coords[1]] = "[S]"
        x = mapir['spawn_position'][1]
        y = mapir['spawn_position'][0]
        item = " "
        icon = ' '
        if mapir['type'] == 'Enemy':
            icon ='[E]'
        elif mapir['type'] == 'Item':
            icon = '[I]'
        elif mapir['type'] == 'Boss':
            icon = '[B]'
        var = 0
        while True:
            with open('mapinstance.json') as fre:
                mapin = json.load(fre)
            current_position = [y, x]
            control = input("")
            if control == 'menu':
                Menu.open_menu()
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
            if y == height:
                y -=1
            elif x == length:
                x -=1
            elif x == -1:
                x +=1
            elif y == -1:
                y +=1
            Map[y][x] = '[X]'
            if mapin['type'] == 'Enemy' or mapin['type'] == 'Item' or mapin['type'] == 'Boss':
                if len(mapin['enemy_positions']) == 0:
                    print(mapin['exit_position'])
                    Map[mapin['exit_position'][0]][mapin['exit_position'][1]] = '[Q]'
                    if current_position == mapin['exit_position']:
                        Location_Creation.change('story')
                        Location_Creation.fulcrum()
                        Maper.map()
                        break
                else:
                    print('else')
                    for i, v in enumerate(mapin['enemy_positions']):
                        print(v, current_position)
                        if current_position == v:
                            if mapin['type'] == 'Enemy':
                                print("ENEMY")
                                enemy_spawn()
                                Turn.determine()
                            elif mapin['type'] == 'Resources':
                                print('ITEM PICKED UP')
                            Location_Creation.remove_enemy_pos(current_position)
                            for index, value in enumerate(mapin['enemy_positions']):
                                Map[value[0]][value[1]] = icon
            elif mapin['type'] == 'Shop':
                coords = mapin['shop_position']
                Map[coords[0]][coords[1]] = "[S]"
                if current_position == mapin['shop_position']:
                    print("A SHOP!!!")
                    Shop.create_shop_instance()
                    Shop.display_purchase()
            if len(mapin['enemy_positions']) == 0:
                Map[mapin['exit_position'][0]][mapin['exit_position'][1]] = '[Q]'
                if current_position == mapin['exit_position']:
                    print('yay')
                    Location_Creation.fulcrum()
                    Location_Creation.change('story')
                    Maper.map()
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
            #use the put_slotin_inventorymethod 
#use a variable within a function to trigger another function 
Maper.map()