def solution(n):
    answer = [n]
    while n != 1 :
        if n % 2 == 0 :
            answer.append(n // 2)
            n = n // 2
        elif n % 2 == 1 :
            answer.append(n*3+1)
            n = n*3+1
            
    return answer