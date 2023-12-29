import json
with open('inventoryi.json')  as fascism:
    invent = json.load(fascism)
for i, (k, v) in enumerate(invent.items()):
    if v[0]['name'] == 'en':
        