# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:14:12 2015
@author: Tanay
"""
"""9.2 Write a method to sort an array of strings so that all the anagrams are next to each other."""

def strng(s):
    tmp=list(s)
    tmp.sort()
    return "".join(tmp)

def comparestr(s1,s2):
    if strng(s1)==strng(s2):
        print 'strings are anagrams'
    else:
        print 'strings are not anagrams'
        
#comparestr('cinema','iceman')

""" 9.3 Given a sorted array of n integers that has been rotated an unknown number of times, give an O(log n) algorithm that finds an element in the array. You may assume that the array was originally sorted in increasing order.
EXAMPLE:
Input: find 5 in array (15 16 19 20 25 1 3 4 5 7 10 14)
Output: 8 (the index of 5 in the array)"""

input=[15,16,19,20,25,1,3,4,5,7,10,14]
start=0
end=len(input)-1
srch=55
mid=(start+end)//2


while input[mid]< input[mid+1]:
    if input[mid]>input[0]:
        start=mid
    else:
        end=mid
    mid=(start+end)//2

if srch>input[0]:
    start=0
    end=mid
else :
    start=mid+1
    end=len(input)-1


def binarySearch(input, srch,start,end):
    start=start
    end=end
    mid = (start+end)/2
    found=False

    while start<=end and not found :
       mid=(start+end)//2
       if input[mid] == srch:
           found=True
       if srch>input[mid]:
           start=mid+1
       else :
           end=mid+1    
    return found

print binarySearch(input, srch,start,end)



