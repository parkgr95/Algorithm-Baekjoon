import sys

n = int(sys.stdin.readline().rstrip())
d = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0: # 왼쪽 위일 경우
            left = 0
        else:
            left = d[i-1][j-1]
        if j == i: # 바로 위일 경우
            up = 0
        else:
            up = d[i-1][j]
        d[i][j] = d[i][j] + max(left, up)

print(max(d[n-1]))