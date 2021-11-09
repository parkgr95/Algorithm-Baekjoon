import sys
n = int(sys.stdin.readline())
arr = [0] + list(map(int, sys.stdin.readline().split()))
d = [i for i in arr]
d[1] = arr[1]

for i in range(2, n + 1):
   for j in range(1, i // 2 + 1):
      d[i] = max(d[i], d[i-j] + d[j])

print(d[n])
