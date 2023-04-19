from math import ceil, log2
from random import randint
from random import shuffle
import math

class UniversalHashing:
    def __init__(self, m, p):
        self.M = m # Max size 
        self.p = p

    def drawRandomHashFunction(self):
        a = randint(1, self.p - 1)
        b = randint(0, self.p - 1)
        print("chosen a",a,"chosen b",b)
        #return the hash function as lambda function
        return lambda x: ((a * x + b) % self.p) % self.M 

if __name__ == '__main__':
    # define prime number
    p = 997
    #n = p # no of keys (0, 1, ... p-1) 
    n = 30
    
    m = ceil(n ** (1.25)) #size of table
    #m = int(n)
    
    keys = [i for i in range(p)]  # keys (0, 1, ... p-1)
    
    shuffle(keys) # shuffle keys
    
    keys = keys[0:n]
    
    print(keys)

    print("table size:",m)
    H = UniversalHashing(m,p)
    
    # go over all keys and add 
    keep_running = True
    two_coll = False
    count_global = 0
    while(keep_running):
        count_global+=1
        print("TRIAN NUMBER ======", count_global)
        T_1 = [ [] for _ in range(m) ]  ## Table 1 with m empty linked lists
        T_2 = [ [] for _ in range(m) ]  ## Table 2
        print("Hash 1:")
        h_1 = H.drawRandomHashFunction()
        print("Hash 2:")
        h_2 = H.drawRandomHashFunction()
        two_coll = False
        for i in range(len(keys)): 
            x = keys[i] # x is my current key
            #Check if the address is empty in T1
            #Note its linked list inside that address
            if(len(T_1[h_1(x)]) == 0): #check if its previously empty (no collision)
                #add key to the LL in T1
                T_1[h_1(x)].append(x)
                #print("{0:0=2d} is stored in Table 1 address: {1:0=2d}".format(x,h_1(x)))
            else: 
                #if there is collision in table 1 in h_1(x)
                #print("--------- collision for",x, "in", h_1(x), " in Table 1")
                if(len(T_2[h_2(x)]) == 0):
                    T_2[h_2(x)].append(x)
                    #print("{0:0=2d} is stored in Table 2 address: {1:0=2d}".format(x,h_2(x)))
                else:
                    # If both t1 and t2 gives collision for current key x
                    print("TWO COLLISIONS - T1 and T2 for",x)
                    two_coll = True
        if two_coll:
            keep_running = True
        else:
            keep_running = False
        
    print('Total trials',count_global)
    # To Print All contents Table 1
    print("PRINTINT ALL CONTENTS OF FINAL TABLE 1")
    for i in range(len(T_1)):
        print(i,T_1[i])
    print("PRINTINT ALL CONTENTS OF FINAL TABLE 2")
    for i in range(len(T_2)):
        print(i,T_2[i])
        
         

