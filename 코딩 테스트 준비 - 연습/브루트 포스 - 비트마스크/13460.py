from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
B = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if B[i][j] == 'R':
            rx, ry = i, j
        elif B[i][j] == 'B':
            bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, dx, dy):
    cnt = 0
    while B[x+dx][y+dy] != '#' and B[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])
            if B[nbx][nby] != 'O':
                if B[nrx][nry] == 'O':
                    return depth
                if nrx == nbx and nry == nby:
                    if rcnt > bcnt:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, depth + 1))
    return -1

print(bfs(rx, ry, bx, by))