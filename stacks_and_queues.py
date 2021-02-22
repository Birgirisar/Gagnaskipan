
class Stack:

    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.stack = [0] * self.capacity

    def __str__(self):
        str_val = ""
        for i in range(self.size - 1):
            str_val += str(self.stack[i]) + ", "
        if self.size > 0:
            str_val += str(self.stack[self.size - 1])
        return str_val

    def push(self, val):
        if self.capacity == self.size:
            self.resize(self.capacity)
        
        self.stack[self.size] = val
        self.size += 1

    def pop(self):
        self.stack[self.size] = []
        self.size -= 1
        return self.stack[self.size]

    def resize(self, capacity):
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.stack[i]
        self.stack = new_arr



class Queue:

    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.que = [0] * self.capacity

    def __str__(self):
        str_val = ""
        for i in range(self.size - 1):
            str_val += str(self.que[i]) + ", "
        if self.size > 0:
            str_val += str(self.que[self.size - 1])
        return str_val

    def add(self, val):
        if self.capacity == self.size:
            self.resize(self.capacity)
        
        for i in range(self.size-1, 0-1, -1):
            self.que[i+1] = self.que[i]
        
        self.que[0] = val
        self.size += 1


    def remove(self):
        for i in range(self.size-1, 0):
                self.que[i] = self.que[i + 1]

        self.que[self.size - 1] = 0
        self.size -= 1
        

    def resize(self, capacity):
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.que[i]
        self.que = new_arr
    

class Deque:

    def __init__(self):
        self.head = 0
        self.tail = -1
        self.size = 0
        self.capacity = 2
        self.array = [None] * self.capacity
    
    def resize(self, capacity):
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.array[i]
        self.array = new_arr
    
    def display(self):
        index = self.head
        for i in range(self.size):
            print(self.array[index])
            index = (index + 1) % self.capacity
    
    def enque(self, item):
        if self.capacity == self.size:
            self.resize(self.capacity)
        
        self.tail = (self.tail + 1) % self.capacity
        self.array[self.tail] = item
        self.size += 1
    
    def deque(self):
        tmp = self.array[self.head]
        self.head = (self.head + 1) % self.capacity

        self.size -= 1
        return tmp
    
        

def main():
    arr = Stack()
    arr.push(4)
    arr.push(2)
    arr.push(6)
    arr.push(9)
    arr.push(1)
    print(arr)
    print(arr.pop())
    print(arr)
    print(arr.pop())
    print(arr)

def main2():
    que = Queue()
    que.add(6)
    que.add(3)
    que.add(7)
    que.add(9)
    print(que)
    que.remove()
    print(que)
    que.remove()
    print(que)

def main3():
    array = Deque()
    array.enque(1)
    array.enque(2)
    array.enque(3)
    array.enque(4)
    array.enque(5)
    array.display()
    print()
    print(array.deque())
    print(array.deque())
    print()
    array.display()
    

main3()



