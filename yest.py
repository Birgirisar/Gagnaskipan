
class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
def print_lis(head):
    if head != None:
        print(head.data, end=" ")
        print_lis(head.next)
    else:
        print('')


tail = Node("D", None)

head = Node("A", Node("B", Node("C", tail)))




node = head

head = tail

tail = node

head.next = tail.next

tail.next = None




print_lis(head)