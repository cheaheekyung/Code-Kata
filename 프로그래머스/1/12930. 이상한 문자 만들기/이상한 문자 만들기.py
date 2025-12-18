def solution(s):
    answer = []
    ind = 0
    a = s.lower()
    for i in range(len(a)) :
        if a[i].isalpha() == False:
            answer.append(a[i])
            ind = 0
        else :
            ind += 1
            if ind % 2 != 0 :
                answer.append(a[i].upper())
            else :
                answer.append(a[i])
                
    return ''.join(answer)