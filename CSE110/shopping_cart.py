#base variables
cart = []
item_count = 0
running = True
removing = False
#
#UI/Input
print("Welcome to Zach Co. Online Shopping Cart!")
while running:
    
    action = input("""
Please select one of the following:
1. Add Item
2. View Cart
3. Remove Item
4. Compute Total
5. Quit
Please enter an action: """)

#Add Item
#I've decided to make the item and price a pair in a list, allowing me to have only one list for the cart.
#I may change the items to tuples
    if action == "1":
        print("")
        new_item = []
        item_name = input("What item would you like to add? ").lower()
        item_price = float(input(f"What is the price of {item_name}? "))
        new_item = [item_name, item_price]
        cart.append(new_item)
        item_count += 1

#View Cart
    elif action == "2":
        print("")
        item_count = 0
        print("The Contents of the shopping cart are:")
        for item in cart:
            item_count += 1
            print(f"{item_count}. {item[0].capitalize()} - ${item[1]}")
        input("\nContinue?\n")

#Remove Item
    elif action == "3":
        print("")
        removing = True
        while removing:
            item_index = int(input("What item would you like to remove? (Enter Index number) "))
            item_index -=1
            if item_index not in range(0,len(cart)):
                print("That is an invalid entry, enter a valid index.")
                continue
            else:
                cart.pop(item_index)
                removing = False

#Compute Total
    elif action == "4":
        total = 0
        for item in cart:
            total = total + item[1]
        
        print(f"\nYour total is: {total}\n")
            
#Quit
    elif action =="5":
        print("")
        print("Goodbye.")
        running = False    
    
    else:
        print("\nEnter a valid number.\n")