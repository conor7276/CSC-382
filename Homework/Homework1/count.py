import time
import random
import os
import psutil


def count_sort(arr):
    max_element = int(max(arr))
    min_element = int(min(arr))
    range_of_elements = max_element - min_element + 1
    # Create a count array to store count of individual
    # elements and initialize count array as 0
    count_arr = [0 for _ in range(range_of_elements)]
    output_arr = [0 for _ in range(len(arr))]
    print("Create buckets with count array: ", count_arr)
    print("Output arr: ", output_arr)
    # Store count of each character
    for i in range(0, len(arr)):
        count_arr[arr[i]-min_element] += 1
    print("Count number of times each number appears buckets ", count_arr)
    # Change count_arr[i] so that count_arr[i] now contains actual
    # position of this element in output array
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i-1]
    print("Add elements together elements: ", count_arr)
    # Build the output character array
    for i in range(len(arr)-1, -1, -1):
        output_arr[count_arr[arr[i] - min_element] - 1] = arr[i]
        count_arr[arr[i] - min_element] -= 1
    print("Create output array: ", output_arr)
    print("Count used: ", count_arr)
    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(0, len(arr)):
        arr[i] = output_arr[i]
    print("Return: ", arr)
    return arr
 
def randomArray(size):
    arr = []

    for _ in range(size):
        arr.append(random.randint(0,1000))

    #print(arr)
    return arr

# Driver code
if __name__ == '__main__':
    process = psutil.Process(os.getpid())
    arr = randomArray(10)
    start = time.time()
    ans = count_sort(arr)
    end = time.time()
    print("Time taken for Counting Sort: ", round(end-start,2), " seconds with array of size ", len(arr))
    print("Memory usage: ", process.memory_full_info().rss / 1000000, " MB")
    print(str(ans))