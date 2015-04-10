def printStars(num):
	for i in range(1, num+1):
		print i*"*"

while True:
	n = int(raw_input("Enter an integer: "))
	printStars(n)
	print