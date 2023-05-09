# import psutil
# import os

def fib(n): # normal recursive solution
    if n == 0 :
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def fibTopDown(n): # top down recursion + memoization
    def fibTopDownHelper(n,fibs):
        if n == 0: # base cases
            return 0
        if n <= 2:
            return 1
        if fibs[n] > 0:
            return fibs[n]
        fibs[n] = fibTopDownHelper(n-1,fibs) + fibTopDownHelper(n-2, fibs)
        return fibs[n]
    
    fibs = {}
    return fibTopDownHelper(n,fibs)


def fibBottomUpForward(n): # bottom up dynamic programming tabulation. Forward.
    if n == 0:
        return 0
    if n <= 2:
        return 1
    dp = {}
    dp[0] = 0
    dp[1] = 1
    for i in range(n):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


def fibBottomUpBackwards(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    
    dp = {}
    dp[0] = 0
    dp[1] = 1
    for i in range(n):
        dp[i+1] += dp[i] # dp[i] is already solved, use it to find another problem
        dp[i+2] += dp[i]
    return n

def main():
    print(fib(4))
    print(fibTopDown(4))
    print(fibBottomUpForward(4))


if __name__  == '__main__':
    main()




