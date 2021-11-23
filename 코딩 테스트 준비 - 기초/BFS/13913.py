import sys
from collections import deque

def path(v):
    arr = []
    temp = v
    for _ in range(time[v] + 1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))

def bfs(start, end):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v == end:
            print(time[v])
            path(v)
            return
        for i in (v - 1, v + 1, v * 2):
            if 0 <= i < MAX and not time[i]:
                time[i] = time[v] + 1
                move[i] = v
                queue.append(i)

MAX = 100001
n, k = map(int, sys.stdin.readline().split())
time = [0] * MAX
move = [0] * MAX
bfs(n, k)