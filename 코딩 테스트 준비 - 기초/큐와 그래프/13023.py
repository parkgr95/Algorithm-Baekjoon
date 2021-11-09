import sys

def dfs(idx, number):
    global check
    if number == 4:
        check = True
        return
    for i in graph[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, number + 1)
            visited[i] = False

if __name__=="__main__":
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(n)]
    visited = [False] * n
    check = False

    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(n):
        visited[i] = True
        dfs(i, 0)
        visited[i] = False

    print(1) if check else print(0)