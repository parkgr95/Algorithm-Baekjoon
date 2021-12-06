import sys

h, w = map(int, sys.stdin.readline().split())  # 세로, 가로
arr = list(map(int, sys.stdin.readline().split())) # 블록 높이

left = 0
right = w - 1

max_left = arr[left]
max_right = arr[w - 1]

result = 0

# 투포인터
while left < right:
    max_left = max(max_left, arr[left])
    max_right = max(max_right, arr[right])
    # 1. 오른쪽 포인터 최대값이 큰 경우, 왼쪽 빗물 구하기 & 왼쪽 이동
    if max_right >= max_left:
        result += max_left - arr[left]
        left += 1
    else:
    # 2. 왼쪽 포인터 최대값이 큰 경우, 오른쪽 빗물 구하기 & 오른쪽 이동
        result += max_right - arr[right]
        right -= 1

print(result)