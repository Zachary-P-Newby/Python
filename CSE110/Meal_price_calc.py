import math

#Asking for prices
child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of a adult's meal? "))
children = int(float(input("How many children are there? ")))
adults = int(float(input("How many adults are there? ")))
tax_rate = float(input("What is the sales tax rate? "))
#Computations
child_total = (child_meal_price * children)
adult_total = (adult_meal_price * adults)
subtotal = child_total + adult_total
sales_tax = (subtotal * (tax_rate * .01))
total = subtotal + sales_tax


#return totals
print(f"\nSubtotal: ${subtotal:.2f}")
print(f"Sales Tax: ${sales_tax:.2f} (at {tax_rate:.1f}% tax rate) ")
print(f"Total: ${total:.2f}")
#payment
print("\nHey Bro.Brown! Try entering in a value less than the needed amount to pay for the meal!")

paying = True
while paying == True:
    payment = float(input("\nWhat is the payment amount? "))

    if payment < total:
        print("This is not enough, please pay for your meal.")
        continue
    else:
        change = (payment - total)
        print(f"Change: ${change:.2f}")
        paying = False