print("Return whether a number is abundant or not")
# abundant is if sum of proper divisors is greater than the number itself.

num = int(input("Enter Number: "))

i = 2
divisors = [1]
while i < num:
	if(num % i == 0):
		divisors.append(i)
	i += 1
print("Proper Divisors:", divisors)
print("Sum of divisors:",sum(divisors))
if(sum(divisors) > num):
	print(num, "is abundant")
else:
	print(num, "is not abundant")
