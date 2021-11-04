import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = [[0] * n for _ in range(2)]

d[0][0] = a[0]
if n > 1:
    ans = -1e9
    for i in range(1, n):
        d[0][i] = max(d[0][i - 1] + a[i], a[i])
        d[1][i] = max(d[0][i - 1], d[1][i - 1] + a[i])
        ans = max(ans, d[0][i], d[1][i])
    print(ans)
else:
    print(d[0][0])