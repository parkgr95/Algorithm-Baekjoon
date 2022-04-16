'''
date : 0416
idea : 피사노 주기
피사노 주기 : 피보나치 수를 K로 나눈 나머지는 항상 주기를 갖게된다는 원리
            주기의 길이가 P 일 때, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M을 나눈 나머지와 같습니다.
            M = 10^K 일 때, K > 2 라면, 주기는 항상 15 * 10^(K - 1)
            출처 : https://kyun2da.github.io/2020/08/30/fibonacci/
'''
n = int(input())
mod = 1000000
p = mod // 10 * 15
dp = [0, 1]

for i in range(2, p):
    dp.append((dp[i - 1] + dp[i - 2]) % mod)

print(dp[n % p])