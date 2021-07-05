import sys

n = int(sys.stdin.readline())
arr = [0]
for i in range(n):
    arr.append(int(sys.stdin.readline()))
d = [0]
d.append(arr[1])
if n > 1:
    d.append(arr[1] + arr[2])
for i in range(3, n+1):
    d.append(max(d[i-1], d[i-3] + arr[i-1] + arr[i], d[i-2] + arr[i]))

print(d[n])