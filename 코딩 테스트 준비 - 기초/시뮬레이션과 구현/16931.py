n, m = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 2 * n * m

for x in range(1, n - 1):
    for y in range(1, m - 1):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if B[x][y] - B[nx][ny] > 0:
                ans += B[x][y] - B[nx][ny]

print(2 * ans)