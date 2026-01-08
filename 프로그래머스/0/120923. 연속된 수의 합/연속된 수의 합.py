def solution(num, total):
    answer = []
    a = total//num
    if num % 2 == 0 :
        b = (num -2) // 2
        answer = list(range(a-b,a+b+2))
        
    else :
        b = (num - 1) // 2
        answer = list(range(a-b,a+b+1))
    return answer