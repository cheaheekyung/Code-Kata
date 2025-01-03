def solution(name, yearning, photo):
    answer = []
    a_dict = dict(zip(name,yearning))
    score = 0
    
    for i in photo :
        score = 0
        for key in i :
            if key in a_dict :
                score += a_dict[key]
        answer.append(score)
    
    return answer