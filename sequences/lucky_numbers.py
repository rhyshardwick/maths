# Write ther first n Lucky numbers
# 1) list all integers until limit
# 2) remove all second numbers
# 3) read second number (n) and remove every nth number
# 4) repeat


CalculateUntil = int(input("Calulate Lucky numbers up until: "))
# Factor to calculate until to ensure we have enough terms after removal
lengthFactor = 3
# Generate a list of integers three times size of CalculateUntil

LuckyNumbers = [1]
i = 2
while i <= (CalculateUntil * lengthFactor):
	LuckyNumbers.append(i)
	i += 1

nthterm = 2
i = 1
while nthterm < (CalculateUntil * lengthFactor):
	



# Print out numbers

n = 0
while n < CalculateUntil:
	print(n + 1, ":", LuckyNumbers[n])
	n += 1
