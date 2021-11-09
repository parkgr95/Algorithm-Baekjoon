import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

visited = [False] * n
answer = []

def dfs(depth, index):
    if depth == m:
        print(" ".join(map(str, answer)))
        return
    last = 0
    for i in range(index, n):
        if not visited[i] and last != array[i]:
            answer.append(array[i])
            last = array[i]
            dfs(depth + 1, i)
            visited[i] = True
            answer.pop()
            visited[i] = False
dfs(0, 0)