import random, json

with open('locationenemy.json') as f:
    location = json.load(f)

class Lakes():   
    def kill_enemy():
        print("ENEMY KILLEd")
        Maper.map()
class Maper():
    def boundaries():
        map_dimensions = location['location_1'][0]['map_dimensions']
        height = map_dimensions[1]
        length = map_dimensions[0]
        return height, length
    def spawn_positions():
        map_dimensions = Maper.boundaries()
        height = map_dimensions[1]
        length = map_dimensions[0] 
        randy = random.randint(0, height - 1)
        randx = random.randint(0, length - 1)
        return randy, randx
    def map():
        map_dimensions = Maper.boundaries()
        height = map_dimensions[1]
        length = map_dimensions[0] 
        enemy_spawny = Maper.spawn_positions()[0]
        enemy_spawnx = Maper.spawn_positions()[1]
        spawn_amount  = 10
        egg = []
        counter = []
        x = 2
        y = 2
        item = " "
        Map = [['[ ]' for i in range(5)] for i in range(height)] 
        player_spawn = Map[y][x]
        for i in range(spawn_amount):
            counter.append([Maper.spawn_positions()[0], Maper.spawn_positions()[1]])
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
            enemy_position = Map[enemy_spawny][enemy_spawnx]
            Map[enemy_spawny][enemy_spawnx] = '[O]'
            print(counter)
            print(current_position)
            if current_position in counter:
                print("ITS AN ENEMY!!!")    
                Lakes.kill_enemy()
            for something in Map:
                print("".join(something))
   
Maper.map()