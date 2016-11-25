#Class that all objects will inherit from
#Provides hitboxes
import pygame

class Entity():
	"""docstring for Entity"""
	def __init__(self):
		super(Entity, self).__init__()
		self.x = 0
		self.y = 0
		self.width = 0
		self.height = 0
		self.hitbox	= pygame.Rect(self.x, self.y, self.width, self.height)

	def hb_follow(self):
		self.hitbox.x = self.x
		self.hitbox.y = self.y
		self.hitbox.width = self.width
		self.hitbox.height = self.height