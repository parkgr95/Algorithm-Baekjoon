from collections import deque
import sys

def bfs():
    while q:
        x, y, z = q.popleft() # x: a의 물통의 양, y: b의 물통의 양, z: c의 물통의
        if visited[x][y]: continue
        visited[x][y] = 1
        if x == 0: ans[z] = 1 # 정답
        # x -> y
        if x > b - y: q.append((x + y - b, b, z))
        else: q.append((0, x + y, z))
        # x -> z
        if x > c - z: q.append((x + z - c, y, c))
        else: q.append((0, y, x + z))
        # y -> x
        if y > a - x: q.append((a, y + x - a, z))
        else: q.append((y + x, 0, z))
        # y -> z
        if y > c - z: q.append((x, y + z - c, c))
        else: q.append((x, 0, y + z))
        # z -> x
        if z > a - x: q.append((a, y, z + x - a))
        else: q.append((z + x, y, 0))
        # z -> y
        if z > b - y: q.append((x, b, z + y - b))
        else: q.append((x, z + y, 0))

if __name__ == "__main__":
    a, b, c = map(int, sys.stdin.readline().split())
    visited = [[0] * (b + 1) for _ in range(a + 1)]
    ans = [0 for _ in range(c+1)]

    q = deque()
    q.append((0, 0, c))
    bfs()
    for i in range(c+1):
        if ans[i]: print(i, end=' ')