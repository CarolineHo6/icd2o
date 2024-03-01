import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame
import math

# Initialize display
pygame.init()

# Make display and caption
screen = pygame.display.set_mode([500, 800])
pygame.display.set_caption("Mini Project - Scene")

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SKY = (204, 255, 255)
BROWN = (153, 76, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 102)
GREY = (125, 125, 125)

# Main Loop
while True:
    screen.fill(SKY)

    # Ground
    pygame.draw.rect(screen, GREEN, (0, 600, 1000, 200))

    # House
    pygame.draw.rect(screen, BROWN, (100, 550, 100, 100))
    pygame.draw.polygon(screen, RED, [(75, 550), (225, 550), (150, 500)])
    pygame.draw.rect(screen, BLUE, (140, 620, 20, 30))
    pygame.draw.circle(screen, BLACK, (130, 575), 15)
    pygame.draw.circle(screen, BLACK, (170, 575), 15)

    # Car
    pygame.draw.polygon(screen, RED, [(270, 580), (280, 570), (290, 570), (300, 580)])
    pygame.draw.rect(screen, RED, (245, 580, 65, 20))
    pygame.draw.circle(screen, BLACK, (265, 600), 5)
    pygame.draw.circle(screen, BLACK, (300, 600), 5)
    pygame.draw.polygon(screen, BLACK, [(273, 579), (283, 572), (288, 572), (298, 579)])

    # Sun
    # Body of sun
    pygame.draw.circle(screen, (YELLOW), (150, 150), 75)

    # Lines
    pygame.draw.line(screen, (YELLOW), (50, 50), (80, 80), 20)
    pygame.draw.line(screen, (YELLOW), (150, 25), (150, 55), 20)
    pygame.draw.line(screen, (YELLOW), (250, 50), (220, 80), 20)
    pygame.draw.line(screen, (YELLOW), (250, 150), (280, 150), 20)
    pygame.draw.line(screen, (YELLOW), (225, 200), (255, 230), 20)
    pygame.draw.line(screen, (YELLOW), (150, 250), (150, 280), 20)
    pygame.draw.line(screen, (YELLOW), (50, 260), (80, 230), 20)
    pygame.draw.line(screen, (YELLOW), (50, 150), (10, 150), 20)

    # Stop sign
    pygame.draw.rect(screen, GREY, (412, 560, 6, 50))
    pygame.draw.polygon(screen, RED, [(400, 550), (410, 540), (420, 540), (430, 550), (430, 560), (420, 570), (410, 570), (400, 560)])

    # Road
    pygame.draw.rect(screen, GREY, (420, 600, 50, 200))
    pygame.draw.rect(screen, WHITE, (443, 600, 5, 200))

    # Thing
    pygame.draw.ellipse(screen, BLACK, pygame.Rect(350, 580, 20, 15), 3)
    pygame.draw.line(screen, BLACK, (360, 595), (360, 615), 3)
    pygame.draw.lines(screen, BLACK, False, [(350, 625), (360, 615), (370, 625)])
    pygame.draw.lines(screen, BLACK, False, [(350, 595), (360, 605), (370, 595)])

    pygame.display.flip()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

