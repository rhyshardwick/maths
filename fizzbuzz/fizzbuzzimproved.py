# outputs the numbers 1-100, saying Fizz for multiples of 3, Buzz for multiples of 5
# and FizzBuzz for multiples of both

test_1_num = 3
test_1_str = "Fizz"
test_2_num = 5
test_2_str = "Buzz"

run_until = 100
n = 1
while n <= run_until:
	output = ""
	if(n % test_1_num == 0):
		output = output + test_1_str
	if(n % test_2_num == 0):
		output = output + test_2_str
	if(output == ""):
		output = n
	print(output)
	n = n + 1

