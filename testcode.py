import time
import json

def zaza():
    with open('player.json', 'r') as g:
        egg = json.load(g)
        print(egg[0]['health'])
        egg[0]['health'] += 100
    with open('player.json', 'w') as f:
        f.write(json.dumps(egg))

with open('player.json', 'r') as g:
    egg1 = json.load(g)
def functioning():
    while egg1[0]['health'] != 1000:
        with open('player.json','r') as f:
            egggg = json.load(f)
        if egggg[0]['health'] == 1000:
            break
        zaza()
        time.sleep(0)


functioning()