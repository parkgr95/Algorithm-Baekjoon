def dfs(a, cnt):
    global ans
    if a == b:
        ans = cnt
        return
    else:
        if 2 * a <= b:
            dfs(2 * a, cnt + 1)
        if 10 * a + 1 <= b:
            dfs(10 * a + 1, cnt + 1)

if __name__ == "__main__":
    a, b = map(int, input().split())
    ans = -1
    dfs(a, 1)
    print(ans)