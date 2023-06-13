#Import infor
from math import pi
import datetime

#get current date
current_date = datetime.date.today()
#print(current_date)

#Get data
print("Please enter tire data:")
print("-"*20)
print("")
width = float(input("Please enter the width of the tire in millimeters (ex 205): "))
ratio = float(input("Please enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Please enter the diameter of the tire in inches (ex 15): "))
print("")

#Begin Calculations
tire_volume = pi * (width**2) * (ratio * (width * ratio + 2540 * diameter))
tire_volume = tire_volume / 10000000000

#give output
print(f"The volume of the tire is {tire_volume:.2f} liters.")


#open/create new file.
with open("C:\\Users\\zpnew\\OneDrive\\byu-idaho\\CSE111\\volume.txt", "at") as volume_file:
    
    print(f"{current_date}, {width}, {ratio}, {diameter}, {tire_volume:.2f}", file=volume_file)