# 완전 탐색
import sys

n = int(sys.stdin.readline())
d = [0] * (n + 1)
array = list(map(int, sys.stdin.readline().split()))

for i in range(2, n + 1):
    for j in range(0, n - 1):
        d[i] = max(d[i], sum(d[j:j + i]))

print(max(d))

# dp
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

s = [a[0]]
for i in range(n - 1):
    s.append(max(s[i] + a[i+1], a[i+1]))

print(max(s))