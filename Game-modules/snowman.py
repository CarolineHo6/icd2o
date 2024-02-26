import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame
import math

pygame.init()

SCREEN_WIDTH = 400
SCREEN_LENGTH = 400
screen = pygame.display.set_mode([SCREEN_LENGTH, SCREEN_WIDTH])
pygame.display.set_caption("Snowman Drawing")

# Colour
WHITE = (255, 255, 255)
SKY = (153, 255, 255)
BLACK = (0, 0, 0)

# Main loop
while True:
    screen.fill(SKY)

    # Snowman Body
    pygame.draw.circle(screen, WHITE, (80, 100), 30)
    pygame.draw.circle(screen, WHITE, (80, 150), 40)
    pygame.draw.circle(screen, WHITE, (80, 210), 50)

    # Eyes and buttons
    pygame.draw.circle(screen, BLACK, (70, 90), 3)
    pygame.draw.circle(screen, BLACK, (90, 90), 3)
    pygame.draw.circle(screen, BLACK, (80, 145), 5)
    pygame.draw.circle(screen, BLACK, (80, 170), 5)
    pygame.draw.circle(screen, BLACK, (80, 195), 5)

    # Smile
    pygame.draw.arc(screen, BLACK, pygame.Rect(60, 105, 40, 10), math.pi, 2*math.pi, 2)

    # Hat
    pygame.draw.rect(screen, BLACK, (60, 30, 40, 50))
    pygame.draw.rect(screen, BLACK, (45, 80, 70, 5))

    pygame.display.flip()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

