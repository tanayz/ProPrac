# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 23:26:44 2015

@author: tanay
"""
import time
def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1

    return found

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
t=time.time()
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))
print time.time()-t

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
t=time.time()
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
print time.time()-t