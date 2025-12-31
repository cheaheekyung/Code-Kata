def solution(s):
    answer = -1
    l = []
    for i in s :
        if len(l) == 0 or l[-1] != i :
            l += i
        elif l[-1] == i :
            l.pop()
        
            
                    
    answer = 0 if len(l) else 1 

    return answer