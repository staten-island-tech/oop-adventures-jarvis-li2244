import time
import sys
import json
from methods import Modified_Functions as mod
with open('inventorye.json')  as eq:
    equips  = json.load(eq)
with open('inventoryi.json') as inv:
    invent = json.load(inv)
with open('item.json') as us:
    item = json.load(us)
with open('skills.json') as infile:
    skills = json.load(infile)
with open('attacks.json') as infile:
    attacks = json.load(infile)
with open('character.json') as infile:
    character = json.load(infile)
def dialogue():
    with open('dialogue.json') as dialogu:
        dialogue = json.load(dialogu)
    for i, (v, k) in enumerate(dialogue.items()):
        for i in range(len(k)):
            mod.delay_print(k[i])
            input()
            print('''''')
class Skills():
    def choose_skills():
        skill_choose = mod.proper_input('str')
        for i, (v) in enumerate(skills):
            if skill_choose != v['name']:
                continue
            print(v['description'])
            verify_skill = mod.proper_input('str')
            if verify_skill == 'y':
                for i, k  in enumerate(character[0]['skills']):
                    if k != None:
                        continue
                    mod.file_modification('character.json', [0,'skills', i], skill_choose )
                    return
        print('skill not found') 
    def modify_skills():
        skill_select = mod.proper_input('str')
        option = mod.proper_input('str')
        for i, k in enumerate(character[0]['skills']):
            if skill_select != k:
                continue
            if option == 'unequip':
                mod.file_modification('character.json',[0, 'skills', i], None)
            elif option == 'exit':
                pass
                #put function that returns to menu here. 
        pass
    def skill_upgrade():
        skill_select = mod.proper_input('str')
        i
    def skill_info():
        pass
    def browse_skills():
        pass
Skills.choose_skills()