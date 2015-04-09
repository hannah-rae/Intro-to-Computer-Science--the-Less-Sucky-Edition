password = raw_input("Enter your password: ")

lower_count = 0
upper_count = 0
num_count = 0
punc_count = 0

for char in password:
	if char.islower():
		lower_count += 1
	elif char.isupper():
		upper_count += 1
	elif char in ['&', '!', '*', '$']:
		punc_count += 1
	elif int(char) in range(10):
		num_count += 1

if lower_count == len(password):
	print "Your password is weak."
elif lower_count >= 1 and upper_count >= 1 and punc_count >= 1 and num_count >= 1 and len(password) >= 10:
	print "Your password is strong."
else:
	print "Your password is mediocre."