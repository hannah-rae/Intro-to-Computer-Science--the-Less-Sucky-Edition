def isPalindrome(wurd):
	wurd = wurd.lower()
	spaceless = ""
	for char in wurd:
		if char != ' ':
			spaceless += char

	reversedWord = ""
	for i in range(len(spaceless)-1, -1, -1):
		reversedWord += spaceless[i]
	if reversedWord == spaceless:
		return True
	else:
		return False

while(True):
	word = raw_input("Enter a word.\n")
	if isPalindrome(word):
		print word, 'is a palindrome.\n'
	else:
		print word, 'is not a palindrome.\n'