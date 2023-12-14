

from pynput import keyboard


print('Press w to move forward  or n to continue:')
location = False 
with keyboard.Events() as events:
    # Block for as much as possible
    event = events.get(1e6)
    location = True if event.key == keyboard.KeyCode.from_char('w') else()
#do [ip install pynput
print(location)