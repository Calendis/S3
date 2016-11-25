#Classes for enemy ships
import pygame
from random import randint
from time import time
from EnemyImages import *
from Entity import *
from math import tan
from math import cos
screen = pygame.display.set_mode()

class Enemy(Entity):
	def __init__(self):
		super(Enemy, self).__init__()
		self.width = 32
		self.height = 32
		self.xspeed = 0
		self.yspeed = 0
		self.shipimg = [sparrow_right_image]
		self.imgno = 0
		self.firing = False
		self.hp = 0
		self.formation = True
		self.points = 0
		self.drops = 0
		self.generictype = "Enemy"

	def update(self):
		screen.blit(self.shipimg[self.imgno],(round(self.x), round(self.y)))
		self.y += self.yspeed
		self.x += self.xspeed

		if self.y > 700:
			self.y = -32
			self.x = randint(0,980)
			self.formation = False

class Shop(Enemy):
	"""docstring for Shop"""
	def __init__(self, x, y):
		super(Shop, self).__init__()
		self.x = x
		self.y = y
		self.width = 128
		self.height = 36
		self.xspeed = 1.5
		self.yspeed = 0.3
		self.shipimg = [shop_image]
		self.hp = 100
		self.points = 50
		self.drops = 2
		self.generictype = "Shop"

	def update(self):
		screen.blit(self.shipimg[self.imgno],(round(self.x), round(self.y)))
		self.y += self.yspeed
		self.x += self.xspeed

		if self.y > 700:
			self.y = -32
			self.x = randint(0,980)

		if self.x > 1000:
			self.x = -200

	def shop(self):
		pygame.time.delay(5000)


class Sparrow(Enemy):
	def __init__(self, x, y):
		super(Sparrow, self).__init__()
		self.x = x
		self.y = y
		self.xspeed = 0
		self.yspeed = 4
		self.shipimg = [sparrow_centre_image, sparrow_right_image, sparrow_left_image]
		self.hp = 1
		self.points = 26
		self.drops = 0.1
		

class Swallow(Enemy):
	def __init__(self, x, y):
		super(Swallow, self).__init__()
		self.x = x
		self.y = y
		self.xspeed = 2
		self.yspeed = 5.5
		self.shipimg = [swallow_centre_image, swallow_right_image, swallow_left_image]
		self.hp = 2
		self.points = 35
		self.drops = 0.1

	def update(self):
		screen.blit(self.shipimg[self.imgno],(round(self.x), round(self.y)))
		self.y += self.yspeed

		if self.y > 700:
			self.y = -32
			self.x = randint(0,980)
			self.formation = False

	def moveright(self):
		self.imgno = 1
		self.x += self.xspeed
	def moveleft(self):
		self.imgno = 2
		self.x -= self.xspeed
	def repos(self):
		self.imgno = 0


class Cardinal(Enemy):
	def __init__(self, x, y):
		super(Cardinal, self).__init__()
		self.x = x
		self.y = y
		self.xspeed = 0
		self.yspeed = 2
		self.shipimg = [cardinal_centre_image, cardinal_right_image, cardinal_left_image]
		self.hp = 20
		self.points = 50
		self.drops = 0.3


class Crow(Enemy):
	def __init__(self, x, y):
		super(Crow, self).__init__()
		self.x = x
		self.y = y
		self.xspeed = 0
		self.yspeed = 1.4
		self.shipimg = [crow_centre_image, crow_right_image, crow_left_image]
		self.hp = 1
		self.points = 120
		self.drops = 0.015
		self.time_elapser = time()

		global mod

		if randint(0,1) == 0:
			mod = -1
		else:
			mod = 1

	def update(self):
		screen.blit(self.shipimg[self.imgno],(round(self.x), round(self.y)))
		self.y += self.yspeed
		self.x += self.xspeed

		self.y = round(self.y, 1)

		if self.y > 700:
			self.y = -32
			self.x = randint(0, 980)
			self.formation = False

		self.xspeed = int(tan(cos(self.y/200))*mod)*2
		if self.x < 16 or self.x > 984:
			self.xspeed = 0


class Bluebird(Enemy):
	def __init__(self, x, y):
		super(Bluebird, self).__init__()
		self.x = x
		self.y = y
		self.xspeed = 0
		self.yspeed = 5.5
		self.shipimg = [bluebird_centre_image, bluebird_right_image, bluebird_left_image]
		self.hp = 4
		self.points = 77
		self.drops = 0.05


class Hawk(Enemy):
	def __init__(self, x, y):
		super(Hawk, self).__init__()
		self.x = x
		self.y = y
		self.height = 40
		self.xspeed = randint(-1,1)
		self.yspeed = -10
		self.shipimg = [hawk_centre_image]
		self.hp = 2
		self.points = 200
		self.drops = 0.03

	def update(self):
		screen.blit(self.shipimg[self.imgno],(round(self.x), round(self.y)))
		self.y += self.yspeed
		self.x += self.xspeed
		if self.y < -32:
			self.y = 700
			self.x = randint(0, 980)
			self.formation = False

			self.xspeed = randint(-1,1)


class SwallowMKII(Enemy):
	def __init__(self, x, y):
		super(SwallowMKII, self).__init__()
		self.x = x
		self.y = y
		self.xspeed = 4
		self.yspeed = 5
		self.shipimg = [swallowmkii_centre_image, swallowmkii_right_image, swallowmkii_left_image]
		self.hp = 4
		self.points = 280
		self.drops = 0.02

	def update(self):
		screen.blit(self.shipimg[self.imgno],(round(self.x), round(self.y)))
		self.y += self.yspeed

		if self.y > 700:
			self.y = -32
			self.x = randint(0,980)
			self.formation = False

	def moveright(self):
		self.imgno = 1
		self.x += self.xspeed
	def moveleft(self):
		self.imgno = 2
		self.x -= self.xspeed
	def repos(self):
		self.imgno = 0