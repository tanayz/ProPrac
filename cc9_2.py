# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:14:12 2015

@author: tanay
"""
def strng(s):
    tmp=list(s)
    tmp.sort()
    return "".join(tmp)

def comparestr(s1,s2):
    if strng(s1)==strng(s2):
        print 'strings are anagrams'
    else:
        print 'strings are not anagrams'
        
comparestr('cinema','iceman')