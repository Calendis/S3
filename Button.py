#Classes for buttons
from ButtonImages import *

class Button(pygame.sprite.Sprite):
	def __init__(self, x, y, imgs):
		self.x = x
		self.y = y
		self.imgs = imgs

class PlayButton(Button):
	def __init__(self, x, y, imgs):
		self.x = x
		self.y = y
		self.imgs = [clickme_default, clickme_hover, clickme_pressed]
		