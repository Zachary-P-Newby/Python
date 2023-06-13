#input
first_age = int(input("What is the age of the first rider? "))
first_height = int(input("What is the height of the first rider? "))
first_pass = (input("Do you have a golden passport? (yes/no) "))
second_rider = input("Is there a second rider? (yes/no) ")

if second_rider.lower() == 'yes':
    is_second = True
    second_age = int(input("What is the age of the second rider? "))
    second_height = int(input("What is the height of the second rider? "))
    second_pass = input("Do you have a golden passport? (yes/no) ")
else:
    is_second = False
    second_pass = "no"

print("")

#passport
if first_pass.lower() == "yes" and first_age in range(12, 18):
    first_age = 18
else:
    pass

if second_pass.lower() == "yes" and second_age in range(12, 18):
    second_age = 18
else:
    pass

#decision
if is_second:
    if first_height < 36 or second_height < 36:
        print("Sorry, you may not ride.")
    else:
        if first_age >= 18 or second_age >= 18:
            print("Welcome to the ride. Please be safe and have fun!")
        else:
            if first_age >= 12 and second_age >=12:
                if first_height >= 52 and second_height >=52:
                    print("Welcome to the ride. Please be safe and have fun!")
                else:
                    print("Sorry, you may not ride.")
else:
    if first_age >= 18 and first_height >= 62:
        print("Welcome to the ride. Please be safe and have fun!")
    else:
        print("Sorry, you may not ride.")