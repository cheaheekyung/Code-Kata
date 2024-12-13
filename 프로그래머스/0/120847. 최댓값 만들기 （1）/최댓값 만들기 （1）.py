def solution(numbers):
    answer = 0
    a = sorted(numbers)
    answer = a[-1] * a[-2]
    return answer