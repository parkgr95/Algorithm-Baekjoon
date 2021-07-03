import sys
input = sys.stdin.readline()
MAX = 100001
d = [0] * max

n = int(input)
for i in range(1, n + 1):
    d[i] = i
    for j in range(1, i):
        if j * j > i:
            break
        d[i] = min(d[i], d[i - j * j] + 1)

print(d[n])