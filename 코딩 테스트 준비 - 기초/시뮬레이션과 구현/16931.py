'''
date : 0415
idea : 구현
'''
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

ans = n * m
for i in range(n):
    for j in range(m):
        if j == 0:
            ans += A[i][j]
        else:
            if A[i][j-1] < A[i][j]:
                ans += A[i][j] - A[i][j-1]

for j in range(m):
    for i in range(n):
        if i == 0:
            ans += A[i][j]
        else:
            if A[i-1][j] < A[i][j]:
                ans += A[i][j] - A[i-1][j]

print(2 * ans)