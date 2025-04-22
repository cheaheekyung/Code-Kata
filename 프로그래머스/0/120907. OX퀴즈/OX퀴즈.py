def solution(quiz):
    answer = []
    for i in quiz :
        a = i.split()
        if eval(''.join(a[:3])) == int(a[-1]) :
            answer += "O"
        else :
            answer += "X"
    return answer