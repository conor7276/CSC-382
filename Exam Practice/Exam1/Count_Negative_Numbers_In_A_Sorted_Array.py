
def count_negatives(arr):
    if(not arr):
        return -1
    
    count = 0
    for num in range(len(arr)):
        if(arr[num] > -1):
            return count
        count += 1
    return count

arr = [-101,-99,-54,-21,-3,6,12,19,20,74,92]
print(count_negatives(arr))
print(count_negatives([]))