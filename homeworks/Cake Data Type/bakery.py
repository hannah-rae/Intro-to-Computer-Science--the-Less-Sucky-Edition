from cake import Cake

print "Welcome to Hannah's bakery!"
num_cakes = int(raw_input("How many cakes would you like to order? "))

cake_list = []
for i in range(num_cakes):
	print "Cake", i+1, "Details"
	frosting = raw_input("Frosting flavor: ")
	cakeType = raw_input("Cake flavor: ")
	writing = raw_input("Writing: ")
	cake_list.append(Cake(cakeType, frosting, writing))

print
print "Receipt"
print
total = 0
for i in range(len(cake_list)):
	cake_cost = cake_list[i].getPrice()
	print "Cake", i+1, ": $", cake_cost
	total += cake_cost
print "Total: $", total