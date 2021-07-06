# 이진 탐색
import sys

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end)//2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
m = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))

for x in s:
    answer = binary_search(a, x, 0, n-1)
    print(answer)