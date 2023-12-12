""" Binary Tree Practice File"""
# I used docstrings from the lessons to save time building the practice file
class BinaryTree:
    """ A Simple Binary Tree that does not allow duplicates. When creating an instance you can include a data value for the root node"""
    def __init__(self, root_data = None):
        
        if root_data:
            self.root = BinaryTree.Node(root_data)
        else:
            self.root = None


    class Node:
        """ Simple Node with data attribute for storing numbers. If no parent node is provided this will become the root node. """
        left = None
        right = None

        def __init__(self, data, parent = None):
            
            self.data = data
            
            if parent == None:
                self.parent = None
            else:
                if parent.data > self.data:
                    parent.right = self  
                else:
                    parent.left = data
            
        """ def __str__(self):
            return str(self.data) """

    def insert(self, data):
        """ Inserts node into tree, if there is no root this will create a new root. will cancel if data value is duplicate """

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
    
    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)


    def _traverse_forward(self, node):
        """


        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """

        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)


    def __reversed__(self):
        """ Iterates through the tree in reverse order. Starting with the largest node and ending with the smallest"""

        yield from self._traverse_backward(self.root)
    
    def _traverse_backward(self, node):
        """ Iterates through the tree starting with the largest node and ending with the smallest """

        #YOUR CODE HERE
        pass
    

    def contains(self, value):
        """ Searches tree to see if the value is contained within. Returns true if found, false if not. """
        
        for i in self:
            if i == value:
                return True
        else:
            return False
        


#Practice Code
#______________________________________________________________________

bi_tree = BinaryTree(20)

bi_tree.insert(15)
bi_tree.insert(24)
bi_tree.insert(16)
bi_tree.insert(11)
bi_tree.insert(13)
bi_tree.insert(12)
bi_tree.insert(9)
bi_tree.insert(16)
bi_tree.insert(25)

# Now to loop through using __iter__function
print(""*5)
print("Nodes:")
for i in bi_tree:
    print(i)

print(""*5)
print(f"Is 12 in tree: {bi_tree.contains(12)}")
print(f"Is 4 in tree: {bi_tree.contains(4)}")


#Revered challange test code:
print(""*5)
for x in reversed(bi_tree):
    print(x)