'''
date : 0422
idea : bfs
'''
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while True:
                if not (0 <= nx < w and 0 <= ny < h):
                    break
                if B[nx][ny] == '*':
                    break
                if visited[nx][ny] < visited[x][y] + 1:
                    break
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx, ny = nx + dx[i], ny + dy[i]

h, w = map(int, input().split())
B, c = [], []
for i in range(w):
    B.append(list(input()))
    for j in range(h):
        if B[i][j] == 'C':
            c.append((i, j))

(sx, sy), (ex, ey) = c
visited = [[float("inf")] * h for _ in range(w)]
bfs(sx, sy)

print(visited[ex][ey] - 1)