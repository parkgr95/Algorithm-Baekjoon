import sys

n = int(sys.stdin.readline())
t = []
p = []
d = [0 for _ in range(n + 1)]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    t.append(a)
    p.append(b)

for i in range(n - 1, -1, -1):
    if t[i] + i > n:
        d[i] = d[i + 1]
    else:
        d[i] = max(d[i + 1], p[i] + d[i + t[i]])

print(d[0])