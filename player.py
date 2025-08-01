import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.timer = 0
		

	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def update(self, dt, *args, **kwargs):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		self.move(dt)
		shots = args[0] if args else None
		self.shoot(shots)
		self.timer -= dt
	def move(self, dt):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			forward = pygame.Vector2(0, 1).rotate(self.rotation)
			self.position += forward * PLAYER_SPEED * dt
		if keys[pygame.K_s]:
			backward = pygame.Vector2(0, 1).rotate(self.rotation)
			self.position -= backward * PLAYER_SPEED * dt
	def shoot(self, shots):
		if self.timer > 0:
			return
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE]:			
			shot = Shot(self.position.x, self.position.y, SHOT_RADIUS, self.rotation)
			shots.add(shot)
			self.timer = PLAYER_SHOOT_COOLDOWN
class Shot(CircleShape):
	containers = ()
	def __init__(self, x, y, radius, rotation):
		super().__init__(x, y, radius)
		self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
		self.add(*self.containers)
		
	def draw(self, screen):
		pygame.draw.circle(screen,
						   (255, 255, 255),
						   (int(self.position.x),
							int(self.position.y)),
						   self.radius,
						   2)
	def update(self, dt, *args, **kwargs):
		self.position += self.velocity * dt
