#Classes for power ups
from PowerImages import *
from random import randint
from Entity import *
screen = pygame.display.set_mode()

class PowerUp(Entity):
	def __init__(self):
		super(PowerUp, self).__init__()
		self.width = 16
		self.height = 24
		self.xspeed = 0
		self.yspeed = 0
		self.name = "DEFAULT POWERUP"
		self.powimg = 0
		self.pow_speed = 0
		self.generictype = "PowerUp"
		self.imgspeeddivider = 1

	def update(self):
		self.imagecount += 1/self.imgspeeddivider
		if self.imagecount > len(self.images)-1:
			self.imagecount = 0
		screen.blit(self.images[round(self.imagecount)],(self.x, self.y))
		self.x += self.xspeed
		self.y += self.yspeed

		if self.x < 0 or self.x > 993:
			self.xspeed *= -1

		if self.y < 0 or self.y > 598:
			self.yspeed *= -1

class SinWave(PowerUp):
	def __init__(self, x, y, xspeed, yspeed):
		super(SinWave, self).__init__()
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
		self.imgspeeddivider = 2

	def update(self):
		self.imagecount += 0.5
		if self.imagecount > 6:
			self.imagecount = 0
		screen.blit(self.images[int(self.imagecount)],(self.x, self.y))
		self.x += self.xspeed
		self.y += self.yspeed

		if self.x < 0 or self.x > 993:
			self.xspeed *= -1

		if self.y < 0 or self.y > 598:
			self.yspeed *= -1


class Super(PowerUp):
	def __init__(self, x, y, xspeed, yspeed):
		super(Super, self).__init__()
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

class IceI(PowerUp):
	def __init__(self, x, y, xspeed, yspeed):
		super(IceI, self).__init__()
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
		self.duration = 500
		self.imgspeeddivider = 4