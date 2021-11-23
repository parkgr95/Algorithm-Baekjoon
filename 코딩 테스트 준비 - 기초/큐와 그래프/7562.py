from collections import deque
import sys

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(sx, sy, ex, ey):
    q = deque()
    q.append((sx, sy))
    arr[sx][sy] = 1
    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            print(arr[x][y] - 1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not arr[nx][ny]:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1

for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    sx, sy, = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())
    arr = [[0] * n for _ in range(n)]
    bfs(sx, sy, ex, ey)