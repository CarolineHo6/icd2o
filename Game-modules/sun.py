import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame

# Initialize Pygame
pygame.init()

# Seting the display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sun Drawing")

# Setting colour
WHITE = (255, 255, 255)
SKY = (153, 255, 255)
YELLOW = (255, 255, 102)

# MAin lOop
while True:
    screen.fill(SKY)

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

    # Update display
    pygame.display.flip()

    # For Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()