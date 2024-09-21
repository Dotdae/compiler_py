class Node: 

    # Initializes the node with the valuo of the data and the pointer
    # in None if there is no next node.

    def __init__(self,data):

        # Node data.

        self.data = data

        # Pointer.

        self.next = None

class LinkedList:

    # Initializes the head of the list, starts as None if th list is empty.

    def __init__(self):

        self.head = None


    # Get a new data and create a new node.

    def add(self, data):

        newNode = Node(data)

        # If the list is empty the new node is the head of the list.

        if not self.head:

            self.head = newNode
        
        # If the list is not empy, the list go to the last node and 
        # the new node is linked to the last one.

        else:

            actual = self.head
            
            while(actual.next):

                actual = actual.next
            
            actual.next = newNode

    # Print each node and in the end print "None" indicating that ther are no more nodes.

    def print(self):

        actual = self.head

        while actual:

            print(actual.data, end= " -> ")

            actual = actual.next
        
        print("None")

    