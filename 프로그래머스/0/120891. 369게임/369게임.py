def solution(order):
    answer = 0
    for i in str(order) :
        if int(i) in (3,6,9) :
            answer += 1
    return answer