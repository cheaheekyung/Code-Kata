def solution(M, N):
    answer = 0
    oM = M
    countM = 0
    countN = 0

    while M > 1 :
        M = M - 1
        countM += 1
    
    while N > 1 :
        N = N - 1
        countN += 1
        
    answer = (oM*countN)+countM
    return answer