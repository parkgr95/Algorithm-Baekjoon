from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == -1:
                if not graph[nx][ny]:
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                elif graph[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return visited[m-1][n-1]

if __name__=="__main__":
    n, m = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(m)]
    visited = [[-1] * n for _ in range(m)]
    visited[0][0] = 0
    print(bfs(0, 0))