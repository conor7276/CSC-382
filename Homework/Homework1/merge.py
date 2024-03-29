import time
import random
import os
import psutil
# Python program for implementation of MergeSort
def mergeSort(arr,swaps):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
        #print("Middle is here at index: ", mid, ' ', arr, end=' ')
        # Dividing the array elements
        L = arr[:mid]
        #print("Left starts at 1 and goes to ", len(L), " ", L, end =' ')
        # into 2 halves
        R = arr[mid:]
        #print("Right starts at ", mid + 1, " and goes until ", len(arr), ' ', R, sep='')
  
        # Sorting the first half
        swaps = mergeSort(L,swaps) + mergeSort(R,swaps)
        #print("Left Merge ", swaps)
        # Sorting the second half
        
        #print("Right Merge ",swaps)
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                swaps += 1
                i += 1
            else:
                arr[k] = R[j]
                swaps += 1
                j += 1
            #print("While and ",swaps)
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            swaps += 1
            i += 1
            k += 1
        #print("while i ",swaps)
        while j < len(R):
            arr[k] = R[j]
            swaps += 1
            j += 1
            k += 1
        #print("while j ",swaps)
        return swaps
    #print("arr < 1" ,swaps)
    return 0
        
    
# generate random numbers for array
def randomArray(size):
    arr = []

    for _ in range(size):
        arr.append(random.randint(0,10000))

    #print(arr)
    return arr

# Driver Code

# code for looping from array sizes 0 to 10000
# for i in range(0,10001,1000):
#     arr = randomArray(i)
#     start = time.time()
#     swaps = 0
#     swaps = mergeSort(arr,swaps)
#     end = time.time()
#     print("Time taken for merge sort: ", round(end-start,2), " seconds", "with array size ", i, " and this many swaps " , swaps)

# code used for comparisons
process = psutil.Process(os.getpid())
arr = randomArray(10000)
start = time.time()
swaps = 0
swaps = mergeSort(arr,swaps=0)
end = time.time()
print("Time taken for merge sort: ", round(end-start,2), " seconds ", "with array size ", len(arr), " and this many swaps " , swaps)
print("Memory usage: ", process.memory_full_info().rss / 1000000, " MB")


        


