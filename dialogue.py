import time
import sys
import json

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)

def dialogue(x):
    with open('dialogue.json') as dialogu:
        dialogue = json.load(dialogu)
    for i, k in enumerate(dialogue[x]):
        delay_print(dialogue[x][i])
        input()
        print(''' ''')
