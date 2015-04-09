class Cake:
	def __init__(self, cake_flavor, frosting_flavor, writing):
		self.cake_flavor = cake_flavor
		self.frosting_flavor = frosting_flavor
		self.writing = writing

	def getPrice(self):
		return 8 + len(self.writing)*0.1