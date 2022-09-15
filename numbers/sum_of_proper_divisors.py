print("Calculates the sum of all proper divisors up to n")
n = int(input("Enter n: "))

# Flowchart
# calculate the sum of the proper factors of all the numbers up to n
# add the values to a list
# compare the sum of the proper factors to eachother
# add the amicable numbers to a running total
# print the total

def sum_of_divisors(n):
	i = 2
	divisors = [1]
	while i < n:
		if(n % i == 0):
			divisors.append(i)
		i += 1
	return sum(divisors)

# Generate list of sum of proper divisors

list = [1]
j = 2
while j <= n:
	list.append(sum_of_divisors(j))
	j += 1

print(list)

