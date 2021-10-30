from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, s):
    q = deque()
    q.append((x, y, s))
    while q:
        x, y, s = q.popleft()
        if x == n-1 and y == m-1:
            return visited[n-1][m-1][s]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] and s == 1:
                    q.appendleft((nx, ny, 0))
                    visited[nx][ny][0] = visited[x][y][1] + 1
                if not graph[nx][ny] and not visited[nx][ny][s]:
                    q.append((nx, ny, s))
                    visited[nx][ny][s] = visited[x][y][s] + 1
    return -1

if __name__=="__main__":
    n, m = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
    visited = [[[0] * 2 for i in range(m)] for i in range(n)]
    visited[0][0][1] = 1
    print(bfs(0, 0, 1))