def solution(i, j, k):
    answer = 0
    a = ''.join(map(str, range(i, j+1)))
    answer = a.count(str(k))
    return answer