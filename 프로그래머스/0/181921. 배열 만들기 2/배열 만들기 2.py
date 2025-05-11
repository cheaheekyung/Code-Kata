def solution(l, r):
    answer = []
    a = {'0','5'}
    for i in range(l,r+1) :
        if set(str(i)) <= a :
            answer.append(i)
        
    return answer if answer else [-1]