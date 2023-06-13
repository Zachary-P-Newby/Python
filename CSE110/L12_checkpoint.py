people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest_age = 100
youngest_person = ""

for person in people:
    
    person = person.split()
    person[1] = int(person[1])

    if person[1] <= youngest_age:
        youngest_age = person[1]
        youngest_person = person[0]
    else:
        pass

print(f"The youngest_person is {youngest_person} at {youngest_age} years old.")