import json
null = None
def inventory():
    egg = []
    testtemp = 10
    with open('inventoryi.json') as farts:
        qwe = json.load(farts)
    for i, (k,w) in enumerate(qwe.items()):
        if w[0]['name'] !=  null:
            egg.append(w[0]['name'])
    if testtemp < 9:
        print("create 1 list instance")
    elif testtemp == 9:
        print("normal display")
    elif testtemp > 9:
        print(testtemp % 9)
    print(f'''
                INVENTORY 
    ══════════════════════════════════
                        1  
    ══════════════════════════════════
                       2
    ══════════════════════════════════
                       3
    ══════════════════════════════════
                       4
    ══════════════════════════════════
                       5
    ══════════════════════════════════
                       6
    ══════════════════════════════════
                       7
    ══════════════════════════════════
                       8
    ══════════════════════════════════
9
    ══════════════════════════════════
                <- - ->
    ''')

egad = []
with open('inventoryi.json') as farts:
    qwe = json.load(farts)
for i, (k,w) in enumerate(qwe.items()):
    egad.append(w[0]['name'])
print(egad)
for i in range(len(egad)+1):
    if egad[i] != None:
        ad = egad.index(egad[i])
        print(egad[i], i)
        break
print(ad)