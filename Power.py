#Classes for power ups
from PowerImages import *
from random import randint
screen = pygame.display.set_mode()

class PowerUp(pygame.sprite.Sprite):
	def __init__(self, x, y, xspeed, yspeed, name, powimg, pow_speed, coolant, duration):
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.name = name
		self.powimg = powimg
		self.pow_speed = pow_speed

class SinWave(PowerUp):
	def __init__(self, x, y, xspeed, yspeed, name, powimg, pow_speed, coolant, duration, imagecount, images):
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.name = "sinwave"
		self.powimg = "none"
		self.pow_speed = 0
		self.imagecount = 0
		self.images = sinwaveimgs
		self.coolant = 0.75
		self.duration = 100

	def update(self):
		self.imagecount += 0.5
		if self.imagecount > 6:
			self.imagecount = 0
		screen.blit(self.images[int(self.imagecount)],(self.x, self.y))
		self.x += self.xspeed
		self.y += self.yspeed


class Super(PowerUp):
	def __init__(self, x, y, xspeed, yspeed, name, powimg, pow_speed, coolant, duration, imagecount, images):
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.name = "super"
		self.powimg = "none"
		self.pow_speed = 0
		self.imagecount = 0
		self.images = superimgs
		self.coolant = 0.7
		self.duration = 45

	def update(self):
		self.imagecount += 1
		if self.imagecount > 4:
			self.imagecount = 0
		screen.blit(self.images[self.imagecount],(self.x, self.y))
		self.x += self.xspeed
		self.y += self.yspeed

class IceI(PowerUp):
	def __init__(self, x, y, xspeed, yspeed, name, powimg, pow_speed, coolant, duration, imagecount, images):
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.name = "icei"
		self.powimg = "none"
		self.pow_speed = 0.2
		self.imagecount = 0
		self.images = iceiimgs
		self.coolant = 0.15
		self.duration = 1000

	def update(self):
		self.imagecount += 0.25
		if self.imagecount > 9:
			self.imagecount = 0
		screen.blit(self.images[int(self.imagecount)],(self.x, self.y))
		self.x += self.xspeed
		self.y += self.yspeed
