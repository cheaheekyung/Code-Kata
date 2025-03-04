def solution(balls, share):
    answer = 0
    a = 1
    b = 1
    for i in range(0,share) :
        a *= (balls-i)
        b *= i+1
    answer = a//b
    return answer