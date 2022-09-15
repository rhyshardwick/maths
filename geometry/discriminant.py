# Calculates the discriminant value
# discriminant: the expression that appears under teh square root (radidical) sign in
# the quadratic equation
# b ** 2 - 4ac

# w3resource exercise uses x, y, z, I will use the more standard a, b, c
print("Calculate the discriminant for the quadratic equation axx + bx + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print("Discriminant:", b ** 2 - 4 * a * c)


