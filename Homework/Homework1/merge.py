import time
import random

# Python program for implementation of MergeSort
def mergeSort(arr,swaps):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        swaps += mergeSort(L, swaps)
  
        # Sorting the second half
        swaps += mergeSort(R, swaps)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                #swaps += 1
                i += 1
            else:
                arr[k] = R[j]
                #swaps += 1
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            #swaps += 1
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            #swaps += 1
            j += 1
            k += 1
        
        return swaps

    return 0
        
    
# Code to print the list
  
  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  

def randomArray(size):
    arr = []

    for _ in range(size):
        arr.append(random.randint(0,100))

    #print(arr)
    return arr

# Driver Code
if __name__ == '__main__':

    for i in range(0,10001,1000):
        arr = randomArray(i)
        start = time.time()
        swaps = 0
        swaps = mergeSort(arr,swaps)
        end = time.time()
        print("Time taken for merge sort: ", end-start, " ", "with array size ", i, " and this many swaps " , swaps)

        


