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
        for i in data['slot1']:
            i['item_inv'] = i['item_inv'].replace(False, True)
        with open('.json','w') as file:
            json.dump(data, file)
            
        
