import sys
x, y = map(int, sys.stdin.readline().split())
z = (y*100)//x

if z >= 99:
    print(-1)
else:
    answer = 0
    l, r = 1, x
    while l <= r:
        mid = (l+r) // 2
        if (y+mid)*100 // (x+mid) <= z:
            l = mid + 1
        else:
            answer = mid
            r = mid - 1

    print(answer)
