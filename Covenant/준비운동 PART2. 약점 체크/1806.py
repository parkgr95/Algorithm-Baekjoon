"""
day : 0524
num : 1806
idea : 투 포인터, 부분합
ref :
"""

n, s = map(int, input().split())
tmp = list(map(int, input().split()))

# 접두사 합(Prefix Sum) 배열 계산
arr = [0]
for t in tmp:
    arr.append(t + arr[-1])

ans = 1e9
end = 0
# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    # 구간 합 계산
    while arr[end] - arr[start] < s and end < n:
        end += 1
    # 부분합이 s이상일 때, 길이가 짧으면 바꿔준다.
    if arr[end] - arr[start] >= s:
        if end - start < ans:
            ans = end - start

print(ans if ans != 1e9 else 0)