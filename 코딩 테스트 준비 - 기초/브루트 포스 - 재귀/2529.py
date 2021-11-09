import sys

k = int(sys.stdin.readline().rstrip())
op = sys.stdin.readline().split()
visited = [False] * 10
max_, min_ = "", ""

def check(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True

def solve(cnt, s):
    global max_, min_
    if cnt == k + 1:
        if not len(min_):
            min_ = s
        else:
            max_ = s
        return
    for i in range(10):
        if not visited[i]:
            if cnt == 0 or check(s[-1], str(i), op[cnt - 1]):
                visited[i] = True
                solve(cnt + 1, s + str(i))
                visited[i] = False

solve(0, "")
print(max_)
print(min_)

# 회고: 재귀에서 포문을 사용하여 모든 케이스 체크. visited로 중복 판별