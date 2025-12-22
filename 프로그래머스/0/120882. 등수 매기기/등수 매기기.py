def solution(score):
    answer = []
    a = []
    for i, j in score :
        a.append((i+j)/2)
    
    b = sorted(a, reverse=True)

    for s in a :
        answer.append(b.index(s)+1)
        
    return answer