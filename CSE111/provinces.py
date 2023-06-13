#Create province list
province_list = []
#Open file C:\\Users\\zpnew\\OneDrive\\byu-idaho\\CSE111\\provinces.txt
with open("C:\\Users\\zpnew\\OneDrive\\byu-idaho\\CSE111\\provinces.txt", mode = "rt") as province_file:
    for line in province_file:
        province_list.append(line.strip())


#print provinces
print(province_list)


#modify list
province_list.pop(0)
province_list.pop(-1)

for index in range(len(province_list)):
    if province_list[index] == "AB":
        province_list[index] = "Alberta"

print("")

#count Albertas
a_count = 0

for line in province_list:
    if line == "Alberta":
        a_count += 1

print(province_list)
print(a_count)