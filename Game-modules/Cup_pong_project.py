import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame
import math
import random

#Initialize pygame
pygame.init()
pygame.mixer.init()
ouch = pygame.mixer.Sound('burp-1.wav')

#Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cup Pong")

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define Variables
clock = pygame.time.Clock()
player_width = 20
player_length = 100
player1_x = 50
player1_y = 350
player2_x = 940
player2_y = 350
player1_speed = 5
player2_speed = 5
GAME_OVER = False
ball_radius = 10
ball_vel_x = 5
ball_vel_y = 5
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2
ball_dir = pygame.math.Vector2(1, 0)
ball = []
p1_score = 0
p2_score = 0

# Create a font object
font1 = pygame.font.SysFont(None, 75)
font2 = pygame.font.SysFont(None, 75)
font3 = pygame.font.SysFont(None, 100)
font_p1 = pygame.font.SysFont(None, 50)
font_p2 = pygame.font.SysFont(None, 50)

# Create a ball
def create_ball():
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)

def intersects(rect:pygame.Rect, r: float, center: [float, float]):
    circle_distance_x = abs(center[0] - rect.centerx)
    circle_distance_y = abs(center[1] - rect.centery)

    if circle_distance_x > rect.w / 2.0 + r or circle_distance_y > rect.h / 2.0 + r:
        return False
    
    if circle_distance_x <= rect.w / 2.0 + r or circle_distance_y <= rect.h / 2.0 + r:
        return True
    
    corner_x = circle_distance_x - rect.w / 2.0
    corner_y = circle_distance_y - rect.h / 2.0
    corner_distance_sq = corner_x ** 2.0 + corner_y ** 2.0
    return corner_distance_sq <= r ** 2.0

# Define Variables
p1_pos = SCREEN_HEIGHT / 2 -  player_length / 2
p2_pos = SCREEN_HEIGHT / 2 - player_length / 2

while p1_score < 8 or p2_score < 8:
    screen.fill(BLACK)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Frame rate
    clock.tick(60)

    #make font
    text1 = font1.render(f"{p1_score}", True, WHITE)
    screen.blit(text1, (100, 25))

    text2 = font2.render(f"{p2_score}", True, WHITE)
    screen.blit(text2, (890, 25))

    # Move players
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_y -= player1_speed
        player1_y = max(player1_y, 100)
    if keys[pygame.K_s]:
        player1_y += player1_speed
        player1_y = min(player1_y, SCREEN_HEIGHT - player_length)
    if keys[pygame.K_UP]:
        player2_y -= player2_speed
        player2_y = max(player2_y, 100)
    if keys[pygame.K_DOWN]:
        player2_y += player2_speed
        player2_y = min(player2_y, SCREEN_HEIGHT - player_length)
        
    p1_pos = max(min(p1_pos, SCREEN_HEIGHT - player_length), 0)
    p2_pos = max(min(p2_pos, SCREEN_HEIGHT - player_length), 0)

    p1_rect = pygame.Rect(player1_x, player1_y, player_width, player_length)
    p2_rect = pygame.Rect(player2_x, player2_y, player_width, player_length)

    if intersects(p1_rect, ball_radius, [ball_x, ball_y]):
        ball_vel_x = -ball_vel_x
        pygame.mixer.Channel(1).play(ouch)

    if intersects(p2_rect, ball_radius, [ball_x, ball_y]):
        ball_vel_x = -ball_vel_x
        pygame.mixer.Channel(1).play(ouch)
    
    # Move ball
    ball = create_ball()
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # Hit wall
    if ball_x > SCREEN_WIDTH:
        ball_vel_x = -ball_vel_x
        p1_score += 1
        ball_x = SCREEN_WIDTH//2
        ball_y = SCREEN_HEIGHT//2
    if ball_x < ball_radius:
        ball_vel_x = -ball_vel_x
        p2_score += 1
        ball_x = SCREEN_WIDTH//2
        ball_y = SCREEN_HEIGHT//2
    if ball_y > SCREEN_HEIGHT or ball_y < ball_radius + 100:
        ball_vel_y = -ball_vel_y
    
    # Draw players
    player1 = pygame.draw.rect(screen, WHITE, pygame.Rect(player1_x, player1_y, player_width, player_length)) #player 1
    player2 = pygame.draw.rect(screen, WHITE, pygame.Rect(player2_x, player2_y, player_width, player_length)) #player 2

    # Draw line
    pygame.draw.line(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT), 2)
    pygame.draw.line(screen, WHITE, (0, 100), (SCREEN_WIDTH, 100), 2)

    # Check if Score is over 8
    if p1_score == 8:
        text3 = font3.render(f"GAME OVER", True, WHITE)
        text_rect = text3.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(text3, text_rect)
        text_p1 = font_p1.render("Player 1 Wins!", True, WHITE)
        text_rect_p1 = text_p1.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        screen.blit(text_p1, text_rect_p1)
    if p2_score == 8:
        text3 = font3.render(f"GAME OVER", True, WHITE)
        text_rect = text3.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        screen.blit(text3, text_rect)
        text_p2 = font_p2.render("Player 2 Wins!", True, WHITE)
        text_rect_p2 = text_p2.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
        screen.blit(text_p2, text_rect_p2)

    pygame.display.flip()




