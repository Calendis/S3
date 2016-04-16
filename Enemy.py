#Classes for enemy ships
import pygame
from random import randint
from WeaponImages import *
from EnemyImages import *
screen = pygame.display.set_mode()

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y, xspeed, yspeed, shipimg, imgno, firing, hp):
		super().__init__()
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.shipimg = shipimg
		self.imgno = 0
		self.firing = firing
		self.hp = hp

class Sparrow(Enemy):
	def __init__(self, x, y, xspeed, yspeed, shipimg, imgno, firing, hp):
		super().__init__(x, y, xspeed, yspeed, shipimg, imgno, firing, hp)
		self.x = x
		self.y = y
		self.xspeed = 0
		self.yspeed = 4
		self.shipimg = [sparrow_centre_image, sparrow_right_image, sparrow_left_image]
		self.imgno = 0
		self.firing = False
		self.hp = 1

	def update(self):
		screen.blit(self.shipimg[self.imgno],(self.x, self.y))
		self.y += self.yspeed
		if self.y > 700:
			self.y = -32
			self.x = randint(0, 700)
		

class Swallow(Enemy):
	def __init__(self, x, y, xspeed, yspeed, shipimg, imgno, firing, hp):
		super().__init__(x, y, xspeed, yspeed, shipimg, imgno, firing, hp)
		self.x = x
		self.y = y
		self.xspeed = 3
		self.yspeed = 5
		self.shipimg = [swallow_centre_image, swallow_right_image, swallow_left_image]
		self.imgno = 0
		self.firing = False
		self.hp = 2

	def update(self):
		screen.blit(self.shipimg[self.imgno],(self.x, self.y))
		self.y += self.yspeed
		if self.y > 700:
			self.y = -32
			self.x = randint(0, 700)
	def moveright(self):
		self.imgno = 1
		self.x += self.xspeed
	def moveleft(self):
		self.imgno = 2
		self.x -= self.xspeed
	def repos(self):
		self.imgno = 0