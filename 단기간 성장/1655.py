'''
date : 0413
idea : heap 구조
'''
import sys
import heapq

left, right = [], []
ans = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left, (-n, n))
    else:
        heapq.heappush(right, (n, n))

    if right and left[0][1] > right[0][0]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[0]
        heapq.heappush(left, (-right_value, right_value))
        heapq.heappush(right, (left_value, left_value))

    ans.append(left[0][1])

for a in ans:
    print(a)