import json
with open('shop.json', 'r') as f:
    shop = json.load(f)

class Merchant():
    def pullname(self):
        var = 1
        leew = []
        for i in range(4):
            check1 = shop[f'PLACEHOLDER{var}'][0]['name']
            var += 1
            leew.append(check1)
        return leew
    def pullchance(self):
        ew = Merchant.pullname(self)
        
    def pullprice(self):
        ew = Merchant.pullname(self)
    def TEST(self):
        ew = Merchant.pullname(self)
#figure out how to print items, add probability to the items appearing, then add price, etc
merch = Merchant()
merch.TEST()