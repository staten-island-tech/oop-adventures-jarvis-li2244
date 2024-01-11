
import sys, json, time
from methods import Modified_Functions
module = Modified_Functions
from item import Inventory
with open('classStats.json') as cs1:
    cs = json.load(cs1)
with open('character.json') as felix:
    charac = json.load(felix)
with open('player.json') as fas:
    player = json.load(fas)
with open('inventorye.json') as infile:
    inventorye =  json.load(infile)
null = None
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
    charac[0]['skills'] = [null, null, null, null]
    with open('character.json', 'w+')  as infile:
        infile.write(json.dumps(charac, indent=2))
def game_menu():
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
class Menu():
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
    ║     Skills     ║
    ╚════════════════╝
    ╔════════════════╗
    ║    Exit Menu   ║
    ╚════════════════╝
    ╔════════════════╗
    ║      Quit      ║
    ╚════════════════╝
    ''')
        idea = module.proper_input('str').lower()
        if idea == 'help':
            print('inv to enter inventory, equip to enter equipment, stat to enter stat, quit to quit and exit to exit')
        elif idea == 'stat':
            print('Opening Stats')
            for i,(k,v) in enumerate(player[0].items()):
                print(k,':',v)
        elif idea == 'equip' or idea == 'equipment':
            print('Opening Equips')
            for i, (k, v) in enumerate(inventorye.items()):
                print(v[0]['type'],":",v[0]['name'])
        elif idea == 'inv':
            print('Opening Inventory')
            Inventory.inventory_display()
        elif idea == 'exit':
            print('Exiting menu')
            print('going back to map')
        elif idea == 'quit':
            sys.exit()
        elif idea == 'skill':
            print('opening skills menu')
            for i, v in enumerate(charac[0]['skills']):
                print(v)
Menu.open_menu()