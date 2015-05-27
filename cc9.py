# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 01:46:17 2015
Given two sorted arrays, A and B, where A has a large enough 
buffer at the end to hold B. Write a method to merge B into A in sorted order
Modified on 05/27 06:36
@author: tanay
"""

a=[1,2,3,4,7,8,9,14,15]+[None]*9
b=[5,6,10,11,12,13,16,17,18]

def abmerge(a,b):
    k=len(a)-1   # Index of last location of array a
    j=len(b)-1     # Index of last element in array b
    i=len(a)-len(b)-1     # Index of last element in array a
    while (i>=0 and j>=0):
        if(a[i]>b[j]):
            a[k]=a[i]
#            print 'i:',i,'k:',k
            k=k-1
            i=i-1
            
        else:
            a[k]=b[j]
#            print 'j:',j,'k:',k
            k=k-1
            j=j-1            
        
    while (j>=0):
        a[k]=b[j]
#        print 'j:',j,'k:',k
        k=k-1
        j=j-1
        
    return a
    
k=abmerge(a,b) 
print k