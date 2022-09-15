nterms = int(input("How many terms? "))

n1 = 0
n2 = 1

if nterms <=0:
	print("Works only for positive integers")
elif nterms == 1:
	print(n1)
else:
	count = 0
	while count < nterms:
		print(n1)
		nth = n1 + n2
		n1 = n2
		n2 = nth
		count += 1
