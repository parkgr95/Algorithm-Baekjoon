'''
date : 0414
idea : 분할 정복
'''
def divide(a, n):
    if n == 1:
        return a % c
    elif n == 2:
        return a * a % c
    else:
        tmp = divide(a, n//2)
        if n % 2:
            return tmp * tmp * a % c
        else:
            return tmp * tmp % c

a, b, c = map(int, input().split())
print(divide(a, b))