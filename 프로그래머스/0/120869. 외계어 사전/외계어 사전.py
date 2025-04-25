def solution(spell, dic):
    total = 0
    answer = 0
    a = sorted(''.join(spell))
    for i in dic :
        if sorted(i) == a :
            total += 1
    if total == 0 :
        answer = 2
    else :
        answer = 1
            
    
    return answer