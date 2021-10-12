import copy
import sys

def move(dir):
    # 상
    if dir == 0:
        for j in range(n):
            idx = 0
            for i in range(1, n): # 위에서부터
                if B[i][j]:
                    temp = B[i][j]
                    B[i][j] = 0
                    if B[idx][j] == 0: # 옮길 칸이 빈 경우
                        B[idx][j] = temp
                    elif B[idx][j] == temp: # 옮길 칸 값이랑 같을 경우
                        B[idx][j] = temp * 2
                        idx += 1
                    else: # 그대로
                        idx += 1
                        B[idx][j] = temp
    # 하
    elif dir == 1:
        for j in range(n):
            idx = n - 1
            for i in range(n - 2, -1, -1): # 아래에서부터
                if B[i][j]:
                    temp = B[i][j]
                    B[i][j] = 0
                    if B[idx][j] == 0:
                        B[idx][j] = temp
                    elif B[idx][j] == temp:
                        B[idx][j] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        B[idx][j] = temp
    # 우
    elif dir == 2:
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if B[i][j]:
                    temp = B[i][j]
                    B[i][j] = 0
                    if B[i][idx] == 0:
                        B[i][idx] = temp
                    elif B[i][idx] == temp:
                        B[i][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        B[i][idx] = temp
    # 좌
    else:
        for i in range(n):
            idx = n - 1
            for j in range(n - 2, -1, -1):
                if B[i][j]:
                    temp = B[i][j]
                    B[i][j] = 0
                    if B[i][idx] == 0:
                        B[i][idx] = temp
                    elif B[i][idx] == temp:
                        B[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        B[i][idx] = temp
def dfs(cnt):
    global B, ans
    if cnt == 5:
        for i in range(n):
            ans = max(ans, max(B[i]))
        return

    tmp = copy.deepcopy(B)
    for i in range(4):
        move(i)
        dfs(cnt + 1)
        B = copy.deepcopy(tmp)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    B = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    ans = 0
    dfs(0)
    print(ans)