from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((1, 0))
    while q:
        s, c = q.popleft()
        if visited[s][s] == -1:
            visited[s][s] = visited[s][c] + 1
            q.append((s, s))
        if s+c <= n and visited[s+c][c] == -1:
            visited[s+c][c] = visited[s][c] + 1
            q.append((s+c, c))
        if s-1 >= 0 and visited[s-1][c] == -1:
            visited[s-1][c] = visited[s][c] + 1
            q.append((s-1, c))

if __name__=="__main__":
    n = int(sys.stdin.readline().rstrip())
    visited = [[-1] * (n+1) for _ in range(n+1)]
    visited[1][0] = 0
    bfs()
    answer = 1e9
    for i in range(n+1):
        if visited[n][i] != -1:
            answer = min(answer, visited[n][i])
    print(answer)