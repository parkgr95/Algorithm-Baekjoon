"""
day : 0523
num : 14888
idea : dfs
ref : if 조건문에 대해 깊게 생각해볼것
"""

n = int(input())
arr = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))
max_, min_, = -int(1e9), int(1e9)

def dfs(now, i):
    global max_, min_, add, sub, mul, div
    if i == n:
        max_, min_ = max(max_, now), min(min_, now)
        return

    if add:
        add -= 1
        dfs(now + arr[i], i + 1)
        add += 1
    if sub:
        sub -= 1
        dfs(now - arr[i], i + 1)
        sub += 1
    if mul:
        mul -= 1
        dfs(now * arr[i], i + 1)
        mul += 1
    if div:
        div -= 1
        dfs(int(now / arr[i]), i + 1)
        div += 1

dfs(arr[0], 1)
print(max_)
print(min_)