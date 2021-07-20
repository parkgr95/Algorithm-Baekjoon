from itertools import combinations
import sys

n = int(sys.stdin.readline())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
m = [i for i in range(n)]
ans = sys.maxsize

for cb in combinations(m, n//2):
    start_sum = 0
    link_sum = 0

    start_member = list(cb)
    link_member = list(set(m) - set(cb))

    start_comb = combinations(start_member, 2)
    link_comb = combinations(link_member, 2)

    for x, y in start_comb:
        start_sum += (s[x][y] + s[y][x])
    for x, y in link_comb:
        link_sum += (s[x][y] + s[y][x])

    ans = min(ans, abs(start_sum - link_sum))

print(ans)