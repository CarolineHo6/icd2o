import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame

pygame.init()

screen = pygame.display.set_mode([400, 400])
pygame.display.set_caption("Elephant Flag")

WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
GREY = (150, 150, 150)

while True:
    screen.fill(WHITE)

    # Flag Pole
    pygame.draw.rect(screen, (100,100,100), (5, 30, 10, 300))
    pygame.draw.circle(screen, (75,75,75), (10, 21), 10)

    # Flag
    pygame.draw.rect(screen, BLACK, (15, 30, 275, 165))

    # Elephant
    pygame.draw.lines(screen, (0,0,0), True, [(100, 50), (200, 55), (250, 80), (190, 150), (140, 150)], 3)
    pygame.draw.lines(screen, (0,0,0), True, [(250, 80), (190, 150), (250, 150)], 3)
    pygame.draw.lines(screen, (0,0,0), True, [(190, 150), (250, 150), (250, 165), (210, 170)], 3)
    pygame.draw.lines(screen, (0,0,0), True, [(250, 80), (250 ,110), (275, 113)], 3)
    pygame.draw.lines(screen, (0,0,0), True, [(90, 110), (93, 170), (110, 180), (200, 100), (90, 70)], 3)
    pygame.draw.lines(screen, (0,0,0), True, [(90, 110), (167, 117), (167, 75), (158, 72)], 3)
    pygame.draw.lines(screen, (0,0,0), True, [(90, 110), (158, 72), (95, 45)], 3)
    pygame.draw.lines(screen, (0,0,0), True, [(32, 90), (28, 93), (31, 94), (34, 92)], 3)
    pygame.draw.lines(screen, (0,0,0), True, [(50, 115), (60, 105), (37, 90), (32, 90)], 3)
    pygame.draw.lines(screen, (0,0,0), True, [(95, 45), (90, 110), (50, 115), (70, 60)], 3)
    
    '''pygame.draw.polygon(screen, (170, 170, 170), [(100, 50), (200, 55), (250, 80), (190, 150), (140, 150)])
    pygame.draw.polygon(screen, (90, 90, 90), [(250, 80), (190, 150), (250, 150)])
    pygame.draw.polygon(screen, (180, 180, 180), [(190, 150), (250, 150), (250, 165), (210, 170)])
    pygame.draw.polygon(screen, (100, 100, 100), [(250, 80), (250 ,110), (275, 113)])
    pygame.draw.polygon(screen, (195, 195, 195), [(90, 110), (93, 170), (110, 180), (200, 100), (90, 70)])
    pygame.draw.polygon(screen, (79, 79, 79), [(90, 110), (167, 117), (167, 75), (158, 72)])
    pygame.draw.polygon(screen, (190, 190, 190), [(90, 110), (158, 72), (95, 45)])
    pygame.draw.polygon(screen, (135, 135, 135), [(32, 90), (28, 93), (31, 94), (34, 92)])
    pygame.draw.polygon(screen, (205, 205, 205), [(50, 115), (60, 105), (37, 90), (32, 90)])
    pygame.draw.polygon(screen, (50, 50, 50), [(95, 45), (90, 110), (50, 115), (70, 60)])'''

    pygame.display.flip()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

