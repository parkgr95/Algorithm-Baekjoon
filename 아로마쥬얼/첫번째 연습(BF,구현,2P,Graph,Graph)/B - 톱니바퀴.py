# 0731
# 톱니바퀴
# idea: 구현 문제. deque를 써서 rotate를 해결해주고, 회전하는 기어의 왼쪽 오른쪽 거이들을 조건에 따라 회전시킨다.
import sys
from collections import deque

gears = [deque(map(int, sys.stdin.readline().strip())) for _ in range(4)]
op = deque(list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().strip())))

while op:
    num, direction = op.popleft()
    num -= 1
    tmp_2 = gears[num][2]
    tmp_6 = gears[num][6]
    gears[num].rotate(direction)
    tmp_d = direction

    # 시작 톱니 왼쪽 방향
    direction = tmp_d
    for i in range(num-1, -1, -1):
        if gears[i][2] != tmp_6:  # 서로 다른 극인 경우
            tmp_6 = gears[i][6]
            gears[i].rotate(direction*-1)
            direction *= -1
        else:
            break

    # 시작 톱니 오른쪽 방향
    direction = tmp_d
    for i in range(num+1, 4):
        if gears[i][6] != tmp_2:  # 서로 다른 극인 경우
            tmp_2 = gears[i][2]
            gears[i].rotate(direction*-1)
            direction *= -1
        else:
            break

ans = 0
for i in range(4):
    if gears[i][0] == 1:
        ans += (2 ** i)

print(ans)