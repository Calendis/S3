#Classes for formations of enemies
from Enemy import *
from random import randint
from math import sin

class Formation():
	def __init__(self, types, xoffset, yoffset, pos):
		self.types = types
		self.xoffset = xoffset
		self.yoffset = yoffset
		self.pos = pos


class BasicLine(Formation):
	def __init__(self, types, xoffset, yoffset, pos):
		self.types = [Sparrow, Swallow, Sparrow]
		self.xoffset = [60,60,60]
		self.yoffset = [0,-42,0]
		self.pos = randint(0,1000)

class DoubleCrow(Formation):
	def  __init__(self, types, xoffset, yoffset, pos):
		self.types = [Crow, Crow]
		self.xoffset = [70,70]
		self.yoffset = randint(0,1)
		if self.yoffset == 0:
			self.yoffset = [-10,-10]
		else:
			self.yoffset = [10,10]

		self.pos = randint(0,1000)

class SingleCardinal(Formation):
	def __init__(self, types, amount, xoffset, yoffset, pos):
		pass