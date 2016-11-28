#Class for the player's ship
import pygame
from Weapon import *
from ShipImages import *
from WeaponImages import *
from ShipSoundLoader import *
from Entity import *
from Power import PowerUp
from time import time
from random import random

screen = pygame.display.set_mode()
weapons = []

class Ship(Entity):
	def __init__(self, x, y, maxspeed, xpowerup, ypowerup, lasertype):
		super(Ship, self).__init__()
		self.x = x
		self.y = y
		self.width = 32
		self.height = 32
		self.xspeed = 0
		self.yspeed = 0
		self.maxspeed = maxspeed
		self.imgplace = 0
		self.shipimgs = [broadsword_centre_image, broadsword_right_image, broadsword_left_image]
		self.firing = False
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup
		self.isleft = False
		self.isright = False
		self.isdown = False
		self.isup = False
		self.hp = 100
		self.can_shoot = True
		self.time_elapser = 0
		self.fire_delay = 0.3
		self.original_fire_delay = self.fire_delay
		self.overheat = 0
		self.coolantbonus = 0
		self.powerleft = 0
		self.powermax = 1
		self.upgrades = [False,False]
		self.lasertype = lasertype
		self.backfire = False
		self.generictype = "Ship"

	def update(self):
		screen.blit(self.shipimgs[self.imgplace],(self.x,self.y))
		self.x += self.xspeed
		self.y += self.yspeed
		
		if self.firing == True:
			self.fire()

		if self.isup == True:
			self.yspeed = -self.maxspeed
			if self.y < 5:
				self.isup = False
		elif self.isup == False and self.isdown != True:
			self.yspeed = 0
		if self.isdown == True:
			if self.y >= 563:
				self.isdown = False
			self.yspeed = self.maxspeed
		elif self.isdown == False and self.isup != True:
			self.yspeed = 0
		if self.isleft == True:
			if self.x < 5:
				self.isleft = False
			self.xspeed = -self.maxspeed
			self.imgplace = 2
		elif self.isleft == False and self.isright != True:
			self.xspeed = 0
		if self.isright == True:
			if self.x > 1000-32-5:
				self.isright = False
			self.xspeed = self.maxspeed
			self.imgplace = 1
		elif self.isright == False and self.isleft != True:
			self.xspeed = 0

		if self.overheat > 0:
			self.overheat -= 0.1 + self.coolantbonus

		self.x = round(self.x, 1)
		self.y = round(self.y, 1)

		'''for upgrade in self.upgrades:
			if upgrade == "damage0":
				self.lasertype = RedStream
			if upgrade == "backfire":
				self.backfire = True'''

		if self.upgrades[0] == "damage0":
			self.lasertype = RedStream
		elif self.upgrades[0] == "light":
			self.lasertype = LightStream
		elif self.upgrades[0] == "revolver":
			self.lasertype = Revolver
		elif self.upgrades[0] == "revolver2":
			self.lasertype = RevolverMkII
		elif self.upgrades[0] == "telsa":
			self.lasertype = Tesla
		elif self.upgrades[0] == "shrap":
			self.lasertype = ShrapnelBlaster
		elif self.upgrades[0] == "shrap2":
			self.lasertype = HotShrapnelBlaster
		elif self.upgrades[0] == "gball":
			self.lasertype = GBall
		elif self.upgrades[0] == "hpball":
			self.lasertype = HPBall
		elif self.upgrades[0] == "blaser":
			self.lasertype = BLaser
		elif self.upgrades[0] == "stream":
			self.lasertype = Stream

		if self.upgrades[1] == "backfire":
			self.backfire = True



	def fire(self):
		if time() - self.time_elapser >= self.fire_delay * self.lasertype(0,0,0,0).delaymultiplier:
			if self.overheat < 44:
				self.can_shoot = True
 	
		if self.can_shoot == True:
			my_weapon = self.lasertype(self.x,self.y, self.xpowerup, self.ypowerup)
			laser1.play()
			weapons.append(my_weapon)
			if self.backfire == True:
				my_weapon_back = self.lasertype(self.x, self.y, self.xpowerup, self.ypowerup)
				my_weapon_back.speed *= -1
				my_weapon_back.y += 42
				weapons.append(my_weapon_back)
				self.overheat += 2 * my_weapon.heatmultiplier
				
			self.overheat += 2 * my_weapon.heatmultiplier
			self.powerdrain()
			self.time_elapser = time()
			self.can_shoot = False


	def repos(self):
		self.imgplace = 0


	def powerdrain(self):
		if self.powerleft >= 1:
				self.powerleft -= 1

		elif self.powerleft < 1:
			if self.xpowerup != "none":
				depower0.play()
				self.xpowerup = "none"
				self.coolantbonus = 0
				self.fire_delay = self.original_fire_delay
				self.powerleft = 0
				self.powermax = 1

	def die(self):
		self.hp = -1.3
		explosion0.play()
		self.overheat = 44	
		self.coolantbonus = -0.1
		self.can_shoot = False
		self.maxspeed = 0
		self.shipimgs = [nothing_image,nothing_image,nothing_image]
		self.y = -2000
