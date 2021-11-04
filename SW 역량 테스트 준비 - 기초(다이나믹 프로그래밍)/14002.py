from collections import deque
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
d = [0] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1
print(max(d))
dmax = max(d)
q = deque()
for i in range(n-1, -1, -1):
    if d[i] == dmax:
        q.appendleft(arr[i])
        dmax -= 1
for x in q:
    print(x, end=" ")
