#Classes for game coins
import pygame
from CoinImages import *

screen = pygame.display.set_mode()

class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y, xspeed, yspeed, coinimg, imagecount, imgs, value):
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.coinimg = coinimg
		self.imagecount = imagecount
		self.imgs = imgs
		self.value = value


class PlatinumCoin(Coin):
	def __init__(self, x, y, xspeed, yspeed, coinimg, imagecount, imgs, value):
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.coinimg = coinimg
		self.imagecount = 0
		self.imgs = platinumcoinimgs
		self.value = 150

	def update(self):
		screen.blit(self.imgs[int(self.imagecount)],(self.x, self.y))

		self.imagecount += 0.5
		if self.imagecount > 9:
			self.imagecount = 0

		
		if self.x < 0 or self.x > 993:
			self.xspeed *= -1

		if self.y < 0 or self.y > 598:
			self.yspeed *= -1

		self.x += self.xspeed
		self.y += self.yspeed

		self.x = round(self.x, 1)
		self.y = round(self.y, 1)


class GoldCoin(Coin):
	def __init__(self, x, y, xspeed, yspeed, coinimg, imagecount, imgs, value):
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.coinimg = coinimg
		self.imagecount = 0
		self.imgs = goldcoinimgs
		self.value = 50

	def update(self):
		screen.blit(self.imgs[int(self.imagecount)],(self.x, self.y))

		self.imagecount += 0.5
		if self.imagecount > 9:
			self.imagecount = 0

		
		'''if self.x < 0 or self.x > 993:
			self.xspeed *= -1

		if self.y < 0 or self.y > 600:
			self.yspeed *= -1'''

		self.x += self.xspeed
		self.y += self.yspeed

		self.x = round(self.x, 1)
		self.y = round(self.y, 1)


class SilverCoin(Coin):
	def __init__(self, x, y, xspeed, yspeed, coinimg, imagecount, imgs, value):
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.coinimg = coinimg
		self.imagecount = 0
		self.imgs = silvercoinimgs
		self.value = 10

	def update(self):
		screen.blit(self.imgs[int(self.imagecount)],(self.x, self.y))

		self.imagecount += 0.5
		if self.imagecount > 9:
			self.imagecount = 0

		
		'''if self.x < 0 or self.x > 993:
			self.xspeed *= -1

		if self.y < 0 or self.y > 600:
			self.yspeed *= -1'''

		self.x += self.xspeed
		self.y += self.yspeed

		self.x = round(self.x, 1)
		self.y = round(self.y, 1)


class CopperCoin(Coin):
	def __init__(self, x, y, xspeed, yspeed, coinimg, imagecount, imgs, value):
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.coinimg = coinimg
		self.imagecount = 0
		self.imgs = coppercoinimgs
		self.value = 1

	def update(self):
		screen.blit(self.imgs[int(self.imagecount)],(self.x, self.y))

		self.imagecount += 0.5
		if self.imagecount > 9:
			self.imagecount = 0

		
		'''if self.x < 0 or self.x > 993:
			self.xspeed *= -1

		if self.y < 0 or self.y > 600:
			self.yspeed *= -1'''

		self.x += self.xspeed
		self.y += self.yspeed

		self.x = round(self.x, 1)
		self.y = round(self.y, 1)