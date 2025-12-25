
n = int(input())
a = list(map(int, input().split()))

answer = 0
for i in a :
    if i == 2 :
        answer += 1
    elif i > 2 :
        k = 0
        for j in range(2, i) :
            if i % j == 0 :
                k += 1
        if k == 0 :
            answer += 1

print(answer)