# 백트래킹
def solve(n):
    cnt = 0
    num = 1
    while True:
        str_num = str(num)
        flag = True
        if len(str_num) == 1:
            pass
        else:
            for i in range(1, len(str_num)):
                if int(str_num[i]) < int(str_num[i - 1]):
                    continue
                else:
                    start = str_num[:i - 1]
                    mid = str(int(str_num[i - 1]) + 1)
                    end = '0' + str_num[i + 1:]
                    num = int(start + mid + end)
                    flag = False
                    break
        if flag:
            cnt += 1
            if cnt == n:
                return num
            num += 1


if __name__ == "__main__":
    n = int(input())
    if n >= 1023:
        print(-1)
    elif n == 0:
        print(0)
    else:
        print(solve(n))

# # 조합
# from itertools import combinations
#
# n = int(input())
#
# nums = []
# for i in range(1, 11):
#     for comb in combinations(range(0, 10), i):
#         comb = list(comb)
#         comb.sort(reverse=True)
#         nums.append(int("".join(map(str, comb))))
# nums.sort()
#
# try:
#     print(nums[n])
# except:
#     print(-1)