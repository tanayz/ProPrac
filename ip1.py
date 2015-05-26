'''Find a pair of elements from an array whose sum equals a given number'''
import time
import numpy as np

input=np.arange(20000)
np.random.shuffle(input)

sm=34598

#Solution with complexity O(n)
t=time.time()
dc={}
for i in range(len(input)-1): #O(n)
    dc[input[i]]=i

for i in range(len(input)-1): #O(1)
    if dc.has_key(sm-input[i]):
        print '#1 :elements are',input[i],sm-input[i],'with time :',time.time()-t
        break
    
#Solution with complexity O(nlogn)
t=time.time()
input.sort()
s=0
e=len(input)-1
while s<e:
    if input[s]+input[e]>sm:
        e=e-1
    elif input[s]+input[e]<sm:
        s=s+1
    else:
        print '#2 :elements are',input[s],input[e],'with time :',time.time()-t
        break
