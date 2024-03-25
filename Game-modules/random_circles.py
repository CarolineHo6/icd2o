import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame
import math
import random

# Initialize Pygame
pygame.init()


# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Random Circle Generator")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define game variables
clock = pygame.time.Clock()
circles = []

# Function to create new circles
def create_circle():
    radius = random.randint(5, 20)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    x = random.randint(0, SCREEN_WIDTH - 2*radius)  # make sure the whole circle can appear on the screen
    y = random.randint(0, SCREEN_HEIGHT - 2*radius)
    circle = {'rect': pygame.Rect(x, y, 2*radius, 2*radius), 'color': color, 'radius': radius}
    circles.append(circle)
# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     # Control the frame rate
    clock.tick(5)  # Set the frame rate to 60 frames per second
    
    # Draw game elements
    for circle in circles:
        pygame.draw.circle(screen, circle['color'], circle['rect'].center, circle['radius'])

    if len(circles) <= 10:
        create_circle()

    # Refresh screen
    pygame.display.flip()


pygame.quit()
sys.exit()
