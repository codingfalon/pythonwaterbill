#a code that calculates various bills based on a preset formula

customerCode = raw_input("r or c or i   ") #must pick if residental or commercial 

while customerCode == "r":
	customerInitial = float(input ("Initial water meter reading in gallons "))
	customerEnding = float(input ("Final water meter reading in gallons "))
	customerGallons = (customerEnding - customerInitial) 
	customerBill = 5.00 + .0005*customerGallons

	print "Customer code: %s" %customerCode 
	print "Initial water meter reading: %s" %customerInitial
	print "Final water meter reading: %s" %customerEnding
	print "Gallons of water used: %s" %customerGallons 
	print "Customer Bill: %s" %customerBill
	customerCode = raw_input("r or c or i") 

while customerCode == "c": 
	customerInitial = float(raw_input ("Initial water meter reading in gallons "))
	customerEnding = float(raw_input ("Final water meter reading in gallons "))
	customerGallons = customerEnding - customerInitial 

	if customerGallons <= 4000000:
		customerBill = 1000.00 
	elif customerGallons > 4000000:
		customerBill = 1000.00 + .00025*customerGallons

	print "Customer code: %s" %customerCode 
	print "Initial water meter reading: %s" %customerInitial
	print "Final water meter reading: %s" %customerEnding
	print "Gallons of water used: %s" %customerGallons 
	print "Customer Bill: %s" %customerBill
	customerCode = raw_input("r or c or i")  

while customer == "i": 
	customerInitial = float(raw_input ("Initial water meter reading in gallons "))
	customerEnding = float(raw_input ("Final water meter reading in gallons "))
	customerGallons = customerEnding - customerInitial

	if customerGallons <= 4000000:
		customerBill = 1000.00
	elif customerGallons > 4000000 and customerGallons<=10000000:
		customerBill = 2000.00
	elif customerGallons > 10000000:
		customerBill = 2000.00 + .00025*customerGallons

	print "Customer code: %s" %customerCode 
	print "Initial water meter reading: %s" %customerInitial
	print "Final water meter reading: %s" %customerEnding
	print "Gallons of water used: %s" %customerGallons 
	print "Customer Bill: %s" %customerBill
	customerCode = raw_input("r or c or i")  