from collections import deque

def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for i in range(1, n + 1):
        if not visited[i] and B[start][i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    visited[start] = False
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if visited[i] and B[v][i]:
                q.append(i)
                visited[i] = False

if __name__ == "__main__":
    n, m, v = map(int, input().split())
    B = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        B[a][b], B[b][a] = 1, 1
    visited = [False] * (n + 1)

    dfs(v)
    print()
    bfs(v)