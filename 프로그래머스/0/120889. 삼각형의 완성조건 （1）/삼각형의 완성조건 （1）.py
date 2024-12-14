def solution(sides):
    answer = 0
    s = sorted(sides)
    if s[-1] < s[0]+s[1]:
        answer = 1
    else :
        answer = 2
    return answer