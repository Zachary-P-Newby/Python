num = int(input("Please enter a positive number: "))

while num < 0: 
    num = int(input("Please enter a positive number: "))
print(f"The number is: {num}")

cookie = False

while cookie == False:
    ask = input("May I have a cookie? (yes/no)").lower()
    if ask == 'yes':
        cookie = True
    else:
        continue

print("Yay! Thank you.")