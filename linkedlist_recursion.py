
class Node: 
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
  
    # This function is in LinkedList class. It inserts 
    # a new node at the beginning of Linked List. 
    def push(self, new_data): 
  
        # 1 & 2: Allocate the Node & 
        #        Put in the data 
        new_node = Node(new_data) 
  
        # 3. Make next of new Node as head 
        new_node.next = self.head 
  
        # 4. Move the head to point to new Node 
        self.head = new_node 
  
    # This function counts number of nodes in Linked List 
    # recursively, given 'node' as starting node. 
    def getCountRec(self, node): 
        if (not node): # Base case 
            return 0
        else: 
            return 1 + self.getCountRec(node.next) 
  
    # A wrapper over getCountRec() 
    def getCount(self): 
       return self.getCountRec(self.head) 
    

    def sortedInsert(self, new_node):
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        
        else:
            curr = self.head
            while curr.next is not None and curr.next.data < new_node.data:
                curr = curr.next

            new_node.next = curr.next
            curr.next = new_node

    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data)
            temp = temp.next

  
# Code execution starts here 
if __name__=='__main__': 
    llist = LinkedList() 
    new_node = Node(5) 
    llist.sortedInsert(new_node) 
    new_node = Node(10) 
    llist.sortedInsert(new_node) 
    new_node = Node(7) 
    llist.sortedInsert(new_node) 
    new_node = Node(3) 
    llist.sortedInsert(new_node) 
    new_node = Node(1) 
    llist.sortedInsert(new_node) 
    new_node = Node(9) 
    llist.sortedInsert(new_node) 
    
    llist.printList() 



