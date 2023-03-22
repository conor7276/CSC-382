
import time
import random
import os
import psutil

# Function to find the partition position
def partition(array, low, high, swaps):
  
    # Choose the rightmost element as pivot
    pivot = array[high]
  
    # Pointer for greater element
    i = low - 1
    
    swap_count = 0
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
  
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            swap_count += 1

    #print("arr after pivot ", arr)
    # Swap the pivot element with 
    # e greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    swap_count += 1
    swaps.append(swap_count)
    #print("after partition ", arr)
    # Return the position from where partition is done
    #print(swaps)
    return i + 1
  
# Function to perform quicksort
  
  
def quick_sort(array, low, high, swaps):
    if low < high:
  
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high, swaps)
  
        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1,swaps)
  
        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high,swaps)


  
def randomArray(size):
    arr = []

    for _ in range(size):
        arr.append(random.randint(0,10000))

    #print(arr)
    return arr



# Driver Code
if __name__ == '__main__':

    # for i in range(0,10001,1000):
    #     arr = randomArray(i)
    #     start = time.time()
    #     swaps = []
    #     quick_sort(arr,0,len(arr)-1,swaps)
    #     end = time.time()
    #     print("Time taken for merge sort: ", round(end-start,2), " seconds ", "with array size ", i, " and this many swaps " , sum(swaps))

    process = psutil.Process(os.getpid())
    arr = randomArray(10000)
    start = time.time()
    swaps = []
    quick_sort(arr,0,len(arr)-1,swaps)
    end = time.time()
    print("Time taken for quick sort: ", round(end-start,2), " seconds ", "with array size ", len(arr), " and this many swaps " , sum(swaps))
    print("Memory usage: ", process.memory_full_info().rss / 1000000, " MB")
    

