

from pynput import keyboard

x = 0
y = 0
movement= True
print('Press w to move forward  or n to continue:')
location = False 
with keyboard.Events() as events:
    event = events.get(1e6)
    while movement == True:
        event.key
        if event.key == keyboard.KeyCode.from_char('w'):
            x += 1 
        if event.key == keyboard.KeyCode.from_char('s'):
            x -= 1 
        if event.key == keyboard.KeyCode.from_char('a'):
            y -= 1 
        if event.key == keyboard.KeyCode.from_char('d'):
            y += 1 
        if x or y >= 5 or x or y >= -1:
            movement == False
    print(f'position: {x},{y}')
#do [ip install pynput
print(location)