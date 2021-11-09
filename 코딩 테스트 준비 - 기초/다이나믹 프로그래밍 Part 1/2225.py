import sys

n, k = map(int, sys.stdin.readline().split())
d = [[0] * 201 for _ in range(201)]

for i in range(201):
    d[1][i] = 1
    d[2][i] = i + 1
for i in range(3, 201):
    d[i][1] = i
    for j in range(2, 201):
        d[i][j] = (d[i][j - 1] + d[i -1][j]) % 1000000000

print(d[k][n])