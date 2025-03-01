def solution(array, n):
    answer = 0
    b = sorted(array)
    a = []
    for i in range(len(b)) :
        a.append(abs(b[i]-n))
    answer = b[a.index(min(a))]
    return answer