import pygame 
from pygame.locals import *
pygame.init() 
game_display = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption('My First Game') 
def event_handler(): 
    for event in pygame.event.get(): 
        if (event.type == QUIT): 
            pygame.quit() 
            quit() 
while True: 
    event_handler() 
    pygame.display.update()