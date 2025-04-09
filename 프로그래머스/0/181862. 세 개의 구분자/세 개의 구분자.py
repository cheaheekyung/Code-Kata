def solution(myStr):
    answer = []
    a=''
    for i in myStr :
        if i not in "abc" :
            a += i
        else :
            if a :
                answer.append(a)
                a = ''
    if a :
        answer.append(a)
    
    if not answer :
        answer = ["EMPTY"]
    return answer