def solution(code):
    answer = ''
    mode = 0 
    for i, j in enumerate(code) :
        if j == '1' :
            mode = 1 - mode
        else :
            if mode == 0 and i % 2 == 0 :
                answer += j
            elif mode == 1 and i % 2 != 0:
                answer += j
    if not answer :
        return "EMPTY"
    return answer