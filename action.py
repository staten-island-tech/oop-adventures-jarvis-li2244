import json
import os
import math
import choose
import creation
import change
from change import characterNum, statsNum, inventorysNum

#json files being altered
with open("character.json", "r") as f:
    jcharacter = json.load(f)

with open("stats.json", "r") as f:
    jstats = json.load(f)

with open("inventorys.json", "r") as f:
    jinventorys = json.load(f)


#json files for info
with open("role.json", "r") as f:
    jrole = json.load(f)

with open("skilltree.json", "r") as f:
    jskilltree = json.load(f)

with open("skills.json", "r") as f:
    jskills = json.load(f)

with open("location.json", "r") as f:
    jlocation = json.load(f)

with open("story.json", "r") as f:
    jstory = json.load(f)        

class ActionC:
    def locationSwitch():
        change.ChangeC.characterNum()
        creation.Info.locationInfo()
        outer = 0
        while outer == 0:
            inner = 0
            locationGo = input("Where do you want to go? ('quit' to end): ").lower()
            if locationGo == "quit":
                break
            for i in range(len(jlocation)):
                if jlocation[i]["location"].lower() == locationGo:
                    for j in range(len(jstory)):
                        if jstory[j]["story"].lower() == jlocation[i]["story"].lower():
                            story = jstory[j]["numEquivalent"]
                            return story
                    for j in range(len(jstory)):
                        if jstory[j]["story"].lower() == jcharacter[characterNum]["story"].lower():
                            storyY = jstory[j]["numEquivalent"]
                            return storyY
                    if storyY < story:
                        print("Unable to travel: Story not advanced enough.")
                        inner = 1
                    else:
                        change.ChangeC.setLocation(locationGo)
                        updateJSONC()
                        creation.Info.nlocationInfo()
                        outer = 1
                        inner = 1
            if inner == 0:
                print("That location does not exist.")

class ActionS:
    def stat_pointsSpend(stat_points):
        change.ChangeS.statsNum()
        creation.Info.statsInfo()
        if stat_points > jstats[statsNum]["stat_points"]:
            print(""), print("You do not have that many stat points.")
            print(f'Stat Points: {jstats[statsNum]["stat_points"]}')
        else:
            outer = 0
            while outer == 0:
                statUpgraded = input("Use stat points on Max_Health, Attack, Defense, Speed, or Mana: ").lower()
                if statUpgraded == "max_health" or "maxhealth" or "max health":
                    change.ChangeS.stat_pointsSubtract(stat_points)
                    change.ChangeS.max_healthAdd(stat_points)
                    change.ChangeS.healthAdd(stat_points)
                    outer = 1
                elif statUpgraded == "attack":
                    change.ChangeS.stat_pointsSubtract(stat_points)
                    change.ChangeS.attackAdd(stat_points)
                    outer = 1
                elif statUpgraded == "defense":
                    change.ChangeS.stat_pointsSubtract(stat_points)
                    change.ChangeS.defenseAdd(stat_points)
                    outer = 1
                elif statUpgraded == "speed":
                    change.ChangeS.stat_pointsSubtract(stat_points)
                    change.ChangeS.speedAdd(stat_points)
                    outer = 1
                elif statUpgraded == "mana":
                    change.ChangeS.stat_pointsSubtract(stat_points)
                    change.ChangeS.manaAdd(stat_points)
                    outer = 1
                else:
                    print("That is not a valid input.")
            updateJSONS()
            creation.Info.nstatsInfo()

class ActionIS:
    def skill_pointsSpend():
        change.ChangeC.characterNum()
        change.ChangeIS.inventorysNum()
        role = jcharacter[characterNum]["role"]
        for i in range(len(jrole)):
            if jrole[i]["role"] == role:
                skilltree = jrole[i]["skilltree"]
        for i in range(len(jskilltree)):
            if jskilltree[i]["skilltree"] == skilltree:
                skilltreeY = jskilltree[i]
                print(""), print("Skill Tree Info")
                print(skilltreeY)
        creation.Info.inventorysInfo()
        print("")
        print(f'Skill Points: {jinventorys[inventorysNum]["skill_points"]}')        
        skill_points = jinventorys[inventorysNum]["skill_points"]
        outer = "n"
        while outer == "n":
            inner = 0
            skillBuy = input("What skill would you like to purchase? ('quit' to end): ").lower()
            if skillBuy == "quit":
                break
            for i in skilltreeY:
                for j in skilltreeY[i]:
                    if len(j) > 1:
                        if skillBuy.lower() == j.lower():
                            inner += 1
                            for k in range(len(jskills)):
                                if jskills[k]["name"].lower() == skillBuy:
                                    skillY = jskills[k]
            if inner == 0:
                print("That skill does not exist.")
            else:
                creation.Info.skillsInfo_specific(skillBuy)
                outin = 0
                while outin == 0:
                    confirm = input("Are you sure you want to purchase this skill? Y/N: ").lower()
                    if confirm == "y":
                        outer = "y"
                        outin = 1
                    elif confirm == "n":
                        outer ="n"
                        outin = 1
                    else:
                        print("That is not a valid input.")
        if skillBuy != "quit":
            if skillY["cost"] > skill_points:
                print(""), print("You do not have enough skill points.")
                print(f'Skill Points: {jinventorys[inventorysNum]["skill_points"]}')
            else:
                inner2 = 0
                for i in jinventorys[inventorysNum]:
                    if i == "id":
                        donothing = 0
                    elif i == "skill_points":
                        donothing = 0
                    else:
                        for j in jinventorys[inventorysNum][i]:
                            if skillBuy == j.lower():
                                print("You already own that skill.")
                                inner2 += 1
            if inner2 == 0:
                change.ChangeIS.skill_pointsSubtract(skillY["cost"])
                if skillY["level"] == "Level_1_Skills":
                    change.ChangeIS.InsertLevel_1_Skills(skillY["name"])
                elif skillY["level"] == "Level_2_Skills":
                    change.ChangeIS.InsertLevel_2_Skills(skillY["name"])
                elif skillY["level"] == "Level_3_Skills":
                    change.ChangeIS.InsertLevel_3_Skills(skillY["name"])
                elif skillY["level"] == "Level_4_Skills":
                    change.ChangeIS.InsertLevel_4_Skills(skillY["name"])
                elif skillY["level"] == "Level_5_Skills":
                    change.ChangeIS.InsertLevel_5_Skills(skillY["name"])
                else:
                    print("Unknown Error")
                updateJSONIS()
                creation.Info.ninventorysInfo()


def updateJSONC():
    new_file = "updated.json"
    with open(new_file, "w") as f:

        json_string = json.dumps(jcharacter, indent=4)

        f.write(json_string)

    os.remove("character.json")
    os.rename(new_file, "character.json")

def updateJSONS():
    new_file = "updated.json"
    with open(new_file, "w") as f:

        json_string = json.dumps(jstats, indent=4)

        f.write(json_string)

    os.remove("stats.json")
    os.rename(new_file, "stats.json")

def updateJSONIS():
    new_file = "updated.json"
    with open(new_file, "w") as f:

        json_string = json.dumps(jinventorys, indent=4)

        f.write(json_string)

    os.remove("inventorys.json")
    os.rename(new_file, "inventorys.json")