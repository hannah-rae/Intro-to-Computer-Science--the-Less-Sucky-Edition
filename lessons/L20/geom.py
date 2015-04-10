import math

class Point:
	def __init__(self, x_value, y_value):
		self.x = x_value
		self.y = y_value

class Rectangle:
	def __init__(self, p1, p2, p3, p4):
		self.top_left = p1
		self.top_right = p2
		self.bottom_left = p3
		self.bottom_right = p4

	def getHeight(self):
		diff_y = self.top_right.y - self.bottom_right.y
		diff_x = self.top_right.x - self.bottom_right.x
		height = math.sqrt( math.pow(diff_x, 2) + math.pow(diff_y, 2) )
		return height

	def getWidth(self):
		diff_y = self.top_right.y - self.top_left.y
		diff_x = self.top_right.x - self.top_left.x
		width = math.sqrt( math.pow(diff_x, 2) + math.pow(diff_y, 2) )
		return width

	def getArea(self):
		return self.getWidth() * self.getHeight()