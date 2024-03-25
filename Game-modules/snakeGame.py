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
pygame.display.set_caption("Key Mover")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Define game variables
player_radius = 10
player_color = BLUE
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 2
projectile_speed = 15
game_over = False
circles = []

# Function to create new circles
def create_circle():
    #circles.clear()  # Clear existing circles
    radius = random.randint(10, 30)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    x = random.randint(0, SCREEN_WIDTH - 2*radius)
    y = random.randint(0, SCREEN_HEIGHT - 2*radius)
    circle = {'rect': pygame.Rect(x, y, 2*radius, 2*radius), 'color': color, 'radius': radius}
    circles.append(circle)

while True:
    screen.fill(GREEN)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    # Keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
        player_x = max(player_x, player_radius)
    elif keys[pygame.K_d]:
        player_x += player_speed
        player_x = min(player_x, SCREEN_WIDTH - player_radius)
    elif keys[pygame.K_w]:
        player_y -= player_speed
        player_y = max(player_y, player_radius)
    elif keys[pygame.K_s]:
        player_y += player_speed
        player_y = min(player_y, SCREEN_HEIGHT - player_radius)
    # Draw player circle
    pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)

    # Refresh screen
    pygame.display.flip()

