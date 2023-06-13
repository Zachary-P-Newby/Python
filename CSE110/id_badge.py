if __name__ == '__main__':
#input
    print("Please enter the following information:")
    first = input("First name: ")
    last = input("Last name: ")
    email = input("Email address: ")
    title = input("Job title: ")
    phone = input("Phone number:")
    id_number = input("ID Number: ")
    
#fix casing
    last = last.upper()
    title = title.title()
    email = email.lower()
#print time
    print("\n")
    print("The ID Card is:")
    print("--"*20)
    print(f"{last}, {first}")
    print(title)
    print(f"ID: {id_number}\n")
    
    print(email)
    print(phone)
    print("--"*20)