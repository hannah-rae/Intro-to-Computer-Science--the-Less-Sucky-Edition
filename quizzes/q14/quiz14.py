# Your name:
# Your partner's name(s):

def pickWinningNumbers(n):
	winningNums = []
	# Want to generate n random, unique numbers
	for i in range(1, n):
		# Generate one random integer
		aNum = random.randint(0, 52)
		# If that number is already in the list, 
		# generate a new number until we find one
		# that is not in the list already
		while (aNum in winningNums)
			aNum = random.randint(0, 52)
		# Now that we have a number unique to the list, add it
		winningNums.append(aNum)
		return winningNums

numRequested = raw_input("How many winning numbers do you need? ")
print pickWinningNumbers(numRequested)

## Describe your corrections in this section ##