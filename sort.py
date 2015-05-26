'''Different sorting functions for practice'''

alist = [54,26,93,17,77,31,44,55,20]

def selsort(l):
    for i in range(len(l)-1,0,-1):
        temp=0
        pt=0
        for j in range(0,i):
            if(l[j]>l[j+1] and l[j]>temp):
                temp=l[j]
                pt=j                              
            
        if l[pt]>l[i]:
            l[pt]=l[i]
            l[i]=temp
            print l,i
    return l

print selsort(alist) 

alist = [54,26,93,17,77,31,44,55,20]              

def selsort1(l):
    for i in range(len(l)-1,0,-1):
        pt=0
        for j in range(0,i+1):
            if(l[j]>l[pt]):
                pt=j                              
            
        temp=l[pt]
        l[pt]=l[i]
        l[i]=temp
        print l,i
    return l

print selsort1(alist) 

def mergesort(l):
    print 'Spliting',l
    if len(l)>1:
        mid=len(l)//2
        lefthalf=l[:mid]
        righthalf=l[mid:]
        
        mergesort(lefthalf)
        mergesort(righthalf)
        
        i=0;j=0;k=0
        
        while(i<len(lefthalf) and j<len(righthalf)):
            if lefthalf[i]<righthalf[j]:
                l[k]=lefthalf[i]
                i=i+1
            else: 
                l[k]=righthalf[j]
                j=j+1
            k=k+1
            
        while(i<len(lefthalf)):
            l[k]=lefthalf[i]
            i=i+1
            k=k+1
        while(j<len(righthalf)):
            l[k]=righthalf[j]
            j=j+1
            k=k+1
        print 'Merging',l

alist = [54,26,93,17,77,31,44,55,20]
mergesort(alist)
print(alist)

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)



        

              
