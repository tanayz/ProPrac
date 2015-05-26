# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 01:46:17 2015

@author: tanay
"""

a=[1,2,3,4,5,6,None, None, None,None, None, None]
b=[8,9,10,11,12,13]
m=6
n=len(b)
def abmerge(a,b,m,n):
    k=m+n-1   # Index of last location of array b
    i=n-1   # Index of last element in array b
    j=m-1   # Index of last element in array a
    while (i>0 & j>0):
        if(a[i]>b[j]):
            a[--k]=a[--i]
            
        else:
            a[--k]=b[--j]
        
    while (j>0):
        a[--k]=b[--j]
    return a
    
k=abmerge(a,b,m,n) 