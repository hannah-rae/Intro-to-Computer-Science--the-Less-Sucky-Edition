class SkyObject:
	def __init__(self, name, mass, radius, classification):
		self.name = name
		self.radius = radius
		self.mass = mass
		self.type = classification

	def getDiameter(self):
		return self.radius*2

	def getCircumference(self):
		return 2*3.14*self.radius

	def getSurfaceArea(self):
		return 4*3.14*self.radius*self.radius

def loadInfo():
	for line in file('objectInfo.txt', 'r'):
		line.rstrip('\r\n')
		a = line.split()
		objectInfo.append(SkyObject(a[0], float(a[1]), float(a[2]), a[3]))
	return objectInfo

objectInfo = []
objectInfo = loadInfo()
while(True):
	userObject = raw_input("Which object would you like to know about?\n")
	for requestedObject in objectInfo:
		if userObject == requestedObject.name:
			break
	userOp = int(raw_input("""What would you like to know about it?\n(0) Radius\n(1) Diameter\n(2) Circumference\n(3) Mass \n(4) Classification \n(5) Surface Area \n(6) Size compared to Earth (ratio of surface areas)\n"""))
	if userOp == 0:
		print 'The radius of', userObject, 'is', requestedObject.radius, 'km.\n'
	elif userOp == 1:
		print 'The diameter of', userObject, 'is', requestedObject.getDiameter(), 'km.\n'
	elif userOp == 2:
		print 'The circumference of', userObject, 'is', requestedObject.getCircumference(), 'km.\n'
	elif userOp == 3:
		print 'The mass of', userObject, 'is', requestedObject.mass, 'Earth masses.\n'
	elif userOp == 4:
		objType = requestedObject.type
		if objType[0] == 'a':
			print userObject, 'is an', objType, '\n'
		else:
			print userObject, 'is a', objType, '\n'
	elif userOp == 5:
		print 'The surface area of', userObject, 'is', requestedObject.getSurfaceArea(), 'km^2.\n'