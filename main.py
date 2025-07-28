import pygame
from circleshape import *
from player import *
from constants import *

def main():
	pygame.init
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
	clock = pygame.time.Clock()
	dt = 0
	while pygame:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		player.draw(screen)
		player.update(dt)
		pygame.display.flip()
		clock.tick(60)
		dt = clock.tick(60) / 1000
	print("Starting Asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")

if __name__ == "__main__":
	main()
