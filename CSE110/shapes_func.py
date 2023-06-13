#square func
def compute_area_square(side):
    return side**2
#rectangle
def compute_area_rectangle(length, width):
    return length * width
#Circle
def compute_area_circle(radius):
    return (radius**2)*3.14

#input
running = True

while running:
    shape = input("What kind of shape do you have? (QUIT to end program) ").lower()
    print("")
    if shape == "square":
        leg = float(input("What is the length of the side of the square? "))
        result = compute_area_square(leg)
        print(f"The area of the square is {result} units squared.\n")
    elif shape == "rectangle":
        i_length = float(input("What is the length of the side of the rectangle? "))
        i_width = float(input("What is the width of the side of the rectangle? "))
        result = compute_area_rectangle(length = i_length, width = i_width)
        print(f"The area of the rectangle is {result} units squared.\n")
    elif shape == "circle":
        radius = float(input("What is the radius of the circle? "))
        result = compute_area_circle(radius)
        print(f"The area of the circle is {result} units squared.\n")
    elif shape == "quit":
        break
    else:
        print("Enter a valid shape\n")
        continue