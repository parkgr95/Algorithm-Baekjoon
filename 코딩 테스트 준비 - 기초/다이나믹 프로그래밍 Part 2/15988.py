import sys

d = [0] * (1000001)
d[1] = 1
d[2] = 2
d[3] = 4
for i in range(4, 1000001):
    d[i] = (d[i - 1] + d[i - 2] + d[i - 3]) % 1000000009

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    print(d[n])