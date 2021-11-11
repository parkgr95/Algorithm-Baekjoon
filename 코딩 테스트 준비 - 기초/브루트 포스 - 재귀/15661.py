from itertools import combinations
import sys

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 10**8
for i in range(1, n//2 + 1):
    tmp = 10**8
    for c in combinations(range(n), i):
        start = [*c]
        link = list(set(range(n)) - set(start))
        s_sum, l_sum = 0, 0
        for j in range(n-1):
            for k in range(n-1):
                try:
                    s_tmp = arr[start[j]][start[k]]
                except IndexError:
                    s_tmp = 0
                try:
                    l_tmp = arr[link[j]][link[k]]
                except IndexError:
                    l_tmp = 0
                s_sum += s_tmp
                l_sum += l_tmp

        tmp = min(tmp, abs(s_sum - l_sum))
    ans = min(ans, tmp)

print(ans)