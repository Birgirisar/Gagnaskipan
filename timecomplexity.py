import random

def power(a,b):
    ret_val = 1
    for _ in range(exp):
            ret_val *= base
    return ret_val

#print(power(5,3)) # tímaflækja: O(n)


def multi(a,b):
    total  = 0
    counter = 0
    while counter < b:
        total += a
        counter += 1
    return total

#print(multi(5,5)) # Tímaflækja: O(n)


def randomm(n):
    lis = [0] * n
    for i in range(len(lis)):
        lis[i] = random.randint(1,6)
    return lis  # tímaflækja: O(n)

def printlis(L):
    for i in range(len(L)):
        print(L[i], end=' ') #O(1)

def incrandom(L):
    rnum = random.randint(0, len(L))
    L[rnum] += 1
    print(L) # tímaflækja: O(1)

lis = randomm(5)
printlis(lis)
#incrandom(lis)



def switch(L):
    r1 = random.randint(0, len(L))
    r2 = random.randint(0, len(L))
    L[r1] = r2
    L[r2] = r1
    print(L) # tímaflækja: O(1)

lis2 = [0,1,2,3,4]
switch(lis2)



