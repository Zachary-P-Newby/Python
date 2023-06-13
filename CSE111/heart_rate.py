print("""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
""")

#obtain user input
age = int(input("How old are you? "))
#Calculations
max_rate = 220 - age

slowest = max_rate  * .65

fastest = max_rate * .85

#Display info
print()

print(f"Your maximum heart rate is {max_rate} beats per minute.\n")
print(f"To strengthen your heart you should try to keep it in a range of\n{slowest} (65%) to {fastest} (85%) beats per minute.")