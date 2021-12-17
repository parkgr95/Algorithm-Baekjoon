n = int(input())
arr = sorted([str(input()) for _ in range(n)], key=len)
ans = 0
for i in range(n):
    check = True
    for j in range(i + 1, n):
        try:
            if arr[j].index(arr[i]) == 0:
                check = False
                break
        except:
            continue
    if check:
        ans += 1
print(ans)