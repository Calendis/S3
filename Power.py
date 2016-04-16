#Classes for power ups
from PowerImages import *
from random import randint
screen = pygame.display.set_mode()

class PowerUp(pygame.sprite.Sprite):
	def __init__(self, x, y, xspeed, yspeed, name, powimg, pow_speed):
		super().__init__()
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.name = name
		self.powimg = powimg
		self.pow_speed = pow_speed

class LimitedPowerUp(PowerUp):
	def __init__(self, x, y, xspeed, yspeed, name, powimg, pow_speed, duration):
		super().__init__()
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.name = name
		self.duration = duration
		self.pow_speed = pow_speed
		self.powimg = powimg

class SinWave(PowerUp):
	def __init__(self, x, y, xspeed, yspeed, name, powimg, pow_speed, imagecount, images):
		super().__init__(x, y, xspeed, yspeed, name, powimg, pow_speed)
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.name = "sinwave"
		self.powimg = sinwave_image1
		self.pow_speed = 0
		self.imagecount = 0
		self.images = [sinwave_image1,sinwave_image2,sinwave_image3,sinwave_image4,sinwave_image5,sinwave_image6,sinwave_image7]

	def update(self):
		self.imagecount += 1
		if self.imagecount > 6:
			self.imagecount = 0
		screen.blit(self.images[self.imagecount],(self.x, self.y))
		self.x += self.xspeed
		self.y += self.yspeed

