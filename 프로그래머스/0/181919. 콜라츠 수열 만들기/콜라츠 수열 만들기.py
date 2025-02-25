def solution(n):
    answer = [n]
    while n != 1 :
        if n % 2 :
            answer.append(n*3+1)
            n = n*3+1
        else :
            answer.append(n // 2)
            n = n // 2
            
    return answer