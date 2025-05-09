def solution(picture, k):
    answer = []
    for i in picture :
        a = ''
        for j in i :
            s = j*k
            a += s
        answer.extend([a] * k)

        
    return answer