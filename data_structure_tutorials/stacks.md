# Stacks - or the Stack
*by Zach Newby*

[Practice file](https://github.com/Zachary-P-Newby/Python/blob/Programming-With-Data-Structures-Fall-2023/data_structure_tutorials/stacks_practice.py)

## Intro
The stack is the first data structure we will learn about. The stack is a container for objects where **the last object put in is the first one pulled out.**
(The stack is called a "last-in, first-out" structure) A good way to visualize the stack would be to imagine a stack of books, if you want to remove a book from the stack, you must remove all of the books on top of it first, or else it will fall over. Objects can only be removed from a stack in the opposite order they were out in.

As Jesus said: 
 > "16 So the last shall be first, and the first last: for many be called, but few chosen."
[Matthew 20:16](https://www.churchofjesuschrist.org/study/scriptures/nt/matt/20?lang=eng&id=p16#p16)

If you have ever experienced a stack trace or stack overflow error, then you have encountered the stack. This is the data structure for which [https://stackoverflow.com](https://stackoverflow.com) is named after.

## The purpose of the stack and why it matters
**The primary purpose of the stack is to function like a real stack and force you to add or remove objects from the end (or top) of the stack.** This may not sound like much, but because you only add or remove objects from the end of the stack (and do not rearrange the order of objects inside of the stack), **the stack naturally retains a record of what was added to it** without any other operations or memory usage. **This makes the stack one of the most useful of all data structures.** Programs use this functionality to keep track of operations on your computer, which is useful for a multitude of purposes, from debugging to error handling. Computer operating systems like the one you are using right now likely could not function without the stack.

The most famous use of the stack is the undo function in text editors or art programs. The operations you perform and state they left the document are recorded to a stack, so if you choose to undo one, the program just moves back to the previous operation by removing the latest action and restoring the document to its previous state. (*Note: This is an extremely simplified version of how undo works. Not to mention the redo function*)

## Stack Performance
The stack's ability to record the order in which things were added to it makes it an incredibly efficient form of record-keeping. In terms of big **O** notation, most operations involving the stack are either **O(n)**, - you loop through a stack until you find the desired object, with n at the most is the length of the stack - or **O(1)** - if you know how far away the desired object is from the start or end you can call it directly, or are just adding or removing an item from the stack. Just be aware that the bigger the stack, the longer it will take to loop through it, so it may be helpful to apply a size limit to the stack.

## How To Use the Stack In Python
The easiest (and quite possibly best) way to make a stack in Python is to create a **list** and only add or remove objects from the. The .append and .pop methods only add or remove items from the end by default and since lists are ordered, the stack is practically built into Python!

### Example:
```
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
```
**[1,2,3]**

```
stack.pop()
print(stack)
``` 

**[1,2]**

As you can see the stack is incredibly easy to use, just remember to not make these mistakes:

## Common pitfalls to avoid

* Inserting or removing an item from somewhere other than the end of the stack. - This disrupts the order and defeats the whole purpose of the stack. The only exception would be removing an item from the start of the stack if you are limiting the size of it. Speaking of which...
* Letting a stack grow uncontrollably - lists in Python have no size limit, so if you let a stack grow out of control it can take up memory on your computer you don't want it to, which can slow operations down or break them altogether. If you are limiting the size of the stack, only remove items from the start or end to maintain the order.
* Using *tuples*, *sets*, or other similar data types. - Tuples are immutable once created, meaning you cannot add or remove items from them, preventing them from functioning as a stack. Sets are unordered, meaning you can't keep track of the order in which items were added to the stack, and they only contain unique values, so if you add the same object multiple times to a set, only one will show up.
