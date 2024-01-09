from map import *
from interactivegui import * 
import sys, json, time
with open('classStats.json') as cs1:
    cs = json.load(cs1)
with open('character.json') as felix:
    charac = json.load(felix)
with open('player.json') as fas:
    player = json.load(fas)
play = play()
def modify(file, content, mode):
    with open(f'{file}.json')  as openfile:
        filed = json.load(openfile)
    if mode == '':
        filed = content
    elif mode != '':
        filed[0][mode] = content
    with open(f'{file}.json', 'w+')  as closedfile:
        closedfile.write(json.dumps(filed, indent=2))
def game_start():
    if input().upper() ==  'Y':
        return True
    else:
        return False
def class_select():
    if game_start() ==  True:
        print(r'''
                    CLASS SELECT
            
    ╔═════════╗╔═════════╗╔═════════╗╔═════════╗
    ║     o   ║║   | \   ║║     /   ║║         ║
    ║    /    ║║  >|-->  ║║   _/_   ║║  -]═──  ║ 
    ║   /     ║║   | /   ║║   /     ║║         ║  
    ╚═════════╝╚═════════╝╚═════════╝╚═════════╝
        MAGE      ARCHER    WARRIOR    ASSASSIN
    ''')
    class_selected = input().lower() 
    if class_selected == 'mage' or class_selected == 'archer' or class_selected == 'warrior' or class_selected == 'assassin':
        print(f'{class_selected} Selected')
        blit_class_stats(class_selected)
    else:
        class_select()
def blit_class_stats(class_name):
    for i,(v,k) in enumerate(cs.items()):
        if class_name == k[0]['class_name']:
            modify('player', k[0]['stats'], '')
            name = input("ENTER YOUR NAME : ")
            modify('player', name, 'name' )
            location_set(class_name)
def location_set(name):
    charac[0]['role'] = name
    charac[0]['name'] = player[0]['name']
    charac[0]['location'] = 'Anthill Forest'
    charac[0]['sub_location'] = 'The Myrminki Village'
    charac[0]['level'] = 0 
    with open('character.json', 'w+')  as infile:
        infile.write(json.dumps(charac, indent=2))
def start_game():
    print('starting game')
    #print some lore here/cutscene or smth and then start the game 
    Maper.map()
def game_run():
    while True:
        pass
def open_menu():
    print(r'''
       MENU 
╔════════════════╗
║    Inventory   ║
╚════════════════╝
╔════════════════╗
║    Equipment   ║     
╚════════════════╝
╔════════════════╗
║      Stat      ║
╚════════════════╝
╔════════════════╗
║      EXIT      ║
╚════════════════╝
''')
    idea = module.proper_input('str')
    if idea == 'help':
        print('inv to enter inventory, equip to enter equipment, stat to enter stat and exit to exit')
        open_menu()
    elif idea == 'stat':
        print('Opening Stats')
        
    elif idea == 'equip':
        print('Opening Equips')
    elif idea == 'inv':
        print('Opening Inventory')
        
    elif idea == 'exit':
        sys.exit()

    
if len('file') == 0:
    print('starting new game')
    class_select()
else:
    print('start where you left off or reset?')
    log = input()
    if log == 'start over':
        print('wiping slate')
        class_select()
    else:
        print('continuing where you left off')
        Maper.map()