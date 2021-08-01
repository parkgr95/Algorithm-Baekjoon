# 0801
# 로봇 프로젝트
# idea: 구멍을 막을 수 있는 두 원소의 차의 절대값의 최댓값을 출력하므로 레고 조각들을 정렬 후 맨 앞과 맨 뒤 값들부터 확인해본다.

import sys

while True:
    try:
        x = int(sys.stdin.readline().strip()) * 10000000
        n = int(sys.stdin.readline().strip())
        l = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])
        i, j = 0, n-1
        result = True
        while i < j:
            if l[i] + l[j] == x:
                print('yes %d %d' %(l[i], l[j]))
                result = False
                break
            elif l[i] + l[j] < x:
                i += 1
            else:
                j -= 1
        if result:
            print('danger')
    except:
        break

