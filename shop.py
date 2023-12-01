import json, random
import json
with open('shop.json', 'r') as f:
    shop = json.load(f)
class Merchant():
    def guiopen(self):
        print("   __________________________________")
        print("  |__________________________________|")
        print("                 SHOP")
        print("     _______    _______     _______      ")
        print("    |       |  |       |   |       |     ")
        print("    |  EGG  |  |       |   |       |     ")
        print("    |_______|  |_______|   |_______|     ")
        print("     _______    _______     _______      ")
        print("    |       |  |       |   |       |     ")
        print("    |       |  |       |   |       |     ")
        print("    |_______|  |_______|   |_______|     ")
        Merchant.dialogue(self)
    def dialogue(self):
        print("ITEMS FOR SALE : [INSERT LIST HERE]")
        ex = input("See anything ya like? : ")
        if ex == "y":
            Merchant.TEST(self)
        else:
            print("Shame, alright then")
            Merchant.new_location(self)
    def pullvar(self):
        var = 1
        leew = []
        for i in range(4):
            var += 1
            leew.append(var)
        return leew
    def TEST(self):
        ew = Merchant.pullvar(self)
        random.shuffle(ew)
        print(f'Items in stock : {ew}')
    def buy(self):
        ew = Merchant.pullvar(self)
        ag = input("input number and amount in this format (#1,200) ")
        x = 0
        if ag == {ew[x]}:
            print(ew[x])
    def exit():
        print("Have a good day")
    def new_location(self):
        #pull current location from json file and print it in here
        location = "PLACE"
        print(" __________________________________")
        print("|                                  |")
        print("|          entering PLACE          |")
        print("|__________________________________|")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("      _")
        print("_____/ \____________________________")
        ew = Merchant.pullname(self)
#figure out how to print items, add probability to the items appearing, then add price, etc
merch = Merchant()
merch.guiopen()
merch.TEST()