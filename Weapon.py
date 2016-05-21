#Classes for lasers and other weapons
import pygame
from WeaponImages import *
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

class Weapon(pygame.sprite.Sprite):
	def __init__(self, speed, weaponimg, x, y, xpowerup, ypowerup):
		super().__init__()
		self.speed = speed
		self.weaponimg = weaponimg
		self.x = x
		self.y = y
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup

class Stream(Weapon):
	def __init__(self, speed, weaponimg, x, y, xpowerup, ypowerup):
		super().__init__(speed, weaponimg, x, y, xpowerup, ypowerup)
		self.speed = 20.0
		self.weaponimg = stream_image
		self.x += 11
		self.y += -14
		self.xpowerup = xpowerup
		self. ypowerup = ypowerup

	def update(self):
		screen.blit(self.weaponimg,(self.x, self.y))
		self.y -= self.speed
		self.x = x_power_up(self.xpowerup, self.x, self.y)
		self.y = y_power_up(self.ypowerup, self.x, self.y)
		self.x = round(self.x, 1)
		self.y = round(self.y, 1)

class GBall(Weapon):
	def __init__(self, speed, weaponimg, x, y, xpowerup, ypowerup):
		super().__init__(speed, weaponimg, x, y, xpowerup, ypowerup)
		self.speed = 30
		self.weaponimg = gball_image
		self.x += 12
		self.y += -10
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup

	def update(self):
		screen.blit(self.weaponimg,(self.x, self.y))
		self.y -= self.speed
		self.x -= int(sin(self.y)*10)
		self.x = x_power_up(self.xpowerup, self.x, self.y)
		self.y = y_power_up(self.ypowerup, self.x, self.y)