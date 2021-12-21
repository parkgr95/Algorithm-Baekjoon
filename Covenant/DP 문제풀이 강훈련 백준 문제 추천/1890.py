n = int(input())
B = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * n for _ in range(n)]
d[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(d[i][j])
            break
        tmp = B[i][j]
        if j + tmp < n:
            d[i][j + tmp] += d[i][j]
        if i + tmp < n:
            d[i + tmp][j] += d[i][j]
