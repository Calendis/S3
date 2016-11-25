#Classes for formations of enemies
from Enemy import *
from random import randint
from math import sin

class Formation():
	def __init__(self):
		self.types = []
		self.xoffset = []
		self.yoffset = []
		self.pos = 0
		

class SingleSparrow(Formation):
	def __init__(self):
		super(SingleSparrow, self).__init__()
		self.types = [Sparrow]
		self.xoffset = [0]
		self.yoffset = [0]
		self.pos = randint(0,1000)


class BasicLine(Formation):
	def __init__(self):
		super(BasicLine, self).__init__()
		self.types = [Sparrow, Sparrow, Swallow, Sparrow, Sparrow]
		self.xoffset = [60,60,60,60,60]
		self.yoffset = [0, 60, -60, 60, 0]
		self.pos = randint(0,1000)

class TripleSparrow(Formation):
	def __init__(self):
		super(TripleSparrow, self).__init__()
		self.types = [Sparrow, Sparrow, Sparrow]
		self.xoffset = [100, 100, 100]
		self.yoffset = [0, 0, 0]
		self.pos = randint(0,1000)

class DoubleCrow(Formation):
	def  __init__(self):
		super(DoubleCrow, self).__init__()
		self.types = [Crow, Crow]
		self.xoffset = [70,70]
		self.yoffset = randint(0,1)
		if self.yoffset == 0:
			self.yoffset = [-10,-10]
		else:
			self.yoffset = [10,10]

		self.pos = randint(0,1000)

class SingleCardinal(Formation):
	def __init__(self):
		super(SingleCardinal, self).__init__()
		self.types = [Cardinal]
		self.xoffset = [0]
		self.yoffset = [0]
		self.pos = randint(0,1000)

class BatteringRam(Formation):
	def __init__(self):
		super(BatteringRam, self).__init__()
		self.types = [Cardinal,Bluebird,Cardinal,Bluebird,Cardinal,Bluebird,Cardinal,Bluebird,Cardinal,Bluebird,Cardinal,Bluebird,Cardinal,Bluebird,Cardinal,Bluebird,Cardinal,Bluebird,Cardinal,Bluebird,Cardinal,Bluebird,Cardinal]
		self.xoffset = []
		for i in range(len(self.types)):
			self.xoffset.append(15)

		self.yoffset = []
		for i in range(len(self.types)):
			if i % 2 == 0:
				self.yoffset.append(50)
			else:
				self.yoffset.append(-400)

		self.pos = randint(0,1000)


class BlueSquad(Formation):
	def __init__(self):
		super(BlueSquad, self).__init__()
		self.types = [Bluebird, Crow, Bluebird]
		self.xoffset = [100, 30, 100]
		self.yoffset = [-50, 0, -50]
		self.pos = randint(0,1000)

class AdvancedLine(Formation):
	def __init__(self):
		super(AdvancedLine, self).__init__()
		self.types = [Bluebird, Bluebird, Swallow, Bluebird, Bluebird]
		self.xoffset = [60,60,60,60,60]
		self.yoffset = [0, 60, -60, 60, 0]
		self.pos = randint(0,1000)

class SingleHawk(Formation):
	def __init__(self):
		super(SingleHawk, self).__init__()
		self.types = [Hawk]
		self.xoffset = [0]
		self.yoffset = [1032]
		self.pos = randint(0,1000)

class AdvancedWing(Formation):
	def __init__(self):
		super(AdvancedWing, self).__init__()
		self.types = [Bluebird, Bluebird, Bluebird, SwallowMKII, Bluebird, Bluebird, Bluebird]
		self.xoffset = [80,60,50,50,50,60,80]
		self.yoffset = [-80, -70, -65, -60, -65, -70, -80]
		self.pos = randint(0,1000)

class SupremeLine(Formation):
	def __init__(self):
		super(SupremeLine, self).__init__()
		self.types = [SwallowMKII,Hawk,Crow,Hawk,SwallowMKII]
		self.xoffset = [100, 20, 70, 20, 100]
		self.yoffset = [1032, 0, -40, 0, 1032]
		self.pos = randint(0,1000)