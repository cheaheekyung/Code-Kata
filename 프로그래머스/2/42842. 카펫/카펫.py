def solution(brown, yellow):
    answer = []
    total  = brown + yellow
    
    y = list(range(yellow,0,-1))
    for i in y :
        if ((yellow / i)+2) * (i+2) == total :
            if i+2 not in answer :
                answer.append(i+2)
                answer.append(yellow//i+2)
    
    return answer