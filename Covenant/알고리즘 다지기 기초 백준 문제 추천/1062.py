def dfs(idx, cnt):
    global answer
    if cnt == k - 5:
        tmp = 0
        for word in words:
            check = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    check = False
                    break
            if check:
                tmp += 1
        answer = max(answer, tmp)
        return
    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = 1
            dfs(i, cnt + 1)
            learn[i] = 0

if __name__ == "__main__":
    n, k = map(int, input().split())
    answer = 0
    words = [set(input()) for _ in range(n)]
    learn = [0] * 26
    for x in ('a', 'c', 'i', 'n', 't'):
        learn[ord(x) - ord('a')] = 1
    if k < 5:
        print(0)
        exit()
    elif k == 26:
        print(n)
        exit()
    dfs(0, 0)
    print(answer)