import pygame, sys, random
sys.path.append(r'C:\Users\CHo\AppData\Local\Programs\Python\Python312\Lib\site-packages')
pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50

GREY = (29, 29, 27)
GREEN = (128, 255, 0)

font = pygame.font.Font(None, 40)
level = font.render("LEVEL 01", False, GREEN)
game_over_surface = font.render("GAME OVER", False, GREEN)
score_text_surface = font.render("SCORE", False, GREEN)
highscore_text_surface = font.render("HIGH-SCORE", False, GREEN)

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2*OFFSET))
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock()

class Alien(pygame.sprite.Sprite):
	def __init__(self, type, x, y):
		super().__init__()
		self.type = type
		path = f"alien{type}.png"
		self.image = pygame.image.load(path)
		self.rect = self.image.get_rect(topleft = (x, y))

	def update(self, direction):
		self.rect.x += direction

class MysteryShip(pygame.sprite.Sprite):
	def __init__(self, screen_width, offset):
		super().__init__()
		self.screen_width = screen_width
		self.offset = offset
		self.image = pygame.image.load("MotherShip.png")

		x = random.choice([self.offset/2, self.screen_width + self.offset - self.image.get_width()])
		if x == self.offset/2:
			self.speed = 3
		else:
			self.speed = -3

		self.rect = self.image.get_rect(topleft = (x, 90))

	def update(self):
		self.rect.x += self.speed
		if self.rect.right > self.screen_width + self.offset/2:
			self.kill()
		elif self.rect.left < self.offset/2:
			self.kill()

class Laser(pygame.sprite.Sprite):
	def __init__(self, position, speed, screen_height):
		super().__init__()
		self.image = pygame.Surface((4,15))
		self.image.fill((243, 216, 63))
		self.rect = self.image.get_rect(center = position)
		self.speed = speed
		self.screen_height = screen_height

	def update(self):
		self.rect.y -= self.speed
		if self.rect.y > self.screen_height + 15 or self.rect.y < 0:
			self.kill()

class Block(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.Surface((3,3))
		self.image.fill((243,216,63))
		self.rect = self.image.get_rect(topleft = (x,y))

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
[1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1]]

class Obstacle:
	def __init__(self, x, y):
		self.blocks_group = pygame.sprite.Group()
		for row in range(len(grid)):
			for column in range(len(grid[0])):
				if grid[row][column] == 1:
					pos_x = x + column * 3
					pos_y = y + row * 3
					block = Block(pos_x, pos_y)
					self.blocks_group.add(block)

class Spaceship(pygame.sprite.Sprite):
	def __init__(self, screen_width, screen_height, offset):
		super().__init__()
		self.offset = offset
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.image = pygame.image.load("spaceship.png")
		self.rect = self.image.get_rect(midbottom = ((self.screen_width + self.offset)/2, self.screen_height))
		self.speed = 6
		self.lasers_group = pygame.sprite.Group()
		self.laser_ready = True
		self.laser_time = 0
		self.laser_delay = 300
		self.laser_sound = pygame.mixer.Sound("fire.wav")

	def get_user_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			self.rect.x += 6

		if keys[pygame.K_LEFT]:
			self.rect.x -= 6

		if keys[pygame.K_SPACE] and self.laser_ready:
			self.laser_ready = False
			laser = Laser(self.rect.center, 5, self.screen_height)
			self.lasers_group.add(laser)
			self.laser_time = pygame.time.get_ticks()
			self.laser_sound.play()

	def update(self):
		self.get_user_input()
		self.constrain_movement()
		self.lasers_group.update()
		self.recharge_laser()

	def constrain_movement(self):
		if self.rect.right > self.screen_width:
			self.rect.right = self.screen_width
		if self.rect.left < self.offset:
			self.rect.left = self.offset

	def recharge_laser(self):
		if not self.laser_ready:
			current_time = pygame.time.get_ticks()
			if current_time - self.laser_time >= self.laser_delay:
				self.laser_ready = True

	def reset(self):
		self.rect = self.image.get_rect(midbottom = ((self.screen_width + self.offset)/2, self.screen_height))
		self.lasers_group.empty()

class Game:
	def __init__(self, screen_width, screen_height, offset):
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.offset = offset
		self.spaceship_group = pygame.sprite.GroupSingle()
		self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height, self.offset))
		self.obstacles = self.create_obstacles()
		self.aliens_group = pygame.sprite.Group()
		self.create_aliens()
		self.aliens_direction = 1
		self.alien_lasers_group = pygame.sprite.Group()
		self.mystery_ship_group = pygame.sprite.GroupSingle()
		self.lives = 3
		self.run = True
		self.score = 0
		self.highscore = 0
		self.explosion_sound = pygame.mixer.Sound("explosion.wav")
		self.load_highscore()

	def create_obstacles(self):
		obstacle_width = len(grid[0]) * 3
		gap = (self.screen_width + self.offset - (4 * obstacle_width))/5
		obstacles = []
		for i in range(4):
			offset_x = (i + 1) * gap + i * obstacle_width
			obstacle = Obstacle(offset_x, self.screen_height - 100)
			obstacles.append(obstacle)
		return obstacles

	def create_aliens(self):
		for row in range(5):
			for column in range(11):
				x = 75 + column * 55
				y = 110 + row * 55

				if row == 0:
					alien_type = 3
				elif row in (1,2):
					alien_type = 2
				else:
					alien_type = 1

				alien = Alien(alien_type, x + self.offset/2, y)
				self.aliens_group.add(alien)

	def move_aliens(self):
		self.aliens_group.update(self.aliens_direction)

		alien_sprites = self.aliens_group.sprites()
		for alien in alien_sprites:
			if alien.rect.right >= self.screen_width + self.offset/2:
				self.aliens_direction = -1
				self.alien_move_down(2)
			elif alien.rect.left <= self.offset/2:
				self.aliens_direction = 1
				self.alien_move_down(2)

	def alien_move_down(self, distance):
		if self.aliens_group:
			for alien in self.aliens_group.sprites():
				alien.rect.y += distance

	def alien_shoot_laser(self):
		if self.aliens_group.sprites():
			random_alien = random.choice(self.aliens_group.sprites())
			laser_sprite = Laser(random_alien.rect.center, -6, self.screen_height)
			self.alien_lasers_group.add(laser_sprite)

	def create_mystery_ship(self):
		self.mystery_ship_group.add(MysteryShip(self.screen_width, self.offset))

	def check_for_collisions(self):
		#Spaceship
		if self.spaceship_group.sprite.lasers_group:
			for laser_sprite in self.spaceship_group.sprite.lasers_group:
				
				aliens_hit = pygame.sprite.spritecollide(laser_sprite, self.aliens_group, True)
				if aliens_hit:
					self.explosion_sound.play()
					for alien in aliens_hit:
						self.score += alien.type * 100
						self.check_for_highscore()
						laser_sprite.kill()

				if pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, True):
					self.score += 500
					self.explosion_sound.play()
					self.check_for_highscore()
					laser_sprite.kill()

				for obstacle in self.obstacles:
					if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
						laser_sprite.kill()

		#Alien Lasers
		if self.alien_lasers_group:
			for laser_sprite in self.alien_lasers_group:
				if pygame.sprite.spritecollide(laser_sprite, self.spaceship_group, False):
					laser_sprite.kill()
					self.lives -= 1
					if self.lives == 0:
						self.game_over()

				for obstacle in self.obstacles:
					if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
						laser_sprite.kill()

		if self.aliens_group:
			for alien in self.aliens_group:
				for obstacle in self.obstacles:
					pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)

				if pygame.sprite.spritecollide(alien, self.spaceship_group, False):
					self.game_over()

	def game_over(self):
		self.run = False

	def reset(self):
		self.run = True
		self.lives = 3
		self.spaceship_group.sprite.reset()
		self.aliens_group.empty()
		self.alien_lasers_group.empty()
		self.create_aliens()
		self.mystery_ship_group.empty()
		self.obstacles = self.create_obstacles()
		self.score = 0

	def check_for_highscore(self):
		if self.score > self.highscore:
			self.highscore = self.score

			with open("highscore.txt", "w") as file:
				file.write(str(self.highscore))

	def load_highscore(self):
		try:
			with open("highscore.txt", "r") as file:
				self.highscore = int(file.read())
		except FileNotFoundError:
			self.highscore = 0

game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

SHOOT_LASER = pygame.USEREVENT
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP = pygame.USEREVENT + 1
pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))

while True:
    #Checking for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SHOOT_LASER and game.run:
            game.alien_shoot_laser()

        if event.type == MYSTERYSHIP and game.run:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP, random.randint(4000,8000))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.run == False:
            game.reset()

    #Updating
    if game.run:
        game.spaceship_group.update()
        game.move_aliens()
        game.alien_lasers_group.update()
        game.mystery_ship_group.update()
        game.check_for_collisions()

    #Drawing
    screen.fill(GREY)

    #UI
    pygame.draw.rect(screen, GREEN, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, GREEN, (25, 730), (775, 730), 3)

    if game.run:
        screen.blit(level, (570, 740, 50, 50))
    else:
        screen.blit(game_over_surface, (570, 740, 50, 50))

    x = 50
    for life in range(game.lives):
        screen.blit(game.spaceship_group.sprite.image, (x, 745))
        x += 50

    screen.blit(score_text_surface, (50, 15, 50, 50))
    formatted_score = str(game.score).zfill(5)
    score_surface = font.render(formatted_score, False, GREEN)
    screen.blit(score_surface, (50, 40, 50, 50))
    screen.blit(highscore_text_surface, (550, 15, 50, 50))
    formatted_highscore = str(game.highscore).zfill(5)
    highscore_surface = font.render(formatted_highscore, False, GREEN)
    screen.blit(highscore_surface, (625, 40, 50, 50))

    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.lasers_group.draw(screen)
    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)
    game.aliens_group.draw(screen)
    game.alien_lasers_group.draw(screen)
    game.mystery_ship_group.draw(screen)

    pygame.display.update()
    clock.tick(60)