while True:
	inputName = raw_input("Who would you like to check for in this class? \n")

	rosterCorrect = False 

	for line in file('roster.txt', 'r'):
		line = line.rstrip('\n')
		if inputName == line:
			rosterCorrect = True
	if rosterCorrect:
		print inputName, "is in the class."
	else:
		print inputName, "is not in the class."
