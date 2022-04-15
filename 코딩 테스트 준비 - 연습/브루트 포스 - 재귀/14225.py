'''
date : 0415
idea : 그리디 알고리즘
'''
n = int(input())

ans = 0
for i in sorted(list(map(int, input().split()))):
    if ans + 1 < i: break
    ans += i

print(ans+1)