from colorama import Fore
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


class ASCII():
    def sprite1():
        print(Fore.WHITE +'HEALTH 80 / 100')
        print(Fore.RED +'|████████████████▒▒▒▒|')
    def sprite2():
        print(Fore.WHITE +'MANA 80 / 100')
        print(Fore.BLUE +'|████████████████▒▒▒▒|')


 
def type():
    x = input("type of display: ")
    return x
def color():
    y = input("type of color")
    egg = "\033[91m"
    if y == "RED".lower():
        egg = "\033[91m"
    return egg
#attempt at health system 
def display(): 
    x = type()
    y = color()
    max = 100
    current = 80
    print(f'{x}: {current}/{max}')
    yes_health = int(current/5) * "█"
    no_health = int((max - current)/5) * "▒"
    print(f'{y} {yes_health}{no_health}  \n')
x = 31


def health_display():
    max = 100
    current = 82
    print(f'ENEMY HEALTH: {current}/{max}')
    yes_health = int(current/5) * "█"
    no_health = int((max - current)/5) * "▒"
    print(f'\033[1;{x};40m{yes_health}{no_health}\n')

health_display()

#health converter, changes a large number to 100
num = int(input("NUMBER: "))
def num_list():
    fact = []
    res = [int(x) for x in str(num)]
    return fact
def rounding(): 
    egg = num_list()
    tem1 = len(egg) - 1
    print(egg)
    for i in range(tem1): 
        LEG = 1 * 10
    if (egg[1]) > 4:
        num = num + LEG
    new_value = int(num/100) * 100
    return new_value
def factor(): 
        num = rounding()
        round(num)
        print("Factors of ",num," (only 100): ")
        for i in range(1, num + 1): 
            if num % i == 0 : 
                if i == 100:
                    e = i
                    egg = int(num/e)
                    return egg
            else:
                print("NO FACTORS")
def egg():
    elege = factor()
    print(elege)
egg()