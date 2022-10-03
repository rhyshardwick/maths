# Write ther first n Lucky numbers
# 1) list all integers until limit
# 2) remove all second numbers
# 3) read second number (n) and remove every nth number
# 4) repeat


n = int(input("Calulate Lucky numbers up until: "))

# Generate a list of integers

luckyNumbers = range(-1, n*n+9, 2) # creates a list of odd numbers from 1 to n squared + 9

i = 2 # start with third term	
while luckyNumbers[i:]: # cycle through from nth term to end
	luckyNumbers = sorted(set(luckyNumbers) - set(luckyNumbers[luckyNumbers[i]::luckyNumbers[i]]))
	i += 1

# Print out numbers
a = 1
while a <= n:
	print(a, ":", luckyNumbers[a])
	a += 1
