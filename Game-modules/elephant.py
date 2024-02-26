import pygame
import math
import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Elephant")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

# Define elephant parameters
elephant_width = 200
elephant_height = 100

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw elephant body
    pygame.draw.ellipse(screen, GRAY, [width/2 - elephant_width/2, height/2 - elephant_height/2, elephant_width, elephant_height])

    # Draw elephant ears
    pygame.draw.ellipse(screen, GRAY, [width/2 - elephant_width/2 - elephant_width/4, height/2 - elephant_height/2 - elephant_height/2, elephant_width/2, elephant_height])
    pygame.draw.ellipse(screen, GRAY, [width/2 + elephant_width/2, height/2 - elephant_height/2 - elephant_height/2, elephant_width/2, elephant_height])

    # Draw elephant eyes
    pygame.draw.ellipse(screen, BLACK, [width/2 - elephant_width/4, height/2 - elephant_height/4, elephant_width/8, elephant_height/8])
    pygame.draw.ellipse(screen, BLACK, [width/2 + elephant_width/8, height/2 - elephant_height/4, elephant_width/8, elephant_height/8])

    # Draw elephant trunk
    pygame.draw.rect(screen, GRAY, [width/2 + elephant_width/4, height/2, elephant_width/2, elephant_height/4])

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()