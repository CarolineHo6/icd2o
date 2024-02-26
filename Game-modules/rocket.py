import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame

# Initialize Pygame
pygame.init()

# Seting the display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rocket Drawing")

# Setting colour
WHITE = (255, 255, 255)
SILVER = (224, 224, 224)
GREY = (60, 60, 60)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# MAin lOop
while True:
    screen.fill(GREY)

    # Rocket Body
    pygame.draw.rect(screen, SILVER, (100, 150, 75, 200))
    pygame.draw.polygon(screen, (SILVER), [(100, 150), (175, 150), (137, 100)])

    # Fins
    pygame.draw.rect(screen, SILVER, (100, 350, 30, 10))
    pygame.draw.rect(screen, (SILVER), (145, 350, 30, 10))

    # Design
    pygame.draw.circle(screen, (BLACK), (137, 180), 25)
    pygame.draw.circle(screen, (RED), (137, 180), 20)

    # Update display
    pygame.display.flip()

    # For Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

