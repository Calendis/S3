#Classes for enemy weapons
import pygame
from WeaponImages import *
from Entity import *
screen = pygame.display.set_mode()

class EnemyWeapon(Entity):
	def __init__(self):
		super(EnemyWeapon, self).__init__()
		self.speed = 0
		self.weaponimg = "none"
		self.damage = 0
		self.generictype = "EnemyWeapon"

	def update(self):
		screen.blit(self.weaponimg,(round(self.x), round(self.y)))
		self.y += self.speed

class StreamG(EnemyWeapon):
	def __init__(self, x, y):
		super(StreamG, self).__init__()
		self.width = 16
		self.height = 16
		self.speed = 11
		self.weaponimg = streamg_image
		self.x = x + 8
		self.y = y + 8
		self.damage = 1
		