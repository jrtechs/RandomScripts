
# coding: utf-8

# In[1]:


#Merge Slot Without Slicing
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

