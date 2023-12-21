import json
def update_position():
    with open('cursor.json', 'r+') as gorillatown:
        curse = json.load(gorillatown)
    with open('cursor.json','w+') as bananajam:
        bananajam.write()
def item_select():
    with open('cursor.json') as f:
        egg = json.load(f)
    pravda = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    coconutbanana = input()
    cursor_pos = [0]['cursor_position']
    if coconutbanana == "W": 
    
        cursor_pos +=1
    pravda[cursor_pos] = '>'
    pravda[cursor_pos - 1] = ' '
    print(pravda)
item_select()