'''
date : 0415
idea : 페르마의 소정리, 분할 정복
'''
def divide(a, n):
    if n == 1:
        return a % p
    elif n == 2:
        return a * a % p
    else:
        tmp = divide(a, n//2)
        if n % 2:
            return tmp * tmp * a % p
        else:
            return tmp * tmp % p

n, k = map(int, input().split())
p = 1000000007
factorial = [1 for _ in range(n + 1)]

for i in range(2, n + 1):
    factorial[i] = factorial[i - 1] * i % p

a = factorial[n - k] * factorial[k] % p
print(factorial[n] * divide(a, p-2) % p)