#make sure to create a global variable for the things here
#json file has individual slots, everytime you recieve an item you update that json file. use the json file for invetory, etc. 
import json

class Inventory():
    rer = 1 

class Acessories():
    egege = 1

inv_update = False
class InvUpdate():
    if inv_update == True:
        with open('.json','r') as file:
            data =  json.load(file)
            data.pop("item")
            data["inventory"]["slot1"]["item"] = True
    elif inv_update != True:
        print("failed update inventory")
        
