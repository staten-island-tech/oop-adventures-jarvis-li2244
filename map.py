import random, json
with open('locationenemy.json') as dropp:
    locatien = json.load(dropp)
with open('mapinstance.json') as mapi:
    minp = json.load(mapi)
name = "Antil Forest"
def fulcrum():
    var = 1
    while var != len(locatien)-1:
        if name in locatien[f'location_{var}'][0]['locationname']: 
            current_location_info = locatien[f'location_{var}'][0]
            return current_location_info
        else: var+=1
egg = fulcrum()
minp = egg
with open('mapinstance.json', 'w+') as fel:
    fel.write(json.dumps(minp, indent = 2))
    fel.seek(0)
with open('mapinstance.json') as aei:
    instance_map = json.load(aei)
with open('character.json') as efe:
    char = json.load(efe)
def update_location_instance(key, value):
    with open('mapinstance.json') as efl:
        mri = json.load(efl)
        mri[key] = value 
    with open('mapinstance.json', 'w+') as fe:
        fe.write(json.dumps(mri, indent = 2 ))
        fe.seek(0)
class Lakes():
    def kill_enemy():
        print("ENEMY KILLED")
        Maper.map()
class Maper():
    def item():
        #basically copy the same formula as enemy_spawning except make it trigger  smht else
        pass
    def spawn_positions():
        map_dimensions = Maper.boundaries()
        height = map_dimensions[1]
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
        height = map_dimensions[1]
        length = map_dimensions[0]
        spawn_amount  = 10
        eg = 0
        Map = [['[ ]' for i in range(length)] for i in range(height)] 
        variablename = [[Maper.spawn_positions()[0], Maper.spawn_positions()[1]] for i in range(spawn_amount)]
        update_location_instance('enemy_positions', variablename)
        for i in range(spawn_amount):
            y_cords = variablename[eg][0]
            x_cords = variablename[eg][1]
            eg +=1
            Map[y_cords][x_cords] = '[O]'
        egg = []
        x = 2
        y = 2
        item = " "
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
            for something in Map:
                print("".join(something))
            if current_position in variablename:
                print("ITS AN ENEMY!!!")    
                Lakes.kill_enemy()
                #use .remove() to remove the enemy_coords once down
            if variablename == None:
                print("Exit Opened")
                rat = False
Maper.map()