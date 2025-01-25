def solution(num, k):
    answer = 0
    num1=str(num)
    k1 =str(k)
    if k1 in num1 :
        answer = num1.index(k1) +1
    else :
        answer = -1
    return answer