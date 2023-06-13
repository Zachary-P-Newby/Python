print("Please rate each the following statistics on a scale of 1 to 10:\n")
#input
size = int(input("How Large is the Loan?: "))
credit = int(input("How good is your credit history?: "))
income = int(input("How high is your income?: "))
down_payment = int(input("How large is your down payment?: "))
#Decision Making
if size >= 5:
    if credit >= 7 and income >= 7:
        decision = True
    elif credit >= 7 or income >=7:
        if down_payment >= 5:
            decision = True
        else:
            decision = False
    else:
        decision = False
else:
    if credit < 4:
        decision = False
    else:
        if income >= 7 or down_payment >= 7:
            decision = True
        elif income >= 4 and down_payment >= 4:
            decision = True
        else:
            decision = False
#Print Result
if decision:
    result = "yes"
else:
    result = "no"
print("")
print(f"Loan size: {size}, Credit: {credit}, Income: {income}, Down Payment: {down_payment}.\n Our Decision: {result}.")