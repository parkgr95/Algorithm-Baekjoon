h, w = map(int, input().split())
B = list(map(int, input().split()))

left, right = 0, w - 1
maxleft, maxright = B[left], B[right]

ans = 0
while left < right:
    maxleft, maxright = max(maxleft, B[left]), max(maxright, B[right])
    if maxleft <= maxright:  # 오른쪽 포인터 최대값이 큰 경우, 왼쪽 빗물 구하기 & 왼쪽 이동
        ans += maxleft - B[left]
        left += 1
    else:  # 왼쪽 포인터 최대값이 큰 경우, 오른쪽 빗물 구하기 & 오른쪽 이동
        ans += maxright - B[right]
        right -= 1

print(ans)

# 회고: 투 포인터 사용!