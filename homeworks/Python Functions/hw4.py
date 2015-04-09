def sumNums():
	sumOfNums = 0
	for num in intArray:
		sumOfNums = sumOfNums + num
	print "Sum of array values:", sumOfNums

def squareNums():
	for i in range(len(intArray)):
		intArray[i] = intArray[i]*intArray[i]
	print "Squared array:", intArray

intArray = [23, 84, 3, -3, 45, 22, 99, 3589, -34, 0, 4, -63]
print "Array:", intArray
sumNums()
squareNums()