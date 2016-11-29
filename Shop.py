#Code for the shop
from Button import Button

class SaleObject(Button):
	"""docstring for SaleObject"""
	def __init__(self, x, y, price, images):
		super(SaleObject, self).__init__()
		self.x = x
		self.y = y
		self.price = price
		self.images = []
