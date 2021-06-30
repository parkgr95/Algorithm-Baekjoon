import sys

n, m = map(int, sys.stdin.readline().split())
arr = set(list(map(int, sys.stdin.readline().split())))
array = list(arr).sort()

visited = [False] * len(array)
answer = []

def dfs(depth):
    if depth == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(len(array)):
        if not visited[i]:
            visited[i] = True
            answer.append(array[i])
            dfs(depth + 1)
            visited[i] = False
            answer.pop()

dfs(0)