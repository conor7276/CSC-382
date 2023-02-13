
def isPalindrome(arr) -> bool:
    back = len(arr) - 1
    front = 0
    for char in range(len(arr)):
        if(arr[back] != arr[front]):
            return False
        
        back -= 1
        front += 1
    return True

print(isPalindrome(['a','b','c','b']))