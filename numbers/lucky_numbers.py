# Write ther first n Lucky numbers
# 1) list all integers until limit
# 2) remove all second numbers
# 3) read second number (n) and remove every nth number
# 4) repeat


CalculateUntil = int(input("Calulate Lucky numbers up until: "))

LuckyNumbers = [1]

i = 2
while i <= CalculateUntil:
	LuckyNumbers.append(i)
	i += 1



print(LuckyNumbers)
