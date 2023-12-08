""" Binary Tree Practice File"""

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
        """ This is a generator function. When a loop is preformed on the tree this function is called. Start at the root and move forward.
        When it hits the end of a subtree it will yield all of the data values of that subtree up to the last point where the subtree split in two."""

        yield from self._traverse_forward(self.root)

    def _traverse_forward(self, node):
        """ Traverse through tree, returning nodes in order from the smallest to the largest """

        if node is not None:
            
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)


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
for i in bi_tree:
    print(i)