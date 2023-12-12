# The Binary Search Tree

[Practice File](https://github.com/Zachary-P-Newby/Python/blob/Programming-With-Data-Structures-Fall-2023/data_structure_tutorials/trees_practice.py)

## Introduction
The **Binary Search Tree** (or **tree** for the rest of this tutorial) is an evolution of the linked list used for storing data in a quickly searchable format. Unlike the linked list where nodes are linked to the previous and following nodes in a straight line, trees break off into branches with each node having two children or *leaf* nodes, and a link back to its *parent*. Trees start at a *root* node instead of a head, and split into one-to-two **subtrees** with each leaf node acting as the new root node. As a result they have multiple *tail* nodes, so we don't bother saving one to special tail reference. Each node can have no more than two leaf nodes linked to it, this keeps trees easy to navigate and allows for the functions used to **traverse** or move through the tree to work properly.

To visualize a tree, imagine an actual (deciduous) tree with the root node as the trunk and each node as the start of a new branch growing off an existing branch. Alternatively, a family tree chart can be used as a visualization, with you as the root node, and your parents being the the two leaf nodes. 

It should be noted that for search functions to work, two conditions must be met:
 1. all of the data must be of the same type or be compatible with each other when performing comparison operations.
Most trees are used for storing **numerical** data types (ie. *ints* and *floats*) because they can be compared using the greater than *>* and less than *<* operators, allowing data to be sorted by comparing its value with the data already in the tree. This allows us to traverse using **recursive** comparison operations instead of looping. If you try to add an object to the tree that can't be compared with the objects already in the tree it will produce an error.

 2. Trees must be balanced.
The subtrees must all be of similar size and length (within a few nodes of each other in length) for the traversal functions to be as efficient as possible. If we have just one long branch, it might as well be a linked or normal list we just loop through.

Data in trees is sorted in regards to how it compares to the roots and leaves of the tree. In the case of numeric data, values smaller than the root are moved to the *left*, while values greater are moved to the *right* until an empty node is found where the value is greater than its neighbors to the left and smaller than its neighbor to the right. This is why the two leaf nodes are called the *left* and *right* nodes. (Although you could left and right around or use lesser and greater)

## Why it Matters and Tree Performance
Trees are used because we can sort, find, and store data using a series of recursive comparison operations instead of loops which has better performance than lists (dynamic arrays) with large amounts of data. Because we use comparison operations we can narrow down and exclude subtrees with each recursive operation until we find one where a value is or would fit. This results in **O(log(n))** operations that are much faster at sorting through the same amount of data in a list format **O(n)**. While the search times are similar with small lists and trees, the tree search function performance scales logarithmically in regards to size (meaning it eventually levels off and never reaches past a certain value) while the looping search function performance scales linearly (in a straight line). Trees are best for storing and sorting through large amounts of data, as the performance is nearly identical to lists for small amounts of data.

## How to Use a Binary Tree
(For this lesson we are combining these two sections)
You will want to use the [Practice File](https://github.com/Zachary-P-Newby/Python/blob/Programming-With-Data-Structures-Fall-2023/data_structure_tutorials/trees_practice.py) as a guide on how to make tree, as it will be much quicker for you to look over the one in there than for me to describe it here, but here is a quick overview on how to make tree class and write class functions/methods for it.

 * When creating a tree class, have an attribute for the *root* node, you will always start at the root and move up branches when traversing the tree.

 * When creating a node class to be used in a tree, you MUST have a *value* attribute. If your nodes can't hold values, you cannot compare them to traverse through the tree. You must also include attributes for the *parent*, *left*, and *right* nodes.

### There are two main ways to traverse a tree:
 1. **iterating (no comparison)**
  You can loop through a tree by redefining the built-in `__iter__` function (which is called on an object whenever you use a for loop object on it). This works by moving up each branch and using recursion to return every node once you reach the end of it. Because the `__iter__` function is a generator function you will have to use the `yield` keyword. The  `._traverse_forward` method is used inside the `__iter__` function I created for the tree.  It goes up each branch in order of smallest to largest, and once it reaches the end it returns each value in the branch until it hits the last split and then moves up the next branch until it has moved up through every branch in the tree.

```
def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
        the root of the BST.  This is called a generator function.
        This function is called when a loop is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)

def _traverse_forward(self, node):
        """
        View the practice file for the full docstring
        """

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
```

 2. Comparison
These are the search algorithms I mentioned above. You start by taking a value want to insert or locate and compare it to the root node. if it is bigger than the root, you move up the right sub-tree, if it is smaller you move up the left. When you move up into a sub-tree, you compare your value with the root node of *that* subtree. (It will be either the *left* or *right* nodes of the previous root node) You narrow down branches of the subtree until you find a place to insert a new node or the one you are looking for.

To illustrate here is the insert function from the practice file. It consists of a main `.insert` function you call to add a new value, and a recursive `._insert` function used inside of it to perform recursive search operations
```
def insert(self, data):
        """ Inserts node into tree, if there is no root this will create a new root. will cancel if the data value is duplicate """

        #Check if root
        if self.root is None:
            self.root = BinaryTree.Node(data)
        else:
            self._insert(data, self.root)


    def _insert(self, data, root):
        """ Inner Insert function """
        
        if data == root.data:
            print("ERROR. DUPLICATE VALUE, OPERATION CANCELLED, DUPLICATES ARE NOT ALLOWED")
        elif data > root.data:
            if root.right == None:
                root.right = BinaryTree.Node(data)
            else:
                self._insert(data, root.right)
        else:
            if root.left == None:
                root.left = BinaryTree.Node(data)
            else:
                self._insert(data, root.left)
```

## Common Pitfalls to Avoid

 * Inserting duplicate values.
 You will want to add duplicate value handling. If you do not add handling for duplicates into your insert method it can produce errors or bugs and when someone tries to insert a value already found inside the tree. You can either prevent duplicates from being added or have the functionality to have them added to the right of the node they match.

 * Adding the wrong data type. Always make sure the data you try to add to a tree is compatible or can be converted to a compatible format.

## Now You Try!
Now it's your turn! Go into the [Practice File](https://github.com/Zachary-P-Newby/Python/blob/Programming-With-Data-Structures-Fall-2023/data_structure_tutorials/trees_practice.py) and play around with the sample BinaryTree class. Try to complete all three challenges

Challenges:
 * Create a *._traverse_backward* method to finish the *.__reversed __* method that allows you to return values from the largest to the smallest. (Hint: Play around with the yield statements in *._traverse_forward*)
 * Create a **BinaryTree** containing the numbers 1 through 50 using a for loop and `range(1,51)`
 * Create a method that removes a node that contains a specific value and any children of it.