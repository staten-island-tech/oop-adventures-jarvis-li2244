import time
import sys
import json

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.075)

def dialogue():
    with open('dialogue.json') as dialogu:
        dialogue = json.load(dialogu)
    for i, (v, k) in enumerate(dialogue.items()):
        for i in range(len(k)):
            delay_print(k[i])
            if input() != 121809901490199023904092490242904920429042904:
                pass
            print('''

''')
dialogue()