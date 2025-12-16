def solution(d, budget):
    a = sorted(d)
    answer = 0
    if sum(a) <= budget:
        answer = len(a) 
    else :
        re = budget
        for i in a :
            re -= i 
            if re < 0 :
                break
            else :
                answer += 1
    return answer