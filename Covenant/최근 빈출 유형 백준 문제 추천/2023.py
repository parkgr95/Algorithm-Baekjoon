import math

n = int(input())

def isPrime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if(x % i == 0):
            return False
    return True

def dfs(cnt):
    if len(str(cnt)) == n:
        print(cnt)
    for i in range(10):
        temp = int(str(cnt) + str(i))
        if isPrime(temp):
            dfs(temp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)