import sys

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

m, n = map(int, sys.stdin.readline().split())
for i in range(m, n + 1):
    if isPrime(i):
        print(i)

# 회고: 에라토스테네스의 체