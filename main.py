from collections import deque
import sys

n, l, r = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if l <= abs(a[nx][ny] - a[x][y]) <= r:
                    q.append([nx, ny])
                    visited[nx][ny] = True
cnt = 0
num = 0
check = False
visited = [[False] * n for _ in range(n)]
bfs(0,0)
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            cnt += 1
            num += int(a[i][j])
        a[i][j] = num // cnt

print(a)