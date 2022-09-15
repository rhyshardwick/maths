# Calculate area of a segment given angle and radius
import math

angle = float(input("Angle: "))
radius = float(input("Radius: "))

print("Area of segment:", math.pi * radius * radius * angle / 360)

