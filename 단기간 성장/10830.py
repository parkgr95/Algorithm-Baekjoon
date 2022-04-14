'''
date : 0414
idea : 분할 정복
'''
def mul(A, B):
    res = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += A[i][k] * B[k][j]
            res[i][j] %= 1000

    return res


def divide(a, b):
    if b == 1:
        return a
    elif b == 2:
        return mul(a, a)
    else:
        tmp = divide(a, b//2)
        if b % 2:
            return mul(mul(tmp, tmp), a)
        else:
            return mul(tmp, tmp)


n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = divide(a, b)
for row in ans:
    for x in row:
        print(x % 1000, end=' ')
    print()