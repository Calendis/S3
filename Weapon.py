#Classes for lasers and other weapons
import pygame
from WeaponImages import *
from Entity import *
from math import sin
from math import tan
from random import randint
screen = pygame.display.set_mode()
def x_power_up(xpowerup, x, y):
	if xpowerup == "tanwave":
		x -= int(tan(y))
	if xpowerup == "sinwave":
		x -= int(sin(sin(y))*20)
	if xpowerup == "super":
		x = randint(0,1000)

	return x

def y_power_up(ypowerup, x, y):
	if ypowerup == "beam":
		y += 16
	if ypowerup == "spread":
		y -= 16

	return y

class Weapon(Entity):
	def __init__(self):
		super(Weapon, self).__init__()
		self.speed = 0
		self.weaponimg = stream_image
		self.xpowerup = "none"
		self.ypowerup = "none"
		self.damage = 0
		self.generictype = "MyWeapon"
		self.heatmultiplier = 1

	def update(self):
		screen.blit(self.weaponimg, (round(self.x), round(self.y)))
		self.y -= self.speed
		self.x = x_power_up(self.xpowerup, self.x, self.y)
		self.y = y_power_up(self.ypowerup, self.x, self.y)

class Stream(Weapon):
	def __init__(self, x, y, xpowerup, ypowerup):
		super(Stream, self).__init__()
		self.width = 10
		self.height = 14
		self.speed = 20
		self.weaponimg = stream_image
		self.x = x + 11
		self.y = y - 14
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup
		self.damage = 1

class LightStream(Weapon):
	"""docstring for LightStream"""
	def __init__(self, x, y, xpowerup, ypowerup):
		super(LightStream, self).__init__()
		self.width = 10
		self.height = 14
		self.speed = 20
		self.weaponimg = lightstream_image
		self.x = x + 11
		self.y = y - 14
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup
		self.damage = 0.5
		self.heatmultiplier = 0.2

class GBall(Weapon):
	def __init__(self, x, y, xpowerup, ypowerup):
		super(GBall, self).__init__()
		self.width = 8
		self.height = 8
		self.speed = 4
		self.weaponimg = gball_image
		self.x = x + 12
		self.y = y - 10
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup
		self.damage = 2

	def update(self):
		screen.blit(self.weaponimg,(round(self.x), round(self.y)))
		self.y -= self.speed
		#self.x -= int(sin(self.y)*10)
		self.x = x_power_up(self.xpowerup, self.x, self.y)
		self.y = y_power_up(self.ypowerup, self.x, self.y)

class RedStream(Weapon):
	def __init__(self, x, y, xpowerup, ypowerup):
		super(RedStream, self).__init__()
		self.width = 10
		self.height = 14
		self.speed = 21
		self.weaponimg = redstream_image
		self.x = x + 11
		self.y = y -14
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup
		self.damage = 2
		self.heatmultiplier = 2