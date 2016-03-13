#Classes for lasers and other weapons
import pygame
from WeaponImages import *
from math import sin
from math import tan
from random import randint
screen = pygame.display.set_mode()

def x_power_up(xpowerup, x, y):
	if xpowerup == "tanwave":
		x -= tan(y)
	if xpowerup == "sinwave":
		x -= sin(sin(y/10))*10
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
		self.speed = 20
		self.weaponimg = stream_image
		self.x += 8
		self.y += -14
		self.xpowerup = xpowerup
		self. ypowerup = ypowerup

	def update(self):
		screen.blit(self.weaponimg,(self.x, self.y))
		self.y -= self.speed
		self.x = x_power_up(self.xpowerup, self.x, self.y)
		self.y = y_power_up(self.ypowerup, self.x, self.y)

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
		self.x -= sin(self.y)*10
		self.x = x_power_up(self.xpowerup, self.x, self.y)
		self.y = y_power_up(self.ypowerup, self.x, self.y)