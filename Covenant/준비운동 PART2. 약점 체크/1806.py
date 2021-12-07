n, s = map(int, input().split())
array = list(map(int, input().split()))

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for a in array:
    sum_value += a
    prefix_sum.append(sum_value)

answer = 1000000001
end = 1
# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    # 구간 합 계산
    while prefix_sum[end] - prefix_sum[start] < s and end < n:
        end += 1
    # 부분합이 s이상일 때, 길이가 짧으면 바꿔준다.
    if prefix_sum[end] - prefix_sum[start] >= s:
        if end - start < answer:
            answer = end - start

if answer != 1000000001:
    print(answer)
else:
    print(0)

# 구간합 & 부분합