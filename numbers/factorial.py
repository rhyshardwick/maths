print("Calculates the factorial")

num = int(input("Input number: "))

if num < 1:
	print("Please enter a positive integer")
elif num == 1:
	factorial = 1
else:
	factorial = 1
	i = 1
	while i < num + 1:
		factorial = factorial * i
		i += 1

print("Factorial:", factorial)




