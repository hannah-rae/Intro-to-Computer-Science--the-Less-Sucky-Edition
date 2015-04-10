import sys

while(True):
	userTeam = raw_input("What is your favorite basketball team?\n")
	if userTeam == "Carolina":
		print "Excellent choice! Goodbye"
		sys.exit()
	elif userTeam == "Duke":
		print "Duke sucks and so do you!\n"
	else:
		print "No it's not. Try again.\n"