# write a function that finds an element in an array using recursion


def find_element(arr, index, element):
    if(len(arr) == index):
        print("Same size gotta go")
        return False
    elif(arr[index] == element):
        print("Found it: ", element, "found in ", index)
        return True
    else:
        print("Not here")
        return find_element(arr,index+1,element)

    

nums = [1,-4,5,10]
print(len(nums))
print(find_element(nums,0,101))
