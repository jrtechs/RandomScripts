
# coding: utf-8

# # 1 Best cases

# **1.1** Bubble sort

# The short version of Bubble sort is given in the online book:  
# https://runestone.academy/runestone/static/FIT5211/SortSearch/TheBubbleSort.html  
# At every iteration, it detects whether an exchange has been made, and only continues iteration if that is the case. Given a sorted list, the first iteration will make no exchange, thus no other iteration will be performed, and only the inner loop will actually iterate over the entire list. The running time in that case is thus $O(n)$. 

# **1.2** Selection sort

# After every pass of selection sort, the only thing we know is that one more item is now in place. The algorithm has no way of knowing and thus using the fact that the list is already sorted. The algorithm will thus perform the whole $O(n^2)$ operations, as in the worst case.

# **1.3** Merge sort

# Merge splits the input list into two, without looking at its contents. the contents are only looked at upon merging, after every item in the list has been split into a sublist of size 1. At this point, all merging operations still need to happen. In this case, the running time is thus also $O(n \log{n})$.

# # 2 Merge sort without slicing

# In[1]:


#start is the index of the first item
#end is the index past the the last item
def indexMergeSort(alist, start = None, end = None):
    if start == None:
        start = 0
    if end == None:
        end = len(alist)  
    #note that the print operations still use slicing for convenience
    #print("Input: ",alist[start:end])
    
    length = end - start
    if length > 1:
        #print("Splitting ",alist[start:end])
        mid = start + length//2
        
        indexMergeSort(alist, start, mid)
        indexMergeSort(alist, mid, end)

        i=start # index for the left part of the list
        j=mid # index for the right part of the list
        #we use a temporary list
        templist = [None] * (length)
        k = 0 #index for the temp list
        while i < mid and j < end:
            if alist[i] < alist[j]:
                templist[k] = alist[i]
                i=i+1
            else:
                #we swap
                templist[k] = alist[j]
                j=j+1
            k=k+1

        while i < mid:
            templist[k] = alist[i]
            i=i+1
            k=k+1

        while j < end:
            templist[k]=alist[j]
            j=j+1
            k=k+1
        
        #we copy the results
        for k in range(length):
            alist[start+k] = templist[k]
            
        #print("Merging ",alist[start:mid], alist[mid:end])

alist = [54,26,93,17,77,31,44,55,20]
indexMergeSort(alist)
print(alist)


# # 3 Benchmarking sorting algorithms

# In[2]:


import random

def generatelist(n, lower = 0, upper = 1000, seed = 0):
    #https://docs.python.org/3/library/random.html
    random.seed(seed)
    l = [None] * n
    for i in range(0,n):
        l[i] = random.randrange(lower, upper)
    return l


# In[3]:


print(generatelist(10))


# Below we have copied the sorting functions from the online book:

# In[4]:


def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


# In[5]:


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1


# In[6]:


def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp


# In[7]:


def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue


# In[8]:


def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      #print("After increments of size",sublistcount,
      #                             "The list is",alist)

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue


# In[9]:


def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)


# In[10]:


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

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
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


# Now we benchmark them:

# In[11]:


sorting_algorithms = [bubbleSort, shortBubbleSort, selectionSort,                      insertionSort, shellSort, mergeSort,                      indexMergeSort, quickSort]
#matplotlib.org/gallery/lines_bars_and_markers/line_styles_reference.html
styles = {}
styles[bubbleSort] = "r-"
styles[shortBubbleSort] = "r:"
styles[selectionSort] = "y-"
styles[insertionSort] = "g-"
styles[shellSort] = "g:"
styles[mergeSort] = "b--"
styles[indexMergeSort] = "b:"
styles[quickSort] = "y--"


# In[19]:


from timeit import default_timer as timer
import datetime
# matplotlib may need to be installed separately
import matplotlib.pyplot as plt 

def computeandplot(sorting_algorithms):
    step = 100
    nsamples = 100
    samples = range(0, nsamples)
    timelimit = 0.05 #seconds, per run
    totaltime = 0
    print("Maximum computing time:",           str(datetime.timedelta(seconds=            timelimit*nsamples*len(sorting_algorithms))))
    for sortalgo in sorting_algorithms:
            attimelimit = False
            times = [timelimit for _ in samples]
            for i in samples:
                if i == 0:
                    times[i] = 0
                    continue
                n = step * i
                if attimelimit == False:
                    l = generatelist(n)
                    start = timer()
                    sortalgo(l)
                    end = timer()
                    times[i] = end - start
                    totaltime += times[i]
                    if times[i] > timelimit:
                        times[i] = timelimit
                        attimelimit = True

            plt.plot(samples, times,                      styles[sortalgo],                      label=sortalgo.__name__)
    print("Actual computing time:", str(datetime.timedelta(seconds=int(totaltime))))
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xlabel("list size / {}".format(step))
    plt.ylabel("time in seconds")
    plt.show()

computeandplot(sorting_algorithms)


# # 4 Sorting small integers

# **4.1**

# In[13]:


def countsort(alist):
    maxv = max(alist)
    l = [0]*(maxv+1)
    for i in alist:
        l[i] += 1
    
    k = 0
    for i in range(0, len(alist)):
        while l[k] == 0:
            k += 1 # we count the number of values = k in alist
        alist[i] = k
        l[k] -= 1


# In[14]:


alist = [54,26,93,17,77,31,44,55,20]
countsort(alist)
print(alist)


# **4.2**

# In[15]:



import math

DEFAULT_BUCKET_SIZE = 5

def bucketsort(array=alist, bucketSize=DEFAULT_BUCKET_SIZE):
  if len(array) == 0:
    return array

  # Determine minimum and maximum values
  minValue = array[0]
  maxValue = array[0]
  for i in range(1, len(array)):
    if array[i] < minValue:
      minValue = array[i]
    elif array[i] > maxValue:
      maxValue = array[i]

  # Initialize buckets
  bucketCount = math.floor((maxValue - minValue) / bucketSize) + 1
  buckets = []
  for i in range(0, bucketCount):
    buckets.append([])

  # Distribute input array values into buckets
  for i in range(0, len(array)):
    buckets[math.floor((array[i] - minValue) / bucketSize)].append(array[i])

  # Sort buckets and place back into input array
  array = []
  for i in range(0, len(buckets)):
    insertion_sort(buckets[i])
    for j in range(0, len(buckets[i])):
      array.append(buckets[i][j])

  return array


# In[16]:


def default_compare(a, b):
   if a < b:
     return -1
   elif a > b:
     return 1
   return 0


# In[17]:



def insertion_sort(array):
  for i in range(1, len(array)):
    item = array[i]
    indexHole = i
    while indexHole > 0 and default_compare(array[indexHole - 1], item) > 0:
      array[indexHole] = array[indexHole - 1]
      indexHole -= 1
    array[indexHole] = item
  return array


# In[18]:


new_sorting_algorithms = [bucketsort, indexMergeSort, quickSort]
styles[bucketsort] = "g--"
computeandplot(new_sorting_algorithms)

