def solution(array):
    answer = 0
    seven = ''.join(map(str, array))
    answer = seven.count('7')
    return answer