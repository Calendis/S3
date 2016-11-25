#Classes for buttons
from ButtonImages import *
from MainSoundLoader import menu0

screen = pygame.display.set_mode()

class Button():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.images = []
		self.img_count = 0
		self.hovered = False

class PlayButton(Button):
	def __init__(self, x, y):
		super(PlayButton, self).__init__()
		self.x = x
		self.y = y
		self.images = [play_default, play_hover, play_pressed]
		self.img_count = 0
		
	def update(self):
		screen.blit(self.images[self.img_count], (self.x, self.y))

		if self.hovered == False:
			if pygame.mouse.get_pos()[0] - self.x < 88 and pygame.mouse.get_pos()[0] - self.x > 0 and pygame.mouse.get_pos()[1] - self.y < 28 and pygame.mouse.get_pos()[1] - self.y > 0:
				self.img_count = 1
				self.hovered = True
				self.when_hovered()
		elif pygame.mouse.get_pos()[0] - self.x not in range(0, 88) or pygame.mouse.get_pos()[1] - self.y not in range(0, 28):
			self.img_count = 0
			self.hovered = False

	def when_clicked(self):
		self.img_count = 2

	def when_hovered(self):
		menu0.play()
