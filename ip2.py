'''http://stackoverflow.com/questions/12232930/finding-out-the-minimum-difference-between-elements-in-an-arrays'''

import time
#import numpy as np

#input=np.arange(20000)
#np.random.shuffle(input)

input = [5,13,8,1,17,23,28,36,42,50,55]

mx=10
mn=10

t=time.time()
for i in range(len(input)): #O(n)
    if(mx<input[i]):
        mx=input[i]
    if(mn>input[i]):
        mn=input[i]
#print mx,mn,time.time()-t

bola = [False]*(mx-mn+1)

for i in range(len(input)):
    bola[input[i]-mn]=True


k=0;p=0;c=0;pm=len(bola)
   
for i in range(len(bola)):
    if bola[i]==True:
         if c>0:   
            p=i-k
            if p<pm:
                pm=p
         k=i;c=1;
         
         
print 'minimum difference :',pm


#for i in range(len(bola)-1):  
#    bola[]