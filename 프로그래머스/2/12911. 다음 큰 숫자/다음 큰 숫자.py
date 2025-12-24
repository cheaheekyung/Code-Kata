def solution(n):
    big = n
    while True :
        big += 1
        if bin(n).count('1') == bin(big).count('1') :
            break
            
    return big