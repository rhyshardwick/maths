print("Calculates the sum of the digits in the number x raised to the power of y")
x = int(input("x: "))
y = int(input("y: "))

print("Total:", sum(int(i) for i in str(x ** y)))
