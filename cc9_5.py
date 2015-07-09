# -*- coding: utf-8 -*-
"""9.5 Given a sorted array of strings which is interspersed with empty strings, write a method to find the location of a given string.
Example: find "ball" in ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""] will return 4
Example: find "ballcar" in ["at", "", "", "", "", "ball", "car", "", "", "dad", "", ""] will return -1"""

input=["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
srch="b0ll"

def string_search(srch, input):
    start=0
    end=len(input)-1
    mid = (start+end)/2
    found=False
    
    while start<=end and not found :
       mid=(start+end)//2
       while input[mid]=="":
         mid=mid+1 
       if input[mid] == srch:
           found=True
       if srch>input[mid]:
           start=mid+1
       else :
           end=mid+1    
    return found

         
string_search(srch, input)

"""
9.6 Given a matrix in which each row and each column is sorted, write a method to find an element in it.
"""

