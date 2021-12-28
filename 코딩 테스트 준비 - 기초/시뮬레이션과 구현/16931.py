n, m = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(n)]

ans = n * m
for i in range(n):
    for j in range(m):
        if i == 0:
            ans += B[j][i]
        if j == 0:
            ans += B[i][j]
        else:
            if B[i][j - 1] < B[i][j]:
                ans += B[i][j] - B[i][j - 1]
            if B[j][i - 1] < B[j][i]:
                ans += B[j][i] - B[j][i - 1]

print(2 * ans)