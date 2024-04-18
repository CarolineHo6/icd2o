import random
import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages') # If you have a sys.path line in your previous games you will need to replace this line with your sys.path. If you don't have a sys.path line just remove this one
import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 360
SPRITE_WIDTH = 256 // 4  # Width of a single sprite frame - Sprite sheet is 256 pixels across and there are 4 images in the row
SPRITE_HEIGHT = 256 // 4  # Height of a single sprite frame - Sprite sheet is 256 pixels high and there are 4 images in the column
NUM_ROWS = 4 #Number of rows on the sprite sheet
NUM_COLS = 4 # Number of columns on the sprite sheet
BACKGROUND_SCROLL_SPEED = 1  # Speed of background scrolling

# Background position
background_x = 0

# Load sprite sheet image
sprite_sheet = pygame.image.load("spritesheet.png")

# Extract individual frames. Load individual pics from sprite sheet into a list
sprite_frames = []
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        x = col * SPRITE_WIDTH
        y = row * SPRITE_HEIGHT
        sprite_frames.append(sprite_sheet.subsurface(pygame.Rect(x, y, SPRITE_WIDTH, SPRITE_HEIGHT)))

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Load background image
background_image = pygame.image.load("background.jpg")
background_rect = background_image.get_rect()

# Player position and movement
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 5

# Animation variables. These will allow us to find the appropriate frame in the list
current_animation = 0  # 0: down, 1: left, 2: right, 3: up
frame_index = 0
animation_speed = 0.2  # Seconds per frame

# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill screen with white

    # Scroll the background
    background_x -= BACKGROUND_SCROLL_SPEED
    if background_x < -background_rect.width:
        background_x = 0

    # Draw the background
    screen.blit(background_image, (background_x, 0))
    screen.blit(background_image, (background_x + background_rect.width, 0))
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
        current_animation = 1  # Set animation to left
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
        current_animation = 2  # Set animation to right
    if keys[pygame.K_UP]:
        player_y -= player_speed
        current_animation = 3  # Set animation to up
    if keys[pygame.K_DOWN]:
        player_y += player_speed
        current_animation = 0  # Set animation to down

    # Display current frame
    screen.blit(sprite_frames[current_animation * NUM_COLS + int(frame_index)], (player_x, player_y))

    # Update frame index for animation
    frame_index += animation_speed
    if int(frame_index) >= NUM_COLS:
        frame_index = 0

    pygame.display.flip()
    clock.tick(60)  # Limit frame rate to 60 FPS

pygame.quit()
sys.exit()
