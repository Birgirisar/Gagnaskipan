class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
        
    def getData(self):
        return self.data
  
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    
    def setData(self,newdata):
        self.data=newdata
        
    def setNext(self,newnext):
        self.next=newnext
    
    def setPrev(self,newprev):
        self.prev=newprev
    
class LinkedList:
    def __init__(self,node):
        self.head=node
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            if cur_node.next==None:
                self.tail=cur_node

  
    def first(self):
        return self.head
    
    def last(self):
        return self.tail    
        
    def before(self,p):
        return p.prev
        
    def after(self,p):
        return p.next  
        
    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False
    
    def size(self):
        cur_node=self.head
        counter=1
        while cur_node.next !=None:
            counter+=1
            cur_node=cur_node.next   
        return counter  
    
    def display(self):
        V=[self.head.data]
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            V.append(cur_node.data)
        return V
    
    def insertAfter(self,p,v):
        v.prev=p
        v.next=p.next
        (p.next).prev=v
        p.next=v
        return v
    
    def insertBefore(self,p,v):
        v.next=p
        v.prev=p.prev
        (p.prev).next=v
        p.prev=v
        return v
        
    def remove(self,p):
        t=p.data
        (p.prev).next=p.next
        (p.next).prev=p.prev
        return t
    
    def __str__(self):
        current = self.head
        to_print = []
        while current:
            to_print.append(current.data)
            current = current.next
        return str(to_print)   

A=Node(1)
B=Node(2)
C=Node(3)
D=Node(4)
E=Node(5)
A.setNext(B)
B.setPrev(A)
B.setNext(C)
C.setPrev(B)
L=LinkedList(A)
L.insertAfter(B,D)
L.insertBefore(B,E)
L.remove(B)
print(L)