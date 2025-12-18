def solution(s):
    answer = ''
    ind = 0
    a = s.lower()
    for i in range(len(a)) :
        if a[i].isalpha() == False:
            answer += a[i]
            ind = 0
        else :
            ind += 1
            if ind % 2 != 0 :
                answer += a[i].upper()
            else :
                answer += a[i]
                
    return answer