n, m = map(int, input().split())

l =[]

for _ in range(m) :
    i,j,k = map(int, input().split())
    l.append([i,j,k])

answer = [0]*n

for q,w,e in l :
    if q != w :
        answer[q-1:w] = [e] * (w - q +1) 
    else :
        answer[q-1] = e 
    
print(*answer)


