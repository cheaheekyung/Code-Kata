def solution(s):
    answer = ''
    ls = s.lower()
    for i in range(len(ls)) :
        if i == 0 :
            if ls[i].isdigit() : 
                answer += ls[0]
            else :
                answer += ls[i].upper()
        elif i>0 and ls[i-1] == " " and ls[i]!=" " :
            answer += ls[i].upper()
        else :
            answer += ls[i]
            
    return answer