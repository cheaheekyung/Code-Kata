def solution(s):
    answer = []
    a = []
    for i in range(len(s)) :
        if s[i] not in a :
            a += s[i]
            answer.append(-1)
        else :
            b = 0
            for j in a[::-1] :
                b += 1
                if s[i] == j :
                    break
            a += s[i]
            answer.append(b)
    return answer