import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
array = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    array[a][b] = array[b][a] = 1
visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n + 1):
        if not visited[i] and array[v][i] == 1:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start] = False
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n + 1):
            if visited[i] and array[v][i] == 1:
                queue.append(i)
                visited[i] = False
dfs(v)
print()
bfs(v)