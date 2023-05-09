import time

def climbStairs(n):
    def climbStairsHelper(n):
        if(n==0):
            return 0
        if(n==1):
            return 1
        if(n==2):
            return 2
        
        return climbStairsHelper(n-1) + climbStairsHelper(n-2)
    
    return climbStairsHelper(n)

start = time.time()
 
#print(climbStairs(40), start - time.time())
del start
#Optimal solution using hash table to save runtime instead of repeating recursive steps
def climbStairsDPRecursive(n):
    stairs = {}
    def climbStairsHelperDP(n,stairs):
        if(n == 0):
            return 0
        if(n == 1):
            return 1
        if(n == 2):
            return 2
        if(n not in stairs):
            stairs[n] = climbStairsHelperDP(n-1, stairs) + climbStairsHelperDP(n-2, stairs)
            return stairs[n]
        else:
            return stairs[n]
    
    return climbStairsHelperDP(n,stairs)

start = time.time()
print(climbStairsDPRecursive(4), start - time.time())
del start


def climbStairsDP(n):
    stairs = {}
    # base cases
    stairs[0] = 0
    stairs[1] = 1
    stairs[2] = 2
    total = 0
    for i in range(n):
        if(i in stairs):
            total += stairs[i]
        else:
            temp_total = 0
            j = i-2
            for j in range(i):
                temp_total += stairs[j]
            stairs[i] = temp_total
            total += stairs[i]

    return total

print(climbStairsDP(4))