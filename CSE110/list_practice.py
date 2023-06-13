friends = []

new_friend = ""
while new_friend != "end":
    new_friend = input("PLease type the name of a friend: ")
    if new_friend != 'end':
        friends.append(new_friend)
    else:
        pass

print("\nYour friends are: ")
for item in friends:
    print(item)