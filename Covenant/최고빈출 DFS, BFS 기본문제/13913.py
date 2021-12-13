from collections import deque

def path(x):
    arr = []
    for _ in range(time[x] + 1):
        arr.append(x)
        x = move[x]
    print(' '.join(map(str, arr[::-1])))

def bfs(start):
    q = deque([start])
    while q:
        x = q.popleft()
        if x == k:
            print(time[x])
            path(x)
            return
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx < MAX and not time[nx]:
                q.append(nx)
                time[nx] = time[x] + 1
                move[nx] = x

MAX = 100001
n, k = map(int, input().split())
time, move = [0] * MAX, [0] * MAX
bfs(n)