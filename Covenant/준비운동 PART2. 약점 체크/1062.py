# 1차
from itertools import combinations

def check():
    global ans
    res = 0
    for i in range(n):
        flag = True
        for j in range(len(words[i])):
            if words[i][j] not in know:
                flag = False
                break
        if flag:
            res += 1
    ans = max(ans, res)
    return ans

if __name__ == "__main__":
    n, k = map(int, input().split())
    know = ['a', 'n', 't', 'i', 'c']
    words = [input() for _ in range(n)]
    learn = []
    for i in range(n):
        learn.extend(set(words[i]) - set(know))
    learn = set(learn)
    ans = 0
    if k < 5:
        print(0)
    elif k == 26:
        print(n)
    else:
        for cb in combinations(learn, k - 5):
            know.extend(cb)
            check()
            know = know[:5]
        print(ans)

# 2번
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

# 회고: 풀지 못해서 결국 dfs로 풀었다...

# 6 6
# antarctica
# antahellotica
# antazzztica
# antazzztica
# antazzztica
# antazzztica

# 6 6
# antarctica
# antahellotica
# antazzztica
# antazzztica
# antazzztica
# antazzztica