#Class for the player's ship
import pygame
from Weapon import *
from ShipImages import *
from WeaponImages import *
from Power import PowerUp
from time import time

screen = pygame.display.set_mode()
weapons = []

class Ship(pygame.sprite.Sprite):
	def __init__(self, x, y, xspeed, yspeed, maxspeed, shipimg, firing,
		xpowerup, ypowerup, isleft, isright, isdown, isup, hp, can_shoot, delay_time,fire_speed):
		super().__init__()
		self.x = x
		self.y = y
		self.xspeed = 0
		self.yspeed = 0
		self.maxspeed = maxspeed
		self.shipimg = shipimg
		self.firing = firing
		self.xpowerup = xpowerup
		self.ypowerup = ypowerup
		self.isleft = False
		self.isright = False
		self.isdown = False
		self.isup = False
		self.hp = 100
		self.can_shoot = True
		self.delay_time = 0
		self.fire_speed = 0.3

	def update(self):
		screen.blit(self.shipimg,(self.x,self.y))
		self.x += self.xspeed
		self.y += self.yspeed
		if self.firing == True:
			if time() - self.delay_time >= self.fire_speed:
				self.can_shoot = True
			if self.can_shoot == True:
				my_weapon = Stream(0,0,self.x,self.y, self.xpowerup, self.ypowerup)
				weapons.append(my_weapon)
				self.delay_time = time()
				self.can_shoot = False

	def repos(self):
		self.shipimg = broadsword_centre_image
		
	def up(self):
		self.yspeed = -self.maxspeed
		isup = True
	def down(self):
		self.yspeed = self.maxspeed
		isdown =  True
	def left(self):
		self.xspeed = -self.maxspeed
		self.shipimg = broadsword_left_image
		isleft =  True
	def right(self):
		self.xspeed = self.maxspeed
		self.shipimg = broadsword_right_image
		isright = True