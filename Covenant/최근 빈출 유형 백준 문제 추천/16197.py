from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        x1, y1, x2, y2, cnt = q.popleft()
        if cnt >= 10:
            return -1
        for i in range(4):
            nx1, ny1, nx2, ny2 = x1 + dx[i], y1 + dy[i], x2 + dx[i], y2 + dy[i]
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                if B[nx1][ny1] == "#":
                    nx1, ny1 = x1, y1
                if B[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                q.append((nx1, ny1, nx2, ny2, cnt + 1))
            elif 0 <= nx1 < n and 0 <= ny1 < m:
                return cnt + 1
            elif 0 <= nx2 < n and 0 <= ny2 < m:
                return cnt + 1
            else:
                continue
if __name__ == "__main__":
    n, m = map(int, input().split())
    q = deque()
    B = []
    temp = []
    for i in range(n):
        B.append(list(input().strip()))
        for j in range(m):
            if B[i][j] == "o":
                temp.append((i, j))
    q.append((temp[0][0], temp[0][1], temp[1][0], temp[1][1], 0))
    print(bfs())