import time
import random
color_red = "\033[91m"
color_purple = "\33[95m"
color_blue1 = "\33[34m"
color_blue2 = "\33[36m"
color_blue3 = "\33[96m"
color_green1 = "\033[92m"
color_green2 = "\033[32m"
color_brown = "\33[33m"
color_yellow = "\33[93m"
color_grey = "\33[37m"
color_default = "\033[0m"
x = 91
health_dis = 0
def health_display(max, current):

    teegreg = max/100
    max1 =int(max/teegreg)
    current1 = int(current/teegreg)
    print(f'{color_default}ENEMY HEALTH: {current}/{max}')
    yes_health = int(current1/4) * "█"
    no_health = int((max1 - current1)/4) * "▒"
    yes_health1 = int(current1/4) * "▌"
    no_health1 = int((max1 - current1)/4) * "║"
    if health_dis == 0:
        print(f'{color_default}╔═════════════════════════╗' )
        print(f'║\033[1;{x};40m{yes_health}{no_health}{color_default}║')
        print(f'{color_default}╚═════════════════════════╝' )
    elif health_dis == 1:
        print(f'{color_default}╔═════════════════════════╗' )
        print(f'║\033[1;{x};40m{yes_health1}{no_health1}{color_default}║')
        print(f'{color_default}╚═════════════════════════╝' )
def battle_gui():
    print(r"""
╔═════════╗ ╔═════════╗ 
║         ║ ║         ║ 
║   ATK   ║ ║   RUN   ║ 
║         ║ ║         ║   
╚═════════╝ ╚═════════╝ 
╔═════════╗ ╔═════════╗
║         ║ ║         ║
║  EQUIP  ║ ║  ITEMS  ║
║         ║ ║         ║  
╚═════════╝ ╚═════════╝
            """)
def actions():
    ere =int(input(""))
    atk_gui() if ere == 1 else(run_gui() if ere == 2 else(equip_gui() if ere == 3 else(items_gui() if ere == 4 else actions())))
def run_gui():
    #dodge will factor into whether you lose stuff when you run away or not 
    dodge = int(100)
    roll = int(100/dodge)
    if random.randint(1, roll) == random.randint(1,roll):
        print(r""" 

        ╔═════════════════════════╗
        ║     ESCAPE SUCESSFUL    ║
        ╚═════════════════════════╝
            """)
    else:
        print(r""" 
        ╔═════════════════════════╗
        ║      ESCAPE FAILED      ║
        ╚═════════════════════════╝
            """)
    
def atk_gui():
    var1 = 4564456
    print(f"""
╔═════════════════════════╗
║    {var1} DMG Dealt     ║
╚═════════════════════════╝
        """)
def equip_gui():
    print(r"""
        """)
def items_gui():
    item_name = "EGG"
    print(f'''
══════════════════════════════════
1. {item_name}                             
══════════════════════════════════
2. {item_name}                             
══════════════════════════════════
3. {item_name}                             
══════════════════════════════════
4. {item_name}                             
══════════════════════════════════
5. {item_name}                             
══════════════════════════════════
6. {item_name}                             
══════════════════════════════════
7. {item_name}                             
══════════════════════════════════
8. {item_name}                             
══════════════════════════════════
9. {item_name}                             
══════════════════════════════════
            ''')
y = 34
def item_desc():
    print(r"""







            """)

#settings for health and mana bars to simplify them 102102010 to 100
def settings_GUI():
    print(r"""





        """)
def attack():
    print("ATTACK!!")
    a = input("")



class Tutorial():
    def battle_gui_tutorial():
        print("For each square in the battle GUI, a number is assigned. Press the number below and enter it to select that option. Here's a visual of the loadout. Why don't you try it out?")
        print(r"""
               GUI               






              """)
class Sprites():
    def intro_screen():
        print(r"""
    _    ____   ____ ___ ___    ____  ____   ____ 
   / \  / ___| / ___|_ _|_ _|  |  _ \|  _ \ / ___|
  / _ \ \___ \| |    | | | |   | |_) | |_) | |  _ 
 / ___ \ ___) | |___ | | | |   |  _ <|  __/| |_| |
/_/   \_\____/ \____|___|___|  |_| \_\_|    \____|
                            
                By: Jarvis and Johnny
                         _
                        ( )
                        \|/
                         |
                        / \      
""")
        print("WELCOME TO AN ASCII RPG GAME")
        print("Credit for ASCII ART: (if any)")
        if input("CLICK ENTER TO START : "):
            Sprites.adjust()
    def boss_screen():
        print(r"""
______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
                                                                                 ____   ___  ____ ____    ____    _  _____ _____ _     _____ _   _   _ 
                                                                                | __ ) / _ \/ ___/ ___|  | __ )  / \|_   _|_   _| |   | ____| | | | | |
                                                                                |  _ \| | | \___ \___ \  |  _ \ / _ \ | |   | | | |   |  _| | | | | | |
                                                                                | |_) | |_| |___) |__) | | |_) / ___ \| |   | | | |___| |___|_| |_| |_|
                                                                                |____/ \___/|____/____/  |____/_/   \_\_|   |_| |_____|_____(_) (_) (_)        
______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
            """)
    def fight_screen():
        print(r"""
              


______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
                                                                                                 _____ ___ ____ _   _ _____ _   _   _  
                                                                                                |  ___|_ _/ ___| | | |_   _| | | | | | 
                                                                                                | |_   | | |  _| |_| | | | | | | | | | 
                                                                                                |  _|  | | |_| |  _  | | | |_| |_| |_| 
                                                                                                |_|   |___\____|_| |_| |_| (_) (_) (_) 
______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

              


""")
        time.sleep(1)
    def adjust():
        print("----------")
        print("Please use this to adjust your terminal and ensure gameplay is able to be properly displayed")
        print("Match your terminal display size to the proper dimensions")
        print("Once done just click enter")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("----------")
        egg = input("")
        if egg != "rreigghuiehuigehuigeuhigeuighehiugehiugehiugehiugrehiugeihugeghiurehgiegihuregiuheghiuregihueghiueghierghiuerghiuergihuvidfuhdihugehirugreiouhgrehiugeriuhgerhioug":
            print("egg")
        
    def sprite0():
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
        print("")
    def sprite1():
        print(r"""
    GHOST ATTACK!!!
          ___
        \/   \/
        |\o o/|  
        |  0  |
        \     |
         \    /
          \  / 
           \|
           """)
    def sprite2():
        print(r"""
      GHOST DEAD
          ___
        \/   \/
        |\x x/|  
        |  0  |
        \     |
         \    /
          \  / 
           \|
           """)
    def sprite3():
        print(r"""
 

         JAY    
          _
         ( )
         \|/
          |
         / \          
           """)
    def sprite4():
        print(r"""

                DA ANT

     \   / 
      \ /  |\_|\_|\    ︵︵︵︵
     |o o|/| \| \| \  /        \
      \ / \|__|__|_ / \        /
      { }  |  |  |     ︶︶︶︶



          """)
    def sprite5():
        print(r"""

            DA DEAD ANT

     \   / 
      \ /  |\_|\_|\    ︵︵︵︵
     |x x|/| \| \| \  /        \
      \ / \|__|__|_ / \        /
      { }  |  |  |     ︶︶︶︶



          """)
    def placeholder0():
        print(r"""




           """)
    def test():
        print(r"""

   \ _________
O|--|_________>
   /




""")
    def axe():
        print(r"""


        ⌢
  0-----\/




""")
    def slime():
        print(r"""
     _ _
  .-’   ‘-.
 /  ^   ^  \
|           |
\    \__/   /
 `-._____.-'
""")
    def YALIKEJAZZ():
        print(r"""

                                                                                            __   __ _      _     ___ _  _______       _   _     _____________ 
                                                                                            \ \ / // \    | |   |_ _| |/ / ____|     | | / \   |__  /__  /__ \
                                                                                             \ V // _ \   | |    | || ' /|  _|    _  | |/ _ \    / /  / /  / /
                                                                                              | |/ ___ \  | |___ | || . \| |___  | |_| / ___ \  / /_ / /_ |_| 
                                                                                              |_/_/   \_\ |_____|___|_|\_\_____|  \___/_/   \_\/____/____|(_) 

        """)
Sprites.axe()
Sprites.sprite4()
health_display(100, 80)
battle_gui()
actions()
Sprites.sprite5()
health_display(100, 0)
Sprites.boss_screen()
time.sleep(1)
Sprites.fight_screen()
Sprites.slime()
#might not need but code for updating dicts(inventory f
# or example)
#add new space below like this:

#to sort(sort function basically)
"""inv = { 
    'Sword' : 1,
    'Potion' : 3
}
loot  = { 
    'Sword' : 1,
    'Potion' : 2,
    'Shield' : 1
}
new_inv = {  
    k: inv.get(k, 0) + loot.get(k, 0)
    for k in set(inv | loot)

}
print(new_inv)"""
