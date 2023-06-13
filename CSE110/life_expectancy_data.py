#Predefine Lists
data = []
total = 0

#Compile Data
with open("life-expectancy.csv") as raw_data: 
    for line in raw_data:
        line = line.strip()
        line = line.split(",")
        data.append(line)
    
    #Remove variable key in data
    data.pop(0)
    
    print("\nCompilation Complete\n")

#Ask for a year
desired_year = input("Enter a year to find the average life expectancy (NO to skip) ")

if desired_year not in ["NO","No","no","nO"]:
    desired_year = int(desired_year)
    year_count = 0
    highest_desired = 0
    lowest_desired = 9999
    highest_country_desired = ""
    lowest_country_desired = ""

    for line in data:
        if int(line[2]) == desired_year:
            
            total += float(line[3])
            year_count += 1
            
            if float(line[3]) >= highest_desired:
                highest_desired = float(line[3])
                highest_country_desired = line[0]
            elif float(line[3]) <= lowest_desired:
                lowest_desired = float(line[3])
                lowest_country_desired = line[0]
            else:
                pass

        else:
            pass
    average_expectancy = total / year_count

#Lowest and highest
overall_lowest = 9999
overall_lowest_entry = ""

for line in data:
    if float(line[3]) <= overall_lowest:
        overall_lowest = float(line[3])
        overall_lowest_entry = line

overall_highest = 0
overall_highest_entry = ""

for line in data:
    if float(line[3]) >= overall_highest:
        overall_highest = float(line[3])
        overall_highest_entry = line


#Return Information
print("--"*10)
if type(desired_year) != type("str"):
    print(f"For the year {desired_year}:")
    print(f"The average life expectancy for {desired_year} was {average_expectancy:.3f} years.")
    print("")
    print(f"The lowest life expectancy for {desired_year} was: {lowest_desired} years in {lowest_country_desired}.")
    print("")
    print(f"The highest life expectancy for {desired_year} was: {highest_desired} years in {highest_country_desired}.")
    print("")
else:
    pass
print(f"The overall lowest life expectancy was: {overall_lowest} years in {overall_lowest_entry[0]}, during {overall_lowest_entry[2]}.")
print("")
print(f"The overall highest life expectancy was: {overall_highest} years in {overall_highest_entry[0]}, during {overall_highest_entry[2]}.")
print("--"*10)
print("")