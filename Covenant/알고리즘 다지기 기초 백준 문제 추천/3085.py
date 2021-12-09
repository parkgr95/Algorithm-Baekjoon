def check(B):
    cnt = 1
    for i in range(n):
        tmp_r, tmp_c = 1, 1
        for j in range(n - 1):
            if B[i][j] == B[i][j + 1]:
                tmp_c += 1
            else:
                cnt = max(cnt, tmp_c)
                tmp_c = 1
            if B[j][i] == B[j + 1][i]:
                tmp_r += 1
            else:
                cnt = max(cnt, tmp_r)
                tmp_r = 1
        cnt = max(cnt, tmp_r, tmp_c)
    return cnt

n = int(input())
B = [list(input()) for _ in range(n)]
ans = check(B)
for i in range(n):
    for j in range(n - 1):
        if B[i][j] != B[i][j + 1]:
            B[i][j], B[i][j + 1] = B[i][j + 1], B[i][j]
            ans = max(ans, check(B))
            B[i][j], B[i][j + 1] = B[i][j + 1], B[i][j]
        if B[j][i] != B[j + 1][i]:
            B[j][i], B[j + 1][i] = B[j + 1][i], B[j][i]
            ans = max(ans, check(B))
            B[j][i], B[j + 1][i] = B[j + 1][i], B[j][i]
print(ans)