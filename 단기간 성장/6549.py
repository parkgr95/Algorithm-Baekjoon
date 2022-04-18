'''
date : 0418
idea : 스택
'''
from collections import deque

while True:
    arr = list(map(int, input().split()))
    n = arr.pop(0)

    if n == 0:
        break

    q = deque()
    ans = 0

    for i in range(n):
        while len(q) and arr[q[-1]] > arr[i]:
            tmp = q.pop()

            if not len(q):
                w = i
            else:
                w = i - q[-1] - 1
            ans = max(ans, w * arr[tmp])
        q.append(i)

    while len(q):
        tmp = q.pop()

        if not len(q):
            w = n
        else:
            w = n - q[-1] - 1
        ans = max(ans, w * arr[tmp])

    print(ans)