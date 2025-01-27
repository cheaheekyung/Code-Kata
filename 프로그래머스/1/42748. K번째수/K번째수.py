def solution(array, commands):
    answer = []
    for i in commands :
        a = array[i[0]-1:i[1]]
        b = sorted(a)[i[2]-1]
        answer.append(b)
    return answer