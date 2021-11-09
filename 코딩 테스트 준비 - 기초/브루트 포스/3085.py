import sys

# 최대 갯수
def check(arr):
    n = len(arr)
    cnt = 1
    for i in range(n):
        tmp_r, tmp_c = 1, 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                tmp_c += 1
            else:
                cnt = max(cnt, tmp_c)
                tmp_c = 1
            if arr[j][i] == arr[j+1][i]:
                tmp_r += 1
            else:
                cnt = max(cnt, tmp_r)
                tmp_r = 1
        cnt = max(cnt, tmp_r, tmp_c)
    return cnt

n = int(sys.stdin.readline().strip())
arr = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]

ans = check(arr)
for i in range(n):
    for j in range(n-1):
        # 열 교환
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            ans = max(ans, check(arr))
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        # 행 교환
        if arr[j][i] != arr[j+1][i]:
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
            ans = max(ans, check(arr))
            arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
print(ans)