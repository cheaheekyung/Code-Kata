def solution(n):
    answer = 0
    r = [1, 1]
    for i in range(1, n) :
        r.append(r[i-1]+ r[i])  
    answer = r[n] % 1234567
    
    return answer