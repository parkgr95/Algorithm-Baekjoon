from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and B[nx][ny] == 1:
                q.append((nx, ny))
                B[nx][ny] = B[x][y] + 1

if __name__ == "__main__":
    n, m = map(int, input().split())
    B = [list(map(int, input())) for _ in range(n)]
    bfs()
    print(B[n - 1][m - 1])