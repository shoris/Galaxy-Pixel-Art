""" a pixel art generator that fills screen 
with randomly chosen colors 
each time key is pressed""" 

import pygame
import random
import os 

SCREEN_WIDTH = 400	
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# RGB
PEACH = (255, 204, 204)
LIGHT_BLUE = (204, 255, 255)
YELLOW = (255, 255, 230)
LIGHT_GREEN = (204, 255, 204)
PERIWINKLE = (230, 242, 255)
LIGHT_ORANGE = (255, 230, 204)
PURPLE_PINK = (204, 102, 153)
SEA_BLUE = (132, 225, 225)
PURPLE = (194, 153, 255)
WHITE = (255, 255, 255)

# background color
BLACK = (0, 0, 0)

# List containing all 10 colors
colors = [PEACH, LIGHT_BLUE, YELLOW, LIGHT_GREEN, PERIWINKLE,
	LIGHT_ORANGE, PURPLE_PINK, SEA_BLUE, PURPLE, WHITE]

class Pixel(pygame.sprite.Sprite):
	"""
	This is the pixel class
	"""
	def __init__(self, color):
		"""
		Constructor-- pass in color and width and height (1)
		"""
		super(Pixel, self).__init__()

		self.image = pygame.Surface([1,1])
		self.image.fill(color)

		self.rect = self.image.get_rect()

# initialize pygame
pygame.init()

# caption
pygame.display.set_caption('Pixel Star Art')

# sprite list
pixel_list = pygame.sprite.Group()

# initialize clock (is this needed??)
clock = pygame.time.Clock()



# main game loop
done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				# function that generates pixels of random color and random location
				pixel = Pixel(random.choice(colors))

				pixel.rect.x = random.randrange(SCREEN_WIDTH)
				pixel.rect.y = random.randrange(SCREEN_HEIGHT)

				pixel_list.add(pixel)
	# clear screen
	screen.fill(BLACK)

	# draw sprites
	pixel_list.draw(screen)

	# flip screen
	pygame.display.flip()

	# pause
	clock.tick(60)
	

# if __name__ == "__main__":
# 	try:
# 		start_program()
# 	except KeyboardInterrupt:
# 		sys.exit(0)


pygame.quit()
