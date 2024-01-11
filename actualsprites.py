import time
import sys
import json

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)

def dialogue():
    with open('dialogue.json') as dialogu:
        dialogue = json.load(dialogu)
    for i, k in enumerate(dialogue['Tutorial: Act I']):
        print(i,k)
        for i in range(len(k)):
            delay_print(k)
            input()
            print(''' ''')
dialogue()