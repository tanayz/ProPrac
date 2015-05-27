# -*- coding: utf-8 -*-
"""
one unsorted array is given.Find out the index i and j ,j> i for 
which a[j] - a[i] is maximum.perform in linear time complexity
"""

input=[5,15,3,10,20,1,19,0,8,16]
mn=input[0];ix=0;ii=0;mx=input[0]

for i in range(len(input)):
    if mn>input[i]:
        mn=input[i]
        ii=i

for i in range(ii,len(input)):        
    if mx<input[i]:
        mx=input[i]
        ix=i
print 'max difference with j>i is :',mx-mn,'and index for max is',ix,' and for min is',ii
        