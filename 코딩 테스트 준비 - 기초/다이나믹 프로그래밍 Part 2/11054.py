import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
rev = arr[::-1]

inc = [1 for i in range(n)]
dec = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if rev[i] > rev[j]:
            dec[i] = max(dec[i], dec[j]+1)
ans = [0] * n
for i in range(n):
    ans[i] = inc[i] + dec[n-i-1] - 1

print(max(ans))