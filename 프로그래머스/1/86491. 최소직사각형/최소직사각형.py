def solution(sizes):
    answer = 0
    a = []
    b = []
    for i in sizes :
        i.sort()
        a.append(i[0])
        b.append(i[1])
    a.sort()
    b.sort()
    answer = a[-1]*b[-1]
    return answer