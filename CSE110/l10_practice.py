running = True

cart = []
while running:
    
    item = input("Please enter the items you wish to purchase. ('quit' to finish) ")
    
    if item.lower() == 'quit':
        running = False
    else:
        cart.append(item)

print("\n The shopping list is:")
for i in range(len(cart)):
    print(f"{i + 1}. {cart[i]}")

new_index = int(input("What item would you like to change? (Enter the index) ")) -1
new_item = input("What is the new item? ")

cart[new_index] = new_item

print("\n The altered shopping list is:")
for i in range(len(cart)):
    print(f"{i + 1}. {cart[i]}")