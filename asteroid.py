import pygame.draw
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		if hasattr(self, 'containers'):
			for group in self.containers:
				group.add(self)
		
	def draw(self, screen):
		pygame.draw.circle(screen,
						   (255, 255, 255),
						   (int(self.position.x),
							int(self.position.y)),
						   self.radius,
						   2)
		
	def update(self, dt, *args, **kwargs):
		self.position += self.velocity * dt
		
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		randangle = random.uniform(20, 50)
		radius1 = self.radius - ASTEROID_MIN_RADIUS
		radius2 = self.radius - ASTEROID_MIN_RADIUS
		new_asteroid1 = Asteroid(self.position.x, self.position.y, radius1)
		new_asteroid2 = Asteroid(self.position.x, self.position.y, radius2)
		new_asteroid1.velocity = self.velocity.rotate(-randangle) * 1.2
		new_asteroid2.velocity = self.velocity.rotate(randangle) * 1.2