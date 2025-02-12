def solution(n):
    answer = []
    
    a = 2
    while n > 1:
        if n % a == 0:
            answer.append(a)
            n //= a
        else:
            a += 1
    
    return list(sorted(set(answer)))
    