from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        water()
        qlen = len(q)
        while qlen:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c:
                    if graph[nx][ny] == "." and not visited[nx][ny]:
                        q.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                    elif graph[nx][ny] == 'D':
                        return visited[x][y]
            qlen -= 1
    return "KAKTUS"

def water():
    wlen = len(w)
    while wlen:
        x, y = w.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == ".":
                w.append((nx, ny))
                graph[nx][ny] = "*"
        wlen -= 1

if __name__=="__main__":
    r, c = map(int, sys.stdin.readline().split())
    graph = []
    visited = [[0] * c for i in range(r)]
    q, w = deque(), deque()
    for i in range(r):
        graph.append(list(sys.stdin.readline().rstrip()))
        for j in range(c):
            if graph[i][j] == "D":
                qx, qy = i, j
            elif graph[i][j] == "S":
                q.append((i, j))
                graph[i][j] = "."
                visited[i][j] = 1
            elif graph[i][j] == "*":
                w.append((i, j))
    print(bfs())