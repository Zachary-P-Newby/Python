# Linked Lists
*By Zach Newby*

[Practice File](https://github.com/Zachary-P-Newby/Python/blob/Programming-With-Data-Structures-Fall-2023/data_structure_tutorials/linked_lists.py)

## Introduction
The linked list is an alternative version of the traditional *list* (dynamic array) where instead of putting each item in a single container object, you store each item in a **node** with *links* (*pointers* or *references*) to the other objects in the linked list. Unlike normal lists where each item is stored next to each other in memory (contiguous storage), **linked lists store their contents randomly in memory.** This is because of the links in each node that hold the list together, they provide a clear path to each value in the list. Generally, you will want to create a linked list parent class and save the node as a child class of it. This makes accessing the linked list as much easier as the parent class acts as an interface and place to store functions that will allow you to travel through the list since you cannot loop through a linked list as you could with a regular list in Python. (More on that later.)

A good way to visualize a linked list is a train, each car is linked to the car before it and after it, with an engine at the front and a caboose at the back.

There are two main varieties of linked lists: **Single Linked** and **Double Linked**.
To make a single linked list you give each node a link to the *head* (the first node in the list - engine), and the *next* node in the list. To make a double linked list you start with a single linked list and to each node you add a link to the node before it (*prev*) and the *tail* (the last node in the list - caboose). The main reason you make a double-linked list over a single-linked list is so you can move through the linked list in **both** directions. Because you only include links to the head, tail, next, and previous nodes, the linked list is *ordered.*  For the rest of the tutorials we will be focusing on the double-linked list, and when the head, tail, prev, and next appear in italics, it refers to the attributes in a linked list of those names.

You are probably wondering what to do when there is no preceding or proceeding node in the list, well instead of putting a link you just put the *None* value (or the equivalent of the language you using like *null*)

## The Purpose of the Linked List and Why it Matters
**The primary reason you use a linked list over a regular list is so you can take advantage of storing objects randomly in memory and better performance.** By storing objects randomly in memory you can prevent memory overflows that you would otherwise have in the regular list. You can put nodes anywhere they fit and don't have to worry about losing them because they are linked to the rest of the list. The last data structure in this tutorial series, **The Tree** similarly uses nodes and links to the linked list, so learning about the linked list can help you understand trees. Linked Lists are also a good way to implement stacks and queues, as they have better performance than the regular list (dynamic array) when performing operations such as inserting or removing an item from the front of the list. Before we can get to that, however, we should go over how a linked list works in Python.

## How to use a Linked List in Python
While Python has a built-in linked list object called the *deque*, making your own version is quite simple. Here is a brief overview of how to make and use a custom linked list class. The practice file contains a customer-linked list based on these instructions for you to experiment with.

**How to Make a Linked List class:**

 1. Define the class:
Define the class using the *class* keyword, and define the *head* and *tail* values. These can be defined in or out of the init function since we will not be creating any nodes upon instantiation
```
class LinkedList:
   """Docstring"""

   head = None
   tail = None

   def __init__():
      pass

```

 2. Create the Node class:
Create the Node class either as a child class of the *LinkedList* class or as a standalone class.

```
class Node:
        """Simple Node"""
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None
```

 3. Create the insert method:
To add Nodes to the *LinkedList* class we will need to create a method (function of the class). To function properly the method will need code to handle if the new node is the first one in the list and code to handle if the list already contains nodes. The practice file contains four insert functions, but here I will just so insert_tail, which is equivalent to the .append method.

```
#This should be inside the linked list class

def insert_tail(self, value):
        """ Inserts a node at the tail of the list """
        new_node = LinkedList.Node(value)
        
        #If this is the first node created, make it both the head and tail
        of self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            #Otherwise set the existing tail to come after the new node and make the new node the tail. 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
```

Note the `new_node = LinkedList.Node(value)`. Because in our example the *Node* class is a child of the *LinkedList* class, we have to include the `LinkedList.` before the node to remind Python where the *Node* class is defined.

 4. Create the remove method.
We will also want at least one method to remove nodes from the linked list, especially if you are making a stack or queue. Here's a method that removes the first node containing a target value.

```
def remove_value(self, target_value):
        """ Removes the first node with the target, if no node has the target value, stop the operation """

        curr = self.head
        target_node = None

        while curr != None :
            if curr.value != target_value:
                curr = curr.next
            else:
                #if the target_value is not found
                target_node = curr
                break
        else:
            target_node = curr

        if target_node == None:
            print("NO NODE WITH THAT VALUE FOUND")
        else:
            #Remove node
            target_node.next.prev = target_node.prev
            target_node.prev.next = target_node.next
            del(target_node)
```

**Using a linked list class**

* Inserting a node:
To insert a node you will have to change the *next* and *prev* values of the nodes that come before and after it. (If any)

```
#Insert potato between carrot and yam

potato_node = LinkedList.Node("Potato")
potato_node.next = yam_node
potato_node.prev = carrot_node

carrot_node.next = potato_node
yam_node.prev = potato_node
```
If you do not know the names of the nodes affected by the insertion, you will have to get a bit clever to properly insert the new node. Luckily, because the attributes of a node are pointers to other nodes, we can access the *next* and *prev* values of those nodes. here's code from the insert_after function that inserts a new node after the first node it finds containing a specific value: 

```
#I cut out the part that selects the node.

#set new_node prev and next
new_node.prev = target_node
new_node.next = target_node.next

#set the prev of the node after the target to be new_node
target_node.next.prev = new_node

#set new node to come after target
target_node.next = new_node    
```

* Removing a node:
Removing a node requires assigning the nodes that come before and after to point to each other. This is done by changing their *next* and *prev* values. Remember this block of code from the remove_value function above?
```
#Remove node
target_node.next.prev = target_node.prev
target_node.prev.next = target_node.next
del(target_node)
```

Remember if there is no node before or after a node you add or remove, (the head and tail nodes), assign *None* or another placeholder value to the *next* or *prev* attributes.

## Linked List Performance
Appending to or removing from the end of a dynamic array (list) and a linked list or both **O(1)** operations in terms of big O performance notation, as you only add or remove one item. However, because removing from or inserting into the front or middle of a dynamic array requires you to shift all the items following the affected item (inserted or removed) in order to back or forward one index, this operation becomes **O(n)** with n being the number of shifted items + the affected item. The larger the list and earlier the affected value is in it, the more values you will have to move. For large *queues* (first in, first out) this can lead to quite a lot of operations and performance costs. Linked lists however only require you to change the nodes before and after the one you insert or remove regardless of where it is. (Reassigning *prev*, *next*, and sometimes *head* or *tail*.) This comes out to two or three **O(1)** operations which equal **O(1)** due to how big O notation works.

TL;DR Linked Lists are much more efficient than dynamic arrays when performing operations at the head or middle of a list, especially with large amounts of data. This makes them ideal for large queues and stacks.

## Common Pitfalls and Mistakes to Avoid
Here are three of the common mistakes you can make when working with linked lists

 * **Trying to loop through a linked list with a for loop.** - Because nodes in a linked list are not stored next to each other in memory and are linked by reference, a *for* loop will not work. A *while* loop that moves through each node until there are none left works instead. If you store the nodes as children of a parent-linked list class you can save this as a method. Here's an example:
 ```
 current_node = self.head #Set starting node

 while current_node != None:
    < perform operation>
    current_node = current_node.next
 
 #When current_node is the tail, the next attribute will be none, so when we assign current_node to next, which is None, it breaks the loop 
 ```
 This is the code that makes the removal met

 * **Assigning the wrong** *next* **and** *prev* **nodes** - Always be sure you put the right *next* and *prev* pointers so you don't accidentally create a linked list that splits into. It would be like trying to connect two train cars to the engine at the same time.

 * **Forgetting to change** *next* **and** *prev* **Values into the nodes you insert or remove between** - If you do you will have what could be called a "phantom node". It points to the rest of the linked list, but the linked list does not point to it, so if you loop through the linked list it will be ignored.


## Now you try:
Now it's your turn! Download the [Practice File](https://github.com/Zachary-P-Newby/Python/blob/Programming-With-Data-Structures-Fall-2023/data_structure_tutorials/linked_lists.py) and see what you can do. See how many challanges you can complete.

Challenges:
 * Create and lopp through a linked list using the linked list class provided
 * Modify __init__ function so you can create nodes when first instanciating
 * Create *remove_head* and *remove_tail* functions for the linked list class provided