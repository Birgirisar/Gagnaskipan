
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
        return DLL_Node(value)
    
    def insert_at_node(self, value, node):
        new_node = self.find_node_to_insert_at(value)
        if node < 1:
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

        #node = DLL_Node(value)
        #if self.header == None:
        #    self.header = node
        #    return
        #elif self.header.next == None:
        #    self.header.next = self.header
        #    self.tailer = self.header
        #    self.tailer.next = None
        #    self.header = node
        #    node.next = self.tailer
        #    return
        #node.next = self.header
        #self.header = node
        
    def get_range_in_SLL(self, min, max):
        # THIS OPERATION SHOULD RETURN A SINGLY-LINKED LIST
        # I.E. an instance of SLL_Node which is the first node in that list
        current = self.header
        return_str = ''
        while current.next != None:
            for i in range(min, max+1):
                if i == current.data:
                    return_str += ' ' + str(i)
            current = current.next
        return return_str
        

    def __str__(self):
        ret_str = ""
        node = self.header.next
        while node != self.trailer:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str


def find_index(head, value):
    if not head:
        return None

    if head.data == value:
        return 0
    
    index = find_index(head.next, value)
    return 1 + index if index != None else None


def ordered_subset(head1, head2):
    if not head1 and not head2:
        return True
    
    if not head1 or not head2:
        return False

    while head1:
        if head1.data == head2.data:
            return ordered_subset(head1.next, head2.next)
        head1 = head1.next
        return True

    return False
    

# NO IMPLEMENTATION OF EXAM SOLUTIONS BELOW THIS LINE
if __name__ == "__main__":

    # MAKE ALL TEST CODE BELOW THIS LINE
    # AND AT THIS INDENT LEVEL!!

    print("\nTesting DLL_ORDERED")
    dl = DLL_Ordered()
    dl.insert_ordered(17)
    dl.insert_ordered(45)
    dl.insert_ordered(12)
    dl.insert_ordered(89)
    dl.insert_ordered(23)
    dl.insert_ordered(56)
    dl.insert_ordered(34)
    dl.insert_ordered(45)
    print("dl: " + str(dl))
    dl.insert_ordered(10)
    dl.insert_ordered(23)
    dl.insert_ordered(22)
    dl.insert_ordered(71)
    dl.insert_ordered(23)
    dl.insert_ordered(45)
    dl.insert_ordered(22)
    dl.insert_ordered(98)
    print("dl: " + str(dl))


    print("\nTesting RANGE")
    def test_range(dl, min, max):
        print("range(" + str(min) + ", " + str(max) + "): " + str(dl.get_range_in_SLL(min, max)))

    test_range(dl, 23, 45)
    test_range(dl, 0, 100)
    test_range(dl, 45, 45)
    test_range(dl, 17, 89)
    test_range(dl, 10, 98)
    test_range(dl, 54, 76)
    test_range(dl, 20, 60)

    print("\nTesting find_index")
    #5 6 3 4
    head = SLL_Node(5, SLL_Node(6, SLL_Node(3, SLL_Node(4, None))))
    print(find_index(head, 3))
    print(find_index(head, 7))
    #5 6 3 4 5
    head = SLL_Node(5, SLL_Node(6, SLL_Node(3, SLL_Node(4, SLL_Node(5, None)))))
    print(find_index(head, 5))
    print(find_index(head, 6))
    print(find_index(head, 4))

    print("\nTesting ordered_subset")
    head1 = SLL_Node(1, SLL_Node(5, SLL_Node(6, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(5, SLL_Node(2, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(3, SLL_Node(2, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(2, SLL_Node(3, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(2, SLL_Node(5, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(2, SLL_Node(4, SLL_Node(5, SLL_Node(6, None)))))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, SLL_Node(7, None)))))))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(1, SLL_Node(2, SLL_Node(100, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))
    head1 = SLL_Node(0, SLL_Node(1, SLL_Node(2, None)))
    head2 = SLL_Node(1, SLL_Node(2, SLL_Node(3, SLL_Node(4, SLL_Node(5, SLL_Node(6, None))))))
    print(ordered_subset(head1, head2))