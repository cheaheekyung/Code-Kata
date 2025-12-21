a = int(input())

for _ in range(a) :
    n, s = input().split()
    answer = ''
    for i in s :
        answer += i*int(n)
    print(answer)
