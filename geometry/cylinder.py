# Calculates and returns volume and surface area of a cylinder

import math

height = float(input("Height: "))
radius = float(input("Radius: "))

area_circle = math.pi * radius * radius
volume = area_circle * height
surface_area = (2 * area_circle) + (height * 2 * math.pi * radius)
print(" ")
print("Results")
print("-------")
print("Volume:", volume)
print("Surface Area:", surface_area)
