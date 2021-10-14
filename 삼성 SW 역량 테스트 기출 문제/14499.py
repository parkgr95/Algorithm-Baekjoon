import sys

def move(dir):
    if dir == 1: # 동
        # 위, 오른, 왼, 아래 -> 오른, 아래, 위, 왼
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif dir == 2: # 서
        # 위, 오른, 왼, 아래 -> 왼, 위, 아래, 오른
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif dir == 3: # 북
        # 위, 앞, 뒤, 아래 -> 앞, 아래, 위, 뒤
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    else: # 남
        # 위, 앞, 뒤, 아래 -> 뒤, 위, 아래, 앞
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

if __name__ == '__main__':
    n, m, x, y, k = map(int, sys.stdin.readline().split())
    B = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    op = list(map(int, sys.stdin.readline().split()))

    # 위, 앞, 오른, 왼, 뒤, 아래
    dice = [0, 0, 0, 0, 0, 0, 0]

    # 동, 서, 북, 남
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]

    for i in op:
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            x, y = nx, ny
            move(i)
            if B[x][y] != 0:
                dice[6] = B[x][y]
                B[x][y] = 0
            else:
                B[x][y] = dice[6]
            print(dice[1])