print("Calculates the smallest multiple of the first n numbers and displays the factors of that number")
print("THIS DOES NOT WORK")
# NOT WORKING - I really can't quite understand what the 'smallest mutiple' is

num = int(input("Input number: "))

# set multiple as num
# reduce num by 1
# see if divisible by num
# if divisble - stop
# if not divisible,  multiple by num
# repeat

num2 = num

multiple = num
factors = [num]
while num >= 2:
	num = num - 1
	if(multiple % num > 0):
		multiple = num * multiple
		factors.append(num)

print(multiple)
print(factors)
