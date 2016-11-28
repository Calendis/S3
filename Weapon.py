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
		self.xspeed = 0
		self.weaponimg = stream_image
		self.xpowerup = "none"
		self.ypowerup = "none"
		self.damage = 0
		self.generictype = "MyWeapon"
		self.heatmultiplier = 1
		self.delaymultiplier = 1

		self.price = 0
		self.manufacturer = "Unknown manufacturer."
		self.description = "Unknown weapon."

	def update(self):
		screen.blit(self.weaponimg, (round(self.x), round(self.y)))
		self.y -= self.speed
		self.x += self.xspeed
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

		self.manufacturer = "Feskin Weaponry"
		self.price = 1000
		self.description = open("txt/weapons/Stream").read()

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
		self.damage = 1.6
		self.heatmultiplier = 1

		self.manufacturer = "Hafna Labs"
		self.price = 1200
		self.description = open("txt/weapons/GBall").read()

class HPBall(Weapon):
	"""docstring for HPBall"""
	def __init__(self, x, y, xpowerup, ypowerup):
		super(HPBall, self).__init__()
		self.width = 8
		self.height = 8
		self.speed = 9
		self.weaponimg = hpball_image
		self.x = x + 12
		self.y = y - 10
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup
		self.damage = 3.5
		self.xspeed = randint(-20,20)/10
		self.heatmultiplier = 2.5

		self.manufacturer = "Hafna Labs"
		self.price = 2400
		self.description = open("txt/weapons/HPBall").read()

class BLaser(Weapon):
	"""docstring for BLaser"""
	def __init__(self, x, y, xpowerup, ypowerup):
		super(BLaser, self).__init__()
		self.width = 3
		self.height = 15
		self.speed = 45
		self.weaponimg = blaser_image
		self.x = x + 14
		self.y = y - 15
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup
		self.damage = 0.3
		self.heatmultiplier = 0.3
		self.delaymultiplier = 0.5

		self.manufacturer = "Hafna Labs"
		self.price = 600
		self.description = open("txt/weapons/BLaser").read()

class ShrapnelBlaster(Weapon):
	"""docstring for Shrap"""
	def __init__(self, x, y, xpowerup, ypowerup):
		super(ShrapnelBlaster, self).__init__()
		self.width = 5
		self.height = 5
		self.speed = 5
		self.weaponimg = shrap_image
		self.x = x + 14
		self.y = y - 10
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup
		self.damage = randint(0,4)/9
		self.heatmultiplier = 0.3
		self.delaymultiplier = 0.1
		self.xspeed = randint(-40,40)/10

		self.manufacturer = "Silk and Spices Corporation"
		self.price = 900
		self.description = open("txt/weapons/Shrap").read()

class HotShrapnelBlaster(Weapon):
	"""docstring for HotShrapnelBlaster"""
	def __init__(self, x, y, xpowerup, ypowerup):
		super(HotShrapnelBlaster, self).__init__()
		self.width = 5
		self.height = 5
		self.speed = 5
		self.x = x + 14
		self.y = y - 10
		self.weaponimg = hotshrap_image
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup
		self.damage = (randint(1,10)/8) + 1
		self.heatmultiplier = 1.3
		self.delaymultiplier = 0.1
		self.xspeed = randint(-40,40)/10

		self.manufacturer = "Silk and Spices Corportaion"
		self.price = 1800
		self.description = open("txt/weapons/HotShrap").read()
		

revolver_xspeeds_pos = 0


class Revolver(Weapon):
	"""docstring for Revolver"""
	def __init__(self, x, y, xpowerup, ypowerup):
		super(Revolver, self).__init__()
		global revolver_xspeeds_pos
		self.width = 5
		self.height = 5
		self.speed = 6
		self.weaponimg = shrap_image
		self.x = x + 14
		self.y = y - 10
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup
		self.damage = 0.3
		self.heatmultiplier = 0.6
		self.delaymultiplier = 0.3
		self.xspeed = sin(revolver_xspeeds_pos) * 5
		revolver_xspeeds_pos += 0.1

class RevolverMkII(Weapon):
	"""docstring for RevolverMkII"""
	def __init__(self, x, y, xpowerup, ypowerup):
		super(RevolverMkII, self).__init__()
		global revolver_xspeeds_pos
		self.width = 5
		self.height = 5
		self.speed = 7
		self.weaponimg = shrap_image
		self.x = x + 14
		self.y = y - 10
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup
		self.damage = 0.2
		self.heatmultiplier = 0.3
		self.delaymultiplier = 0.2
		self.xspeed = sin(revolver_xspeeds_pos) * 2.5
		revolver_xspeeds_pos += 0.1
		

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
		self.delaymultiplier = 0.85

		self.manufacturer = "Feskin Weaponry"
		self.price = 1900
		self.description = open("txt/weapons/LightStream").read()

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

		self.manufacturer = "Feskin Weaponry"
		self.price = 2000
		self.description = open("txt/weapons/RedStream").read()

class Tesla(Weapon):
	"""docstring for Tesla"""
	def __init__(self, x, y, xpowerup, ypowerup):
		super(Tesla, self).__init__()
		self.width = 8
		self.height = 32
		self.speed = 13
		self.weaponimg = teslablast_image
		self.x = x + 12
		self.y = y - 19
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup
		self.damage = 3
		self.heatmultiplier = 2.5
		self.delaymultiplier = 3.5

		self.manufacturer = "Forlorn Technology"
		self.price = 3000
		self.description = open("txt/weapons/Tesla").read()
		