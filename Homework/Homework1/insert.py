import time
import random
import os
import psutil
def insertionSort(arr):

    start = time.time()
    steps = 0

    for i in range(1, len(arr)):

        key = arr[i]

        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            steps += 1

        arr[j+1] = key
    
    
    end = time.time()
    #print("Time taken to insertion sort of size ", len(arr), " ", end -start, " in ", steps, " steps.")
    return steps

def randomArray(size):
    arr = []

    for _ in range(size):
        arr.append(random.randint(0,100))

    #print(arr)
    return arr



arr = randomArray(10000)
process = psutil.Process(os.getpid())
start = time.time()
swaps = 0
swaps = insertionSort(arr)
end = time.time()
print("Time taken for merge sort: ", round(end-start,2), " seconds ", "with array size ", len(arr), " and this many swaps " , swaps)
print("Memory usage: ", process.memory_full_info().rss / 1000000, " MB")
# for i in range(0, 10001, 1000):
#     arr = randomArray(i)
#     insertionSort(arr)
#print(insertionSort(arr))