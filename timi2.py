#O(1)
def big_O_1_example():
    n = 1000000 # O(1)
    list_ = [1,2,3,4,5,6,7,8,9]
    print(list_[0])


#O(log(n))  hvaða veldi þarf ég að setja 2 í til að fá n
def big_O_logn_example():
    n = 1000000
    a = 0
    while n > 1:
        a = a + 1
        n = n / 2
    print(a)



#O(1+1+1+n) verður O(n)
def big_O_n_example():
    n = 100 # O(1)
    a = 0 # O(1)
    for i in range(n): # O(n)
        a = a + 1
    print(a)


#O(n^2)
def big_O_n2_example():
    n = 100 # O(1)
    a = 0 # O(1)
    for i in range(n): # O(n)
        for j in range(n):
            a = a + 1
    print(a)


#O(n^2) skrifum alltaf bara stærsta factorinn ef þú ert með O(n^2 + n) þá skrifum við bara O(n^2)

#O(2*n^2) verður O(n^2) því veldið hefur svo miklu meiri áhrif á tímann

#O(n^3) ....

#O(2^n)

#O(n!)

