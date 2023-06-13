#Input
f_temp = float(input("Plese enter a temprature in farenheit: "))

#Calc
sub_temp = f_temp - 32.0
c_temp = sub_temp * (5/9)

print(f"The temprature in Celsius is: {c_temp:.1f} degrees.")