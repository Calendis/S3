#Classes for buttons
from ButtonImages import *

screen = pygame.display.set_mode()

class Button(pygame.sprite.Sprite):
	def __init__(self, x, y, images, img_count, hovered):
		self.x = x
		self.y = y
		self.images = images
		self.img_count = img_count
		self.hovered = hovered

class PlayButton(Button):
	def __init__(self, x, y, images, img_count, hovered):
		self.x = x
		self.y = y
		self.images = [play_default, play_hover, play_pressed]
		self.img_count = 0
		self.hovered = False
		
	def update(self):
		screen.blit(self.images[self.img_count], (self.x, self.y))

		if pygame.mouse.get_pos()[0] - self.x < 88 and pygame.mouse.get_pos()[0] - self.x > 0 and pygame.mouse.get_pos()[1] - self.y < 28 and pygame.mouse.get_pos()[1] - self.y > 0:
			self.img_count = 1
			self.hovered = True
		else:
			self.img_count = 0
			self.hovered = False

	def when_clicked(self):
		self.img_count = 2
