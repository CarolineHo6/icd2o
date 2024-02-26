import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame

# Initialize Pygame
pygame.init()

# Seting the display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Car Drawing")

# Setting colour
WHITE = (255, 255, 255)
GREEN = (0, 255, 94)
BLACK = (0, 0, 0)

# MAin lOop
while True:
    screen.fill(WHITE)

    # Car body
    pygame.draw.rect(screen, GREEN, (50, 100, 100, 50))
    pygame.draw.rect(screen, GREEN, (25, 125, 25, 25))

    # Windows
    pygame.draw.rect(screen, BLACK, (55, 105, 35, 20))
    pygame.draw.rect(screen, BLACK, (110, 105, 35, 20))

    # Wheels
    pygame.draw.circle(screen, BLACK, (50, 150), 10)
    pygame.draw.circle(screen, BLACK, (130, 150), 10)

    # Update display
    pygame.display.flip()

    # For Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

