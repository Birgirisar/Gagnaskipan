
class SLL_Node:
    # THIS IMPLEMENTATION OF SINGLY-LINKED LIST NODE
    # MUST BE USED UNCHANGED, FOR TESTING PURPOSES
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        ret_str = ""
        node = self
        while node != None:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


class DLL_Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL_Ordered:
    def __init__(self):
        self.header = DLL_Node()
        self.trailer = DLL_Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header

    def find_node_to_insert_at(self, value):
        if self.header is None:
            return None
        
        while self.header != None:
            if self.header.data == value:
                pass


        return None
    
    def insert_at_node(self, value, node):
        new_node = DLL_Node(value)
        if node == 0:
            if self.header == None:
                self.header = new_node
                return
            elif self.header.next == None:
                self.header.next = self.header
                self.tailer = self.header
                self.tailer.next = None
                self.header = new_node
                new_node.next = self.tailer
                return
        
            new_node.next = self.header
            self.header = new_node
        elif node == 1:
            new_node.next = self.header
            self.header.prev = new_node
            self.header = new_node
        else:    
            temp = self.header
            for i in range(1, node):
                if(temp != None):
                    temp = temp.next   
            if temp != None:
                new_node.next = temp.next
                new_node.prev = temp
                temp.next = new_node  
                if (new_node.next != None):
                    new_node.next.prev = new_node         
        return 

    def insert_ordered(self, value):
        new_node = self.find_node_to_insert_at(value)

        if self.header is None:
            self.header = new_node
        
        elif self.header.data >= new_node.data:
            new_node.next = self.header
            new_node.next.prev = new_node 
            self.header = new_node 
        else:  
            current = self.header
  
            while ((current.next is not None) and (current.next.data < new_node.data)):
                current = current.next
      
            new_node.next = current.next
  
            if current.next is not None: 
                new_node.next.prev = new_node 
  
            current.next = new_node 
            new_node.prev = current
        return str(new_node)
        
    
    def get_range_in_SLL(self, min, max):
        # THIS OPERATION SHOULD RETURN A SINGLY-LINKED LIST
        # I.E. an instance of SLL_Node which is the first node in that list
        pass

    def __str__(self):
        ret_str = ""
        node = self.header.next
        while node != self.trailer:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


test = DLL_Ordered()
test.insert_ordered(10)
test.insert_ordered(5)
test.insert_ordered(1)
test.insert_ordered(4)
print(test)


