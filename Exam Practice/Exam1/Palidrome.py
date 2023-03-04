
def isPalindrome(arr) -> bool:
    back = len(arr) - 1
    front = 0
    for char in range(len(arr)):
        if(arr[back] != arr[front]):
            return False
        
        back -= 1
        front += 1
    return True

def betterPalindrome(arr) -> bool:
    back = len(arr)-1 
    front = 0
    while(front < back):
        if(arr[back] != arr[front]):
            return False
        back-=1
        front+=1

    return True


print(isPalindrome(['a','b','c','b','a']))
print(betterPalindrome(['a','b','c','b','a']))