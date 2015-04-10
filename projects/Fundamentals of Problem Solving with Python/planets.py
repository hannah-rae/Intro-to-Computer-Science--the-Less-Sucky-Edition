def getRadius(planet):
	for body in planetInfo:
		if body[0] == planet:
			return int(body[2])

def getDiameter(planet):
	return getRadius(planet)*2

def getCircumference(planet):
	return getDiameter(planet)*3.14

def getSurfaceArea(planet):
	rad = getRadius(planet)
	surfaceArea = 2*3.14*(rad*rad)
	return surfaceArea

def getMass(planet):
	for body in planetInfo:
		if body[0] == planet:
			return body[1]

def getType(planet):
	for body in planetInfo:
		if body[0] == planet:
			return body[3]

def compareSurfAreaToEarth(planet):
	ratio = getSurfaceArea(planet)/getSurfaceArea("Earth")
	return ratio

def loadInfo():
	for line in file('objectInfo.txt', 'r'):
		line.rstrip('\r\n')
		planetArray = line.split()
		planetInfo.append(planetArray)
	return planetInfo

planetInfo = []
planetInfo = loadInfo()
while(True):
	userPlanet = raw_input("Which object would you like to know about?\n")
	userOp = int(raw_input("""What would you like to know about it?\n(0) Radius\n(1) Diameter\n(2) Circumference\n(3) Mass \n(4) Classification \n(5) Surface Area \n(6) Size compared to Earth (ratio of surface areas)\n"""))

	if userOp == 0:
		print 'The radius of', userPlanet, 'is', getRadius(userPlanet), 'km.\n'
	elif userOp == 1:
		print 'The diameter of', userPlanet, 'is', getDiameter(userPlanet), 'km.\n'
	elif userOp == 2:
		print 'The circumference of', userPlanet, 'is', getCircumference(userPlanet), 'km.\n'
	elif userOp == 3:
		print 'The mass of', userPlanet, 'is', getMass(userPlanet), 'Earth masses.\n'
	elif userOp == 4:
		objType = getType(userPlanet)
		if objType[0] == 'a':
			print userPlanet, 'is an', objType, '\n'
		else:
			print userPlanet, 'is a', objType, '\n'
	elif userOp == 5:
		print 'The surface area of', userPlanet, 'is', getSurfaceArea(userPlanet), 'km^2.\n'
	elif userOp == 6:
		saRatio = compareSurfAreaToEarth(userPlanet)
		if saRatio < 1:
			print userPlanet, 'is', saRatio, 'times smaller than Earth.\n'
		else:
			print userPlanet, 'is', saRatio, 'times larger than Earth.\n'