#Import infor
from math import pi

#Get data
print("Please enter tire data:")
print("-"*20)
print("")
width = float(input("Please enter the width of the tire in millimeters (ex 205): "))
ratio = float(input("Please enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Please enter the diameter of the tire in inches (ex 15): "))
print("")

#Begin Calculations
volume = pi * (width**2) * (ratio * (width * ratio + 2540 * diameter))
volume = volume / 10000000000

#give output
print(f"The volume of the tire is {volume:.2f} liters.")