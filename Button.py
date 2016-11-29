#Classes for buttons
from ButtonImages import *
from MainSoundLoader import menu0

screen = pygame.display.set_mode()

class Button():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.images = [clickme_default, clickme_hover, clickme_pressed]
		self.img_count = 0
		self.hovered = False
		self.width = 92
		self.height = 21

	def update(self):
		screen.blit(self.images[self.img_count], (self.x, self.y))

		if self.hovered == False:
			if pygame.mouse.get_pos()[0] - self.x < self.width and pygame.mouse.get_pos()[0] - self.x > 0 and pygame.mouse.get_pos()[1] - self.y < self.height and pygame.mouse.get_pos()[1] - self.y > 0:
				self.img_count = 1
				self.hovered = True
				self.when_hovered()
		elif pygame.mouse.get_pos()[0] - self.x not in range(0, self.width) or pygame.mouse.get_pos()[1] - self.y not in range(0, self.height):
			self.img_count = 0
			self.hovered = False

	def when_clicked(self):
		self.img_count = 2

	def when_hovered(self):
		menu0.play()

class PlayButton(Button):
	def __init__(self, x, y):
		super(PlayButton, self).__init__()
		self.x = x
		self.y = y
		self.images = [play_default, play_hover, play_pressed]
		self.width = 88
		self.height = 28

class ExitButton(Button):
	"""docstring for ExitButton"""
	def __init__(self, x, y):
		super(ExitButton, self).__init__()
		self.x = x
		self.y = y
		
