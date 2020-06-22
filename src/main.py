import pygame
import time
from random import randint

black = (0,0,0)
white = (255,255,255)

pygame.init()

surfaceWidth = 800
surfaceHeight = 500

imageHeight = 50
imageWidth = 50

surface = pygame.display.set_mode((surfaceWidth, surfaceHeight))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

def blocks(x_block, y_block, block_width, block_height, gap):
	pygame.draw.rect(surface, white, [x_block, y_block, block_width, block_height])
	pygame.draw.rect(surface, white, [x_block, y_block+block_height+gap, block_width, block_height])


def replay_or_quit():
	for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		elif event.type == pygame.KEYDOWN:
			continue

		return event.key
	return None

def makeTextObjs(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()

def msgSurface(text):
	smallText = pygame.font.Font('freesansbold.ttf', 20)
	largeText = pygame.font.Font('freesansbold.ttf', 150)

	titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
	titleTextRect.center = surfaceWidth/2, surfaceHeight/2
	surface.blit(titleTextSurf, titleTextRect)

	typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
	typTextRect.center = surfaceWidth/2, ((surfaceHeight/2) + 100)
	surface.blit(typTextSurf, typTextRect)

	pygame.display.update()
	time.sleep(1)

	while replay_or_quit() == None:
		clock.tick()

	main()


def gameOver():
	msgSurface('Kaboom!')

def helicopter(x, y, image):
	surface.blit(img, (x,y))

img = pygame.image.load('../img/bee.png')
img = pygame.transform.scale(img, (50, 50))

def main():
	x = 150
	y = 200
	y_move = 5
	x_block = surfaceWidth
	y_block = 0
	block_width = 75
	block_height = randint(0, surfaceHeight)
	gap = imageHeight*3
	block_move = 3


	game_over = False

	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					y_move = -5
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					y_move = 5

		y += y_move

		surface.fill(black)
		helicopter(x, y, img)

		blocks(x_block, y_block, block_width, block_height, gap)
		x_block -= block_move

		if y > surfaceHeight-50 or y < 0:
			gameOver()

		pygame.display.update()
		clock.tick(60)

main()
pygame.quit()
quit()