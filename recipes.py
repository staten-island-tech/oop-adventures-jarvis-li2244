import json

with open('recipes.json') as f:
    recipes = json.load(f)
luo = []
luo.append(recipes[0]['item_1'][0]['items_needed'])
print(luo)