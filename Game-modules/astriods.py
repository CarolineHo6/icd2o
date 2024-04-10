import random
import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame
import os
import math
pygame.init()
pygame.mixer.init()
fire = pygame.mixer.Sound('fire.wav')
thrust = pygame.mixer.Sound('thrust.wav')
smallBoom = pygame.mixer.Sound('bangSmall.wav')
mediumBoom = pygame.mixer.Sound('bangMedium.wav')
largeBoom = pygame.mixer.Sound('bangLarge.wav')
extraShip = pygame.mixer.Sound('extraShip.wav')

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
life_levels = [25, 75, 125, 250, 500, 1000, 2000, 5000, 10000, 100000, 200000]
level = 0
colour_levels = [WHITE, (102,204,0), (102, 178, 255), (255,153,204), (204,204,0), (255, 69,0), (0,191,255), (106,90,205), (250,250,210), (240,255,240),(0,0,0)]


# Define game variables
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 18)
score = 0
lives = 5
circles = []
bullets = []
direction_angle = -90  # Angle in degrees up is 0
spaceship_speed = 0
allowshoot = True
gameOver = False
def create_bullet():
    angle_rad = math.radians(direction_angle)
    radius = 3
    color = BLACK
    if level == 10:
        color = WHITE
    y_vel = (spaceship_speed + 3) * math.sin(angle_rad)
    x_vel = (spaceship_speed + 3) * math.cos(angle_rad)
    x,y = calculate_bounding_box(spaceship).center
    
    
    bullet = {'rect': pygame.Rect(x, y, 2*radius, 2*radius), 'color': color, 'radius': radius, 'x_vel': x_vel, 'y_vel':y_vel}
    bullets.append(bullet)

# Function to create new circlular asteroids
def create_circles(explode, circle):
    radius = random.randint(10, 20)
    if explode == True:
        radius = 5
    color = BLACK
    if level == 10:
        color = WHITE
    speedx = random.randint(-3, 3)
    speedy = random.randint(-2, 2)
    if speedx == 0:
        speedx = 1
    if speedy == 0:
        speedy = 1
    print(circle)
    if (circle == None):
        x = 0
        y = 0
    else:
        x = circle['rect'].x
        y = circle['rect'].y
    if explode == False:
        if speedy > 0 and speedx > 0: #it is going down so let's start at the top of the screen
            x = random.randint(0, SCREEN_WIDTH - 2*radius)
            y = -2*radius
        elif speedy < 0 and speedx > 0:
            x = -2*radius
            y = random.randint(0, SCREEN_HEIGHT - 2*radius)
        elif speedy < 0 and speedx < 0:
            x = random.randint(0, SCREEN_WIDTH - 2*radius)
            y = SCREEN_HEIGHT + 2*radius
        elif speedy > 0 and speedx < 0:
            x = SCREEN_WIDTH + 2*radius
            y = random.randint(0, SCREEN_HEIGHT - 2*radius)
    c = {'rect': pygame.Rect(x, y, 2*radius, 2*radius), 'color': color, 'radius': radius, 'width':2, 'speedx':speedx, 'speedy':speedy}
    circles.append(c)
    if explode == True:
        speedx = random.randint(-3, 3)
        speedy = random.randint(-2, 2)
        if speedx == 0:
            speedx = 1
        if speedy == 0:
            speedy = 1
        
        c = {'rect': pygame.Rect(x, y, 2*radius, 2*radius), 'color': color, 'radius': radius, 'width':2, 'speedx':speedx, 'speedy':speedy}
        circles.append(c)

spaceship = [(SCREEN_WIDTH//2,SCREEN_HEIGHT//2), (SCREEN_WIDTH//2-15,SCREEN_HEIGHT//2+5), (SCREEN_WIDTH//2,SCREEN_HEIGHT//2-25), (SCREEN_WIDTH//2+15,SCREEN_HEIGHT//2+5)]
def centroid(polygon):
    sum_x = sum(p[0] for p in polygon)
    sum_y = sum(p[1] for p in polygon)
    return sum_x / len(polygon), sum_y / len(polygon)
# Function to rotate a point around the origin
def rotate_point(point, angle):
    angle_rad = math.radians(angle)
    px, py = point
    qx = px * math.cos(angle_rad) - py * math.sin(angle_rad)
    qy = px * math.sin(angle_rad) + py * math.cos(angle_rad)
    return qx, qy
# Function to rotate a polygon around its center
def rotate_polygon(polygon, angle):
    cx, cy = centroid(polygon)
    translated_polygon = [(x - cx, y - cy) for x, y in polygon]
    rotated_polygon = [rotate_point(point, angle) for point in translated_polygon]
    return [(x + cx, y + cy) for x, y in rotated_polygon]
# Function to translate a point in a specific direction by a given distance
def translate_point(point, angle, distance):
    angle_rad = math.radians(angle)
    dx = distance * math.cos(angle_rad)
    dy = distance * math.sin(angle_rad)
    return point[0] + dx, point[1] + dy
# Function to calculate the bounding box rectangle of a polygon
def calculate_bounding_box(polygon_points):
    min_x = min(point[0] for point in polygon_points)
    max_x = max(point[0] for point in polygon_points)
    min_y = min(point[1] for point in polygon_points)
    max_y = max(point[1] for point in polygon_points)
    bounding_box_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    return bounding_box_rect
# Game loop
running = True
while running:
    screen.fill(colour_levels[level])
    clock.tick(60)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if len(bullets) < 10 and allowshoot:
                create_bullet()
                allowshoot = False
                pygame.mixer.Sound.play(fire)
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            allowshoot = True
    
    if len(circles) < 10 and random.randint(1,20)== 5:
        create_circles(False, None)
    color_text = BLACK
    if level == 10:
        color_text = WHITE
    score_text = font.render(f"Score: {score}", True, color_text)
    screen.blit(score_text, (35, 10))
    if not gameOver:
        lives_text = font.render(f"Lives: {lives}", True, color_text)
        screen.blit(lives_text, (SCREEN_WIDTH - lives_text.get_width() - 35, 10))
        next_life_text = font.render(f"Next New Life: {life_levels[level]} Points", True, color_text)
        screen.blit(next_life_text, (SCREEN_WIDTH - next_life_text.get_width() - 35, SCREEN_HEIGHT - next_life_text.get_height() - 10))
    else:
        gameOverText = font.render("GAME OVER (Play Again (Y)?)", True, color_text)
        gameOverText_rect = gameOverText.get_rect()
        gameOverText_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(gameOverText, gameOverText_rect)
    # Move player circle with keyboard input
    if not gameOver:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            direction_angle -= 5
            spaceship = rotate_polygon(spaceship, -5)
        if keys[pygame.K_RIGHT]:
            direction_angle += 5
            spaceship = rotate_polygon(spaceship, 5)
        if keys[pygame.K_UP] and spaceship_speed < 4:
            spaceship_speed += 0.1
            pygame.mixer.Sound.play(thrust)
        if keys[pygame.K_DOWN]:
            spaceship_speed -= 0.1
            if spaceship_speed < 0:
                spaceship_speed = 0
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_y]:
            gameOver = False
            score = 0
            lives = 5
            level = 0 

    
    spaceship = [translate_point(point, direction_angle, spaceship_speed) for point in spaceship]
    if not gameOver:
        pygame.draw.polygon(screen, color_text, spaceship)  # Outline
    # Check if any point has an x-coordinate less than -100
    if any(point[0] < -50 for point in spaceship):
        # Shift the entire spaceship to the opposite side of the screen
        spaceship = [(point[0] + SCREEN_WIDTH, point[1]) for point in spaceship]
    
    # Check if any point has an x-coordinate less than -100
    if any(point[0] > SCREEN_WIDTH + 50 for point in spaceship):
        # Shift the entire spaceship to the opposite side of the screen
        spaceship = [(point[0] - SCREEN_WIDTH, point[1]) for point in spaceship]
        # Check if any point has an y-coordinate less than -100
    if any(point[1] < -50 for point in spaceship):
        # Shift the entire spaceship to the opposite side of the screen
        spaceship = [(point[0], point[1] + SCREEN_HEIGHT) for point in spaceship]
    
    # Check if any point has an -coordinate less than -100
    if any(point[1] > SCREEN_HEIGHT + 50 for point in spaceship):
        # Shift the entire spaceship to the opposite side of the screen
        spaceship = [(point[0], point[1] - SCREEN_HEIGHT) for point in spaceship]
    
    spaceship_rect = calculate_bounding_box(spaceship)
    for circle in circles:
        circle['rect'].x += circle['speedx']
        circle['rect'].y += circle['speedy']
        pygame.draw.circle(screen, circle['color'], circle['rect'].center, circle['radius'], width=circle['width'])
        if circle['rect'].x < -3*circle['radius']:
            circles.remove(circle)
        elif circle['rect'].y < -3*circle['radius']:
            circles.remove(circle)
        elif circle['rect'].x > SCREEN_WIDTH + 3*circle['radius']:
            circles.remove(circle)
        elif circle['rect'].y > SCREEN_HEIGHT + 3*circle['radius']:
            circles.remove(circle)
        if circle['rect'].colliderect(spaceship_rect):
            lives -= 1
            pygame.mixer.Sound.play(largeBoom)
            spaceship = [(SCREEN_WIDTH//2,SCREEN_HEIGHT//2), (SCREEN_WIDTH//2-15,SCREEN_HEIGHT//2+5), (SCREEN_WIDTH//2,SCREEN_HEIGHT//2-25), (SCREEN_WIDTH//2+15,SCREEN_HEIGHT//2+5)]
            direction_angle = -90
            spaceship_speed = 0
            circles.clear()
            bullets.clear()
            if lives == -1:
                gameOver = True
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
        
        #did they collide with a asteroid
        for circle in circles:
            if bullet['rect'].colliderect(circle['rect']):
                if bullet in bullets:
                    bullets.remove(bullet)
                if level == 0:
                    score +=1 
                else: 
                    score += level
                if life_levels[level] < score:
                    level +=1
                    lives += 1
                    pygame.mixer.Sound.play(extraShip)
                if circle['radius'] < 12:
                    pygame.mixer.Sound.play(smallBoom)
                    circles.remove(circle)
                else:
                    pygame.mixer.Sound.play(mediumBoom)
                    create_circles(True, circle)
                    circles.remove(circle)

    
    pygame.display.flip()
# Quit Pygame
pygame.quit()
