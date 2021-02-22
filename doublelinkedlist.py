
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class DDL_Deque:
    def __init__(self):
        self.header = None
        self.trailer = None
        self.size = 0
    
    def push_front(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.header = new_node
            self.trailer = new_node
            self.size = 1
        else:
            new_node.next = self.header
            self.header.prev = new_node
            self.header = new_node
            self.size += 1
        
    def pop_front(self):
        val = self.header.data
        self.header = self.header.next
        if self.header != None:
            self.header.prev = None
        self.size -= 1
        return val
    
    def push_back(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.header = new_node
            self.trailer = new_node
            self.size = 1
        else:
            new_node.prev = self.trailer
            self.trailer.next = new_node
            self.trailer = new_node
            self.size += 1
        
    def pop_back(self):
        val = self.trailer.data
        self.trailer = self.trailer.prev
        if self.trailer != None:
            self.trailer.next = None
        self.size -= 1
        return val
    
    def printItOut(self):
        """
        Prints out the list from head to tail all on one line.
        :return: None
        """
        temp = self.header
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    def print_reverse(self):
        temp = self.trailer
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.prev
        print()
    
    def get_size(self):
        return self.size



node = DDL_Deque()
node.push_front(6)
node.push_front(10)
node.push_front(2)
node.push_front(4)
node.printItOut()

node.push_back(24)
node.printItOut()
node.print_reverse()

print(node.pop_front())
node.printItOut()

print(node.pop_back())
node.printItOut()

print(node.get_size())
