'''
date : 0413
idea : knapsack 알고리즘
'''
n, k = map(int, input().split())
bp = {}
for i in range(1, n + 1):
    bp[i] = list(map(int, input().split()))

dp = [[0] * (k + 1) for _ in range(n + 1)]
# print(dp)

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = bp[i][0], bp[i][1]

        if j < w:  # 현재 허용 무게보다 물건의 무게가 더 무겁다면 넣지 않는다.
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[n][k])