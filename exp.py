#messing around with pygame(experimental)

import pygame
from sys import exit
from PIL import Image

pygame.init()
screen = pygame.display.set_mode()
Clock = pygame.time.Clock()
test_forest = pygame.image.load('sprites/forest.png').convert()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    new_image = pygame.transform.scale(test_forest,(500, 1200))
    screen.blit(new_image,(0, 0))
    pygame.display.update()
    Clock.tick(60)
    
    



