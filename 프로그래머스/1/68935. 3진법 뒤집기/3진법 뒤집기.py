def solution(n):
    answer = 0
    th = n
    st = ''
    while th >= 3 :
        st += str(th % 3)
        th //= 3
    st += str(th % 3)
    
    answer = int(st, 3)
    return answer