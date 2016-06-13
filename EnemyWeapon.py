#Classes for enemy weapons
import pygame
from WeaponImages import *
screen = pygame.display.set_mode()

class EnemyWeapon(pygame.sprite.Sprite):
	def __init__(self, speed, weaponimg, x, y, damage):
		self.speed = speed
		self.weaponimg = weaponimg
		self.x = x
		self.y = y
		self.damage = damage



class StreamG(EnemyWeapon):
	def __init__(self, speed, weaponimg, x, y, damage):
		self.speed = 11.0
		self.weaponimg = streamg_image
		self.x = x + 8
		self.y = y + 8
		self.damage = 1

	def update(self):
		screen.blit(self.weaponimg,(self.x, self.y))
		self.y += self.speed