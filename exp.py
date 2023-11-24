#messing around with pygame

import pygame
from sys import exit
screen = pygame.display.set_mode((1000,750))
pygame.display.set_caption('GUNGAME')
clock = pygame.time.Clock()
test_surface = pygame.Surface((100, 200))
test_surface.fill('white')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
    screen.blit(test_surface, (200, 100))
    pygame.display.update() 
    clock.tick(60)



