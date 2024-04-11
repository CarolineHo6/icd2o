import random
import sys
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
import pygame
pygame.init()

GREY = (29, 29, 27)
GREEN = (0, 255, 17)

# Screen
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
SPACE = 50
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space invaders")

# Sounds
pygame.mixer.init()
explode = pygame.mixer.Sound('explosion.wav')
shooting = pygame.mixer.Sound('fire.wav')

#Texts
font = pygame.font.Font(None, 40)

#Set clock
clock = pygame.time.Clock()

# Aliens
class Alien(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        self.type = type
        path = f"alien{type}.png"
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft = (x, y))

    def update(self, direction):
        self.rect.x += direction

class Mother_Ship(pygame.sprite.Sprite):
    def __init__(self, screen_width, offset):
        super().__init__()
        self.screen_width = screen_width
        self.offset = offset
        self.image = pygame.image.load("MotherShip.png")
        x = random.choice([self.offset/2, self.screen_width + self.offset - self.image.get_width()])
        if x == self.offset//2:
            self.speed = 3
        else:
            self.speed = -3
        self.rect = self.image.get_rect(topleft = (x, 90))
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen_width + self.offset//2:
            self.kill()
        elif self.rect.left < self.offset//2:
            self.kill()

# Bullets
class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, speed, screen_height):
        super().__init__()
        self.image = pygame.Surface((1, 15))
        self.image.fill((GREEN))
        self.rect = self.image.get_rect(center = position)
        self.speed = speed
        self.screen_height = screen_height

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > self.screen_height +15 or self.rect.y < 0:
            print("Killed")
            self.kill()

# Barriers
class Area(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((3,3))
        self.image.fill((GREEN))
        self.rect = self.image.get_rect(topleft = (x,y))
#The 2D array to create the obstacles and where the blocks are
grid = [
[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
[1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]
]

#Obstacles
class Barrier:
    def __init__(self, x, y):
        self.area_group = pygame.sprite.Group()
        for row in range(len(grid)): #interates through the row to see if it says one then they should print a block
            for column in range(len(grid[0])): #interates through the column to see if it says one then they should print a block
                if grid[row][column] == 1:
                    p_x = x + column * 3
                    p_y = y + row * 3
                    block = Area(p_x, p_y)
                    self.area_group.add(block)

#Sprite Class
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, space):
        super().__init__()
        self.space = space
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect(midbottom = ((self.screen_width/2 + self.space)/2, self.screen_height))
        self.speed = 6
        self.bullets_group = pygame.sprite.Group()
        self.bullet_go = True
        self.bullet_time = 0
        self.bullet_delay = 300

    def get_user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_SPACE] and self.bullet_go:
            pygame.mixer.Channel(2).play(shooting)
            self.bullet_go = False
            bullet = Bullet(self.rect.center, 5, self.screen_height)
            self.bullets_group.add(bullet)
            self.bullet_time = pygame.time.get_ticks()
    
    def update(self):
        self.get_user_input()
        self.restrict_move()
        self.recharge_bullet()
    
    def restrict_move(self):
        if self.rect.height > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.left < self.space:
            self.rect.left = self.space

    def recharge_bullet(self):
        if not self.bullet_go:
            current_time = pygame.time.get_ticks()
            if current_time - self.bullet_time >= self.bullet_delay:
                self.bullet_go = True
    
    def restart(self):
        self.rect = self.image.get_rect(midbottom = (self.screen_width/2, self.screen_height))
        self.bullets_group.clear()

# Game class for cleaning up stuff
class Game:
    def __init__(self, screen_width, screen_height, space):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.space = space
        #Spaceship
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height, self.space))
        #Barriers
        self.barriers = self.create_barriers()
        #Aliens
        self.aliens_group = pygame.sprite.Group()
        self.create_aliens()
        self.aliens_direction = 1
        self.alien_bullets_group = pygame.sprite.Group()
        # Mystery ship
        self.motherShip_group = pygame.sprite.GroupSingle()
        self.lives = 3
        self.run = True
        self.score = 0
        self.level = 1


    def create_barriers(self):
        barrier_width = len(grid[0]) * 3
        gap = (self.screen_width +self.space - (4*barrier_width))/5
        barriers = []
        # barrier spacing
        for i in range(4):
            space_x = (i+1) * gap + i * barrier_width
            barrier = Barrier(space_x, self.screen_height - 100)
            barriers.append(barrier)
        return barriers
    
    def create_aliens(self):
        for row in range(5):
            for column in range(11):
                x = 75 + column * 55
                y = 110 + row * 55
                if row == 0:
                    alien_type = 3
                elif row in (1, 2):
                    alien_type = 2
                else:
                    alien_type = 1
                alien = Alien(alien_type, x + self.space/2, y)
                self.aliens_group.add(alien)
    
    def move_aliens(self):
        self.aliens_group.update(self.aliens_direction)
        alien_sprites = self.aliens_group.sprites()
        for alien in alien_sprites:
            if alien.rect.right >= self.screen_width + self.space/2:
                self.aliens_direction = -1
                self.down_aliens(2)
            elif alien.rect.left <= self.space/2:
                self.aliens_direction = 1
                self.down_aliens(2)

    def down_aliens(self, distance):
        if self.aliens_group:
            for alien in self.aliens_group.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens_group.sprites():
            random_alien = random.choice(self.aliens_group.sprites())
            bullet_sprite = Bullet(random_alien.rect.center, -6, self.screen_height)
            self.alien_bullets_group.add(bullet_sprite)
    
    def create_mother_ship(self):
        self.motherShip_group.add(Mother_Ship(self.screen_width, self.space))

    def collision_check(self):
        #ship
        if self.spaceship_group:
            for bullet_sprite in self.spaceship_group.sprite.bullets_group:
                aliens_hit = pygame.sprite.spritecollide(bullet_sprite, self.aliens_group, True)
                if aliens_hit:
                    for alien in aliens_hit:
                        self.score += alien.type * 100
                        bullet_sprite.kill()
                        pygame.mixer.Channel(1).play(explode)
                
                if pygame.sprite.spritecollide(bullet_sprite, self.motherShip_group, True):
                        self.score += 500
                        bullet_sprite.kill()
                        pygame.mixer.Channel(1).play(explode)
                
                for barrier in self.barriers:
                    if pygame.sprite.spritecollide(bullet_sprite, barrier.area_group, True):
                        bullet_sprite.kill()
                        pygame.mixer.Channel(2).play(explode)
            
        #Alien shots
        if self.alien_bullets_group:
            for bullet_sprite in self.alien_bullets_group:
                if pygame.sprite.spritecollide(bullet_sprite, self.spaceship_group, False):
                    bullet_sprite.kill()
                    pygame.mixer.Channel(1).play(explode)
                    self.lives -= 1
                    if self.lives == 0:
                        self.game_over()

                for barrier in self.barriers:
                    if pygame.sprite.spritecollide(bullet_sprite, barrier.area_group, True):
                        pygame.mixer.Channel(1).play(explode)
                        bullet_sprite.kill()
        
        if self.aliens_group:
            #If aliens colide with barriers
            for alien in self.aliens_group:
                for barrier in self.barriers:
                    pygame.sprite.spritecollide(alien, barrier.area_group, True)
                    pygame.mixer.Channel(1).play(explode)
            
            if pygame.sprite.spritecollide(alien, self.spaceship_group, False):
                self.game_over()

    def levels(self):
        self.level += self.score//1000

    def text(self):
        self.level_surface = font.render(f"LEVEL {self.level}", True, GREEN)
        screen.blit(self.level_surface, (SCREEN_WIDTH  - 10, 10))
        self.score_text_surface = font.render(f"SCORE: {self.score}", True, GREEN)
        screen.blit(self.score_text_surface, (10, 10))

    def game_over(self):
        print("Game Over")
        if self.lives == 0:
            self.game_over = font.render("GAME OVER", True, GREEN)
            screen.blit(self.game_over, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        self.run = False

    def restart(self):
        self.run = True
        self.lives = 3
        self.spaceship_group.sprite.restart()
        self.aliens_group.empty()
        self.alien_bullets_group.empty()
        self.create_aliens()
        self.barriers = self.create_barriers()
        self.score = 0

# Game class
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SPACE)

SHOOT_BULLET = pygame.USEREVENT
pygame.time.set_timer(SHOOT_BULLET, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

while True:
    # Shutting it down if you exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SHOOT_BULLET and game.run:
            game.alien_shoot()
            pygame.mixer.Channel(2).play(shooting)
        if event.type == MYSTERYSHIP and game.run:
            game.create_mother_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000, 8000))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:
            game.restart()
    
    #Updating
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_shoot()
        game.alien_bullets_group.update()
        game.motherShip_group.update()
        game.collision_check()
        game.text()

    # Screen filling
    screen.fill(GREY)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.bullets_group.draw(screen)
    for obstacle in game.barriers:
        obstacle.area_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_bullets_group.draw(screen)
    game.motherShip_group.draw(screen)

    #UI
    game.text()

    pygame.display.flip()
    clock.tick(60)

