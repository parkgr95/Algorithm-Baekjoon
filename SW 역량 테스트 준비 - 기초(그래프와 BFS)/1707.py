from collections import deque
import sys

def bfs(start):
    visited[start] = 1
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = -visited[v]
                q.append(i)
            else:
                if visited[i] == visited[v]:
                    return False
    return True

if __name__ == '__main__':
    k = int(sys.stdin.readline())
    for _ in range(k):
        v, e = map(int, sys.stdin.readline().split())
        graph = [[] for _ in range(v+1)]
        visited = [0] * (v + 1)
        check = True

        for _ in range(e):
            a, b = map(int, sys.stdin.readline().split())
            graph[a].append(b)
            graph[b].append(a)

        for i in range(1, v+1):
            if not visited[i]:
                if not bfs(i):
                    check = False
                    break

        print("YES" if check else "NO")