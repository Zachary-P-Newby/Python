#Ask for nums
num1 = int(input("What is the first number?"))
num2 = int(input("What is the second number?"))
#Compare and print
if num1 > num2:
    print("The first number is greater.")
else:
    print("The first number is not greater.")

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

if num1 < num2:
    print("The second number is greater.")
else:
    print("The second number is not greater")

print("")
#Animal time!
animal = input("What is your favourite animal?" )

if animal.lower() == "fox":
    print("That is my favourite animal too.")
else:
    print("That is not my favourite.")