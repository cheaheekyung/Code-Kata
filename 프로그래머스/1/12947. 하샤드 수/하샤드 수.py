def solution(x):
    answer = True
    xs = str(x)
    sumx = 0
    
    for i in xs :
        sumx += int(i)
    
    if x % sumx != 0 :
        answer = False
    
    return answer