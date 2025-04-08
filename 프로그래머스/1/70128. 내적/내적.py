def solution(a, b):
    answer = 0
    n = len(a)-1
    
    while n > -1 :
        answer += a[n]*b[n]
        n -= 1
    
    return answer