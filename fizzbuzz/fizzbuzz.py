# outputs the numbers 1-100, saying Fizz for multiples of 3, Buzz for multiples of 5
# and FizzBuzz for multiples of both

run_until = 100
n = 1
while n <= run_until:
	if(n % 3 == 0):
		if(n % 5 == 0):
			print("FizzBuzz")
		else:
			print("Fizz")
	elif(n % 5 == 0):
		print("Buzz")
	else:
		print(n)
	n = n + 1

