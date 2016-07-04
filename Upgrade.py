#Script for upgrades
from UpgradeImages import *
from Weapon import *
screen = pygame.display.set_mode()

class Upgrade(pygame.sprite.Sprite):
	def __init__(self, x, y, xspeed, yspeed, name, images, imgplc):
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.name = name
		self.images = images
		self.imgplc = imgplc


class Damage0(Upgrade):
	def __init__(self, x, y, xspeed, yspeed, name, images, imgplc):
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.name = "damage0"
		self.images = [damage0_image_0,damage0_image_1,damage0_image_2,damage0_image_3,damage0_image_4,damage0_image_5,damage0_image_6,damage0_image_7]
		self.imgplc = 0

	def update(self):
		screen.blit(self.images[self.imgplc],(self.x, self.y))
		self.imgplc += 1
		if self.imgplc > len(self.images)-1:
			self.imgplc = 0

		self.x += self.xspeed
		self.y += self.yspeed

		if self.x < 0 or self.x > 993:
			self.xspeed *= -1

		if self.y < 0 or self.y > 598:
			self.yspeed *= -1

class Backfire(Upgrade):
	def __init__(self, x, y, xspeed, yspeed, name, images, imgplc):
		self.x = x
		self.y = y
		self.xspeed = xspeed
		self.yspeed = yspeed
		self.name = "backfire"
		self.images = [backfire_image_0, backfire_image_1, backfire_image_2, backfire_image_3, backfire_image_4, backfire_image_5]
		self.imgplc = 0

	def update(self):
		screen.blit(self.images[self.imgplc],(self.x, self.y))
		self.imgplc += 1
		if self.imgplc > len(self.images)-1:
			self.imgplc = 0

		self.x += self.xspeed
		self.y += self.yspeed

		if self.x < 0 or self.x > 993:
			self.xspeed *= -1

		if self.y < 0 or self.y > 598:
			self.yspeed *= -1