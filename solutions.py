

def is_divisible(num, div):
    if div == 0:
        return False
    if (num == 0):
        return True
    elif (num < 0):
        return False
    return is_divisible(num-div, div)

#print(is_divisible(14,0))


def count_matches(lis):
    count = 0
    pos = 0

    if lis[pos] == lis[pos + 1]:
        count += 1
        pos += 1
    else:
        pos += 1
        return count + count_matches(lis)
    return pos
    
lis = [3,4,5,5,6]
#print(count_matches(lis))


class ArrayList:
    def __init__(self, capacity = 4):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        str_val = ""
        for i in range(self.size - 1):
            str_val += str(self.arr[i]) + ", "
        if self.size > 0:
            str_val += str(self.arr[self.size - 1])
        return str_val

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.insert(value, 0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
    
        if index < 0 or index > self.size:
            return

        if self.capacity == self.size:
            self.resize(self.capacity)

        for i in range(self.size-1, index-1, -1):
            self.arr[i+1] = self.arr[i]

        self.arr[index] = value
        self.size += 1
    
    def resize(self, new_capacity):
        # TODO: remove 'pass' and implement functionality
        self.capacity *= 2
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.insert(value, self.size)

    def count_instances(self, value):
        pass

def main():
    test = ArrayList()
    test.prepend(4)
    test.prepend(5)
    test.prepend(7)
    test.prepend(4)
    print(str(test))
    test.insert(3,3)
    print(str(test))
    test.prepend(10)
    print(str(test))
    test.append(18)
    print(str(test))



class Library:
    def __init__(self,d={}):
        self.isbn = None
        self.name = None
        self.d = d

    def add_book(self, ISBN, name):
        if ISBN not in self.d.keys():
            self.d[ISBN] = name

    def get_book(self, ISBN):
        return self.d[ISBN]

    def change_book(self, ISBN, new_name):
        if ISBN in self.d.keys():
            self.d[ISBN] = new_name
        
    def remove_book(self, ISBN):
        if ISBN in self.d.keys():
            self.d.pop(ISBN)

    def __str__(self):
        return self.d

        



def main2():
    tes = Library()
    tes.add_book(1234, 'blabla')
    tes.add_book(1235, 'ulala')
    tes.add_book(45, 'jaja')
    tes.remove_book(45)
    tes.change_book(1234, 'nunu')
    print(tes.get_book(1234))
    
    
main2()