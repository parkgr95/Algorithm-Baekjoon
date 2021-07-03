import sys
from collections import deque

def bfs(start, end):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        if v == end:
            print(time[v])
            return
        for i in (v - 1, v + 1, v * 2):
            if 0 <= i < MAX and not time[i]:
                time[i] = time[v] + 1
                print(time[i])
                queue.append(i)

MAX = 100001
n, k = map(int, sys.stdin.readline().split())
time = [0] * MAX

bfs(n, k)
