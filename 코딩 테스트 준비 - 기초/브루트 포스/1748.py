import sys

n = sys.stdin.readline().rstrip()
ans = 0
for i in range(len(n) - 1):
    ans += 9 * (10**i) * (i+1)
ans += (int(n) - (10**(len(n)-1)) + 1) * len(n)
print(ans)