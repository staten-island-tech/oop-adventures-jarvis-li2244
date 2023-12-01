
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

x = 31
def health_display():
    max = 100
    current = 80
    teegreg = max/100
    max1 =int(max/teegreg)
    current1 = int(current/teegreg)
    print(f'{color_default}ENEMY HEALTH: {current}/{max}')
    yes_health = int(current1/5) * "█"
    no_health = int((max1 - current1)/5) * "▒"
    print(f'\033[1;{x};40m{yes_health}{no_health}\n')
y = 34
def mana_display():
    max = 1901904290
    current = 1301904290
    teegreg = max/100
    max1 =int(max/teegreg)
    current1 = int(current/teegreg)
    print(f'{color_default}ENEMY MANA: {current}/{max}')
    yes_health = int(current1/5) * "█"
    no_health = int((max1 - current1)/5) * "▒"
    print(f'\033[1;{y};40m{yes_health}{no_health}\n')

#settings for health and mana bars to simplify them 102102010 to 100



class Sprites():
    def sprite1():
        print("""
         GHOST
          ___
        \/   \/
        |\O O/|  
        |  0  |
        \     |
         \  _/
          \|
        """)
Sprites.sprite1()
health_display()