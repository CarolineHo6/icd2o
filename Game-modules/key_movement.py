import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame
import math

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

# Define game variables
clock = pygame.time.Clock()

player_radius = 10
player_color = BLUE
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5
projectile_speed = 15
game_over = False
circles = []

def create_circle(n,e,s,w):
    radius = 3
    color = BLACK
    x = player_x
    y = player_y
    y_vel = 0
    x_vel = 0
    if (n):
        y_vel = -projectile_speed
    elif (s):
        y_vel = projectile_speed
    
    if(e):
        x_vel = projectile_speed
    elif(w):
        x_vel = -projectile_speed
     
    circle = {'rect': pygame.Rect(x, y, 2*radius, 2*radius), 'color': color, 'radius': radius, 'x_vel': x_vel, 'y_vel':y_vel}
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
    clock.tick(60)  # Set the frame rate to 60 frames per second
    
    # Move player circle with keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
        player_x = max(player_x, player_radius)  # Ensure player does not move off the left edge
    if keys[pygame.K_d]:
        player_x += player_speed
        player_x = min(player_x, SCREEN_WIDTH - player_radius)  # Ensure player does not move off the right edge
    if keys[pygame.K_w]:
        player_y -= player_speed
        player_y = max(player_y, player_radius)  # Ensure player does not move off the top edge
    if keys[pygame.K_s]:
        player_y += player_speed
        player_y = min(player_y, SCREEN_HEIGHT - player_radius)  # Ensure player does not move off the bottom edge
    if keys[pygame.K_SPACE]:
        create_circle(keys[pygame.K_w],keys[pygame.K_d],keys[pygame.K_s],keys[pygame.K_a])
    # Draw player circle
    pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)

    for circle in circles:
        circle['rect'].x += circle['x_vel']
        circle['rect'].y += circle['y_vel']

        pygame.draw.circle(screen, circle['color'], circle['rect'].center, circle['radius'])

    # Refresh screen
    pygame.display.flip()


pygame.quit()
sys.exit()


