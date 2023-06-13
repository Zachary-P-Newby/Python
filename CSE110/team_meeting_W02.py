import math
#Square
sq_length = int(input("What is the legth of a side of the square in centemeters? "))
sq_area = sq_length**2
print(f"The area of the square in square centemeters is: {sq_area}")
# print(f"The area of the square in square meters is: {sq_area /10000}")
#Rectangle
rect_length = int(input("\nWhat is the length of the rectangle in centemeters? "))
rect_width = int(input("What is the width of the rectangle in centemeters? "))
rect_area = rect_length * rect_width
print(f"The area of the rectangle in square centemeters is: {rect_area}")
# print(f"The area of the rectangle in square meters is: {rect_area /10000}")
#Circle
radius = float(input("\nWhat is the radius of the circle in centemeters? "))
circle_area = (radius ** 2)* math.pi
print(f"The area of the circle in square centemeters is: {circle_area}")
#print(f"The area of the circle in square meters is: {circle_area / 10000}")
#One input, many outputs
length = int(input("\nEnter a value for multiple computations: "))
square = length **2
circle = square * math.pi
cube = length **3
sphere = (4/3)* math.pi* cube#Cube is lenth cubed, or in this case radius cubed = r^3
print(f"""
Results:
Area of Square: {square}
Area of Circle: {circle}
Volume of Cube: {cube}
Volume of Sphere: {sphere}
""")