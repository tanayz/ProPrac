# -*- coding: utf-8 -*-
"""
Find the first unique value from an unsorted array
"""
import time

input=[2,3,3,2,11,7,3,11,9,10,7,8,12,12,8,5,10,9,8,2,11]

t=time.time()
dc={}
for i in range(len(input)-1): #O(n)
    if dc.has_key(input[i]):
      dc[input[i]]+=1
    else:
      dc[input[i]]=1 

for i in range(len(dc)):
    if dc.values()[i]==1:
        print '#1 First unique value : ',dc.keys()[i]
        break
print 'Time taken',time.time()-t

    
input.sort()    
for i in range(len(input)-1):
    if input[i]!=input[i+1]:
        if ((i+1==len(input)-1) or (input[i+1]!=input[i+2])):
            print '#2 First unique value : ',input[i+1]
            break
        
print 'Time taken',time.time()-t

"""
Find top k most frequent number :http://www.careercup.com/question?id=5632249361858560
"""
# sort dc in terms of values in descending order and pick up top k