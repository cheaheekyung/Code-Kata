n, m = map(int, input().split())
#4x3
answer = []
for c in range(n*2) :
    i = list(map(int, input().split()))
    if c >= n :
        answer[c-n] = [a + b for a, b in zip(answer[c-n], i)]

    else :
        answer.append(i)
        
for row in answer:
    print(*row)