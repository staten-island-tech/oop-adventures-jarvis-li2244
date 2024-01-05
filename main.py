import interactivegui
import item
import recipes
import map
def game_start():
    print('click enter to start')
    if input() == '':
        print('game start')
    else:
        game_start()