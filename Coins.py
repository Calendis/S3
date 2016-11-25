#Classes for game coins
import pygame
from CoinImages import *
from Entity import *

screen = pygame.display.set_mode()

class Coin(Entity):
	def __init__(self):
		super(Coin, self).__init__()
		self.width = 6
		self.height = 6
		self.xspeed = 0
		self.yspeed = 0
		self.imagecount = 0
		self.imgs = []
		self.value = 0
		self.generictype = "Coin"

	def update(self):
		screen.blit(self.imgs[int(self.imagecount)],(round(self.x), round(self.y)))

		self.imagecount += 0.5
		if self.imagecount > 9:
			self.imagecount = 0

		self.x += self.xspeed
		self.y += self.yspeed


class PlatinumCoin(Coin):
	def __init__(self, x, y, xspeed, yspeed):
		super(PlatinumCoin, self).__init__()
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.imgs = platinumcoinimgs
		self.value = 150

	def update(self):
		screen.blit(self.imgs[int(self.imagecount)],(round(self.x), round(self.y)))

		self.imagecount += 0.5
		if self.imagecount > 9:
			self.imagecount = 0

		
		if self.x < 0 or self.x > 993:
			self.xspeed *= -1

		if self.y < 0 or self.y > 598:
			self.yspeed *= -1

		self.x += self.xspeed
		self.y += self.yspeed


class GoldCoin(Coin):
	def __init__(self, x, y, xspeed, yspeed):
		super(GoldCoin, self).__init__()
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.imgs = goldcoinimgs
		self.value = 50

class SilverCoin(Coin):
	def __init__(self, x, y, xspeed, yspeed):
		super(SilverCoin, self).__init__()
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.imgs = silvercoinimgs
		self.value = 10

class CopperCoin(Coin):
	def __init__(self, x, y, xspeed, yspeed):
		super(CopperCoin, self).__init__()
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.imgs = coppercoinimgs
		self.value = 1
