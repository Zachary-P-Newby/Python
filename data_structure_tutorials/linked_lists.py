""" Practice file for linked_list.md tutorial """
# I based this on the linked list in the course practice files

"""This is the LinkedList class the instrutions in llinked_lists.md are based on, and some sample code to show the class in action.
Feel free to play around with this linked list class, try modifying it, like adding remove_head or remove_tail methods, or making Node a standalone class. You could even use it as a template to make your own. """

#The Node can either be a standalone class or a child class of the linked List, 
""" class Node:
        
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None """

class LinkedList:
    """ Simple Linked List Class that acts as interface to store and access nodes.
    When first created the linked list will be empty, you can change this to create a node when you create a new instance, but you will have to pass in a value.
    Because child classes are only defined when a new instance is created, you cannot create nodes in the __init__ method if the Node class is a child of the LinkedList class"""
    
    head = None
    tail = None

    class Node:
        """Simple Node"""
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None
        

    def __init__(self):
        #The head and tail values can be defined either inside or outside of the methods since we do not create any nodes upon instantiating.
        """self.head = None
        self.tail = None """
    

    def __str__(self):
        """ Str method for printing LinkedList """
        result = ""
        curr = self.head
        while curr != None:
            result = result + f" {curr.value},"
            curr = curr.next
        
        return result
        

    def insert_head(self, value):
        """ Inserts a node at the head of the list """
        new_node = LinkedList.Node(value)
        #new_node = Node(value)
        
        #If this is the first node created, make it both the head and tail
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            #Otherwise set the exsisting head to come after the new node and make the new_node the head. 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    

    def insert_tail(self, value):
        """ Inserts a node at the tail of the list """
        new_node = LinkedList.Node(value)
        
        #If this is the first node created, make it both the head and tail
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            #Otherwise set the exsisting tail to come after the new node and make the new node the tail. 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def insert_after(self, target_value,  value):
        """ Inserts a new node after the first node with the value specified (target_value), if there is no value, make insert new node at tail"""
        new_node = LinkedList.Node(value)
        target_node = None

        curr = self.head
        while curr.value != target_value:
            if curr == self.tail:
                self.insert_tail(value)
                break
            else:
                curr = curr.next
        else:
            target_node = curr
            #set new_node prev and next
            new_node.prev = target_node
            new_node.next = target_node.next
            #set the prev of the node after the target to be new_node
            target_node.next.prev = new_node
            #set new node to come after target
            target_node.next = new_node    


    def insert_before(self, target_value,  value):
        """ Inserts a new node before the first node with the value specified (target_value), if there is no value, make insert new node at tail"""
        new_node = LinkedList.Node(value)
        target_node = None

        curr = self.head
        while curr.value != target_value:
            if curr == self.tail:
                self.insert_tail(value)
                break
            else:
                curr = curr.next
        else:
            target_node = curr
            #set new_node prev and next
            new_node.next = target_node
            new_node.prev = target_node.prev
            #set the next of the node before the target to be new_node
            target_node.prev.next = new_node
            #set new node to come before target
            target_node.prev = new_node


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
    
    def remove_head():
        """ Try to make this method on your own """

        #YOUR CODE HERE
        pass


    def remove_tail():
        """ Try to make this method on your own """

        #YOUR CODE HERE
        pass
#____________________________________________________________________________________________
#Smaple code
linked_list = LinkedList()

linked_list.insert_head("Apple")
print(linked_list)
linked_list.insert_tail("Orange")

linked_list.insert_after("Apple", "Coconut")

linked_list.insert_before("Orange","candy")
print(linked_list)

linked_list.remove_value("candy")
print(linked_list)

linked_list.remove_value("Pear")
print(linked_list)