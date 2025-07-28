import sys
from asteroidfield import *
from player import *
from constants import *
from asteroid import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	print("Starting Asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		for drawable_obj in drawable:
			drawable_obj.draw(screen)
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game Over!")
				sys.exit()
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
