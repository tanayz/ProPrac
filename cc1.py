# -*- coding: utf-8 -*-
'''Misclaneous string programs'''


import time
import numpy as np


#Performing reverse a string

name=list('Tanay')
rname=[]
for l in range(len(name)):
    rname.append(name[len(name)-l-1])

print 'The reverse of string',''.join(name),'is',''.join(rname )

#Check uniqueness of a string

def isunq(name):
    uchk={}
    lname=list(name)
    for l in range(len(lname)):
        if (lname[l] in uchk.keys()):
            return False
        else:
           uchk[lname[l]]=True
    return True 

def isunq2(name):
  if(len(name))!=len(set(name)):
      return False
  return True
 
isunq("Tanay") 
#Remove duplicates from a string

def delunq(name):
    uchk={}
    lname=list(name)
    for l in range(len(lname)):
        if (lname[l] in uchk.keys()):
            lname[l]=''            
        else:
           uchk[lname[l]]=True
    print 'Deduplicated string is:',''.join(lname)

delunq("Tanay")
#1.4:Write a method to decide if two strings are anagrams or not.

def anagram(str1,str2):
    lstr1=list(str1);lstr2=list(str2)
    lstr1.sort();lstr2.sort()
    for i in range(len(lstr1)):
        if(lstr1[i]!=lstr2[i]):
            return False
    return True
 
    
'''1.7 Write an algorithm such that if an element in an MxN matrix is 0, 
    its entire row and column is set to 0. ;''' 
  
def mnary():
     x = np.array([[1, 0, 3], [4, 5, 6]], np.int32);
     i=0;j=0 
     for i in range(len(x[:,j])):
         for j in range(len(x[i,:])):
             if(x[i,j]==0):
                 x[i,:]=0;x[:,j]=0
                 return x
     
     return x
mnary()                 
              
'''1.8 Assume you have a method isSubstring which checks if one word is a substring of another. 
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to 
isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”).'''  

#ls.insert(0,ls.pop())

def issubstring(s1,s2):
    if s1.find(s2)==-1:
        return False
    return True

def isrotate(s1,s2):
    ls1=list(s1);ls2=list(s2)
    for i in range(len(ls2)):   
        ls2.insert(0,ls2.pop())
        if((ls2[0]==ls1[0])&(ls2[len(ls2)-1]==ls1[len(ls1)-1])):
            if(issubstring(''.join(ls1),''.join(ls2))):
                return True
    return False


  
  
#Computation
test=['Tanay', 'Arnab', 'Sumir', 'Samir', 'Debasree', 'Rina', 'Tanmoy', 'Kalyani','Peter','Moly',
      'Dev','Eugene','Sarah','Kate','Aiden']

t=time.time();
for i in range(len(test)):
    isunq(test[i]);
print 'Computation time for isunique:',time.time()-t

t=time.time();
for i in range(len(test)):
    isunq2(test[i]);
print 'Computation time for isunique2:',time.time()-t




