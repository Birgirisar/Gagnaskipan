
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def remove_first(self):
        temp = self.head
        self.head = self.head.next
        temp = None
    
    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
    
    def remove_last(self):
        last = self.head
        while last.next:
            prev = last
             last = last.next
        prev.next = None

    def print_lis(self):
        while self.head != None:
            print(self.head.data)
            self.head = self.head.next
        

class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def add(self):
        self.ll.add_to_front(data)

    def remove_first(self):
        return self.ll.remove_first()


lis = LinkedList()
lis.head = Node('Mon')
lis.add_to_front('Sun')
lis.add_to_front('Sat')
lis.append('Tue')
lis.append('Wed')


lis.remove_last()
lis.remove_first()
lis.print_lis()