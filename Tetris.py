import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame
import random

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Shapes of Tetris blocks
SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
     [2, 2, 0]],

    [[3, 3, 0],
     [0, 3, 3]],

    [[4, 0, 0],
     [4, 4, 4]],

    [[0, 0, 5],
     [5, 5, 5]],

    [[6, 6],
     [6, 6]],

    [[7, 7, 7, 7]]
]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

# Functions
def draw_block(x, y, color):
    pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def new_piece():
    shape = random.choice(SHAPES)
    piece = {
        'shape': shape,
        'x': GRID_WIDTH // 2 - len(shape[0]) // 2,
        'y': 0
    }
    return piece

def draw_piece(piece):
    shape = piece['shape']
    x = piece['x']
    y = piece['y']
    color = colors[shape[0][0]]
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] != 0:
                draw_block(x + j, y + i, color)

def move_piece(piece, dx, dy):
    piece['x'] += dx
    piece['y'] += dy

def is_collision(piece, dx, dy):
    shape = piece['shape']
    x = piece['x'] + dx
    y = piece['y'] + dy
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] != 0:
                if x + j < 0 or x + j >= GRID_WIDTH or y + i >= GRID_HEIGHT:
                    return True
    return False

# Main loop
piece = new_piece()
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the piece down
    if not is_collision(piece, 0, 1):
        move_piece(piece, 0, 1)
    else:
        # Place the piece and create a new one
        # (For simplicity, we don't remove completed lines)
        piece = new_piece()

    draw_piece(piece)

    pygame.display.flip()
    clock.tick(5)  # Adjust the speed of falling pieces

pygame.quit()