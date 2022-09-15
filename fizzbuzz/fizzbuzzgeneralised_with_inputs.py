
# Outputs the numbers 1-100, saying Fizz for multiples of 3, Buzz for multiples of 5
# and FizzBuzz for multiples of both
# updated to include any divisor waned

# prompt for max number to run to

last_number = (int(input("Run until which number? ")) + 1)

divisor = []
divisor_label = []
print("Please enter divisors when prompted, and then labels for those divisors when prompted")
print("For example, divisor of 3, followed by label of Fizz")
print("Once you have entered all divisors and labels, type run")

# prompt for divisors

while 1 > 0:
	value = input("Enter divisor or type run: ")
	if(value == "run"):
		break
	divisor.append(int(value))
	label = input("Enter label: ")
	divisor_label.append(label)

# fizzbuzz

for n in range(1, last_number):
	output = ""
	for i in range(len(divisor)):
		if(n % divisor[i] == 0):
			output = output + divisor_label[i]
	if(output == ""):
		output = n
	print(output)
	n = n + 1

