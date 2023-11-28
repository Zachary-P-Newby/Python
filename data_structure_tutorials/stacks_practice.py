""" Practice file for stacks.md stack tutorial """

#Here's an example of a stack for you to play around with. Remember to only use lists and append or pop from the end of the list!

print("")

stack = []

stack.append("Went to the store")
stack.append("Bought milk")
stack.append("Came home")
stack.append("Ate cookies")
stack.append("Jumped on my bed")

for i in stack:
    print(i)

print("")

stack.pop()
stack.pop()

for i in stack:
    print(i)