#Variables
commit = "Commitment"
favourite = input("What is your favourite letter? ")
print("")
#printing
for letter in commit:
    if letter == favourite.lower() or letter == favourite.upper():
        print("_", end ="")
    else:
        print(letter.lower(), end ="")


#Stretch Challanges
quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."
print("")

running = True

while running:
    number = int(input("Please enter a number: "))

    for i, letter in enumerate(quote):
        if i % number == 0:
            print(quote[i].upper(), end ="")
        else:
            print(quote[i].lower(), end ="")
    choice = input("\nWould you like to enter another number? (yes/no)").lower()

    if choice == "yes":
        continue
    else:
        print("Goodbye.")
        running = False