# Linked Lists
*By Zach Newby*

[Practice File](https://github.com/Zachary-P-Newby/Python/blob/Programming-With-Data-Structures-Fall-2023/data_structure_tutorials/linked_lists.py)

## Introduction
The linked list is an alternative version of the traditional list (dynamic array) where instead of putting each item in a single container object, you store each item in a **node** with *links* (*pointers* or *references*) to the other objects in the linked list. Unlike normal lists where each item is stored next to eachother in memory, **linked lists store their contents randomly in memory.** This is because of the links in each node that hold the list together-.

A good way to visulaize a linked list is a train, each car is linked to the car before it and after it, with an engine at the front and a caboose at the back.

There are two main varieties of linked list: **Single Linked** and **Double Linked**.
To make a single linked list you give each node a link to the *head* (the first node in the list - engine), and the *next* node in the list. To make a double linked list you start with a single linked list and to each node you add a link to the node before it (*prev*) and the *tail* (the last node in the list - caboose). The main reason you make a double linked list over a single linked list is so you can move through the linked list in **both** directions. Because you only include links to the head, tail, next, and previous nodes, the linked list is *ordered.*  For the rest of the tutorials we ill be focusing on the double linked list because it is an expanded version of the single linked list.

You are probably wondering what to do when there is not preceeding or following node in the list, well instead of putting a link you just put the *None* value (or the equivalent of the language you using like *null*)

## The Purpose of the Linked List and Why it Matters
**The primary reason you use a linked list over a regular list is so you can you can take advantage of storing objects randomly in memory and better preformance.** By storing objects randomly in memory you can prevent memory overflows that you would otherwise have in the regular list. You can put nodes anywhere they fit and don't have to worry about losing them because they are linked to the rest of the list. The last data structure in this tutorial series, **The Tree** uses nodes and links in a similar manner to the linked list, so learning about the linked list can help you understand trees. Linked Lists are also a good way to implement stacks and queues, as they have better preformance than the regular list (dynamic array) when preforming operations such as inserting at or a removing an item from the front of the list. Before we can get to that however, we should go over how a linked list actually works in Python.

## How to use a Linked List in Python
While python has a built in linked list object called the *deque*, making your own version is quite simple. Here's is how to make a simple double linked list and use it Python:

### Define the class
Create an **Node** class with the following attributes
    * *value* - whatever value you wish to store
    * *head* - pointer
    * *tail* - pointer
    * *next* - pointer
    * *prev* - pointer
    This can be a stand alone object, or a child class of a Linked_list class.
    
    ```
    {
        class Node(value, head = self, tail = self, next = None, prev =  None):
            self.value = value
            self.head = head
            self.tail = tail
            self.next = next
            self.prev = prev
    }
    ```
### Create the head node
Create a node to act as the head by entering argument for value, and the default values will take care of the rest.

```
 {
    #Create head - you can define default values will take care of the rest 
    head_node = Node("Howdy")  
 }
 ``` 

### Add a node (append to the tail)
Then for each new node you create and add to the end of the linked list, assign *prev* to the previous node you created, assign its *next* value to the new node, and reassign the *tail* in all the previous nodes to the new tail.

 ```
 {
    #Create head - you can define default values will take care of the rest 
    head_node = Node("Howdy")

    
 }
 ``` 
 3. 

## Linked List Preformance
Due to how adding and removing items from a linked list works compared to a regular list (dynamic array) the linked list has better preformance