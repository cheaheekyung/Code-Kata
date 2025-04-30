def solution(sides):
    answer = 0
    sums = sum(sides)
    maxs = max(sides)
    mins = min(sides)
    
    for i in range(1,sums) :
        if i+mins > maxs :
            answer += 1
        
    return answer