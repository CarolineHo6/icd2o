import random
import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame
import os
import math
pygame.init()
pygame.mixer.init()

# Sound
fire = pygame.mixer.Sound('fire.wav')

#Screen
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 17)
life_levels = [25, 75, 125, 250, 500, 1000, 2000, 5000, 10000, 100000, 200000]
level = 0

# Define Variables
clock = pygame.time.Clock()
player_x = SCREEN_WIDTH//2
player_y = 650
player_width = 40
player_height = 20
player_speed = 2
score = 0

bullets = []
bullet_speed = 10
bullet_y = 625
bullet_x = 3
direction_angle = -90
allow_shoot = True
gameOver = False
width = 1

aliens = []
alien_x = 20
alien_y = 70
alien_vel = 3

barrier1 = []
barrier2 = []
barrier3 = []
barrier4 = []
b_y = 600

# Function to calculate the bounding box rectangle of a polygon
def calculate_bounding_box(polygon_points):
    min_x = player_x - 20
    max_x = player_x + 20
    min_y = player_y - 15
    max_y = player_y + 10
    bounding_box_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    return bounding_box_rect

# Create bullets
def create_bullet():
    angle_rad = math.radians(direction_angle)
    radius = 3
    color = GREEN
    if level == 10:
        color = WHITE
    y_vel = (player_speed + 3) * math.sin(angle_rad)
    x_vel = (player_speed + 3) * math.cos(angle_rad)
    x,y = calculate_bounding_box(player).center
    
    
    bullet = {'rect': pygame.Rect(x, y, 2*radius, 2*radius), 'color': color, 'radius': radius, 'x_vel': x_vel, 'y_vel':y_vel}
    bullets.append(bullet)

# Create aliens, make an array
def create_aliens():
    # Top row
    t = pygame.draw.rect(screen, GREEN, (alien_x, alien_y, 20, 20))
    t1 = pygame.draw.rect(screen, GREEN, (alien_x + 30, alien_y, 20, 20))
    t2 = pygame.draw.rect(screen, GREEN, (alien_x + 60, alien_y, 20, 20))
    t3 = pygame.draw.rect(screen, GREEN, (alien_x + 90, alien_y, 20, 20))
    t4 = pygame.draw.rect(screen, GREEN, (alien_x + 120, alien_y, 20, 20))
    t5 = pygame.draw.rect(screen, GREEN, (alien_x + 150, alien_y, 20, 20))
    t6 = pygame.draw.rect(screen, GREEN, (alien_x + 180, alien_y, 20, 20))
    t7 = pygame.draw.rect(screen, GREEN, (alien_x + 210, alien_y, 20, 20))
    top = [t, t1, t2, t3, t4, t5, t6, t7]

    # middle row
    m = pygame.draw.rect(screen, GREEN, (alien_x, alien_y + 30, 20, 20))
    m1 = pygame.draw.rect(screen, GREEN, (alien_x + 30, alien_y + 30, 20, 20))
    m2 = pygame.draw.rect(screen, GREEN, (alien_x + 60, alien_y + 30, 20, 20))
    m3 = pygame.draw.rect(screen, GREEN, (alien_x + 90, alien_y + 30, 20, 20))
    m4 = pygame.draw.rect(screen, GREEN, (alien_x + 120, alien_y + 30, 20, 20))
    m5 = pygame.draw.rect(screen, GREEN, (alien_x + 150, alien_y + 30, 20, 20))
    m6 = pygame.draw.rect(screen, GREEN, (alien_x + 180, alien_y + 30, 20, 20))
    m7 = pygame.draw.rect(screen, GREEN, (alien_x + 210, alien_y + 30, 20, 20))
    middle = [m, m1, m2, m3, m4, m5, m6, m7]

    # bottom row
    b = pygame.draw.rect(screen, GREEN, (alien_x, alien_y + 60, 20, 20))
    b1 = pygame.draw.rect(screen, GREEN, (alien_x + 30, alien_y + 60, 20, 20))
    b2 = pygame.draw.rect(screen, GREEN, (alien_x + 60, alien_y + 60, 20, 20))
    b3 = pygame.draw.rect(screen, GREEN, (alien_x + 90, alien_y + 60, 20, 20))
    b4 = pygame.draw.rect(screen, GREEN, (alien_x + 120, alien_y + 60, 20, 20))
    b5 = pygame.draw.rect(screen, GREEN, (alien_x + 150, alien_y + 60, 20, 20))
    b6 = pygame.draw.rect(screen, GREEN, (alien_x + 180, alien_y + 60, 20, 20))
    b7 = pygame.draw.rect(screen, GREEN, (alien_x + 210, alien_y + 60, 20, 20))
    bottom = [b, b1, b2, b3, b4, b5, b6, b7]

    return top, middle, bottom

# Create Barriers, blocks
def create_barriers():
    # Barrier 1
    b1 = pygame.draw.rect(screen, GREEN, (50, b_y, 10, 10))
    b2 = pygame.draw.rect(screen, GREEN, (65, b_y, 10, 10))
    b3 = pygame.draw.rect(screen, GREEN, (50, b_y - 15, 10, 10))
    b4 = pygame.draw.rect(screen, GREEN, (65, b_y - 15, 10, 10))
    b5 = pygame.draw.rect(screen, GREEN, (65, b_y - 30, 10, 10))
    b6 = pygame.draw.rect(screen, GREEN, (80, b_y - 15, 10, 10))
    b7 = pygame.draw.rect(screen, GREEN, (80, b_y - 30, 10, 10))
    b8 = pygame.draw.rect(screen, GREEN, (80, b_y - 45, 10, 10))
    b9 = pygame.draw.rect(screen, GREEN, (95, b_y - 15, 10, 10))
    b10 = pygame.draw.rect(screen, GREEN, (95, b_y - 30, 10, 10))
    b11 = pygame.draw.rect(screen, GREEN, (95, b_y - 45, 10, 10))
    b12 = pygame.draw.rect(screen, GREEN, (110, b_y, 10, 10))
    b13 = pygame.draw.rect(screen, GREEN, (110, b_y - 15, 10, 10))
    b14 = pygame.draw.rect(screen, GREEN, (110, b_y - 30, 10, 10))
    b15 = pygame.draw.rect(screen, GREEN, (125, b_y, 10, 10))
    b16 = pygame.draw.rect(screen, GREEN, (125, b_y - 15, 10, 10))
    b17 = pygame.draw.rect(screen, GREEN, (50, b_y + 15, 10, 10))
    b18 = pygame.draw.rect(screen, GREEN, (65, b_y + 15, 10, 10))
    b19 = pygame.draw.rect(screen, GREEN, (110, b_y + 15, 10, 10))
    b20 = pygame.draw.rect(screen, GREEN, (125, b_y + 15, 10, 10))
    barrier1 = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19, b20]

    # Barrier 2
    a1 = pygame.draw.rect(screen, GREEN, (158, b_y, 10, 10))
    a2 = pygame.draw.rect(screen, GREEN, (173, b_y, 10, 10))
    a3 = pygame.draw.rect(screen, GREEN, (158, b_y - 15, 10, 10))
    a4 = pygame.draw.rect(screen, GREEN, (173, b_y - 15, 10, 10))
    a5 = pygame.draw.rect(screen, GREEN, (173, b_y - 30, 10, 10))
    a6 = pygame.draw.rect(screen, GREEN, (188, b_y - 15, 10, 10))
    a7 = pygame.draw.rect(screen, GREEN, (188, b_y - 30, 10, 10))
    a8 = pygame.draw.rect(screen, GREEN, (188, b_y - 45, 10, 10))
    a9 = pygame.draw.rect(screen, GREEN, (203, b_y - 15, 10, 10))
    a10 = pygame.draw.rect(screen, GREEN, (203, b_y - 30, 10, 10))
    a11 = pygame.draw.rect(screen, GREEN, (203, b_y - 45, 10, 10))
    a12 = pygame.draw.rect(screen, GREEN, (218, b_y, 10, 10))
    a13 = pygame.draw.rect(screen, GREEN, (218, b_y - 15, 10, 10))
    a14 = pygame.draw.rect(screen, GREEN, (218, b_y - 30, 10, 10))
    a15 = pygame.draw.rect(screen, GREEN, (233, b_y, 10, 10))
    a16 = pygame.draw.rect(screen, GREEN, (233, b_y - 15, 10, 10))
    a17 = pygame.draw.rect(screen, GREEN, (158, b_y + 15, 10, 10))
    a18 = pygame.draw.rect(screen, GREEN, (173, b_y + 15, 10, 10))
    a19 = pygame.draw.rect(screen, GREEN, (218, b_y + 15, 10, 10))
    a20 = pygame.draw.rect(screen, GREEN, (233, b_y + 15, 10, 10))
    barrier2 = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20]

    # Barrier 3
    r1 = pygame.draw.rect(screen, GREEN, (266, b_y, 10, 10))
    r2 = pygame.draw.rect(screen, GREEN, (281, b_y, 10, 10))
    r3 = pygame.draw.rect(screen, GREEN, (266, b_y - 15, 10, 10))
    r4 = pygame.draw.rect(screen, GREEN, (281, b_y - 15, 10, 10))
    r5 = pygame.draw.rect(screen, GREEN, (281, b_y - 30, 10, 10))
    r6 = pygame.draw.rect(screen, GREEN, (296, b_y - 15, 10, 10))
    r7 = pygame.draw.rect(screen, GREEN, (296, b_y - 30, 10, 10))
    r8 = pygame.draw.rect(screen, GREEN, (296, b_y - 45, 10, 10))
    r9 = pygame.draw.rect(screen, GREEN, (311, b_y - 15, 10, 10))
    r10 = pygame.draw.rect(screen, GREEN, (311, b_y - 30, 10, 10))
    r11 = pygame.draw.rect(screen, GREEN, (311, b_y - 45, 10, 10))
    r12 = pygame.draw.rect(screen, GREEN, (326, b_y, 10, 10))
    r13 = pygame.draw.rect(screen, GREEN, (326, b_y - 15, 10, 10))
    r14 = pygame.draw.rect(screen, GREEN, (326, b_y - 30, 10, 10))
    r15 = pygame.draw.rect(screen, GREEN, (341, b_y, 10, 10))
    r16 = pygame.draw.rect(screen, GREEN, (341, b_y - 15, 10, 10))
    r17 = pygame.draw.rect(screen, GREEN, (266, b_y + 15, 10, 10))
    r18 = pygame.draw.rect(screen, GREEN, (281, b_y + 15, 10, 10))
    r19 = pygame.draw.rect(screen, GREEN, (326, b_y + 15, 10, 10))
    r20 = pygame.draw.rect(screen, GREEN, (341, b_y + 15, 10, 10))
    barrier3 = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20]

    # Barrier 4
    i1 = pygame.draw.rect(screen, GREEN, (374, b_y, 10, 10))
    i2 = pygame.draw.rect(screen, GREEN, (389, b_y, 10, 10))
    i3 = pygame.draw.rect(screen, GREEN, (374, b_y - 15, 10, 10))
    i4 = pygame.draw.rect(screen, GREEN, (389, b_y - 15, 10, 10))
    i5 = pygame.draw.rect(screen, GREEN, (389, b_y - 30, 10, 10))
    i6 = pygame.draw.rect(screen, GREEN, (404, b_y - 15, 10, 10))
    i7 = pygame.draw.rect(screen, GREEN, (404, b_y - 30, 10, 10))
    i8 = pygame.draw.rect(screen, GREEN, (404, b_y - 45, 10, 10))
    i9 = pygame.draw.rect(screen, GREEN, (419, b_y - 15, 10, 10))
    i10 = pygame.draw.rect(screen, GREEN, (419, b_y - 30, 10, 10))
    i11 = pygame.draw.rect(screen, GREEN, (419, b_y - 45, 10, 10))
    i12 = pygame.draw.rect(screen, GREEN, (434, b_y, 10, 10))
    i13 = pygame.draw.rect(screen, GREEN, (434, b_y - 15, 10, 10))
    i14 = pygame.draw.rect(screen, GREEN, (434, b_y - 30, 10, 10))
    i15 = pygame.draw.rect(screen, GREEN, (449, b_y, 10, 10))
    i16 = pygame.draw.rect(screen, GREEN, (449, b_y - 15, 10, 10))
    i17 = pygame.draw.rect(screen, GREEN, (375, b_y + 15, 10, 10))
    i18 = pygame.draw.rect(screen, GREEN, (389, b_y + 15, 10, 10))
    i19 = pygame.draw.rect(screen, GREEN, (434, b_y + 15, 10, 10))
    i20 = pygame.draw.rect(screen, GREEN, (449, b_y + 15, 10, 10))
    barrier4 = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15, i16, i17, i18, i19, i20]

    return barrier1, barrier2, barrier3, barrier4
    

# Create a font object
font1 = pygame.font.SysFont(None, 75)

while True:
    screen.fill(BLACK)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
            if len(bullets) < 1 and allow_shoot:
                create_bullet()
                allow_shoot = False
                pygame.mixer.Sound.play(fire)
            if i.type == pygame.KEYUP and i.key == pygame.K_SPACE:
                allowshoot = True
    
    # Frame rate
    clock.tick(70)

    # Move players
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
        player_x = max(player_x, 30)
    if keys[pygame.K_d]:
        player_x += player_speed
        player_x = min(player_x, SCREEN_WIDTH - 30)
    # Lines
    pygame.draw.line(screen, GREEN, (0, 700), (SCREEN_WIDTH, 700), 2)

    # Player stuff
    # Make player
    player = pygame.draw.polygon(screen, GREEN, [(player_x - 20, player_y - 10), (player_x - 2, player_y - 10), (player_x - 2, player_y -15), (player_x + 3, player_y - 15), (player_x + 3, player_y - 10), (player_x + 20, player_y - 10), (player_x + 20, player_y + 10), (player_x - 20, player_y + 10)])
    player_rect = calculate_bounding_box(player)

    # Text
    #make font
    text1 = font1.render(f"{score}", True, WHITE)
    screen.blit(text1, (30, 725))

    # Aliens (a.k.a space invaders)
    create_aliens()
    alien_x += alien_vel
    if not gameOver:
        if alien_x < 0:
            alien_x += alien_vel
            alien_x = min(alien_x, 0)
        if alien_x + 230 > 500:
            alien_x -= alien_vel
            alien_x = max(alien_x, SCREEN_WIDTH)
        elif alien_x + 250 > 500:
            alien_y + 50

    # create barriers
    create_barriers()

    # bullet colliding stuff
    for bullet in bullets:
        bullet['rect'].x += bullet['x_vel']
        bullet['rect'].y += bullet['y_vel']
        pygame.draw.circle(screen, bullet['color'], bullet['rect'].center, bullet['radius'])
        if bullet['rect'].x < -3*bullet['radius']:
            bullets.remove(bullet)
        elif bullet['rect'].y < -3*bullet['radius']:
            bullets.remove(bullet)
        elif bullet['rect'].x > SCREEN_WIDTH + 3*bullet['radius']:
            bullets.remove(bullet)
        elif bullet['rect'].y > SCREEN_HEIGHT + 3*bullet['radius']:
            bullets.remove(bullet)

    pygame.display.flip()

