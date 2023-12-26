import json, random 

with open('shop.json') as felon:
    shop =  json.load(felon)
class Shop:
    def return_items():
        items = []
        shop_item_length = 3
        for i in range(shop_item_length):
            value_check = random.randint(0, int(len(shop))-1)
            items.append(shop[f'PLACEHOLDER{value_check}'])
        return items
print(Shop.return_items())
