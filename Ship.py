#Class for the player's ship
import pygame
from Weapon import *
from ShipImages import *
from WeaponImages import *
from ShipSoundLoader import *
from Power import PowerUp
from time import time
from random import random

screen = pygame.display.set_mode()
weapons = []

class Ship(pygame.sprite.Sprite):
	def __init__(self, x, y, xspeed, yspeed, maxspeed, imgplace, shipimgs, firing,
		xpowerup, ypowerup, isleft, isright, isdown, isup, hp, can_shoot, time_elapser, fire_delay, overheat,
		coolantbonus, powerleft, powermax):
		super().__init__()
		self.x = x
		self.y = y
		self.xspeed = 0.0
		self.yspeed = 0.0
		self.maxspeed = maxspeed
		self.imgplace = 0
		self.shipimgs = [broadsword_centre_image, broadsword_right_image, broadsword_left_image]
		self.firing = firing
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
		self.overheat = 0
		self.coolantbonus = 0
		self.powerleft = 0
		self.powermax = 1

	def update(self):
		screen.blit(self.shipimgs[self.imgplace],(self.x,self.y))
		self.x += self.xspeed
		self.y += self.yspeed
		
		if self.firing == True:
			self.fire()

		if self.isup == True:
			self.yspeed = -self.maxspeed
		elif self.isup == False and self.isdown != True:
			self.yspeed = 0
		if self.isdown == True:
			if self.y >= 560:
				self.y -= self.maxspeed
				self.isdown = False
			self.yspeed = self.maxspeed
		elif self.isdown == False and self.isup != True:
			self.yspeed = 0
		if self.isleft == True:
			self.xspeed = -self.maxspeed
			self.imgplace = 2
		elif self.isleft == False and self.isright != True:
			self.xspeed = 0
		if self.isright == True:
			self.xspeed = self.maxspeed
			self.imgplace = 1
		elif self.isright == False and self.isleft != True:
			self.xspeed = 0

		if self.overheat > 0:
			self.overheat -= 0.07

		self.x = round(self.x, 1)
		self.y = round(self.y , 1)

	def fire(self):
		if time() - self.time_elapser >= self.fire_delay:
			if self.overheat < 44:
				self.can_shoot = True
 	
		if self.can_shoot == True:
			my_weapon = Stream(0,0,self.x,self.y, self.xpowerup, self.ypowerup)
			laser1.play()
			weapons.append(my_weapon)
			self.overheat += 2 - self.coolantbonus
			self.powerdrain()
			self.time_elapser = time()
			self.can_shoot = False


	def repos(self):
		self.imgplace = 0


	def powerdrain(self):
		if self.powerleft >= 1:
			self.powerleft -= 1
		elif self.powerleft < 1:
			self.xpowerup = "none"
			self.coolantbonus = 0
			self.fire_delay = 0.3
			self.powerleft = 0
			self.powermax = 1

	def die(self):
		explosion0.play()
		#self.overheat = 512
		self.coolantbonus = -2
		self.can_shoot = False
		self.maxspeed = 0
		self.shipimgs = [nothing_image,nothing_image,nothing_image]
		self.y = -2000
