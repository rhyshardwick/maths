print("Calculates the sum of amicables up to n")
n = int(input("Enter n: "))

# Flowchart
# calculate the sum of the proper divisors
# test to see if the sum fo the proper divisors of the result is the same
# test to ensure the numbers are not the same
# if not, add to list
# sum list and print sum

def sum_of_divisors(n):
	i = 2
	divisors = [1]
	while i < n:
		if(n % i == 0):
			divisors.append(i)
		i += 1
	return sum(divisors)

# Generate list of sum of proper divisors
print("Amicable Numbers:")
list = []
j = 2
while j <= n:
	a = sum_of_divisors(j)
	b = sum_of_divisors(a)
	if(b == j):
		if(j != a):
			if j not in list:
				print(j, a)
				list.append(j)
				list.append(a)
	j += 1

#print(list)
print("Sum of amicable numbers:",int(sum(list)))
