import random, json
with open('locationenemy.json') as dropp:
    locatien = json.load(dropp)
#initializing the mapinstance
with open('mapinstance.json') as mapi:
    minp = json.load(mapi)
locations = ['Anthil Foreest', 'Castle Walls', 'Residency Area', 'Academy', 'Royal Garden', 'Royal Palace', 'Cellars(ALCOHOL TIME)']
name = 'A Room'
def fulcrum():
    var = 1
    while var != len(locatien)+1:
        if name == locatien[f'location_{var}'][0]['locationname']: 
            print('yay')
            current_location_info = locatien[f'location_{var}'][0]
            return current_location_info
        else: var+=1
def modify(change, var, mode):
    with open('player.json', 'r+') as r:
        unique_variable = json.load(r)
    if mode == 'set':
        unique_variable[0][f'{var}'] = change
    elif mode == 'add':
        unique_variable[0][f'{var}'] += change
    elif mode == 'subtract':
        unique_variable[0][f'{var}'] -= change
    elif mode == 'append':
        unique_variable[0][f'{var}'].append(change)
    with open('player.json','w+') as i:
        i.write(json.dumps(unique_variable, indent = 2))
        i.seek(0)
egg = fulcrum()
minp = egg
with open('mapinstance.json', 'w+') as fel:
    fel.write(json.dumps(minp, indent = 2))
    fel.seek(0)
#just json file opening here
with open('shop.json')  as fre:
    ihop = json.load(fre)
with open('mapinstance.json') as aei:
    instance_map = json.load(aei)
with open('character.json') as efe:
    char = json.load(efe)
print('3')
#updating whatever key pair needed
def update_location_instance(key, value):
    with open('mapinstance.json') as efl:
        mri = json.load(efl)
        mri[f'{key}'] = value
    with open('mapinstance.json', 'w+') as fe:
        fe.write(json.dumps(mri, indent = 2 ))
        fe.seek(0)
#removing enemy_position once it's dead
def remove_enemy_pos(item_removal):
    with open('mapinstance.json', 'r+') as frit:
        friot = json.load(frit)
        try:
            friot['enemy_positions'].remove(item_removal)
        except ValueError:
            pass
    with open('mapinstance.json', 'w+') as felon:
        felon.write(json.dumps(friot, indent=2))
        felon.seek(0)
#placeholder for battle system, once finished with this file
class Lakes():
    def kill_enemy():
        print("ENEMY KILLED")
#map function 
class Maper():
    def item():
        #basically copy the same formula as enemy_spawning except make it trigger  smht else
        pass
    def spawn_positions():
        map_dimensions = Maper.boundaries()
        height = map_dimensions[1]#probably reduce this somehow
        length = map_dimensions[0] 
        randy = random.randint(0, height - 1)
        randx = random.randint(0, length - 1)
        return randy, randx
    def boundaries():
        map_dimensions = instance_map['map_dimensions']
        height = map_dimensions[1]
        length = map_dimensions[0]
        return height, length
    def map():
        map_dimensions = Maper.boundaries()
        height, length= map_dimensions[1],  map_dimensions[0]
        spawn_amount  = 10
        eg = 0
        Map = [['[ ]' for i in range(length)] for i in range(height)] 
        if instance_map['type'] == 'Enemy':
            variablename = [[Maper.spawn_positions()[0], Maper.spawn_positions()[1]] for i in range(spawn_amount)]
            update_location_instance('enemy_positions', variablename)
            for i in range(spawn_amount):
                y_cords = variablename[eg][0]
                x_cords = variablename[eg][1]
                eg +=1
                Map[y_cords][x_cords] = '[O]'
        elif instance_map['type'] == 'Shop':
            coords = instance_map['shop_position']
            Map[coords[0]][coords[1]] = "[S]"
        x = instance_map['spawn_position'][1]
        y = instance_map['spawn_position'][0]
        item = " "
        var = 0
        while True:
            with open('mapinstance.json') as fre:
                mapir = json.load(fre)
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
            if y == height:
                y -=1
            elif x == length:
                x -=1
            elif x == -1:
                x +=1
            elif y == -1:
                y +=1
            Map[y][x] = '[X]'
            print(current_position)
            if instance_map['type'] == 'Enemy':
                i = 0
                if len(mapir['enemy_positions']) == 0:
                    print('You may proceed to the next location')
                else:
                    while  i  != len(mapir['enemy_positions']):
                        if current_position == mapir['enemy_positions'][var]:
                            print("ITS AN ENEMY!!!")
                            Lakes.kill_enemy()
                            remove_enemy_pos(current_position)
                            i = len(mapir['enemy_positions'])
                        else:
                            var += 1
                            if var >= len(mapir['enemy_positions']):
                                var = 0
                            i += 1
            elif instance_map['type'] == 'Shop':
                if instance_map['type'] == 'Shop':
                    coords = instance_map['shop_position']
                    Map[coords[0]][coords[1]] = "[S]"
                if current_position == mapir['shop_position']:
                    print("A SHOP!!!")
                    Shop.create_items()
            for something in Map:
                print("".join(something))
class Shop:
    def return_items():
        items = []
        shop_item_length = 3
        for i in range(shop_item_length):
            value_check = random.randint(0, int(len(ihop))-1)
            items.append(ihop[f'PLACEHOLDER{value_check}'])
        return items
    def dict_to_list(): 
        egg = Shop.return_items()
        dict_list = []
        virus = 0
        for i in range(len(egg)):
            temp_value = egg[virus][0]
            new_list = [(key, value) for key, value in temp_value.items()]
            dict_list.append(new_list)
            virus += 1
        print(dict_list)     
        return dict_list
    def display():
        pi = Shop.dict_to_list()
        print(f'''
    ╔═════════╗ ╔═════════╗ ╔═════════╗
    ║         ║ ║         ║ ║         ║    
    ║{pi[0][0][1].center(9,' ')}║ ║{pi[1][0][1].center(9,' ')}║ ║{pi[2][0][1].center(9,' ')}║
    ║         ║ ║         ║ ║         ║
    ╚═════════╝ ╚═════════╝ ╚═════════╝         
              ''')
    def purcahse():
        egg =  Shop.dict_to_list()
        choose = int(input(""))
        possible_options = len(egg)
        while choose > possible_options-1 or choose < 0:
            choose = int(input("Enter a Valid Choice Please: "))
        print(f'item name: {egg[choose][0][1]}')
        print(f'price: {egg[choose][1][1]}')
        puma  = input()
        print("Exit = exit shop, Y ")
        if puma == 'Y':
            return  egg[choose][0][1],egg[choose][1][1]
        elif puma == 'Exit':
            print('exiting shop')
        elif puma != 'Y': 
            print('damn alright')
    def player_update():
        frag = Shop.purcahse()
        with open('player.json') as asci:
            pls = json.load(asci)
        egg = pls[0]['coins'] - frag[1]
        print(egg)
        if int(egg) <= 0:
            print('broke')
        else:
            modify(egg, 'coins', 'set')
        
Shop.player_update()

#use a variable within a function to trigger another function 