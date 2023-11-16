# 
data = [10, 20, 30, 40, 50]
#middle = (((last - first) /2) + first)
#middle = int(-((last- first)//-2)) 
#middle = (last - first)//2

def ceildiv(a, b):
    return -(a // -b)

first = 0
last = 9

middle = (-((last - first) // -2) + first)

print(f"middle index: {middle}")

""" first = 3
last = 5

middle = (-((last - first) // -2) + first)

print(f"middle index: {middle}")

first = 0
last = 3

middle = (-((last - first) // -2) + first)

print(f"middle index: {middle}") """