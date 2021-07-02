import sys

def tsp(now, before):
    if dp[now][before]:
        return dp[now][before]
    if before == (1<<n) - 1:
        return path[now][0] if path[now][0] > 0 else sys.maxsize
    cost = sys.maxsize
    for i in range(1, n):
        if not(before>>i) % 2 and path[now][i]:
            tmp = tsp(i, before|(1<<i))
            cost = min(cost, tmp + path[now][i])
    dp[now][before] = cost
    return cost

n = int(sys.stdin.readline())
path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*(1<<n) for _ in range(n)]

print(tsp(0, 1))