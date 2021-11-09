import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
i, j = 0, 1
tmp = arr[i]
while i < n:
    if tmp == m:
        ans += 1
        tmp -= arr[i]
        i += 1

    if j == n and tmp < m:
        break
    elif tmp < m:
        tmp += arr[j]
        j += 1
    elif tmp > m:
        tmp -= arr[i]
        i += 1
print(ans)
