# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:23:44 2015
@author: uszllmd
"""
def rtarr(alist,k):
    '''How to rotate an array with O(n)'''
    temp=[None] * (k+1)
    for i in range(k,0,-1):
        temp[i]=alist.pop()
    temp=temp[1:]+alist
    return temp

rtarr.__doc__,rtarr([1,2,3,4,5,6,7,8,9,10,11,12],4)


def rdarr(alist):
    '''Remove duplicates from sorted array'''
    temp={}
    for x in range(len(alist)):
        if x not in temp.keys():
            temp[alist[x]]=1
    return temp.keys()

rdarr.__doc__,rdarr([1,2,3,3,6,6,9,9,9,10,12,12])


def loarr(alist):
    '''Longest Substring Without Repeating Characters'''
    st=list(set(alist))
    hs={}
    for x in range(len(st)):
        hs[st[x]]=1
    for x in range(len(alist)):
        hs[alist[x]]+=1
    
    for x in hs.keys():
        if hs[x]==max(hs.values()):
            return x,hs[x]
    
loarr.__doc__,loarr(list('aaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbcccccccccccdddddeeeeeeeeeeeefffffffffffffffff'))