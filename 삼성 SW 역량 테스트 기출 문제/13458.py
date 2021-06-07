n = int(input())
applicant = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for num in applicant:
    if num >= b: 
        num -= b
        if num % c == 0:
            answer += num // c
        else:
            answer += num // c + 1
            
print(answer + n)