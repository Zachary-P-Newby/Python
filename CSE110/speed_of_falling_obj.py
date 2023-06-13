import math

#Input information here
print("Welcome to the velocity calculator. Please enter the following:")
m = float(input("Mass (in Kilograms): "))
g = float(input("Gravity\n(9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area of projectile (in square meters): "))
C = float(input("The drag constant (0.5 for sphere, 1.1 for cylinder): "))

#Inner value of c
c = (0.5 * p * A * C)
#Begin Calculations
velocity_at_t = (math.sqrt((m * g)/ c)) * (1 - math.exp( (-1 * math.sqrt(m * g * c)/m) * t) )

#Print Output
print(f"The inner value of c is {c:.3f}")
print(f"The velocity of the object after {t:.2f} seconds is {velocity_at_t:.3f}")
