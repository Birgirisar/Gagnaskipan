
class IndexOutOfBounds(Exception):
    pass

class Empty(Exception):
    pass

class ArrayList:
    def __init__(self):
        # TODO: remove 'pass' and implement functionality
        self.capacity = 1
        self.size = 0
        self.array = [0]*2
    
    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        # TODO: remove 'pass' and implement functionality
        return_string = ''
    
        for i in range(self.size):
            return_string = return_string + str(self.array[i]) + ', '
        return_string = return_string[:-2]
        return return_string

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        #self.array = [value, *self.array]
        if self.capacity == self.size:
            self.resize(self.capacity)

        for i in range(self.size-1, 0-1, -1):
            self.array[i+1] = self.array[i]
        
        self.array[0] = value
        self.size += 1
        

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        # TODO: remove 'pass' and implement functionality
        try:
            if index < 0 or index > self.size:
                raise IndexOutOfBounds

            if self.capacity == self.size:
                self.resize(self.capacity)

            for i in range(self.size-1, index-1, -1):
                self.array[i+1] = self.array[i]

            self.array[index] = value
            self.size += 1
        except IndexOutOfBounds:
            print('Index out of bounds!')

    #Time complexity: O(1) - constant time
    def append(self, value):
        # TODO: remove 'pass' and implement functionality
        if self.capacity == self.size:
            self.resize(self.capacity)
        self.array[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        try:
            if index < 0 or index > self.size:
                raise IndexOutOfBounds
            self.array[index] = value
        except IndexOutOfBounds:
            print('Index out of bounds!')

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        try:
            if self.size <= 0:
                raise Empty
            return self.array[0]
        except Empty:
            print("The list is empty!")

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        try:
            if index < 0 or index > self.size:
                raise IndexOutOfBounds
            return self.array[index]
        except IndexOutOfBounds:
            print("Index out of bounds!")

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        try:
            if self.size <= 0:
                raise Empty
            return self.array[self.size-1]
        except Empty:
            print("The list is empty!")


    #Time complexity: O(n) - linear time in size of list
    def resize(self, new_capacity):
        # TODO: remove 'pass' and implement functionality
        self.capacity *= 2
        new_array = [0] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array


    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        try:
            if index<0 or index>= self.size:
                raise IndexOutOfBounds

            if index == self.size - 1:
                self.array[index] = 0
                self.size -= 1
                return
            
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = 0
            self.size -= 1
        except IndexOutOfBounds:
            print("Index out of bounds!")

    #Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        if self.size == 0:
            pass
        for _ in range(self.size):
            self.size -= 1
        

    #Time complexity: O(n) - linear time in size of sublist
    def sublist(self, start, length):
        # TODO: remove 'pass' and implement functionality
        try:
            if length < 0 or length >= self.size:
                raise IndexOutOfBounds
            new_array = [0] * length
            self.size = length
            for i in range(0 , length):
                new_array[i] = self.array[start + i]
            self.array = new_array
        except IndexOutOfBounds:
            print("Index out of bounds!")   

    #Time complexity: O(n) - linear time in size of concatinated list
    # OR

    #Time complexity: O(n+m) - linear time in size of both lists, self and other
    def concatenate(self, other):
        # TODO: remove 'pass' and implement functionality
        lis2_length = 0
    
        while True:
            try:
                other[lis2_length]
                lis2_length += 1
            except IndexError:
                break
        
        index = 0
        new_array = [0] * (self.size + lis2_length)
        for i in range(self.size):
            new_array[i] = self.array[i]
        for i in range(self.size, (self.size + lis2_length)):
            new_array[i] = other[index]
            index += 1
        self.size += lis2_length
        self.array = new_array
            

if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level
