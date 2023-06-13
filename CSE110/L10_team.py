accounts = []

balances = []

print("Enter the names and balances of bank accounts (Type: quit when done)")
running = True
while running:
    new_account = input("\nWhat is the name of this account? ").lower()
    
    if new_account != 'quit':
        accounts.append(new_account)
        new_balance = float(input("What is the balance? "))
        balances.append(new_balance)

        continue
    else:
        running = False


print("\nAccount Information:")

for i in range(len(accounts)):
    print(f"{i+1}. {accounts[i]} - {balances[i]}")

#print(accounts)
#print(len(accounts))
#print(balances)
#print(len(balances))

total = 0
for i in balances:
    total += i

average = total / len(balances)

print(f"Total: {total}\nAverage: {average}\n")