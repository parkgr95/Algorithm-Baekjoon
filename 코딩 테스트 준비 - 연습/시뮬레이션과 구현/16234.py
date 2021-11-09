# pypy3로 제출
from collections import deque
import sys

n, l, r = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
b = a

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    global check
    q = deque()
    q.append([i, j])
    temp = []
    temp.append([i, j])
    num, cnt = 0, 0
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        num += a[x][y]
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny]:
                continue
            if l <= abs(a[nx][ny] - a[x][y]) <= r:
                visited[nx][ny] = True
                q.append([nx, ny])
                temp.append([nx, ny])

    move = num // cnt

    if cnt > 1:
        check = True
        for x, y in temp:
            a[x][y] = move

ans = 0
while True:
    check = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)

    if not check:
        break
    ans += 1

print(ans)