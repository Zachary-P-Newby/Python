#import modules
import datetime as dt

#Get the date
date = dt.datetime.now()
day = date.weekday()
#day = 4

#tax
tax_rate = 0.06

#Enter subtotal
subtotal = float(input("What is the subtotal? "))

#Calculate TOtal

if day == 2 or day == 3:
    if subtotal >= 50:
        discount = subtotal * 0.1
        total = subtotal * 0.9
    else:
        discount = 0
        total = subtotal
else:
    discount = 0
    total = subtotal

sales_tax = total * tax_rate

total += sales_tax

#Return Result
print("")
print("--"*10)
print("Reciept:")
print(f"""
Subtotal: ${subtotal:.2f}
Discount: ${discount:.2f}
Tax Rate: {tax_rate * 100}%
Total: ${total:.2f}
""")
print("--"*10)