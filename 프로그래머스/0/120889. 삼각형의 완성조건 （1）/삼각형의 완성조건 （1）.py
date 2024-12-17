def solution(sides):
    answer = 0
    triangle = sorted(sides)
    if triangle[2] < triangle[1]+triangle[0]:
        answer = 1
    else :
        answer = 2
    
    return answer