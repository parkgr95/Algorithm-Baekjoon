from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, color):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and B[nx][ny] == color and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt

m, n = map(int, input().split())
B = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

white, blue = 0, 0
for i in range(n):
    for j in range(m):
        if B[i][j] == 'W' and not visited[i][j]:
            white += bfs(i, j, 'W')**2
        elif B[i][j] == 'B' and not visited[i][j]:
            blue += bfs(i, j, 'B') ** 2

print(white, blue)

# 입력값이 가로인지 세로인지 확인할 것!