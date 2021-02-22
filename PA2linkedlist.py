
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def pop_front(self):
        temp = self.head
        self.head = self.head.next
        temp = None
    
    def push_back(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
    
    def pop_back(self):
        last = self.head
        while last.next:
            prev = last
            last = last.next
        prev.next = None
    
    def get_size(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count


    def __str__(self):
        return_string = ''
        node = self.head

        if node != None:
            return_string += str(node.data)
            node = node.next
            while node:
                return_string += ' ' + str(node.data)
                node = node.next

        return_string += ''
        return return_string


def get_size(head):
    head = self.head
    if head is None:
        return 0
    else:
        return 1 + get_size(head.next)



if __name__ == '__main__':
    test = LinkedList()
    test.push_front(4)
    test.push_back(6)
    test.push_front(1)
    test.push_back(8)
    print(test)
    test.pop_front()
    test.pop_back()
    print(test)
    ###############


        