"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a value and a priority.
        """

        def __init__(self, value, priority):
            """
            Initialize a new node
            """
            self.value = value
            self.priority = priority

        def __str__(self):
            """
            Display a single node
            """
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Add a new value to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        new_node = Priority_Queue.Node(value, priority)
        self.queue.append(new_node)

    def dequeue(self):
        """
        Remove the next value from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        values with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority values are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """
        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(1, len(self.queue)):
            if self.queue[index].priority > self.queue[high_pri_index].priority:
                high_pri_index = index
            #elif self.queue[index].priority == self.queue[high_pri_index].priority:

        # Remove and return the item with the highest priority
        value = self.queue[high_pri_index].value
        #print(self.queue[high_pri_index])
        del self.queue[high_pri_index]
        return value
        
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result

#I had to make this for debugging purposes
def display_queue(queue):
    print("")
    for item in queue:
        print(item)
    print("")


# Test Cases

# Test 1
# Scenario: Test 6 items with unique priorities
# Expected Result: Roy, Fay, Helen, Brian, Lowell, Joe
print("Test 1")
myQueue = Priority_Queue()

myQueue.enqueue("Joe",1)
myQueue.enqueue("Helen",4)
myQueue.enqueue("Lowell",2)
myQueue.enqueue("Brian",3)
myQueue.enqueue("Fay",5)
myQueue.enqueue("Roy",6)

print(myQueue.dequeue())
#print(myQueue.queue)
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
print(myQueue.dequeue())
# Defect(s) Found: 
#   priority and value were swapped in Priority_Queue.enqueue Function, 
#   fixed by swapping them back; and nodes were not being deleted in Priority_Queue.dequeue Function, fixed by adding del self.queue[high_pri_index] statment

print("=================")

# Test 2
# Scenario: Verify Queue is empty, reuse queue from test 1
# Expected Result: Return error message stating queue is empty
print("Test 2")
print(myQueue.dequeue())
# Defect(s) Found: 
#   Nodes were not being deleted in Priority_Queue.dequeue Function  fixed by adding del self.queue[high_pri_index] statment

print("=================")

# NOTE: I fixed the defects found in tests one and two before beginning test 3

# Test 3
# Scenario: Test queue when multiple items have same priority
# Expected Result: George, Jerome, Montmorency, Harris
print("Test 3")
leQueue = Priority_Queue()

leQueue.enqueue("George",3)
leQueue.enqueue("Jeorome",2)
leQueue.enqueue("Montmorency",2)
leQueue.enqueue("Harris",1)

display_queue(leQueue.queue)
print(leQueue.dequeue())
display_queue(leQueue.queue)
print(leQueue.dequeue())
display_queue(leQueue.queue)
print(leQueue.dequeue())
display_queue(leQueue.queue)
print(leQueue.dequeue())

# Defect(s) Found: 
#   Of two nodes with the same priority, the last one added was being dequeued first, 
#   instead of beind dequed last, fixed by changing '>=' in high_priority_index assigner to '>'

print("=================")

# Test 4
# Scenario: 
# Expected Result: 
print("Test 4")

# Defect(s) Found: 

print("=================")