# outputs the numbers 1-100, saying Fizz for multiples of 3, Buzz for multiples of 5
# and FizzBuzz for multiples of both
# updated to include any divisor waned

# tuples of divisors and corresponding labels
divisor = (3, 5, 7, 11)
divisor_label = ("Fizz", "Buzz", "Fuzz", "Bizz")

# how long to run for
last_number = 100

for n in range(1, last_number):
	output = ""
	for i in range(len(divisor)):
		if(n % divisor[i] == 0):
			output = output + divisor_label[i]
	if(output == ""):
		output = n
	print(output)
	n = n + 1
