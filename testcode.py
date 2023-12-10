import json



with open('player.json', 'r') as g:
    egg = json.load(g)
    print(egg[0]['health'])
    egg[0]['health'] = 100
with open('player.json', 'w') as f:
    f.write(json.dumps(egg))

with open('player.json', 'r') as g:
    egg = json.load(g)
    print(egg[0]['health'])