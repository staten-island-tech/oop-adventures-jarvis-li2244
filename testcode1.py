import json
with open('item.json') as falafel:
    item = json.load(falafel)

name = "en"
gel = item[0][f'{name}'][0]['stats'][0]
egg = list(gel.items())
print(len(egg))
