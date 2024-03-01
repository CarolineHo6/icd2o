import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame
import math

pygame.init()

screen = pygame.display.set_mode([900, 700])
pygame.display.set_caption("Elephant")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLACK = (0,0,0)
GREY = (200,200,200)

while True:
    screen.fill(WHITE)

    #House
    pygame.draw.rect(screen, BLUE, (150, 300, 200, 150))  # (x, y, width, height)
    pygame.draw.polygon(screen, BROWN, [(150, 300), (250, 200), (350, 300)])
    pygame.draw.rect(screen, BROWN, (225, 380, 50, 70))
    pygame.draw.circle(screen, YELLOW, (200, 330), 20)  # Window 1
    pygame.draw.circle(screen, YELLOW, (300, 330), 20)  # Window 2

    # Trees
    pygame.draw.rect(screen, BROWN, (80, 350, 40, 100))  # (x, y, width, height)
    pygame.draw.polygon(screen, GREEN, [(0, 350), (100, 200), (200, 350)])
    pygame.draw.polygon(screen, GREEN, [(20, 300), (100, 150), (180, 300)])
    pygame.draw.polygon(screen, GREEN, [(40, 250), (100, 120), (160, 250)])

    pygame.draw.rect(screen, BROWN, (430, 350, 40, 100))  # (x, y, width, height)
    pygame.draw.polygon(screen, GREEN, [(400, 350), (450, 200), (500, 350)])
    pygame.draw.polygon(screen, GREEN, [(400, 300), (450, 150), (500, 300)])
    pygame.draw.polygon(screen, GREEN, [(400, 250), (450, 120), (500, 250)])

    # Car
    pygame.draw.rect(screen, GREEN, (50, 500, 100, 50))
    pygame.draw.rect(screen, GREEN, (25, 525, 25, 25))
    pygame.draw.rect(screen, BLACK, (55, 505, 35, 20))
    pygame.draw.rect(screen, BLACK, (110, 505, 35, 20))
    pygame.draw.circle(screen, BLACK, (50, 550), 10)
    pygame.draw.circle(screen, BLACK, (130, 550), 10)

    # Sun
    pygame.draw.circle(screen, (YELLOW), (750, 150), 75)
    pygame.draw.line(screen, (YELLOW), (650, 50), (680, 80), 20)
    pygame.draw.line(screen, (YELLOW), (750, 25), (750, 55), 20)
    pygame.draw.line(screen, (YELLOW), (850, 50), (820, 80), 20)
    pygame.draw.line(screen, (YELLOW), (850, 150), (880, 150), 20)
    pygame.draw.line(screen, (YELLOW), (825, 200), (855, 230), 20)
    pygame.draw.line(screen, (YELLOW), (750, 250), (750, 280), 20)
    pygame.draw.line(screen, (YELLOW), (650, 260), (680, 230), 20)
    pygame.draw.line(screen, (YELLOW), (650, 150), (610, 150), 20)

    # Stick Man
    pygame.draw.circle(screen, BLACK, (200, 500), 10, 2)
    pygame.draw.line(screen, BLACK, (200, 510), (200, 530), 2)
    pygame.draw.lines(screen, BLACK, False, [(190, 540), (200, 530), (210, 540)], 2)
    pygame.draw.lines(screen, BLACK, False, [(190, 530), (200, 520), (210, 530)], 2)

    # Flag
    pygame.draw.rect(screen, GREY, (500, 300, 10, 175))
    pygame.draw.rect(screen, BLUE, (510, 300, 60, 40))
    pygame.draw.arc(screen, GREEN, pygame.Rect(515, 305, 55, 35), 0, 2*math.pi/2, 2)

    pygame.display.flip()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

