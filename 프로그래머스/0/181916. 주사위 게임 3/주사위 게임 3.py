def solution(a, b, c, d):
    l = sorted([a,b,c,d])
    s = {a,b,c,d}
    m = list(s)
    answer = 0
    if len(s) == 4 :
        answer += min(s)
    elif len(s) == 1 :
        answer += 1111*a
    elif len(s) == 2 :
        if l[1] == l[2] :
            if l[0] == l[1] :
                answer += (10*l[0]+l[-1])**2
            else :
                answer += (10*l[-1]+l[0])**2
        else :
            answer += (m[0]+m[1]) * abs(m[0]-m[1])
    elif len(s) == 3 :
        g = 1
        for i in l :
            if l.count(i) == 1 :
                g *= i
        answer += g
    
    return answer