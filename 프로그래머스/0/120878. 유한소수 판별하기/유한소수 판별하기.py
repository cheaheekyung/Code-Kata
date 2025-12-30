def solution(a, b):
    answer = 0
    
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    g = x  
    
    b //= g
    
    while b % 2 == 0 :
        b //= 2
    while b % 5 == 0 :
        b //= 5
    if b == 1 :
        answer = 1
    else : 
        answer = 2
    
    return answer