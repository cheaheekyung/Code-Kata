n, x = map(int, input().split())
l = list(map(int, input().split()))
answer = []

for i in l :
    if i >= 1 and i < x :
        answer.append(i)
print(*answer)