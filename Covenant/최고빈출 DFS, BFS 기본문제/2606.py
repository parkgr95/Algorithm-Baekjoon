from collections import deque

n = int(input())
B = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(int(input())):
    i, j = map(int, input().split())
    B[i][j], B[j][i] = 1, 1
visited = [False] * (n + 1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    cnt = 0
    while q:
        v = q.popleft()
        for i in range(1, n + 1):
            if not visited[i] and B[v][i]:
                q.append(i)
                visited[i] = True
                cnt += 1
    return cnt

print(bfs(1))