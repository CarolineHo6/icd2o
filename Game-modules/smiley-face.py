import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame
import math
pygame.init()
# Set up the display
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Smiley Face Drawing")
# Define colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
# Main loop
while True:
    screen.fill(WHITE)  # Fill the screen with white color
    
    # Draw the face (circle)
    pygame.draw.circle(screen, YELLOW, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 150)
    
    # Draw the eyes (circles)
    pygame.draw.circle(screen, BLACK, (150, 150), 20)
    pygame.draw.circle(screen, BLACK, (250, 150), 20)
    
    # Draw the mouth (arc)
    pygame.draw.arc(screen, BLACK, (100, 155, 200, 125), math.pi, 2 * math.pi, 6)
    
    # Update the display
    pygame.display.flip()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
